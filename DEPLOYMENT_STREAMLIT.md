# 🚀 Deploy Overview Chatbot to Streamlit Cloud

This guide will walk you through deploying your Overview AI RAG Chatbot to Streamlit Cloud.

## 📋 Prerequisites

1. **GitHub Account**: Your code must be in a GitHub repository
2. **Streamlit Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)
3. **OpenAI API Key**: For the chatbot to generate responses

## 🔧 Pre-Deployment Setup

### 1. Prepare Your Repository

Ensure your repository has the following structure:
```
overview-chatbot/
├── streamlit_app.py          # Main entry point
├── rag_chatbot.py           # Your chatbot implementation
├── requirements.txt         # Python dependencies
├── packages.txt            # System dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── overview_docs_chunked/   # Your chunked documentation
└── README.md
```

### 2. Environment Variables

You'll need to set these in Streamlit Cloud:
- `OPENAI_API_KEY`: Your OpenAI API key

### 3. Data Preparation

The deployment will need access to your chunked documentation. You have two options:

#### Option A: Include in Repository (Recommended for small datasets)
- Keep `overview_docs_chunked/` in your repository
- Update `.gitignore` to allow this directory

#### Option B: External Storage (For large datasets)
- Use cloud storage (AWS S3, Google Cloud Storage)
- Modify the code to download data on startup

## 🚀 Deployment Steps

### Step 1: Push to GitHub

```bash
# Initialize git if not already done
git init
git add .
git commit -m "Initial commit for Streamlit deployment"
git branch -M main
git remote add origin https://github.com/yourusername/overview-chatbot.git
git push -u origin main
```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)
2. **Sign in**: Use your GitHub account
3. **New App**: Click "New app"
4. **Configure App**:
   - **Repository**: Select your GitHub repository
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **App URL**: Choose a custom subdomain (optional)

### Step 3: Set Environment Variables

1. In your app settings, go to "Secrets"
2. Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

### Step 4: Deploy

Click "Deploy" and wait for the build to complete.

## 🔧 Configuration Files

### streamlit_app.py
```python
#!/usr/bin/env python3
"""
Streamlit Cloud Deployment Entry Point
"""
import streamlit as st
from rag_chatbot import main

if __name__ == "__main__":
    main()
```

### .streamlit/config.toml
```toml
[global]
developmentMode = false

[server]
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#7c3aed"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#262730"
```

### packages.txt
```
build-essential
python3-dev
```

## 🐛 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check that all dependencies are in `requirements.txt`
   - Ensure system dependencies are in `packages.txt`
   - Verify Python version compatibility

2. **Import Errors**
   - Make sure all files are in the correct locations
   - Check that `streamlit_app.py` can import from `rag_chatbot.py`

3. **Memory Issues**
   - Reduce the number of search results
   - Use smaller embedding models
   - Consider external storage for large datasets

4. **API Key Issues**
   - Verify the environment variable name matches your code
   - Check that the API key is valid and has sufficient credits

### Debug Commands

Add these to your app for debugging:
```python
import streamlit as st

# Debug information
st.write("Environment variables:", st.secrets)
st.write("Current working directory:", os.getcwd())
st.write("Available files:", os.listdir("."))
```

## 📊 Monitoring

### Performance Monitoring
- Monitor app usage in Streamlit Cloud dashboard
- Check for memory usage and response times
- Monitor OpenAI API usage and costs

### Error Tracking
- Check Streamlit Cloud logs for errors
- Monitor user feedback and issues
- Track search performance and accuracy

## 🔄 Updates and Maintenance

### Updating the App
1. Make changes to your local code
2. Push to GitHub
3. Streamlit Cloud will automatically redeploy

### Database Updates
- If you update the documentation chunks, redeploy the app
- Consider implementing a versioning system for the database

## 💰 Cost Considerations

### Streamlit Cloud
- Free tier available
- Paid plans for more resources and features

### OpenAI API
- Monitor usage to control costs
- Consider implementing rate limiting
- Use appropriate models for your use case

## 🔒 Security Best Practices

1. **API Keys**: Never commit API keys to your repository
2. **Environment Variables**: Use Streamlit secrets for sensitive data
3. **Input Validation**: Validate user inputs to prevent injection attacks
4. **Rate Limiting**: Implement rate limiting to prevent abuse

## 📈 Scaling Considerations

### For High Traffic
- Consider using external vector databases (Pinecone, Weaviate)
- Implement caching for frequently asked questions
- Use load balancing for multiple instances

### For Large Datasets
- Use external storage for documentation chunks
- Implement pagination for search results
- Consider using more efficient embedding models

## 🎯 Next Steps

1. **Test thoroughly** in the deployed environment
2. **Monitor performance** and user feedback
3. **Optimize** based on usage patterns
4. **Add features** like user authentication, analytics, etc.

---

**Need help?** Check the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud) or create an issue in your repository. 