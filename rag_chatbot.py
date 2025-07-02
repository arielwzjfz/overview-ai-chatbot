import os
import json
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
import openai
from typing import List, Dict, Any
import yaml
import re
import string

class OverviewRAGChatbot:
    def __init__(self, chunks_dir: str = "overview_docs_chunked"):
        self.chunks_dir = chunks_dir
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = None
        self.setup_vector_database()
        
    def extract_content_from_markdown(self, file_path: str) -> Dict[str, Any]:
        """Extract content and metadata from a markdown chunk file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split YAML frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                markdown_content = parts[2]
                
                # Parse YAML metadata with error handling
                try:
                    metadata = yaml.safe_load(yaml_content)
                    if metadata is None:
                        metadata = {}
                except yaml.YAMLError as e:
                    print(f"Warning: YAML parsing error in {file_path}: {e}")
                    metadata = {}
                
                # Clean markdown content (remove extra whitespace, etc.)
                markdown_content = markdown_content.strip()
                
                # Clean metadata - remove None values and ensure all values are strings
                clean_metadata = {}
                for key, value in metadata.items():
                    if value is not None:
                        if isinstance(value, (int, float, bool)):
                            clean_metadata[key] = str(value)
                        elif isinstance(value, str):
                            clean_metadata[key] = value
                        else:
                            clean_metadata[key] = str(value)
                
                return {
                    'metadata': clean_metadata,
                    'content': markdown_content
                }
        
        return {'metadata': {}, 'content': content}
    
    def setup_vector_database(self):
        """Set up ChromaDB collection and populate with chunked documents."""
        collection_name = "overview_docs"
        
        # Check if collection already exists
        try:
            self.collection = self.chroma_client.get_collection(collection_name)
            # st.success("✅ Using existing vector database")  # Hidden message
            return
        except:
            pass
        
        st.info("🔄 Setting up vector database...")
        
        # Create collection
        self.collection = self.chroma_client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        
        # Process all chunk files
        chunk_files = [f for f in os.listdir(self.chunks_dir) 
                      if f.endswith('.md') and not f.startswith('.')]
        
        documents = []
        metadatas = []
        ids = []
        
        print(f"Processing {len(chunk_files)} chunk files...")
        
        for i, filename in enumerate(chunk_files):
            file_path = os.path.join(self.chunks_dir, filename)
            chunk_data = self.extract_content_from_markdown(file_path)
            
            if chunk_data['content'].strip():  # Only add non-empty chunks
                # Ensure metadata doesn't contain None values
                clean_metadata = {}
                for key, value in chunk_data['metadata'].items():
                    if value is not None:
                        clean_metadata[key] = str(value) if not isinstance(value, str) else value
                
                documents.append(chunk_data['content'])
                metadatas.append(clean_metadata)
                ids.append(f"chunk_{i}")
                
                if i < 5:  # Debug first 5 files
                    print(f"  File {i+1}: {filename}")
                    print(f"    Content length: {len(chunk_data['content'])}")
                    print(f"    Metadata keys: {list(clean_metadata.keys())}")
        
        # Create embeddings and add to collection
        embeddings = self.embedding_model.encode(documents)
        
        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
        st.success(f"✅ Vector database created with {len(documents)} chunks")
    
    @staticmethod
    def normalize_text(text):
        # Lowercase, remove punctuation, and extra whitespace
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def search_documents(self, query: str, n_results: int = 15) -> List[Dict[str, Any]]:
        """Search for relevant documents using semantic similarity with keyword boost and post-filter for exact matches and section title matches."""
        
        # Query expansion for better matching of section titles and content
        expanded_query = query
        query_lower = query.lower()
        
        # If asking about features, expand the query to include related terms
        if any(term in query_lower for term in ['supported features', 'features', 'capabilities']):
            expanded_query = f"{query} supported features capabilities specifications"
        elif any(term in query_lower for term in ['ethernet', 'ethernetip', 'ethernet/ip']):
            expanded_query = f"{query} ethernet ip integration communication"
        
        query_embedding = self.embedding_model.encode([expanded_query])
        
        # Get semantic search results
        semantic_results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results * 2,  # Get more results for filtering
            include=['documents', 'metadatas', 'distances']
        )
        
        # Convert to list of results
        results = [
            {
                'content': doc,
                'metadata': meta,
                'distance': dist
            }
            for doc, meta, dist in zip(
                semantic_results['documents'][0],
                semantic_results['metadatas'][0],
                semantic_results['distances'][0]
            )
        ]
        
        # Boost relevance for chunks containing query keywords
        query_words = query_lower.split()
        norm_query = OverviewRAGChatbot.normalize_text(query)
        
        for result in results:
            content_lower = result['content'].lower()
            metadata_lower = str(result['metadata']).lower()
            
            # Boost score if query words are found in content or metadata
            keyword_matches = 0
            for word in query_words:
                if len(word) > 2:  # Only consider words longer than 2 characters
                    if word in content_lower or word in metadata_lower:
                        keyword_matches += 1
            
            # Apply boost based on keyword matches
            if keyword_matches > 0:
                boost_factor = 1 + (keyword_matches * 0.3)  # 30% boost per keyword match
                result['distance'] = result['distance'] / boost_factor
                
            # Special boost for exact phrase matches
            if 'supported features' in query_lower and 'supported features' in content_lower:
                result['distance'] = result['distance'] / 2.0  # 50% boost for exact phrase match
            # Special boost for chunks containing specific feature content
            if any(term in query_lower for term in ['supported features', 'features']) and any(term in content_lower for term in ['cyclic i/o', 'data throughput', 'custom data']):
                result['distance'] = result['distance'] / 2.5  # 60% boost for specific feature content
            
            # Section title match boost
            chunk_title = result['metadata'].get('chunk_title', '')
            title = result['metadata'].get('title', '')
            norm_chunk_title = OverviewRAGChatbot.normalize_text(chunk_title)
            norm_title = OverviewRAGChatbot.normalize_text(title)
            if norm_query and (norm_query == norm_chunk_title or norm_query == norm_title):
                result['distance'] = result['distance'] / 3.0  # 66% boost for section/title match
        
        # Sort by improved distance and take top n_results
        results.sort(key=lambda x: x['distance'])
        top_results = results[:n_results]
        
        # Post-filter: Always include any chunk with an exact phrase match, even if outside top n_results
        # Also boost chunks where the phrase appears as a section title
        important_phrases = ['supported features', 'features', 'capabilities', 'specifications']
        for phrase in important_phrases:
            if phrase in query_lower:
                # Find all results with the exact phrase in content
                phrase_matches = [r for r in results if phrase in r['content'].lower()]
                
                # Special handling for section titles
                for match in phrase_matches:
                    content_lower = match['content'].lower()
                    # Check if phrase appears as a section title (usually followed by newlines or at start)
                    if (phrase in content_lower and 
                        (content_lower.startswith(phrase) or 
                         f'\n{phrase}' in content_lower or 
                         f'# {phrase}' in content_lower or
                         f'## {phrase}' in content_lower)):
                        # Boost this result significantly
                        match['distance'] = match['distance'] / 3.0  # 66% boost for section title match
                
                # Add to top_results if not already present (by content and metadata)
                def is_duplicate(r1, r2):
                    return r1['content'] == r2['content'] and r1['metadata'] == r2['metadata']
                for match in phrase_matches:
                    if not any(is_duplicate(match, r) for r in top_results):
                        top_results.append(match)
        
        # Post-filter: Always include any chunk where the query matches the chunk_title or title
        for result in results:
            chunk_title = result['metadata'].get('chunk_title', '')
            title = result['metadata'].get('title', '')
            norm_chunk_title = OverviewRAGChatbot.normalize_text(chunk_title)
            norm_title = OverviewRAGChatbot.normalize_text(title)
            if norm_query and (norm_query == norm_chunk_title or norm_query == norm_title):
                def is_duplicate(r1, r2):
                    return r1['content'] == r2['content'] and r1['metadata'] == r2['metadata']
                if not any(is_duplicate(result, r) for r in top_results):
                    top_results.append(result)
        
        return top_results
    
    def add_clickable_links(self, response: str, relevant_docs: List[Dict[str, Any]]) -> str:
        """Add clickable links to document titles mentioned in the response."""
        import re
        
        # Create a mapping of document titles to URLs
        title_to_url = {}
        for doc in relevant_docs:
            title = doc['metadata'].get('title', '')
            chunk_title = doc['metadata'].get('chunk_title', '')
            url = doc['metadata'].get('url', '')
            
            if title and url:
                title_to_url[title] = url
            if chunk_title and url:
                title_to_url[chunk_title] = url
        
        # Also check all chunks in the database for more comprehensive linking
        try:
            all_chunks = self.collection.get(include=['metadatas'])
            for i, metadata in enumerate(all_chunks['metadatas']):
                title = metadata.get('title', '')
                chunk_title = metadata.get('chunk_title', '')
                url = metadata.get('url', '')
                
                if title and url:
                    title_to_url[title] = url
                if chunk_title and url:
                    title_to_url[chunk_title] = url
        except:
            pass  # If collection doesn't exist or other error, continue with just relevant docs
        
        # Process the response to add links
        processed_response = response
        
        # Sort titles by length (longest first) to avoid partial matches
        sorted_titles = sorted(title_to_url.keys(), key=len, reverse=True)
        
        for title in sorted_titles:
            if title and title in processed_response:
                url = title_to_url[title]
                # Create a clickable link
                link_html = f'<a href="{url}" target="_blank" style="color: #7c3aed; text-decoration: underline; font-weight: bold;">{title}</a>'
                # Replace the title with the link (case-insensitive)
                processed_response = re.sub(
                    re.escape(title), 
                    link_html, 
                    processed_response, 
                    flags=re.IGNORECASE
                )
        
        return processed_response
    
    def detect_language(self, text: str) -> str:
        """Detect the language of the input text."""
        # Simple language detection based on character sets
        chinese_chars = len([c for c in text if '\u4e00' <= c <= '\u9fff'])
        spanish_chars = len([c for c in text.lower() if c in 'áéíóúñü'])
        
        if chinese_chars > 0:
            return "Chinese"
        elif spanish_chars > 0:
            return "Spanish"
        else:
            # Check for Spanish words with word boundaries to avoid false positives
            spanish_words = ['hola', 'gracias', 'por favor', 'para', 'con', 'sin', 'como', 'donde', 'cuando', 'que tal', 'buenos dias', 'buenas tardes', 'buenas noches']
            text_lower = text.lower()
            
            # Count Spanish words that appear as whole words
            spanish_word_count = 0
            for word in spanish_words:
                if word in text_lower:
                    # Check if it's a whole word (not part of another word)
                    import re
                    if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
                        spanish_word_count += 1
            
            # Only detect as Spanish if there are multiple Spanish words or clear Spanish indicators
            if spanish_word_count >= 2 or spanish_chars > 0:
                return "Spanish"
            else:
                return "English"
    
    def generate_response(self, query: str, context_docs: List[Dict[str, Any]]) -> str:
        """Generate a response using OpenAI API with retrieved context."""
        if not context_docs:
            # Detect language and provide appropriate response
            detected_lang = self.detect_language(query)
            if detected_lang == "Chinese":
                return "抱歉，我找不到相关信息来回答您的问题。请尝试重新表述您的问题。"
            elif detected_lang == "Spanish":
                return "Lo siento, no pude encontrar información relevante para responder a su pregunta. Por favor, intente reformular su consulta."
            else:
                return "I'm sorry, I couldn't find relevant information to answer your question. Please try rephrasing your query."
        
        # Detect user's language
        detected_lang = self.detect_language(query)
        
        # Debug: Print detected language (you can remove this later)
        print(f"Debug: Query: '{query}' -> Detected language: {detected_lang}")
        
        # Prepare context
        context = "\n\n".join([
            f"Document {i+1}:\n{doc['content']}\n"
            for i, doc in enumerate(context_docs)
        ])
        
        # Create language-specific prompts
        if detected_lang == "Chinese":
            system_prompt = "你是Overview AI文档的助手。请根据提供的文档内容回答用户问题。"
            instructions = """
- 仅基于提供的文档内容回答
- 如果内容信息不足，请说明
- 提供具体、可操作的信息
- 如果有多个相关部分，请综合信息
- 保持回答简洁但信息丰富
- 适当包含相关技术细节
- 请用中文回答
"""
            no_info_msg = "抱歉，提供的文档内容中没有足够的信息来回答这个问题。"
        elif detected_lang == "Spanish":
            system_prompt = "Eres un asistente útil para la documentación de Overview AI. Responde la pregunta del usuario basándote en el contexto de documentación proporcionado."
            instructions = """
- Responde SOLO basándote en el contexto de documentación proporcionado
- Si el contexto no contiene suficiente información, indícalo
- Sé útil y proporciona información específica y accionable
- Si hay múltiples secciones relevantes, sintetiza la información
- Mantén las respuestas concisas pero informativas
- Incluye detalles técnicos relevantes cuando sea apropiado
- Responde en español
"""
            no_info_msg = "Lo siento, el contexto proporcionado no contiene suficiente información para responder a esta pregunta."
        else:
            system_prompt = "You are a helpful assistant for Overview AI documentation. Answer the user's question based on the provided documentation context. When users ask about specific features, capabilities, or technical details, provide the exact information from the documentation without paraphrasing."
            instructions = """
- Answer based ONLY on the provided documentation context
- If the context doesn't contain enough information, say so
- Be helpful and provide specific, actionable information
- If there are multiple relevant sections, synthesize the information
- Keep responses concise but informative
- Include relevant technical details when appropriate
- Respond in English
"""
            no_info_msg = "I'm sorry, the provided context doesn't contain enough information to answer this question."
        
        # Create prompt
        prompt = f"""{system_prompt}

Context from documentation:
{context}

User Question: {query}

Instructions:
{instructions}

IMPORTANT: When the user asks about specific features, capabilities, or sections, use the EXACT information from the provided context. Do not paraphrase or generalize. If there are specific bullet points, numbers, or technical details in the context, include them verbatim in your response.

If the user asks about "Supported Features" or similar, look for chunks that contain bullet points or lists of features and include those exact details in your response.

Please include source references in your answer when appropriate, mentioning which document or section the information comes from.

Answer:"""
        
        try:
            # You'll need to set OPENAI_API_KEY in your environment
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            error_msg = f"Error generating response: {str(e)}. Please check your OpenAI API key."
            if detected_lang == "Chinese":
                error_msg = f"生成响应时出错: {str(e)}。请检查您的OpenAI API密钥。"
            elif detected_lang == "Spanish":
                error_msg = f"Error al generar respuesta: {str(e)}. Por favor, verifique su clave API de OpenAI."
            return error_msg

def main():
    st.set_page_config(
        page_title="Overview AI Documentation Assistant",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize language in session state if not exists
    if 'selected_language' not in st.session_state:
        st.session_state.selected_language = "English"
    
    # Get current selected language
    current_lang = st.session_state.selected_language
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    /* CSS Variables for theme-adaptive colors */
    :root {
        --header-bg-light: linear-gradient(90deg, #e0e7ff 0%, #f3e8ff 100%);
        --header-bg-dark: linear-gradient(90deg, #1e1b4b 0%, #312e81 100%);
        --text-light: #1e293b;
        --text-dark: #f1f5f9;
        --subtext-light: #475569;
        --subtext-dark: #cbd5e1;
        --border-light: #6366f1;
        --border-dark: #8b5cf6;
        --sidebar-bg-light: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
        --sidebar-bg-dark: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        --accent-bg-light: #f8fafc;
        --accent-bg-dark: #1e293b;
    }
    
    /* Light theme (default) */
    .main-header {
        background: transparent;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: none;
        color: var(--text-light);
    }
    
    .logo-container {
        text-align: center;
    }
    
    /* Purple accent for sidebar */
    .css-1d391kg {
        background: var(--sidebar-bg-light);
        border-right: 3px solid var(--border-light);
    }
    
    /* Purple styling for info boxes */
    .stAlert {
        border-left: 4px solid var(--border-light);
        background-color: var(--accent-bg-light);
    }
    
    /* Purple accent for expanders */
    .streamlit-expanderHeader {
        border-left: 3px solid var(--border-light);
        background-color: var(--accent-bg-light);
    }
    
    /* Purple accent for chat messages */
    .stChatMessage {
        border-left: 3px solid var(--border-light);
    }
    
    /* Purple accent for input area */
    .stTextInput > div > div > input {
        border-color: var(--border-light);
    }
    
    /* Purple accent for buttons */
    .stButton > button {
        background-color: var(--border-light);
        border-color: var(--border-light);
    }
    
    .stButton > button:hover {
        background-color: #4f46e5;
        border-color: #4f46e5;
    }
    
    /* Language button styling */
    .language-button {
        margin: 5px;
        border-radius: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .language-button.active {
        background-color: #7c3aed !important;
        border-color: #7c3aed !important;
        color: white !important;
        box-shadow: 0 4px 8px rgba(124, 58, 237, 0.3);
    }
    
    .language-button:not(.active) {
        background-color: rgba(124, 58, 237, 0.1) !important;
        border-color: #7c3aed !important;
        color: #7c3aed !important;
    }
    
    .language-button:not(.active):hover {
        background-color: rgba(124, 58, 237, 0.2) !important;
        transform: translateY(-2px);
    }
    
    /* Dark theme support */
    @media (prefers-color-scheme: dark) {
        .main-header {
            background: transparent;
            border: none;
            color: var(--text-dark);
        }
        
        .css-1d391kg {
            background: var(--sidebar-bg-dark);
            border-right: 3px solid var(--border-dark);
        }
        
        .stAlert {
            border-left: 4px solid var(--border-dark);
            background-color: var(--accent-bg-dark);
        }
        
        .streamlit-expanderHeader {
            border-left: 3px solid var(--border-dark);
            background-color: var(--accent-bg-dark);
        }
        
        .stChatMessage {
            border-left: 3px solid var(--border-dark);
        }
        
        .stTextInput > div > div > input {
            border-color: var(--border-dark);
        }
        
        .stButton > button {
            background-color: var(--border-dark);
            border-color: var(--border-dark);
        }
        
        .stButton > button:hover {
            background-color: #a855f7;
            border-color: #a855f7;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display Overview AI logo at the top
    try:
        st.image("overview_logo.png", width=150)
    except:
        st.markdown("### Overview AI")
    
    # Header with title and language buttons
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.write("")  # Empty space for balance
    
    with col2:
        st.markdown('<h1 style="color: #000000; font-weight: bold; text-shadow: 0 0 10px rgba(255,255,255,0.8);">Overview AI Documentation Assistant</h1>', unsafe_allow_html=True)
        
        # Dynamic subtitle based on selected language
        if current_lang == "Chinese":
            subtitle_text = "我是您的24小时在线的Overview AI助手，让我撸起袖子帮您启动产品 💪！"
        elif current_lang == "Spanish":
            subtitle_text = "¡Soy su asistente de IA de Overview 24/7, vamos a poner su producto en funcionamiento 💪!"
        else:
            subtitle_text = "I am your 24/7 Overview AI helper, I am ready to roll up my sleeves and get your product up and running 💪!"
            
        st.markdown(f'<p style="color: #374151; font-style: italic; text-shadow: 0 0 8px rgba(255,255,255,0.6);">{subtitle_text}</p>', unsafe_allow_html=True)
        
        # Language selection buttons
        st.markdown('<div style="text-align: center; margin-top: 10px;">', unsafe_allow_html=True)
        
        # Create three columns for language buttons
        lang_col1, lang_col2, lang_col3 = st.columns(3)
        
        with lang_col1:
            is_active = current_lang == "English"
            button_style = "background-color: #7c3aed; color: white; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;" if is_active else "background-color: rgba(124, 58, 237, 0.1); color: #7c3aed; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;"
            
            if st.button("🇺🇸 English", key="lang_en", 
                        help="Switch to English interface",
                        use_container_width=True):
                st.session_state.selected_language = "English"
                st.rerun()
        
        with lang_col2:
            is_active = current_lang == "Chinese"
            button_style = "background-color: #7c3aed; color: white; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;" if is_active else "background-color: rgba(124, 58, 237, 0.1); color: #7c3aed; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;"
            
            if st.button("🇨🇳 中文", key="lang_zh", 
                        help="切换到中文界面",
                        use_container_width=True):
                st.session_state.selected_language = "Chinese"
                st.rerun()
        
        with lang_col3:
            is_active = current_lang == "Spanish"
            button_style = "background-color: #7c3aed; color: white; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;" if is_active else "background-color: rgba(124, 58, 237, 0.1); color: #7c3aed; border: 2px solid #7c3aed; border-radius: 20px; font-weight: bold;"
            
            if st.button("🇪🇸 Español", key="lang_es", 
                        help="Cambiar a interfaz en español",
                        use_container_width=True):
                st.session_state.selected_language = "Spanish"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.write("")  # Empty space for balance
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Language support info based on selected language
    current_lang = st.session_state.selected_language
    if current_lang == "Chinese":
        st.info("🌍 **多语言支持**: 您可以用中文、英文或西班牙文提问。我会用相同的语言回答！")
    elif current_lang == "Spanish":
        st.info("🌍 **Soporte Multilingüe**: Puede hacer preguntas en español, inglés o chino. ¡El chatbot responderá en el mismo idioma!")
    else:
        st.info("🌍 **Multilingual Support**: You can ask questions in English, Chinese (中文), or Spanish (Español). The chatbot will respond in the same language!")
    
    # Documentation reference block with light purple styling
    if current_lang == "Chinese":
        st.markdown("""
        <div style="background-color: rgba(124, 58, 237, 0.1); border-left: 4px solid #7c3aed; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
            <p style="margin: 0; color: #7c3aed; font-weight: 500;">📖 如需更详细和准确的解释（包含图片说明），请参考 <a href="https://docs.overview.ai/docs" target="_blank" style="color: #7c3aed; text-decoration: underline; font-weight: bold;">Overview 官方文档</a>。</p>
        </div>
        """, unsafe_allow_html=True)
    elif current_lang == "Spanish":
        st.markdown("""
        <div style="background-color: rgba(124, 58, 237, 0.1); border-left: 4px solid #7c3aed; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
            <p style="margin: 0; color: #7c3aed; font-weight: 500;">📖 Para una explicación más detallada y precisa con ilustraciones, consulte la <a href="https://docs.overview.ai/docs" target="_blank" style="color: #7c3aed; text-decoration: underline; font-weight: bold;">documentación oficial de Overview</a>.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Multilingual documentation reference text
        if current_lang == "Chinese":
            doc_text_before = "📖 如需详细解释和可视化说明，请查看"
            link_text = "Overview官方文档"
            doc_text_after = "或点击'查看来源'查找相关文章。"
        elif current_lang == "Spanish":
            doc_text_before = "📖 Para explicaciones detalladas con visualizaciones, consulte la "
            link_text = "documentación oficial de Overview"
            doc_text_after = " o haga clic en 'Ver Fuentes' para el artículo relacionado."
        else:  # English
            doc_text_before = "📖 For detailed explanations with visuals, see "
            link_text = "Overview's official docs"
            doc_text_after = " or click 'View Sources' for the related article."
        
        st.markdown(f"""
        <div style="background-color: rgba(124, 58, 237, 0.1); border-left: 4px solid #7c3aed; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
            <p style="margin: 0; color: #7c3aed; font-weight: 500;">{doc_text_before}<a href="https://docs.overview.ai/docs" target="_blank" style="color: #7c3aed; text-decoration: underline; font-weight: bold;">{link_text}</a>{doc_text_after}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = OverviewRAGChatbot()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="overview moon logo.png"):
                st.markdown(message["content"])
        else:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Example question bubbles with custom styling
    st.markdown("""
    <style>
    .example-button {
        background-color: rgba(124, 58, 237, 0.1) !important;
        border: 1px solid rgba(124, 58, 237, 0.3) !important;
        color: #7c3aed !important;
        border-radius: 15px !important;
        padding: 8px 16px !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
    }
    .example-button:hover {
        background-color: rgba(124, 58, 237, 0.2) !important;
        border-color: rgba(124, 58, 237, 0.5) !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if current_lang == "Chinese":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 如何使用分类器", key="example1_zh", use_container_width=True, help="点击询问如何使用分类器"):
                st.session_state.example_question = "如何使用分类器"
                st.rerun()
        with col2:
            if st.button("🧭 基本操作是什么", key="example2_zh", use_container_width=True, help="点击询问基本操作"):
                st.session_state.example_question = "基本操作是什么"
                st.rerun()
    elif current_lang == "Spanish":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 ¿Cómo usar el clasificador?", key="example1_es", use_container_width=True, help="Haga clic para preguntar cómo usar el clasificador"):
                st.session_state.example_question = "¿Cómo usar el clasificador?"
                st.rerun()
        with col2:
            if st.button("🧭 ¿Cuál es la navegación básica?", key="example2_es", use_container_width=True, help="Haga clic para preguntar sobre navegación básica"):
                st.session_state.example_question = "¿Cuál es la navegación básica?"
                st.rerun()
    else:  # English
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 How to use the Classifier", key="example1_en", use_container_width=True, help="Click to ask about using the classifier"):
                st.session_state.example_question = "How to use the Classifier"
                st.rerun()
        with col2:
            if st.button("🧭 What are the basic navigation", key="example2_en", use_container_width=True, help="Click to ask about basic navigation"):
                st.session_state.example_question = "What are the basic navigation"
                st.rerun()
    
    # Reduce spacing between example questions and chat input
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    
    # Chat input with dynamic placeholder
    if current_lang == "Chinese":
        placeholder_text = "用中文、英文或西班牙文提问..."
    elif current_lang == "Spanish":
        placeholder_text = "Haga una pregunta en español, inglés o chino..."
    else:
        placeholder_text = "Ask a question in English, Chinese, or Spanish..."
    
    # Check if there's an example question to process
    prompt = None
    if 'example_question' in st.session_state and st.session_state.example_question:
        prompt = st.session_state.example_question
        # Clear the example question to prevent reprocessing
        del st.session_state.example_question
    
    # Always show the chat input
    chat_input = st.chat_input(placeholder_text)
    
    # Use example question if available, otherwise use chat input
    if prompt is None:
        prompt = chat_input
    
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant", avatar="overview moon logo.png"):
            # Dynamic loading message
            if current_lang == "Chinese":
                spinner_text = "正在搜索文档..."
            elif current_lang == "Spanish":
                spinner_text = "Buscando documentación..."
            else:
                spinner_text = "Searching documentation..."
                
            with st.spinner(spinner_text):
                # Search for relevant documents
                relevant_docs = st.session_state.chatbot.search_documents(prompt, n_results=15)
                
                # Generate response
                response = st.session_state.chatbot.generate_response(prompt, relevant_docs)
                
                # Process response to add clickable links for document titles
                processed_response = st.session_state.chatbot.add_clickable_links(response, relevant_docs)
                
                st.markdown(processed_response, unsafe_allow_html=True)
                
                # Show sources (collapsible)
                if current_lang == "Chinese":
                    sources_title = "📚 查看来源"
                elif current_lang == "Spanish":
                    sources_title = "📚 Ver Fuentes"
                else:
                    sources_title = "📚 View Sources"
                    
                with st.expander(sources_title):
                    for i, doc in enumerate(relevant_docs):
                        # Get metadata with fallbacks
                        title = doc['metadata'].get('title', 'Unknown')
                        category = doc['metadata'].get('category', 'Unknown')
                        language = doc['metadata'].get('language', 'Unknown')
                        chunk_title = doc['metadata'].get('chunk_title', '')
                        url = doc['metadata'].get('url', '')
                        relevance_score = 1 - doc['distance']
                        chunk_content = doc['content']
                        
                        # Create a sub-expander for each source
                        with st.expander(f"Source {i+1}: {title} (Score: {relevance_score:.2f})", expanded=False):
                            # Display source information
                            st.markdown(f"**Document Title:** {title}")
                            if chunk_title and chunk_title != title:
                                st.markdown(f"**Section:** {chunk_title}")
                            st.markdown(f"**Category:** {category}")
                            st.markdown(f"**Language:** {language}")
                            st.markdown(f"**Relevance Score:** {relevance_score:.2f}")
                            
                            if url and url != 'Unknown' and url != '':
                                st.markdown(f"[🔗 View Original Source]({url})", unsafe_allow_html=True)
                            
                            st.markdown("---")
                            
                            # Show the actual chunk content
                            st.markdown("**Chunk Content:**")
                            st.markdown(f"```\n{chunk_content}\n```")
                            
                            # Add a copy button for the chunk content
                            if st.button(f"📋 Copy Chunk {i+1}", key=f"copy_chunk_{i}"):
                                st.write("Chunk content copied to clipboard!")
                                # Note: In a real implementation, you'd use pyperclip or similar
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with information
    with st.sidebar:
        # Sidebar header with logo
        try:
            st.image("overview_logo.png", width=100)
        except:
            st.markdown("### Overview AI")
        
        st.markdown("---")
        # Dynamic About section based on selected language
        if current_lang == "Chinese":
            st.markdown('<h3 style="color: #000000; font-weight: bold; text-shadow: 0 0 8px rgba(255,255,255,0.7);">ℹ️ 关于</h3>', unsafe_allow_html=True)
            st.markdown("""
            这个AI助手使用AI技术搜索**[Overview AI文档](https://docs.overview.ai/)**，为您的问题提供准确的答案。
            
            **[🔗 链接到Overview AI文档](https://docs.overview.ai/)**
            
            **示例问题:**
            
            **中文:**
            - "如何设置MQTT通信？"
            - "OV20i的技术规格是什么？"
            
            **English:**
            - "How do I set up MQTT communication?"
            - "What are the technical specifications of OV20i?"
            
            **Español:**
            - "¿Cómo configuro la comunicación MQTT?"
            - "¿Cuáles son las especificaciones técnicas de OV20i?"
            
            **功能特点:**
            - 跨所有文档的语义搜索
            - 多语言支持（英文、中文、西班牙文）
            - 上下文感知响应
            - 来源引用
            - 自动语言检测
            """)
            
        elif current_lang == "Spanish":
            st.markdown('<h3 style="color: #000000; font-weight: bold; text-shadow: 0 0 8px rgba(255,255,255,0.7);">ℹ️ Acerca de</h3>', unsafe_allow_html=True)
            st.markdown("""
            Este chatbot utiliza IA para buscar en la **[documentación de Overview AI](https://docs.overview.ai/)** y proporcionar respuestas precisas a sus preguntas.
            
            **[🔗 Enlace a la documentación de Overview AI](https://docs.overview.ai/)**
            
            **Preguntas de ejemplo:**
            
            **Español:**
            - "¿Cómo configuro la comunicación MQTT?"
            - "¿Cuáles son las especificaciones técnicas de OV20i?"
            
            **English:**
            - "How do I set up MQTT communication?"
            - "What are the technical specifications of OV20i?"
            
            **中文:**
            - "如何设置MQTT通信？"
            - "OV20i的技术规格是什么？"
            
            **Características:**
            - Búsqueda semántica en toda la documentación
            - Soporte multilingüe (Inglés, Chino, Español)
            - Respuestas conscientes del contexto
            - Citas de fuentes
            - Detección automática de idioma
            """)
            
        else:  # English
            st.markdown('<h3 style="color: #000000; font-weight: bold; text-shadow: 0 0 8px rgba(255,255,255,0.7);">ℹ️ About</h3>', unsafe_allow_html=True)
            st.markdown("""
            This chatbot uses AI to search through **[Overview AI documentation](https://docs.overview.ai/)** and provide accurate answers to your questions.
            
            **[🔗 Link to the Overview AI documentation](https://docs.overview.ai/)**
            
            **Example Questions:**
            
            **English:**
            - "How do I set up MQTT communication?"
            - "What are the technical specifications of OV20i?"
            
            **中文:**
            - "如何设置MQTT通信？"
            - "OV20i的技术规格是什么？"
            
            **Español:**
            - "¿Cómo configuro la comunicación MQTT?"
            - "¿Cuáles son las especificaciones técnicas de OV20i?"
            
            **Features:**
            - Semantic search across all documentation
            - Multi-language support (English, Chinese, Spanish)
            - Context-aware responses
            - Source citations
            - Automatic language detection
            """)

if __name__ == "__main__":
    main() 