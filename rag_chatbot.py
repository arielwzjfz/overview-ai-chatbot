import os
import json
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
import openai
from typing import List, Dict, Any
import yaml
import re

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
            st.success("✅ Using existing vector database")
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
    
    def search_documents(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Search for relevant documents using semantic similarity."""
        query_embedding = self.embedding_model.encode([query])
        
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results,
            include=['documents', 'metadatas', 'distances']
        )
        
        return [
            {
                'content': doc,
                'metadata': meta,
                'distance': dist
            }
            for doc, meta, dist in zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            )
        ]
    
    def detect_language(self, text: str) -> str:
        """Detect the language of the input text."""
        # Simple language detection based on character sets
        chinese_chars = len([c for c in text if '\u4e00' <= c <= '\u9fff'])
        spanish_chars = len([c for c in text.lower() if c in 'áéíóúñü'])
        
        if chinese_chars > 0:
            return "Chinese"
        elif spanish_chars > 0 or any(word in text.lower() for word in ['hola', 'gracias', 'por', 'para', 'con', 'sin', 'que', 'como', 'donde', 'cuando']):
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
            system_prompt = "You are a helpful assistant for Overview AI documentation. Answer the user's question based on the provided documentation context."
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
        page_title="Overview AI Documentation Chatbot",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Overview AI Documentation Assistant")
    st.markdown("Ask questions about Overview AI products and get instant answers from the documentation!")
    
    # Language support info
    st.info("🌍 **Multilingual Support**: You can ask questions in English, Chinese (中文), or Spanish (Español). The chatbot will respond in the same language!")
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = OverviewRAGChatbot()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question in English, Chinese, or Spanish..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Searching documentation..."):
                # Search for relevant documents
                relevant_docs = st.session_state.chatbot.search_documents(prompt)
                
                # Generate response
                response = st.session_state.chatbot.generate_response(prompt, relevant_docs)
                
                st.markdown(response)
                
                # Show sources (collapsible)
                with st.expander("📚 View Sources"):
                    for i, doc in enumerate(relevant_docs):
                        # Get metadata with fallbacks
                        title = doc['metadata'].get('title', 'Unknown')
                        category = doc['metadata'].get('category', 'Unknown')
                        language = doc['metadata'].get('language', 'Unknown')
                        chunk_title = doc['metadata'].get('chunk_title', '')
                        url = doc['metadata'].get('url', '')
                        relevance_score = 1 - doc['distance']
                        
                        # Display source information
                        st.markdown(f"**Source {i+1}:** {title}")
                        if chunk_title and chunk_title != title:
                            st.markdown(f"**Section:** {chunk_title}")
                        st.markdown(f"**Category:** {category}")
                        st.markdown(f"**Language:** {language}")
                        st.markdown(f"**Relevance Score:** {relevance_score:.2f}")
                        
                        if url and url != 'Unknown' and url != '':
                            st.markdown(f"[🔗 View Source]({url})", unsafe_allow_html=True)
                        
                        st.markdown("---")
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot uses AI to search through Overview AI documentation and provide accurate answers to your questions.
        
        **Features:**
        - Semantic search across all documentation
        - Multi-language support (English, Chinese, Spanish)
        - Context-aware responses
        - Source citations
        - Automatic language detection
        
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
        """)
        
        st.header("🔧 Setup")
        st.markdown("""
        To use this chatbot, you need:
        1. OpenAI API key set as environment variable
        2. Required Python packages installed
        
        See requirements.txt for dependencies.
        """)

if __name__ == "__main__":
    main() 