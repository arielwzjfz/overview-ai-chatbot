#!/usr/bin/env python3
"""
Deep Overview AI Documentation Scraper
Goes beyond category pages to find all individual articles within each category.
Aims to find all 80+ individual articles.
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import json
from urllib.parse import urljoin, urlparse
import re
from typing import List, Dict, Set, Optional
import logging
import hashlib
import html2text
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('deep_scraper.log'),
        logging.StreamHandler()
    ]
)

class DeepOverviewScraper:
    def __init__(self, base_url: str = "https://docs.overview.ai"):
        self.base_url = base_url
        self.docs_url = f"{base_url}/docs"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        self.visited_urls: Set[str] = set()
        self.category_urls: List[Dict] = []
        self.article_urls: List[Dict] = []
        self.output_dir = "overview_docs_deep"
        self.max_retries = 3
        self.retry_delay = 2
        
        # HTML to Markdown converter
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # Don't wrap text
        self.h2t.unicode_snob = True
        self.h2t.escape_snob = True
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
    def get_page_content(self, url: str, retries: int = 0) -> Optional[BeautifulSoup]:
        """Fetch and parse a web page with retry logic."""
        try:
            logging.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Check if we got a valid HTML response
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' not in content_type:
                logging.warning(f"Non-HTML content type: {content_type} for {url}")
                return None
                
            return BeautifulSoup(response.content, 'html.parser')
            
        except requests.RequestException as e:
            if retries < self.max_retries:
                logging.warning(f"Retry {retries + 1}/{self.max_retries} for {url}: {e}")
                time.sleep(self.retry_delay * (retries + 1))
                return self.get_page_content(url, retries + 1)
            else:
                logging.error(f"Failed to fetch {url} after {self.max_retries} retries: {e}")
                return None
    
    def extract_category_urls(self, soup: BeautifulSoup, page_url: str) -> List[Dict]:
        """Extract category URLs from the main documentation page."""
        categories = []
        
        # Look for category links
        selectors = [
            'a[href*="/docs/"]',
            'a[href*="start-here"]',
            'a[href*="hardware"]',
            'a[href*="software"]',
            'a[href*="walkthrough"]',
            'a[href*="how-to"]',
            'a[href*="plc"]',
            'a[href*="ethernet"]',
            'a[href*="robot"]',
            'a[href*="faq"]',
            'a[href*="drawings"]',
            'a[href*="quick-start"]',
            'a[href*="overview-software"]',
            'a[href*="tools"]',
            'a[href*="electrical"]',
            'a[href*="node-red"]',
            'a[href*="ov20i"]',
            'a[href*="ov80i"]',
            'a[href*="ov20i-new-version"]',
        ]
        
        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(page_url, href)
                    
                    # Skip if already visited
                    if full_url in self.visited_urls:
                        continue
                    
                    # Check if it's a valid category URL
                    if self.is_valid_category_url(full_url):
                        title = self.extract_title(link)
                        category = self.extract_category(link, soup)
                        language = self.extract_language(full_url)
                        
                        category_info = {
                            'url': full_url,
                            'title': title,
                            'category': category,
                            'language': language,
                            'source_page': page_url,
                            'link_text': link.get_text(strip=True),
                            'link_classes': ' '.join(link.get('class', [])),
                            'timestamp': time.time()
                        }
                        
                        categories.append(category_info)
                        self.visited_urls.add(full_url)
        
        return categories
    
    def extract_individual_articles(self, soup: BeautifulSoup, category_url: str, category_info: Dict) -> List[Dict]:
        """Extract individual article URLs from a category page."""
        articles = []
        
        # Look for individual article links within the category
        selectors = [
            # Common article link patterns
            'a[href*="/docs/"]',
            'a[href*="article"]',
            'a[href*="guide"]',
            'a[href*="tutorial"]',
            'a[href*="setup"]',
            'a[href*="installation"]',
            'a[href*="configuration"]',
            'a[href*="manual"]',
            'a[href*="reference"]',
            'a[href*="api"]',
            'a[href*="sdk"]',
            'a[href*="example"]',
            'a[href*="demo"]',
            'a[href*="test"]',
            'a[href*="troubleshoot"]',
            'a[href*="faq"]',
            'a[href*="help"]',
            'a[href*="support"]',
            
            # Specific to Overview AI
            'a[href*="ov20i"]',
            'a[href*="ov80i"]',
            'a[href*="hardware"]',
            'a[href*="software"]',
            'a[href*="walkthrough"]',
            'a[href*="plc"]',
            'a[href*="robot"]',
            'a[href*="node-red"]',
            'a[href*="electrical"]',
            'a[href*="tools"]',
            'a[href*="overview-software"]',
            'a[href*="drawings"]',
            'a[href*="quick-start"]',
            
            # Navigation and content links
            '.article-link',
            '.docs-link',
            '.content-link',
            '.nav-link',
            '.menu-link',
            '.toc-link',
            '.sidebar-link',
            '.breadcrumb-link',
            
            # List items that might contain articles
            'li a',
            '.list-item a',
            '.menu-item a',
            '.nav-item a',
        ]
        
        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(category_url, href)
                    
                    # Skip if already visited
                    if full_url in self.visited_urls:
                        continue
                    
                    # Check if it's a valid individual article URL
                    if self.is_valid_article_url(full_url, category_url):
                        title = self.extract_title(link)
                        article_category = category_info.get('category', 'Unknown')
                        language = category_info.get('language', 'English')
                        
                        article_info = {
                            'url': full_url,
                            'title': title,
                            'category': article_category,
                            'language': language,
                            'parent_category': category_info,
                            'source_page': category_url,
                            'link_text': link.get_text(strip=True),
                            'link_classes': ' '.join(link.get('class', [])),
                            'timestamp': time.time(),
                            'is_individual_article': True
                        }
                        
                        articles.append(article_info)
                        self.visited_urls.add(full_url)
        
        return articles
    
    def extract_title(self, link) -> str:
        """Extract title from a link element."""
        # Try multiple methods to get the title
        title = link.get_text(strip=True)
        
        if not title:
            title = link.get('title', '')
        
        if not title:
            title = link.get('aria-label', '')
        
        if not title:
            # Try to get from parent elements
            parent = link.parent
            if parent:
                title = parent.get_text(strip=True)
        
        return title or "Untitled"
    
    def extract_category(self, link, soup) -> str:
        """Extract category information from the link context."""
        # Look for category information in parent elements
        parent = link.parent
        while parent and parent.name != 'body':
            if parent.get('class'):
                classes = ' '.join(parent.get('class'))
                if any(cat in classes.lower() for cat in ['category', 'section', 'group']):
                    return parent.get_text(strip=True)[:100]
            parent = parent.parent
        
        # Try to find category from page structure
        category_selectors = [
            '.category-title',
            '.section-title',
            '.page-title',
            'h1',
            'h2'
        ]
        
        for selector in category_selectors:
            elements = soup.select(selector)
            if elements:
                return elements[0].get_text(strip=True)[:100]
        
        return "General"
    
    def extract_language(self, url: str) -> str:
        """Extract language from URL."""
        if '/en/' in url:
            return 'English'
        elif '/es-mx/' in url:
            return 'Spanish'
        elif '/zh-cn/' in url:
            return 'Chinese'
        else:
            return 'English'  # Default
    
    def is_valid_category_url(self, url: str) -> bool:
        """Check if URL is a valid category URL."""
        parsed = urlparse(url)
        
        # Must be from the same domain
        if not url.startswith(self.base_url):
            return False
        
        # Skip common non-category URLs
        skip_patterns = [
            '/search',
            '/api/',
            '/assets/',
            '/images/',
            '/css/',
            '/js/',
            '/fonts/',
            '.pdf',
            '.zip',
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.svg',
            '.ico',
            'mailto:',
            'tel:',
            '#',
            'javascript:'
        ]
        
        for pattern in skip_patterns:
            if pattern in url.lower():
                return False
        
        # Must have some path content
        if parsed.path == '/' or len(parsed.path) < 2:
            return False
        
        return True
    
    def is_valid_article_url(self, url: str, category_url: str) -> bool:
        """Check if URL is a valid individual article URL."""
        # Must be from the same domain
        if not url.startswith(self.base_url):
            return False
        
        # Skip common non-article URLs
        skip_patterns = [
            '/search',
            '/api/',
            '/assets/',
            '/images/',
            '/css/',
            '/js/',
            '/fonts/',
            '.pdf',
            '.zip',
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.svg',
            '.ico',
            'mailto:',
            'tel:',
            '#',
            'javascript:'
        ]
        
        for pattern in skip_patterns:
            if pattern in url.lower():
                return False
        
        # Must be different from category URL (to avoid duplicates)
        if url == category_url:
            return False
        
        # Must have more specific path than category
        parsed_url = urlparse(url)
        parsed_category = urlparse(category_url)
        
        if len(parsed_url.path) <= len(parsed_category.path):
            return False
        
        return True
    
    def scrape_all_docs(self) -> List[Dict]:
        """Main method to scrape all documentation articles."""
        logging.info("Starting deep documentation scraping...")
        
        # Step 1: Find all category URLs
        logging.info("Step 1: Finding category URLs...")
        pages_to_visit = [self.docs_url]
        
        # Also try common documentation entry points
        common_paths = [
            "/docs/ov20i",
            "/docs/ov80i", 
            "/docs/ov20i-new-version",
            "/docs/hardware",
            "/docs/software",
            "/docs/walkthroughs",
            "/docs/plc-communication",
            "/docs/robots"
        ]
        
        for path in common_paths:
            full_url = urljoin(self.base_url, path)
            if full_url not in pages_to_visit:
                pages_to_visit.append(full_url)
        
        while pages_to_visit:
            current_url = pages_to_visit.pop(0)
            
            if current_url in self.visited_urls:
                continue
                
            self.visited_urls.add(current_url)
            
            soup = self.get_page_content(current_url)
            if not soup:
                continue
            
            # Extract category URLs from current page
            categories = self.extract_category_urls(soup, current_url)
            self.category_urls.extend(categories)
            
            # Add a small delay to be respectful
            time.sleep(1)
        
        # Remove duplicate categories
        seen_urls = set()
        unique_categories = []
        for category in self.category_urls:
            if category['url'] not in seen_urls:
                seen_urls.add(category['url'])
                unique_categories.append(category)
        
        self.category_urls = unique_categories
        logging.info(f"Found {len(self.category_urls)} category URLs")
        
        # Step 2: Visit each category and find individual articles
        logging.info("Step 2: Finding individual articles within categories...")
        for i, category in enumerate(self.category_urls, 1):
            logging.info(f"Processing category {i}/{len(self.category_urls)}: {category['title']}")
            
            soup = self.get_page_content(category['url'])
            if not soup:
                continue
            
            # Extract individual articles from this category
            articles = self.extract_individual_articles(soup, category['url'], category)
            self.article_urls.extend(articles)
            
            logging.info(f"  Found {len(articles)} individual articles in {category['title']}")
            
            # Add a small delay to be respectful
            time.sleep(1)
        
        # Remove duplicate articles
        seen_urls = set()
        unique_articles = []
        for article in self.article_urls:
            if article['url'] not in seen_urls:
                seen_urls.add(article['url'])
                unique_articles.append(article)
        
        self.article_urls = unique_articles
        logging.info(f"Found {len(self.article_urls)} unique individual articles")
        return self.article_urls
    
    def clean_html_for_markdown(self, soup: BeautifulSoup) -> str:
        """Clean HTML content for better Markdown conversion."""
        # Remove unwanted elements
        for element in soup.find_all(['script', 'style', 'nav', 'footer', '.sidebar', '.menu']):
            element.decompose()
        
        # Clean up common issues
        for element in soup.find_all(['div', 'span']):
            if not element.get_text(strip=True):
                element.decompose()
        
        return str(soup)
    
    def download_article_as_markdown(self, article: Dict) -> bool:
        """Download HTML content and convert to Markdown for RAG."""
        try:
            soup = self.get_page_content(article['url'])
            if not soup:
                return False
            
            # Clean HTML
            clean_html = self.clean_html_for_markdown(soup)
            
            # Convert to Markdown
            markdown_content = self.h2t.handle(clean_html)
            
            # Create frontmatter metadata
            frontmatter = f"""---
title: "{article['title']}"
category: "{article['category']}"
language: "{article['language']}"
url: "{article['url']}"
source_page: "{article['source_page']}"
parent_category: "{article.get('parent_category', {}).get('title', '')}"
is_individual_article: {article.get('is_individual_article', False)}
scraped_at: "{datetime.now().isoformat()}"
---

"""
            
            # Combine frontmatter and content
            full_markdown = frontmatter + markdown_content
            
            # Create a safe filename
            url_hash = hashlib.md5(article['url'].encode()).hexdigest()[:8]
            safe_title = re.sub(r'[^\w\s-]', '', article['title'])
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            filename = f"{url_hash}-{safe_title[:40]}.md"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save the Markdown content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_markdown)
            
            # Update article info with filename
            article['filename'] = filename
            article['filepath'] = filepath
            article['format'] = 'markdown'
            
            logging.info(f"Downloaded as Markdown: {filename}")
            return True
            
        except Exception as e:
            logging.error(f"Error downloading {article['url']}: {e}")
            return False
    
    def download_all_articles(self):
        """Download HTML content for all found articles as Markdown."""
        logging.info(f"Starting download of {len(self.article_urls)} articles as Markdown...")
        
        successful_downloads = 0
        for i, article in enumerate(self.article_urls, 1):
            logging.info(f"Downloading {i}/{len(self.article_urls)}: {article['title']}")
            
            if self.download_article_as_markdown(article):
                successful_downloads += 1
            
            # Add delay between downloads
            time.sleep(0.5)
        
        logging.info(f"Successfully downloaded {successful_downloads}/{len(self.article_urls)} articles as Markdown")
    
    def save_urls_to_json(self, filename: str = "deep_article_urls.json"):
        """Save all found URLs to a JSON file."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.article_urls, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Saved URLs to {filepath}")
    
    def generate_deep_summary_report(self):
        """Generate a summary report of the deep scraping results."""
        report = {
            'total_categories': len(self.category_urls),
            'total_individual_articles': len(self.article_urls),
            'languages': {},
            'categories': {},
            'scraping_timestamp': time.time(),
            'base_url': self.base_url,
            'format': 'markdown',
            'rag_ready': True
        }
        
        # Count articles by language and category
        for article in self.article_urls:
            language = article.get('language', 'English')
            category = article.get('category', 'General')
            
            if language not in report['languages']:
                report['languages'][language] = 0
            report['languages'][language] += 1
            
            if category not in report['categories']:
                report['categories'][category] = 0
            report['categories'][category] += 1
        
        # Save report
        report_path = os.path.join(self.output_dir, 'deep_scraping_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Generated deep summary report: {report_path}")
        return report
    
    def run(self):
        """Run the complete deep scraping process."""
        try:
            # Step 1: Find all category URLs
            self.scrape_all_docs()
            
            # Step 2: Save URLs to JSON
            self.save_urls_to_json()
            
            # Step 3: Download all articles as Markdown
            self.download_all_articles()
            
            # Step 4: Generate summary report
            report = self.generate_deep_summary_report()
            
            logging.info("Deep scraping completed successfully!")
            logging.info(f"Summary: {report['total_individual_articles']} individual articles in {len(report['languages'])} languages across {len(report['categories'])} categories")
            logging.info("All content saved as Markdown for optimal RAG chunking!")
            
        except Exception as e:
            logging.error(f"Error during scraping: {e}")
            raise

def main():
    """Main function to run the deep scraper."""
    scraper = DeepOverviewScraper()
    scraper.run()

if __name__ == "__main__":
    main() 