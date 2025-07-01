#!/usr/bin/env python3
"""
RAG Chunking Example for Overview AI Documentation
Demonstrates different chunking strategies for the Markdown files.
"""

import os
import json
import re
from typing import List, Dict, Any
from pathlib import Path
import yaml

class RAGChunker:
    def __init__(self, docs_dir: str = "overview_docs_rag"):
        self.docs_dir = docs_dir
        self.chunks = []
        
    def load_markdown_files(self) -> List[Dict[str, Any]]:
        """Load all Markdown files with their metadata."""
        documents = []
        
        for file_path in Path(self.docs_dir).glob("*.md"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract frontmatter and content
            frontmatter, markdown_content = self.parse_frontmatter(content)
            
            documents.append({
                'filepath': str(file_path),
                'filename': file_path.name,
                'frontmatter': frontmatter,
                'content': markdown_content,
                'full_content': content
            })
        
        return documents
    
    def parse_frontmatter(self, content: str) -> tuple:
        """Parse YAML frontmatter from Markdown content."""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    markdown_content = parts[2].strip()
                    return frontmatter, markdown_content
                except yaml.YAMLError:
                    pass
        
        # No frontmatter found
        return {}, content
    
    def chunk_by_headers(self, document: Dict[str, Any], max_chunk_size: int = 1000) -> List[Dict[str, Any]]:
        """Chunk document by Markdown headers."""
        content = document['content']
        chunks = []
        
        # Split by headers (##, ###, ####)
        header_pattern = r'^(#{2,4})\s+(.+)$'
        sections = re.split(header_pattern, content, flags=re.MULTILINE)
        
        current_chunk = ""
        current_header = ""
        
        for i in range(0, len(sections), 3):
            if i + 1 < len(sections):
                header_level = sections[i]
                header_text = sections[i + 1]
                section_content = sections[i + 2] if i + 2 < len(sections) else ""
                
                # If adding this section would exceed chunk size, save current chunk
                if len(current_chunk + section_content) > max_chunk_size and current_chunk:
                    chunks.append(self.create_chunk(document, current_chunk, current_header))
                    current_chunk = ""
                    current_header = ""
                
                current_header = header_text
                current_chunk += f"\n{header_level} {header_text}\n{section_content}"
        
        # Add final chunk
        if current_chunk:
            chunks.append(self.create_chunk(document, current_chunk, current_header))
        
        return chunks
    
    def chunk_by_sentences(self, document: Dict[str, Any], max_chunk_size: int = 1000) -> List[Dict[str, Any]]:
        """Chunk document by sentences."""
        content = document['content']
        chunks = []
        
        # Split by sentences (simple approach)
        sentences = re.split(r'[.!?]+', content)
        
        current_chunk = ""
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            # If adding this sentence would exceed chunk size, save current chunk
            if len(current_chunk + sentence) > max_chunk_size and current_chunk:
                chunks.append(self.create_chunk(document, current_chunk, "Sentence-based chunk"))
                current_chunk = ""
            
            current_chunk += sentence + ". "
        
        # Add final chunk
        if current_chunk:
            chunks.append(self.create_chunk(document, current_chunk, "Sentence-based chunk"))
        
        return chunks
    
    def chunk_by_fixed_size(self, document: Dict[str, Any], chunk_size: int = 1000, overlap: int = 200) -> List[Dict[str, Any]]:
        """Chunk document by fixed size with overlap."""
        content = document['content']
        chunks = []
        
        start = 0
        while start < len(content):
            end = start + chunk_size
            
            # Try to break at sentence boundary
            if end < len(content):
                # Look for sentence ending within the last 100 characters
                search_start = max(start + chunk_size - 100, start)
                sentence_end = content.rfind('.', search_start, end)
                if sentence_end > start + chunk_size // 2:  # Only break if we find a reasonable boundary
                    end = sentence_end + 1
            
            chunk_content = content[start:end].strip()
            if chunk_content:
                chunks.append(self.create_chunk(document, chunk_content, f"Fixed-size chunk {len(chunks)+1}"))
            
            start = end - overlap
        
        return chunks
    
    def create_chunk(self, document: Dict[str, Any], content: str, section_title: str = "") -> Dict[str, Any]:
        """Create a chunk with metadata."""
        chunk_id = f"{document['filename']}_{len(self.chunks)}"
        
        return {
            'chunk_id': chunk_id,
            'filename': document['filename'],
            'filepath': document['filepath'],
            'section_title': section_title,
            'content': content,
            'content_length': len(content),
            'metadata': {
                'title': document['frontmatter'].get('title', ''),
                'category': document['frontmatter'].get('category', ''),
                'language': document['frontmatter'].get('language', ''),
                'url': document['frontmatter'].get('url', ''),
                'source_page': document['frontmatter'].get('source_page', ''),
                'scraped_at': document['frontmatter'].get('scraped_at', ''),
            }
        }
    
    def chunk_all_documents(self, strategy: str = "headers", **kwargs) -> List[Dict[str, Any]]:
        """Chunk all documents using the specified strategy."""
        documents = self.load_markdown_files()
        all_chunks = []
        
        print(f"Processing {len(documents)} documents using {strategy} chunking...")
        
        for doc in documents:
            if strategy == "headers":
                chunks = self.chunk_by_headers(doc, **kwargs)
            elif strategy == "sentences":
                chunks = self.chunk_by_sentences(doc, **kwargs)
            elif strategy == "fixed":
                chunks = self.chunk_by_fixed_size(doc, **kwargs)
            else:
                raise ValueError(f"Unknown chunking strategy: {strategy}")
            
            all_chunks.extend(chunks)
            print(f"  {doc['filename']}: {len(chunks)} chunks")
        
        self.chunks = all_chunks
        return all_chunks
    
    def save_chunks(self, output_file: str = "rag_chunks.json"):
        """Save chunks to JSON file."""
        output_path = os.path.join(self.docs_dir, output_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.chunks, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.chunks)} chunks to {output_path}")
    
    def generate_chunking_report(self) -> Dict[str, Any]:
        """Generate a report about the chunking results."""
        if not self.chunks:
            return {}
        
        # Calculate statistics
        content_lengths = [chunk['content_length'] for chunk in self.chunks]
        categories = {}
        languages = {}
        
        for chunk in self.chunks:
            category = chunk['metadata']['category']
            language = chunk['metadata']['language']
            
            categories[category] = categories.get(category, 0) + 1
            languages[language] = languages.get(language, 0) + 1
        
        report = {
            'total_chunks': len(self.chunks),
            'avg_chunk_size': sum(content_lengths) / len(content_lengths),
            'min_chunk_size': min(content_lengths),
            'max_chunk_size': max(content_lengths),
            'categories': categories,
            'languages': languages,
            'total_content_length': sum(content_lengths)
        }
        
        # Save report
        report_path = os.path.join(self.docs_dir, 'chunking_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"Generated chunking report: {report_path}")
        return report

def main():
    """Example usage of the RAG chunker."""
    chunker = RAGChunker()
    
    # Example 1: Chunk by headers (recommended for documentation)
    print("=== Header-based Chunking ===")
    chunks = chunker.chunk_all_documents(strategy="headers", max_chunk_size=1500)
    chunker.save_chunks("chunks_by_headers.json")
    report = chunker.generate_chunking_report()
    
    print(f"\nHeader-based chunking results:")
    print(f"  Total chunks: {report['total_chunks']}")
    print(f"  Average chunk size: {report['avg_chunk_size']:.0f} characters")
    print(f"  Categories: {len(report['categories'])}")
    print(f"  Languages: {len(report['languages'])}")
    
    # Example 2: Chunk by fixed size with overlap
    print("\n=== Fixed-size Chunking ===")
    chunks = chunker.chunk_all_documents(strategy="fixed", chunk_size=1000, overlap=200)
    chunker.save_chunks("chunks_by_fixed_size.json")
    
    # Example 3: Chunk by sentences
    print("\n=== Sentence-based Chunking ===")
    chunks = chunker.chunk_all_documents(strategy="sentences", max_chunk_size=800)
    chunker.save_chunks("chunks_by_sentences.json")
    
    print("\nChunking completed! Files saved in overview_docs_rag/")

if __name__ == "__main__":
    main() 