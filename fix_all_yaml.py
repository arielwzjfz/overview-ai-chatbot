#!/usr/bin/env python3
"""
Comprehensive YAML frontmatter fix for all chunked Markdown files
"""

import os
import re
import yaml

def clean_yaml_content(yaml_content):
    """Clean and fix YAML content by escaping special characters."""
    
    def escape_text(text):
        """Escape special characters in text."""
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)").replace(".", "\\.").replace("[", "\\[").replace("]", "\\]")
    
    # Replace problematic characters in chunk_title
    yaml_content = re.sub(r'chunk_title: "([^"]*)"', lambda m: 
        f'chunk_title: "{escape_text(m.group(1))}"', 
        yaml_content)
    
    # Also fix any other fields that might have similar issues
    yaml_content = re.sub(r'title: "([^"]*)"', lambda m: 
        f'title: "{escape_text(m.group(1))}"', 
        yaml_content)
    
    return yaml_content

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
        'chunk_end_line': None,
        'chunked_at': 'Unknown',
        'chunking_method': 'header_based'
    }
    
    for field, default_value in required_fields.items():
        if field not in metadata or metadata[field] is None:
            metadata[field] = default_value
    
    return metadata

def fix_markdown_file(file_path):
    """Fix YAML frontmatter in a single Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only process if there is a YAML frontmatter
    if not content.startswith('---'):
        return False
    
    # Split YAML frontmatter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    yaml_content = parts[1]
    rest_content = parts[2]
    
    # Clean YAML content
    fixed_yaml = clean_yaml_content(yaml_content)
    
    # Parse and validate metadata
    try:
        metadata = yaml.safe_load(fixed_yaml)
        metadata = ensure_valid_metadata(metadata)
    except yaml.YAMLError as e:
        print(f"Warning: Still can't parse YAML in {file_path}: {e}")
        # Create minimal valid metadata
        metadata = ensure_valid_metadata({})
    
    # Convert back to YAML
    try:
        fixed_yaml = yaml.dump(metadata, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        print(f"Warning: Can't dump YAML for {file_path}: {e}")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n' + fixed_yaml + '---' + rest_content)
    
    return True

def main():
    print("🔧 Fixing all YAML frontmatter issues")
    print("=" * 50)
    
    chunks_dir = "overview_docs_chunked"
    fixed_count = 0
    total_count = 0
    
    for fname in os.listdir(chunks_dir):
        if not fname.endswith('.md'):
            continue
        
        total_count += 1
        fpath = os.path.join(chunks_dir, fname)
        
        if fix_markdown_file(fpath):
            fixed_count += 1
            print(f"Fixed: {fname}")
    
    print(f"\n📊 Summary:")
    print(f"Total files processed: {total_count}")
    print(f"Files fixed: {fixed_count}")
    print(f"Files unchanged: {total_count - fixed_count}")

if __name__ == "__main__":
    main() 