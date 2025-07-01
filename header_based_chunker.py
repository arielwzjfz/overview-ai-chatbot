#!/usr/bin/env python3
"""
Header-based chunking for Overview AI documentation.
Splits Markdown content at natural semantic boundaries defined by headers.
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Any
import hashlib
from datetime import datetime

class HeaderBasedChunker:
    def __init__(self, input_dir: str = "overview_docs_deep", output_dir: str = "overview_docs_chunked"):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Header patterns to match different levels
        self.header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        
        # Metadata extraction pattern
        self.frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
        
    def extract_frontmatter(self, content: str) -> Dict[str, Any]:
        """Extract YAML frontmatter from Markdown content."""
        match = self.frontmatter_pattern.search(content)
        if match:
            try:
                import yaml
                return yaml.safe_load(match.group(1)) or {}
            except:
                return {}
        return {}
    
    def find_header_positions(self, content: str) -> List[tuple]:
        """Find all header positions and levels in the content."""
        headers = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            match = self.header_pattern.match(line)
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                headers.append((i, level, title))
        
        return headers
    
    def extract_chunk_content(self, content: str, start_line: int, end_line: int) -> str:
        """Extract content between start_line and end_line."""
        lines = content.split('\n')
        if end_line is None:
            chunk_lines = lines[start_line:]
        else:
            chunk_lines = lines[start_line:end_line]
        return '\n'.join(chunk_lines)
    
    def create_chunk_metadata(self, original_metadata: Dict[str, Any], chunk_info: Dict[str, Any]) -> Dict[str, Any]:
        """Create metadata for a chunk."""
        chunk_metadata = original_metadata.copy()
        chunk_metadata.update({
            'chunk_id': chunk_info['chunk_id'],
            'chunk_index': chunk_info['chunk_index'],
            'total_chunks': chunk_info['total_chunks'],
            'chunk_title': chunk_info['title'],
            'chunk_level': chunk_info['level'],
            'chunk_start_line': chunk_info['start_line'],
            'chunk_end_line': chunk_info['end_line'],
            'chunked_at': datetime.now().isoformat(),
            'chunking_method': 'header_based'
        })
        
        # Ensure required fields have proper values
        if not chunk_metadata.get('title') or chunk_metadata['title'] == 'Unknown':
            chunk_metadata['title'] = chunk_info['title']
        else:
            # Clean up the title if it's too long
            original_title = chunk_metadata.get('title', '')
            if len(original_title) > 100:
                chunk_metadata['title'] = original_title[:100].split('...')[0].strip()
        
        if not chunk_metadata.get('category') or chunk_metadata['category'] == 'Unknown':
            chunk_metadata['category'] = original_metadata.get('category', 'General')
            
        if not chunk_metadata.get('language') or chunk_metadata['language'] == 'Unknown':
            chunk_metadata['language'] = original_metadata.get('language', 'English')
            
        if not chunk_metadata.get('url') or chunk_metadata['url'] == 'Unknown':
            chunk_metadata['url'] = original_metadata.get('url', '')
            
        return chunk_metadata
    
    def chunk_file(self, file_path: Path) -> List[Dict[str, Any]]:
        """Chunk a single Markdown file based on headers."""
        print(f"Processing: {file_path.name}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter = self.extract_frontmatter(content)
        
        # Remove frontmatter from content for processing
        content_without_frontmatter = self.frontmatter_pattern.sub('', content)
        
        # Find all headers
        headers = self.find_header_positions(content_without_frontmatter)
        
        if not headers:
            # No headers found, treat entire content as one chunk
            chunk_id = hashlib.md5(f"{file_path.name}_chunk_0".encode()).hexdigest()[:8]
            
            # Clean up title - take first 100 characters and remove extra content
            original_title = frontmatter.get('title', file_path.stem)
            clean_title = original_title[:100].split('...')[0].strip()
            
            chunk_info = {
                'chunk_id': chunk_id,
                'chunk_index': 0,
                'total_chunks': 1,
                'title': clean_title,
                'level': 1,
                'start_line': 0,
                'end_line': None
            }
            return [{
                'chunk_id': chunk_id,
                'chunk_index': 0,
                'total_chunks': 1,
                'title': clean_title,
                'level': 1,
                'start_line': 0,
                'end_line': None,
                'content': content_without_frontmatter,
                'metadata': self.create_chunk_metadata(frontmatter, chunk_info)
            }]
        
        chunks = []
        
        for i, (line_num, level, title) in enumerate(headers):
            # Determine end line for this chunk
            if i + 1 < len(headers):
                end_line = headers[i + 1][0]
            else:
                end_line = None
            
            # Extract chunk content
            chunk_content = self.extract_chunk_content(content_without_frontmatter, line_num, end_line)
            
            # Create chunk ID
            chunk_id = hashlib.md5(f"{file_path.name}_chunk_{i}".encode()).hexdigest()[:8]
            
            # Clean up title - take first 100 characters
            clean_title = title[:100].strip()
            
            # Create chunk info
            chunk_info = {
                'chunk_id': chunk_id,
                'chunk_index': i,
                'total_chunks': len(headers),
                'title': clean_title,
                'level': level,
                'start_line': line_num,
                'end_line': end_line
            }
            
            chunks.append({
                'chunk_id': chunk_id,
                'chunk_index': i,
                'total_chunks': len(headers),
                'title': clean_title,
                'level': level,
                'start_line': line_num,
                'end_line': end_line,
                'content': chunk_content,
                'metadata': self.create_chunk_metadata(frontmatter, chunk_info)
            })
        
        return chunks
    
    def save_chunk(self, chunk: Dict[str, Any], original_filename: str) -> str:
        """Save a chunk to a Markdown file with frontmatter."""
        # Create filename for chunk
        chunk_filename = f"{chunk['chunk_id']}-{original_filename}"
        chunk_path = self.output_dir / chunk_filename
        
        # Create frontmatter using yaml.dump for proper escaping
        import yaml
        
        # Clean metadata for YAML serialization
        clean_metadata = {}
        for key, value in chunk['metadata'].items():
            if value is not None:
                if isinstance(value, str):
                    # Remove any problematic characters that could break YAML
                    clean_value = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', ' ')
                    # Remove any remaining problematic characters
                    clean_value = clean_value.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
                    clean_value = clean_value.replace('{', '').replace('}', '').replace('*', '').replace('→', '->')
                    clean_metadata[key] = clean_value
                elif isinstance(value, (int, float, bool)):
                    clean_metadata[key] = value
                else:
                    clean_metadata[key] = str(value)
        
        # Generate YAML frontmatter
        yaml_content = yaml.dump(clean_metadata, default_flow_style=False, allow_unicode=True, sort_keys=False)
        frontmatter = f"---\n{yaml_content}---\n\n"
        
        # Write chunk content
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(chunk['content'])
        
        return str(chunk_path)
    
    def process_all_files(self) -> Dict[str, Any]:
        """Process all Markdown files in the input directory."""
        markdown_files = list(self.input_dir.glob("*.md"))
        
        if not markdown_files:
            print(f"No Markdown files found in {self.input_dir}")
            return {}
        
        print(f"Found {len(markdown_files)} Markdown files to process")
        
        all_chunks = []
        chunking_stats = {
            'total_files': len(markdown_files),
            'total_chunks': 0,
            'files_processed': 0,
            'chunks_by_level': {},
            'chunks_by_language': {},
            'chunks_by_category': {}
        }
        
        for file_path in markdown_files:
            try:
                chunks = self.chunk_file(file_path)
                
                for chunk in chunks:
                    # Save chunk to file
                    chunk_file_path = self.save_chunk(chunk, file_path.name)
                    
                    # Update stats
                    chunking_stats['total_chunks'] += 1
                    
                    # Track chunks by header level
                    level = chunk['level']
                    chunking_stats['chunks_by_level'][level] = chunking_stats['chunks_by_level'].get(level, 0) + 1
                    
                    # Track chunks by language
                    language = chunk['metadata'].get('language', 'Unknown')
                    chunking_stats['chunks_by_language'][language] = chunking_stats['chunks_by_language'].get(language, 0) + 1
                    
                    # Track chunks by category
                    category = chunk['metadata'].get('category', 'Unknown')
                    chunking_stats['chunks_by_category'][category] = chunking_stats['chunks_by_category'].get(category, 0) + 1
                    
                    # Add file path to chunk info
                    chunk['file_path'] = chunk_file_path
                    all_chunks.append(chunk)
                
                chunking_stats['files_processed'] += 1
                print(f"  Created {len(chunks)} chunks from {file_path.name}")
                
            except Exception as e:
                print(f"Error processing {file_path.name}: {e}")
        
        # Save chunking report
        report_path = self.output_dir / "header_chunking_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(chunking_stats, f, indent=2, ensure_ascii=False)
        
        # Save all chunks metadata
        chunks_metadata_path = self.output_dir / "all_chunks_metadata.json"
        with open(chunks_metadata_path, 'w', encoding='utf-8') as f:
            json.dump(all_chunks, f, indent=2, ensure_ascii=False)
        
        return chunking_stats

def main():
    """Main function to run header-based chunking."""
    print("Starting Header-Based Chunking for Overview AI Documentation")
    print("=" * 60)
    
    chunker = HeaderBasedChunker()
    stats = chunker.process_all_files()
    
    print("\n" + "=" * 60)
    print("CHUNKING COMPLETE!")
    print("=" * 60)
    print(f"Files processed: {stats['files_processed']}/{stats['total_files']}")
    print(f"Total chunks created: {stats['total_chunks']}")
    print(f"Output directory: {chunker.output_dir}")
    
    print("\nChunks by header level:")
    for level, count in sorted(stats['chunks_by_level'].items()):
        print(f"  Level {level} (#{'#' * level}): {count} chunks")
    
    print("\nChunks by language:")
    for language, count in sorted(stats['chunks_by_language'].items()):
        print(f"  {language}: {count} chunks")
    
    print("\nTop categories by chunk count:")
    sorted_categories = sorted(stats['chunks_by_category'].items(), key=lambda x: x[1], reverse=True)
    for category, count in sorted_categories[:10]:
        print(f"  {category}: {count} chunks")
    
    print(f"\nDetailed report saved to: {chunker.output_dir}/header_chunking_report.json")
    print(f"All chunks metadata saved to: {chunker.output_dir}/all_chunks_metadata.json")

if __name__ == "__main__":
    main() 