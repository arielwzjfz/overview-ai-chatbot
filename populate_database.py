#!/usr/bin/env python3
"""
Script to populate ChromaDB with chunked documents
"""

import os
import yaml
import chromadb
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def extract_content_from_markdown(file_path):
    """Extract content and metadata from a markdown chunk file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split YAML frontmatter and content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            markdown_content = parts[2]
            
            # Parse YAML metadata
            try:
                metadata = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                print(f"Warning: YAML parsing error in {file_path}: {e}")
                metadata = {}
            
            # Clean markdown content
            markdown_content = markdown_content.strip()
            
            return {
                'metadata': metadata,
                'content': markdown_content
            }
    
    return {'metadata': {}, 'content': content}

def ensure_valid_metadata(metadata):
    """Ensure metadata is a valid non-empty dict."""
    if not metadata:
        metadata = {}
    
    # Ensure all required fields exist with default values
    required_fields = {
        'title': 'Unknown',
        'category': 'Unknown',
        'language': 'Unknown',
        'url': 'Unknown',
        'source_page': 'Unknown',
        'parent_category': 'Unknown',
        'is_individual_article': False,
        'scraped_at': 'Unknown',
        'chunk_id': 'Unknown',
        'chunk_index': 0,
        'total_chunks': 1,
        'chunk_title': 'Unknown',
        'chunk_level': 1,
        'chunk_start_line': 0,
        'chunk_end_line': 0,  # Changed from None to 0
        'chunked_at': 'Unknown',
        'chunking_method': 'header_based'
    }
    
    # Clean metadata - replace None values and ensure all values are valid
    cleaned_metadata = {}
    for field, default_value in required_fields.items():
        value = metadata.get(field, default_value)
        if value is None:
            value = default_value
        cleaned_metadata[field] = value
    
    # Also clean any additional fields that might have None values
    for field, value in metadata.items():
        if field not in cleaned_metadata and value is not None:
            cleaned_metadata[field] = value
    
    return cleaned_metadata

def populate_database():
    print("🚀 Populating ChromaDB Database")
    print("=" * 50)
    
    # Initialize components
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Create or get collection
    try:
        collection = client.create_collection(
            name="overview_docs",
            metadata={"hnsw:space": "cosine"}
        )
    except Exception as e:
        if "already exists" in str(e):
            print("Collection already exists, getting existing collection...")
            collection = client.get_collection("overview_docs")
        else:
            raise e
    
    # Process all chunk files
    chunks_dir = "overview_docs_chunked"
    chunk_files = [f for f in os.listdir(chunks_dir) 
                  if f.endswith('.md') and not f.startswith('.')]
    
    print(f"📁 Found {len(chunk_files)} chunk files")
    
    documents = []
    metadatas = []
    ids = []
    
    # Process files with progress bar
    for i, filename in enumerate(tqdm(chunk_files, desc="Processing chunks")):
        file_path = os.path.join(chunks_dir, filename)
        chunk_data = extract_content_from_markdown(file_path)
        
        if chunk_data['content'].strip():  # Only add non-empty chunks
            documents.append(chunk_data['content'])
            metadatas.append(ensure_valid_metadata(chunk_data['metadata']))
            ids.append(f"chunk_{i}")
    
    print(f"📄 Processed {len(documents)} valid chunks")
    
    if len(documents) == 0:
        print("❌ No valid documents found!")
        return False
    
    # Create embeddings
    print("🧠 Creating embeddings...")
    embeddings = embedding_model.encode(documents)
    print(f"✅ Created embeddings with shape: {embeddings.shape}")
    
    # Add to collection
    print("💾 Adding to ChromaDB...")
    collection.add(
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    # Verify
    count = collection.count()
    print(f"✅ Database populated with {count} documents")
    
    # Test search
    print("\n🔍 Testing search...")
    test_query = "MQTT communication"
    query_embedding = embedding_model.encode([test_query])
    
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3,
        include=['documents', 'metadatas', 'distances']
    )
    
    print(f"Search query: '{test_query}'")
    print(f"Found {len(results['documents'][0])} results")
    
    for i, (doc, meta, dist) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    )):
        print(f"\nResult {i+1}:")
        print(f"  Relevance: {1 - dist:.3f}")
        print(f"  Title: {meta.get('title', 'Unknown')[:50]}...")
        print(f"  Content preview: {doc[:100]}...")
    
    return True

if __name__ == "__main__":
    populate_database() 