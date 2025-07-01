# Overview AI Documentation Chatbot - Deployment Guide

This guide covers different deployment options for your RAG-powered documentation chatbot.

## 🚀 Quick Local Setup

### Prerequisites
- Python 3.8+
- OpenAI API key
- Git (optional)

### Step 1: Install Dependencies
```bash
# Clone or download the project
git clone <your-repo-url>
cd overview-chatbot-cursor

# Install dependencies
python setup_chatbot.py
```

### Step 2: Set Environment Variables
```bash
# Set your OpenAI API key
export OPENAI_API_KEY='sk-...'

# For Windows (PowerShell):
# $env:OPENAI_API_KEY="your-api-key-here"
```

### Step 3: Run the Chatbot
```bash
streamlit run rag_chatbot.py
```

The chatbot will be available at `http://localhost:8501`

## ☁️ Streamlit Cloud Deployment

### Step 1: Prepare for Deployment
1. Create a `requirements.txt` file (already included)
2. Create a `.streamlit/config.toml` file for configuration:

```toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
```

### Step 2: Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the following environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
5. Deploy!

### Step 3: Configure Secrets
In Streamlit Cloud, add your secrets in the app settings:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

## 🐳 Docker Deployment

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Set environment variables
ENV OPENAI_API_KEY=""

# Run the application
CMD ["streamlit", "run", "rag_chatbot.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2: Build and Run
```bash
# Build the Docker image
docker build -t overview-chatbot .

# Run the container
docker run -p 8501:8501 -e OPENAI_API_KEY="your-api-key" overview-chatbot
```

## 🌐 Production Web Application

### Option 1: Flask/FastAPI Backend + React Frontend

#### Backend (Flask)
```python
# app.py
from flask import Flask, request, jsonify
from rag_chatbot import OverviewRAGChatbot

app = Flask(__name__)
chatbot = OverviewRAGChatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question')
    
    # Get relevant documents
    relevant_docs = chatbot.search_documents(question)
    
    # Generate response
    response = chatbot.generate_response(question, relevant_docs)
    
    return jsonify({
        'response': response,
        'sources': relevant_docs
    })

if __name__ == '__main__':
    app.run(debug=True)
```

#### Frontend (React)
```jsx
// ChatComponent.jsx
import React, { useState } from 'react';

function ChatComponent() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: input })
    });
    
    const data = await response.json();
    setMessages([...messages, 
      { role: 'user', content: input },
      { role: 'assistant', content: data.response }
    ]);
    setInput('');
  };

  return (
    <div>
      {/* Chat interface */}
    </div>
  );
}
```

### Option 2: Next.js Full-Stack Application

```bash
# Create Next.js app
npx create-next-app@latest overview-chatbot-web
cd overview-chatbot-web

# Install dependencies
npm install axios
```

```javascript
// pages/api/chat.js
import { OverviewRAGChatbot } from '../../../rag_chatbot';

const chatbot = new OverviewRAGChatbot();

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const { question } = req.body;
  
  try {
    const relevant_docs = chatbot.search_documents(question);
    const response = chatbot.generate_response(question, relevant_docs);
    
    res.status(200).json({ response, sources: relevant_docs });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

## 🔧 Environment Configuration

### Production Environment Variables
```bash
# Required
OPENAI_API_KEY=your-openai-api-key

# Optional
CHROMA_DB_PATH=./chroma_db
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-3.5-turbo
MAX_TOKENS=500
SEARCH_RESULTS=5
```

### Configuration File
Create a `config.py` file:
```python
import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    CHROMA_DB_PATH = os.getenv('CHROMA_DB_PATH', './chroma_db')
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
    LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-3.5-turbo')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 500))
    SEARCH_RESULTS = int(os.getenv('SEARCH_RESULTS', 5))
```

## 📊 Monitoring and Analytics

### Add Logging
```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log user interactions
def log_interaction(question, response, sources):
    logger.info(f"Question: {question}")
    logger.info(f"Response: {response[:100]}...")
    logger.info(f"Sources: {len(sources)} documents")
```

### Add Analytics
```python
# Track usage metrics
import json
from collections import defaultdict

class Analytics:
    def __init__(self):
        self.metrics = defaultdict(int)
    
    def track_question(self, question, response_length):
        self.metrics['total_questions'] += 1
        self.metrics['total_response_length'] += response_length
    
    def save_metrics(self):
        with open('analytics.json', 'w') as f:
            json.dump(dict(self.metrics), f)
```

## 🔒 Security Considerations

### API Key Security
- Never commit API keys to version control
- Use environment variables or secret management services
- Rotate API keys regularly

### Rate Limiting
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/chat', methods=['POST'])
@limiter.limit("10 per minute")
def chat():
    # Your chat logic here
    pass
```

### Input Validation
```python
import re

def validate_question(question):
    if not question or len(question.strip()) < 3:
        raise ValueError("Question too short")
    
    if len(question) > 1000:
        raise ValueError("Question too long")
    
    # Check for potentially harmful content
    harmful_patterns = ['script', 'javascript:', 'data:']
    for pattern in harmful_patterns:
        if pattern.lower() in question.lower():
            raise ValueError("Invalid input detected")
    
    return question.strip()
```

## 🚀 Performance Optimization

### Caching
```python
import redis
import hashlib
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_response(question):
    question_hash = hashlib.md5(question.encode()).hexdigest()
    cached = redis_client.get(f"chat:{question_hash}")
    return json.loads(cached) if cached else None

def cache_response(question, response):
    question_hash = hashlib.md5(question.encode()).hexdigest()
    redis_client.setex(f"chat:{question_hash}", 3600, json.dumps(response))
```

### Async Processing
```python
import asyncio
import aiohttp

async def async_generate_response(question, context_docs):
    # Async implementation for better performance
    pass
```

## 📈 Scaling Considerations

### Horizontal Scaling
- Use load balancers for multiple instances
- Implement session management
- Use shared databases for vector storage

### Database Optimization
- Consider using PostgreSQL with pgvector for production
- Implement connection pooling
- Add database indexing

### CDN and Caching
- Use CDN for static assets
- Implement response caching
- Consider edge computing for global deployment

## 🎯 Next Steps

1. **Choose your deployment strategy** based on your needs
2. **Set up monitoring and analytics** to track usage
3. **Implement security measures** for production use
4. **Optimize performance** based on usage patterns
5. **Plan for scaling** as your user base grows

For questions or issues, refer to the main README.md file or create an issue in the repository. 