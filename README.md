# 🤖 Overview AI Documentation Chatbot

A multilingual RAG (Retrieval-Augmented Generation) chatbot that provides instant answers from Overview AI documentation using semantic search and AI-powered responses.

## 🌟 Features

- **Multilingual Support**: Ask questions in English, Chinese (中文), or Spanish (Español)
- **Semantic Search**: Advanced document retrieval using sentence transformers
- **Context-Aware Responses**: AI-generated answers based on relevant documentation
- **Source Citations**: View source documents with relevance scores
- **Header-Based Chunking**: Intelligent document segmentation for better context
- **Real-time Processing**: Instant responses with source links

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Required Python packages (see `requirements.txt`)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd overview-ai-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the chatbot**
   ```bash
   streamlit run rag_chatbot.py
   ```

5. **Open your browser**
   - Local: http://localhost:8501
   - Network: http://your-ip:8501

## 📚 Usage Examples

### English
- "How do I set up MQTT communication?"
- "What are the technical specifications of OV20i?"
- "How do I create my first recipe?"

### 中文
- "如何设置MQTT通信？"
- "OV20i的技术规格是什么？"
- "如何创建第一个配方？"

### Español
- "¿Cómo configuro la comunicación MQTT?"
- "¿Cuáles son las especificaciones técnicas de OV20i?"
- "¿Cómo creo mi primera receta?"

## 🛠️ Project Structure

```
overview-ai-chatbot/
├── rag_chatbot.py              # Main chatbot application
├── header_based_chunker.py     # Document chunking utility
├── deep_overview_scraper.py    # Web scraper for documentation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

## 🔧 Core Components

### 1. RAG Chatbot (`rag_chatbot.py`)
- **Multilingual language detection**
- **Semantic search using ChromaDB**
- **OpenAI-powered response generation**
- **Streamlit web interface**

### 2. Document Chunker (`header_based_chunker.py`)
- **Header-based document segmentation**
- **YAML metadata preservation**
- **Multi-language support**
- **Semantic structure preservation**

### 3. Web Scraper (`deep_overview_scraper.py`)
- **Comprehensive documentation crawling**
- **Multi-language content extraction**
- **Markdown conversion with metadata**
- **Robust error handling**

## 📊 Documentation Coverage

The chatbot has access to:
- **English documentation**: 580 chunks
- **Chinese documentation**: 61 chunks
- **Spanish documentation**: 17 chunks

**Total**: 658 semantically meaningful chunks across all languages

## 🔍 How It Works

1. **Document Processing**: Scrapes Overview AI documentation and converts to Markdown
2. **Chunking**: Splits documents at natural header boundaries for semantic coherence
3. **Embedding**: Creates vector embeddings for semantic search
4. **Search**: Finds relevant document chunks using similarity search
5. **Generation**: Uses OpenAI to generate contextual responses
6. **Display**: Shows answers with source citations and metadata

## 🎯 Key Technologies

- **Streamlit**: Web interface
- **ChromaDB**: Vector database for semantic search
- **Sentence Transformers**: Text embeddings
- **OpenAI GPT**: Response generation
- **PyYAML**: Metadata handling
- **BeautifulSoup**: Web scraping

## 📝 Configuration

### Environment Variables
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

### Customization
- Modify `rag_chatbot.py` for UI changes
- Adjust `header_based_chunker.py` for different chunking strategies
- Update `deep_overview_scraper.py` for different documentation sources

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Overview AI for their comprehensive documentation
- OpenAI for GPT models
- Streamlit for the web framework
- ChromaDB for vector storage
- Sentence Transformers for embeddings

## 📞 Support

For questions or issues:
1. Check the existing documentation
2. Search through existing issues
3. Create a new issue with detailed information

---

**Made with ❤️ for the Overview AI community** 