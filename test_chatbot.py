#!/usr/bin/env python3
"""
Test script to verify chatbot functionality
"""

import os
import yaml
from rag_chatbot import OverviewRAGChatbot

def test_chunk_loading():
    """Test if chunks can be loaded properly"""
    print("Testing chunk loading...")
    
    chunks_dir = "overview_docs_chunked"
    chunk_files = [f for f in os.listdir(chunks_dir) 
                  if f.endswith('.md') and not f.startswith('.')]
    
    print(f"Found {len(chunk_files)} chunk files")
    
    # Test first few files
    for i, filename in enumerate(chunk_files[:3]):
        file_path = os.path.join(chunks_dir, filename)
        print(f"\nTesting file {i+1}: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split YAML frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                markdown_content = parts[2]
                
                try:
                    metadata = yaml.safe_load(yaml_content)
                    print(f"  ✅ YAML parsed successfully")
                    print(f"  📄 Content length: {len(markdown_content)}")
                    print(f"  🏷️  Title: {metadata.get('title', 'N/A')}")
                    print(f"  🌍 Language: {metadata.get('language', 'N/A')}")
                    print(f"  📂 Category: {metadata.get('category', 'N/A')}")
                except yaml.YAMLError as e:
                    print(f"  ❌ YAML parsing error: {e}")
            else:
                print(f"  ❌ Invalid YAML structure")
        else:
            print(f"  ❌ No YAML frontmatter found")

def test_chatbot_initialization():
    """Test chatbot initialization"""
    print("\nTesting chatbot initialization...")
    
    try:
        chatbot = OverviewRAGChatbot()
        print("✅ Chatbot initialized successfully")
        
        # Test search
        print("\nTesting search functionality...")
        results = chatbot.search_documents("MQTT communication", n_results=3)
        print(f"✅ Search returned {len(results)} results")
        
        for i, result in enumerate(results):
            print(f"  Result {i+1}:")
            print(f"    Title: {result['metadata'].get('title', 'N/A')}")
            print(f"    Language: {result['metadata'].get('language', 'N/A')}")
            print(f"    Distance: {result['distance']:.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Chatbot initialization failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Overview AI Chatbot")
    print("=" * 50)
    
    test_chunk_loading()
    success = test_chatbot_initialization()
    
    if success:
        print("\n✅ All tests passed! Chatbot is working correctly.")
    else:
        print("\n❌ Tests failed. Please check the errors above.") 