#!/usr/bin/env python3
"""
Setup script for Overview AI Documentation Chatbot
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def check_openai_key():
    """Check if OpenAI API key is set."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  Warning: OPENAI_API_KEY environment variable not set!")
        print("   You'll need to set it to use the chatbot.")
        print("   You can set it by running:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        return False
    else:
        print("✅ OpenAI API key found!")
        return True

def main():
    print("🚀 Setting up Overview AI Documentation Chatbot")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed. Please check the error messages above.")
        return
    
    # Check OpenAI key
    check_openai_key()
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Set your OpenAI API key:")
    print("   export OPENAI_API_KEY='your-api-key-here'")
    print("\n2. Run the chatbot:")
    print("   streamlit run rag_chatbot.py")
    print("\n3. Open your browser to the URL shown in the terminal")
    print("\n💡 The first run will take a few minutes to create the vector database.")

if __name__ == "__main__":
    main() 