import os
import re

def fix_yaml_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only process if there is a YAML frontmatter
    if not content.startswith('---'):
        return False
    
    # Split YAML frontmatter and the rest
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    yaml_content = parts[1]
    rest_content = parts[2]
    
    # Only fix if there is a backslash in the YAML
    if '\\' not in yaml_content:
        return False
    
    # Escape all backslashes in YAML (double them)
    fixed_yaml = yaml_content.replace('\\', '\\\\')
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---' + fixed_yaml + '---' + rest_content)
    return True

def main():
    chunk_dir = 'overview_docs_chunked'
    fixed_count = 0
    for fname in os.listdir(chunk_dir):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(chunk_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            head = f.read(500)
        if '\\' in head:
            if fix_yaml_frontmatter(fpath):
                print(f'Fixed: {fname}')
                fixed_count += 1
    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main() 