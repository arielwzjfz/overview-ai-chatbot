#!/usr/bin/env python3
"""
Test script to verify search functionality
"""

from rag_chatbot import OverviewRAGChatbot

def test_search():
    print("🧪 Testing Search Functionality")
    print("=" * 50)
    
    # Initialize chatbot
    chatbot = OverviewRAGChatbot()
    
    # Test query
    query = "what are the supported features of ethernet ip integration"
    print(f"Query: {query}")
    
    # Search for documents
    results = chatbot.search_documents(query, n_results=15)
    print(f"\nFound {len(results)} results:")
    
    # Check each result
    found_supported_features = False
    for i, result in enumerate(results, 1):
        if i > 20:  # Limit display to first 20 results
            break
        title = result['metadata'].get('title', 'Unknown')
        chunk_title = result['metadata'].get('chunk_title', '')
        distance = result['distance']
        relevance = 1 - distance
        
        print(f"\n{i}. {title}")
        if chunk_title and chunk_title != title:
            print(f"   Section: {chunk_title}")
        print(f"   Relevance: {relevance:.3f}")
        
        # Check if this contains "Supported Features"
        content = result['content'].lower()
        if 'supported features' in content:
            print(f"   ✅ CONTAINS 'Supported Features'")
            found_supported_features = True
            
            # Show a snippet of the content
            start = content.find('supported features')
            snippet = content[start:start+200]
            print(f"   Snippet: {snippet}...")
    
    if found_supported_features:
        print(f"\n✅ SUCCESS: Found 'Supported Features' chunk in results!")
    else:
        print(f"\n❌ FAILED: 'Supported Features' chunk not found in top {len(results)} results")
        
        # Let's check if it exists at all
        print("\n🔍 Checking if 'Supported Features' chunks exist in database...")
        all_results = chatbot.search_documents("supported features", n_results=50)
        supported_chunks = [r for r in all_results if 'supported features' in r['content'].lower()]
        print(f"Found {len(supported_chunks)} chunks containing 'Supported Features' in top 50 results")
        
        for chunk in supported_chunks[:3]:
            title = chunk['metadata'].get('title', 'Unknown')
            chunk_title = chunk['metadata'].get('chunk_title', '')
            distance = chunk['distance']
            relevance = 1 - distance
            print(f"  - {title} (Section: {chunk_title}, Relevance: {relevance:.3f})")

if __name__ == "__main__":
    test_search() 