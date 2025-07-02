#!/usr/bin/env python3
"""
Debug script to test search functionality for "Supported Features" queries
"""

import os
import yaml
from sentence_transformers import SentenceTransformer
import chromadb
from typing import List, Dict, Any

class DebugSearch:
    def __init__(self, chunks_dir: str = "overview_docs_chunked"):
        self.chunks_dir = chunks_dir
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = None
        
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
                
                return {
                    'metadata': metadata,
                    'content': markdown_content
                }
        
        return {'metadata': {}, 'content': content}
    
    def search_documents(self, query: str, n_results: int = 10) -> List[Dict[str, Any]]:
        """Search for relevant documents using semantic similarity."""
        try:
            self.collection = self.chroma_client.get_collection("overview_docs")
        except:
            print("❌ Collection not found. Please run the chatbot first to create the database.")
            return []
        
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
    
    def find_chunk_by_content(self, search_term: str) -> List[Dict[str, Any]]:
        """Find chunks that contain specific text."""
        matching_chunks = []
        
        chunk_files = [f for f in os.listdir(self.chunks_dir) 
                      if f.endswith('.md') and not f.startswith('.')]
        
        for filename in chunk_files:
            file_path = os.path.join(self.chunks_dir, filename)
            chunk_data = self.extract_content_from_markdown(file_path)
            
            content = chunk_data['content'].lower()
            if search_term.lower() in content:
                matching_chunks.append({
                    'filename': filename,
                    'metadata': chunk_data['metadata'],
                    'content': chunk_data['content'],
                    'file_path': file_path
                })
        
        return matching_chunks

def main():
    print("🔍 Debug Search for 'Supported Features'")
    print("=" * 60)
    
    debug_search = DebugSearch()
    
    # Test different queries
    queries = [
        "Supported Features",
        "Supported Features in Ethernet/IP Integration",
        "Ethernet/IP Supported Features",
        "Supported Features of Ethernet/IP",
        "what are the supported features of ethernet ip integration"
    ]
    
    for query in queries:
        print(f"\n🔎 Testing query: '{query}'")
        print("-" * 40)
        
        # Test semantic search
        results = debug_search.search_documents(query, n_results=10)
        print(f"Semantic search returned {len(results)} results:")
        
        for i, result in enumerate(results[:5], 1):  # Show first 5
            title = result['metadata'].get('title', 'Unknown')
            chunk_title = result['metadata'].get('chunk_title', '')
            distance = result['distance']
            relevance = 1 - distance
            
            print(f"  {i}. {title}")
            if chunk_title and chunk_title != title:
                print(f"     Section: {chunk_title}")
            print(f"     Relevance: {relevance:.3f}")
            
            # Check if this result contains "Supported Features"
            content = result['content'].lower()
            if 'supported features' in content:
                print(f"     ✅ CONTAINS 'Supported Features'")
            print()
    
    # Direct text search
    print("\n🔍 Direct text search for 'Supported Features':")
    print("-" * 40)
    
    matching_chunks = debug_search.find_chunk_by_content("Supported Features")
    print(f"Found {len(matching_chunks)} chunks containing 'Supported Features':")
    
    for i, chunk in enumerate(matching_chunks[:5], 1):  # Show first 5
        title = chunk['metadata'].get('title', 'Unknown')
        chunk_title = chunk['metadata'].get('chunk_title', '')
        print(f"  {i}. {title}")
        if chunk_title and chunk_title != title:
            print(f"     Section: {chunk_title}")
        print(f"     File: {chunk['filename']}")
        print()

if __name__ == "__main__":
    main() 