import os
import re
import yaml
import json
from difflib import SequenceMatcher

CHUNKS_DIR = "overview_docs_chunked"
ARTICLES_JSON = "overview_docs_deep/deep_article_urls.json"

# Load article metadata
with open(ARTICLES_JSON, 'r', encoding='utf-8') as f:
    articles = json.load(f)

def best_article_match(filename, articles):
    """Find the best matching article for a chunked file by substring similarity."""
    # Remove extension and use lower case
    base = filename.lower().replace('.md', '')
    best_score = 0
    best_article = None
    for article in articles:
        # Try matching on URL and title
        url = article.get('url', '').lower()
        title = article.get('title', '').lower()
        score_url = SequenceMatcher(None, base, url).ratio()
        score_title = SequenceMatcher(None, base, title).ratio()
        score = max(score_url, score_title)
        if score > best_score:
            best_score = score
            best_article = article
    return best_article if best_score > 0.2 else None  # Only accept reasonable matches

def patch_chunk_file(filepath, article):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return False
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    yaml_content = parts[1]
    rest_content = parts[2]
    try:
        metadata = yaml.safe_load(yaml_content)
    except Exception:
        metadata = {}
    # Patch metadata
    if article:
        metadata['title'] = article.get('title', 'Unknown')
        metadata['url'] = article.get('url', 'Unknown')
        metadata['category'] = article.get('category', metadata.get('category', 'Unknown'))
        metadata['language'] = article.get('language', metadata.get('language', 'Unknown'))
    # Write back
    fixed_yaml = yaml.dump(metadata, default_flow_style=False, allow_unicode=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\n' + fixed_yaml + '---' + rest_content)
    return True

def main():
    print("🔧 Patching chunked files with correct metadata...")
    files = [f for f in os.listdir(CHUNKS_DIR) if f.endswith('.md')]
    patched = 0
    for fname in files:
        fpath = os.path.join(CHUNKS_DIR, fname)
        article = best_article_match(fname, articles)
        if patch_chunk_file(fpath, article):
            patched += 1
            print(f"Patched: {fname} -> {article['url'] if article else 'No match'}")
    print(f"\n✅ Patched {patched} files.")

if __name__ == "__main__":
    main() 