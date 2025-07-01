#!/usr/bin/env python3
"""
Debug script to check ChromaDB contents and search functionality
"""

import chromadb
from sentence_transformers import SentenceTransformer

def debug_chroma():
    print("🔍 Debugging ChromaDB Database")
    print("=" * 50)
    
    # Connect to database
    client = chromadb.PersistentClient(path="./chroma_db")
    
    try:
        # Get collection
        collection = client.get_collection("overview_docs")
        print("✅ Collection 'overview_docs' found")
        
        # Get collection info
        count = collection.count()
        print(f"📊 Total documents in collection: {count}")
        
        if count == 0:
            print("❌ No documents found in collection!")
            return False
        
        # Get a sample of documents
        print("\n📄 Sample documents:")
        results = collection.get(limit=3)
        
        for i, (doc, metadata) in enumerate(zip(results['documents'], results['metadatas'])):
            print(f"\nDocument {i+1}:")
            print(f"  Content preview: {doc[:100]}...")
            print(f"  Metadata: {metadata}")
        
        # Test search
        print("\n🔍 Testing search functionality:")
        embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Test query
        test_query = "MQTT communication"
        query_embedding = embedding_model.encode([test_query])
        
        search_results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=3,
            include=['documents', 'metadatas', 'distances']
        )
        
        print(f"Search query: '{test_query}'")
        print(f"Found {len(search_results['documents'][0])} results")
        
        for i, (doc, meta, dist) in enumerate(zip(
            search_results['documents'][0],
            search_results['metadatas'][0],
            search_results['distances'][0]
        )):
            print(f"\nResult {i+1}:")
            print(f"  Distance: {dist}")
            print(f"  Relevance: {1 - dist:.3f}")
            print(f"  Title: {meta.get('title', 'Unknown')[:50]}...")
            print(f"  Content preview: {doc[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    debug_chroma() 