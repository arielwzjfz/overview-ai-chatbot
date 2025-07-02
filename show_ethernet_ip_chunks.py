#!/usr/bin/env python3
"""
Script to show all chunks related to Ethernet/IP Integration
"""

import os
import yaml
import re
from typing import List, Dict, Any
import sys

def extract_content_from_markdown(file_path: str) -> Dict[str, Any]:
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

def find_ethernet_ip_chunks(chunks_dir: str = "overview_docs_chunked") -> List[Dict[str, Any]]:
    """Find all chunks related to Ethernet/IP Integration."""
    ethernet_ip_chunks = []
    
    # Get all markdown files
    chunk_files = [f for f in os.listdir(chunks_dir) 
                  if f.endswith('.md') and not f.startswith('.')]
    
    for filename in chunk_files:
        file_path = os.path.join(chunks_dir, filename)
        chunk_data = extract_content_from_markdown(file_path)
        
        # Check if this chunk is related to Ethernet/IP
        metadata = chunk_data['metadata']
        content = chunk_data['content']
        
        # Check various indicators of Ethernet/IP content
        is_ethernet_ip = False
        
        # Check filename - look for specific Ethernet/IP patterns
        if 'EthernetIP' in filename or 'Ethernet/IP' in filename:
            is_ethernet_ip = True
        
        # Check metadata more specifically
        title = metadata.get('title', '').lower()
        category = metadata.get('category', '').lower()
        chunk_title = metadata.get('chunk_title', '').lower()
        url = metadata.get('url', '').lower()
        
        # More specific checks for Ethernet/IP content
        ethernet_terms = ['ethernet/ip', 'ethernetip', 'ethernet ip']
        
        if any(term in title for term in ethernet_terms):
            is_ethernet_ip = True
        if any(term in category for term in ethernet_terms):
            is_ethernet_ip = True
        if any(term in chunk_title for term in ethernet_terms):
            is_ethernet_ip = True
        if any(term in url for term in ethernet_terms):
            is_ethernet_ip = True
        
        # Check content for Ethernet/IP specific terms
        content_lower = content.lower()
        if any(term in content_lower for term in ethernet_terms):
            is_ethernet_ip = True
        
        if is_ethernet_ip:
            ethernet_ip_chunks.append({
                'filename': filename,
                'metadata': metadata,
                'content': content,
                'file_path': file_path
            })
    
    return ethernet_ip_chunks

def display_ethernet_ip_chunks():
    """Display all Ethernet/IP Integration chunks in a formatted way."""
    print("🔍 Searching for Ethernet/IP Integration chunks...")
    print("=" * 80)
    
    chunks = find_ethernet_ip_chunks()
    
    if not chunks:
        print("❌ No Ethernet/IP Integration chunks found!")
        return
    
    print(f"✅ Found {len(chunks)} Ethernet/IP Integration chunks:")
    print("=" * 80)
    
    # Sort chunks by title for better organization
    chunks.sort(key=lambda x: x['metadata'].get('title', ''))
    
    for i, chunk in enumerate(chunks, 1):
        metadata = chunk['metadata']
        content = chunk['content']
        
        print(f"\n📄 CHUNK {i}/{len(chunks)}")
        print("-" * 60)
        
        # Display metadata
        print(f"📁 File: {chunk['filename']}")
        print(f"📋 Title: {metadata.get('title', 'Unknown')}")
        print(f"🏷️  Category: {metadata.get('category', 'Unknown')}")
        print(f"🌐 Language: {metadata.get('language', 'Unknown')}")
        print(f"🔗 URL: {metadata.get('url', 'Unknown')}")
        
        chunk_title = metadata.get('chunk_title', '')
        if chunk_title and chunk_title != metadata.get('title', ''):
            print(f"📖 Section: {chunk_title}")
        
        # Display content (truncated for readability)
        print(f"\n📝 Content Preview ({len(content)} characters):")
        print("-" * 40)
        
        # Show first 500 characters and last 200 characters if content is long
        if len(content) > 700:
            print(content[:500] + "\n...\n" + content[-200:])
        else:
            print(content)
        print("-" * 40)
        
        if i < len(chunks):
            print("\n" + "=" * 80)

def show_chunk_summary():
    """Show a summary of all Ethernet/IP chunks."""
    chunks = find_ethernet_ip_chunks()
    
    if not chunks:
        print("❌ No Ethernet/IP Integration chunks found!")
        return
    
    print(f"\n📊 SUMMARY: {len(chunks)} Ethernet/IP Integration chunks found")
    print("=" * 60)
    
    # Group by language
    languages = {}
    for chunk in chunks:
        lang = chunk['metadata'].get('language', 'Unknown')
        if lang not in languages:
            languages[lang] = []
        languages[lang].append(chunk)
    
    for lang, lang_chunks in languages.items():
        print(f"\n🌐 {lang} ({len(lang_chunks)} chunks):")
        for chunk in lang_chunks:
            title = chunk['metadata'].get('title', 'Unknown')
            chunk_title = chunk['metadata'].get('chunk_title', '')
            if chunk_title and chunk_title != title:
                print(f"  • {title} - {chunk_title}")
            else:
                print(f"  • {title}")

def export_ethernet_ip_chunks_markdown(output_file="ethernet_ip_chunks.md"):
    """Export all Ethernet/IP Integration chunks to a Markdown file."""
    chunks = find_ethernet_ip_chunks()
    
    if not chunks:
        print("❌ No Ethernet/IP Integration chunks found!")
        return
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Ethernet/IP Integration Chunks\n\n")
        f.write(f"Total Chunks: {len(chunks)}\n\n")
        # Group by language
        languages = {}
        for chunk in chunks:
            lang = chunk['metadata'].get('language', 'Unknown')
            if lang not in languages:
                languages[lang] = []
            languages[lang].append(chunk)
        for lang, lang_chunks in languages.items():
            f.write(f"## Language: {lang} ({len(lang_chunks)} chunks)\n\n")
            for i, chunk in enumerate(lang_chunks, 1):
                metadata = chunk['metadata']
                content = chunk['content']
                f.write(f"### Chunk {i}: {metadata.get('title', 'Unknown')}\n")
                f.write(f"- **File:** `{chunk['filename']}`\n")
                f.write(f"- **Category:** {metadata.get('category', 'Unknown')}\n")
                f.write(f"- **Section:** {metadata.get('chunk_title', '')}\n")
                f.write(f"- **URL:** {metadata.get('url', 'Unknown')}\n")
                f.write(f"- **Language:** {metadata.get('language', 'Unknown')}\n\n")
                f.write(f"#### Content\n\n")
                f.write("```\n")
                f.write(content)
                f.write("\n```")
                f.write("\n\n")
    print(f"✅ Exported {len(chunks)} Ethernet/IP Integration chunks to {output_file}")

def main():
    """Main function to run the script."""
    print("🚀 Ethernet/IP Integration Chunks Viewer")
    print("=" * 80)
    
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--markdown":
            export_ethernet_ip_chunks_markdown()
        else:
            # Show summary first
            show_chunk_summary()
            
            # Ask user if they want to see detailed chunks
            print("\n" + "=" * 80)
            response = input("\nWould you like to see detailed chunk content? (y/n): ").lower().strip()
            
            if response in ['y', 'yes']:
                display_ethernet_ip_chunks()
            else:
                print("✅ Summary displayed. Run the script again with 'y' to see detailed content.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 