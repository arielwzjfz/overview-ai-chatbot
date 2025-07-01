#!/usr/bin/env python3
"""
Enhanced Overview AI Documentation Scraper
Specifically designed for https://docs.overview.ai/docs with advanced features.
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import json
from urllib.parse import urljoin, urlparse, parse_qs
import re
from typing import List, Dict, Set, Optional
import logging
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('enhanced_scraper.log'),
        logging.StreamHandler()
    ]
)

class EnhancedOverviewScraper:
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
        self.article_urls: List[Dict] = []
        self.output_dir = "overview_docs_enhanced"
        self.max_retries = 3
        self.retry_delay = 2
        
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
    
    def extract_article_urls_from_page(self, soup: BeautifulSoup, page_url: str) -> List[Dict]:
        """Extract article URLs from a documentation page with enhanced selectors."""
        articles = []
        
        # Enhanced selectors for Overview AI docs
        selectors = [
            # General documentation links
            'a[href*="/docs/"]',
            'a[href*="article"]',
            
            # Specific to Overview AI structure
            'a[href*="ov20i"]',
            'a[href*="ov80i"]',
            'a[href*="ov20i-new-version"]',
            'a[href*="hardware"]',
            'a[href*="software"]',
            'a[href*="walkthrough"]',
            'a[href*="plc"]',
            'a[href*="robot"]',
            'a[href*="faq"]',
            'a[href*="drawings"]',
            'a[href*="quick-start"]',
            'a[href*="overview-software"]',
            'a[href*="tools"]',
            'a[href*="electrical"]',
            'a[href*="node-red"]',
            
            # Common documentation patterns
            '.article-link',
            '.docs-link',
            '.content-link',
            'nav a',
            '.sidebar a',
            '.menu a',
            '.toc a',
            '.navigation a',
            
            # Breadcrumb and category links
            '.breadcrumb a',
            '.category-link',
            '.section-link',
            
            # Search result links
            '.search-result a',
            '.result-link'
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
                    
                    # Check if it's a valid documentation URL
                    if self.is_valid_docs_url(full_url):
                        title = self.extract_title(link)
                        category = self.extract_category(link, soup)
                        
                        article_info = {
                            'url': full_url,
                            'title': title,
                            'category': category,
                            'source_page': page_url,
                            'link_text': link.get_text(strip=True),
                            'link_classes': ' '.join(link.get('class', [])),
                            'timestamp': time.time()
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
    
    def is_valid_docs_url(self, url: str) -> bool:
        """Check if URL is a valid documentation article URL."""
        parsed = urlparse(url)
        
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
        
        # Must have some path content
        if parsed.path == '/' or len(parsed.path) < 2:
            return False
        
        return True
    
    def find_navigation_links(self, soup: BeautifulSoup, page_url: str) -> List[str]:
        """Find navigation links to other documentation pages."""
        nav_urls = []
        
        # Enhanced navigation selectors
        nav_selectors = [
            'a[href*="page"]',
            'a[href*="category"]',
            'a[href*="section"]',
            '.pagination a',
            '.next',
            '.prev',
            '.category-link',
            '.section-link',
            '.breadcrumb a',
            '.toc a',
            'nav a',
            '.navigation a'
        ]
        
        for selector in nav_selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(page_url, href)
                    if full_url not in self.visited_urls and self.is_valid_docs_url(full_url):
                        nav_urls.append(full_url)
        
        return nav_urls
    
    def scrape_all_docs(self) -> List[Dict]:
        """Main method to scrape all documentation articles."""
        logging.info("Starting enhanced documentation scraping...")
        
        # Start with the main docs page
        pages_to_visit = [self.docs_url]
        
        # Also try common documentation entry points
        common_paths = [
            "/docs/ov20i",
            "/docs/ov80i", 
            "/docs/ov20i-new-version",  # Add the new OV20i (2.0) section
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
            
            # Extract article URLs from current page
            articles = self.extract_article_urls_from_page(soup, current_url)
            self.article_urls.extend(articles)
            
            # Find navigation links for further exploration
            nav_links = self.find_navigation_links(soup, current_url)
            pages_to_visit.extend(nav_links)
            
            # Add a small delay to be respectful
            time.sleep(1)
        
        # Remove duplicates based on URL
        seen_urls = set()
        unique_articles = []
        for article in self.article_urls:
            if article['url'] not in seen_urls:
                seen_urls.add(article['url'])
                unique_articles.append(article)
        
        self.article_urls = unique_articles
        logging.info(f"Found {len(self.article_urls)} unique article URLs")
        return self.article_urls
    
    def download_article_content(self, article: Dict) -> bool:
        """Download HTML content for a single article."""
        try:
            soup = self.get_page_content(article['url'])
            if not soup:
                return False
            
            # Create a safe filename using URL hash and title
            url_hash = hashlib.md5(article['url'].encode()).hexdigest()[:8]
            safe_title = re.sub(r'[^\w\s-]', '', article['title'])
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            filename = f"{url_hash}-{safe_title[:40]}.html"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save the HTML content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            # Update article info with filename
            article['filename'] = filename
            article['filepath'] = filepath
            
            logging.info(f"Downloaded: {filename}")
            return True
            
        except Exception as e:
            logging.error(f"Error downloading {article['url']}: {e}")
            return False
    
    def download_all_articles(self):
        """Download HTML content for all found articles."""
        logging.info(f"Starting download of {len(self.article_urls)} articles...")
        
        successful_downloads = 0
        for i, article in enumerate(self.article_urls, 1):
            logging.info(f"Downloading {i}/{len(self.article_urls)}: {article['title']}")
            
            if self.download_article_content(article):
                successful_downloads += 1
            
            # Add delay between downloads
            time.sleep(0.5)
        
        logging.info(f"Successfully downloaded {successful_downloads}/{len(self.article_urls)} articles")
    
    def save_urls_to_json(self, filename: str = "article_urls_enhanced.json"):
        """Save all found URLs to a JSON file."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.article_urls, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Saved URLs to {filepath}")
    
    def generate_summary_report(self):
        """Generate a summary report of the scraping results."""
        report = {
            'total_articles': len(self.article_urls),
            'categories': {},
            'scraping_timestamp': time.time(),
            'base_url': self.base_url
        }
        
        # Count articles by category
        for article in self.article_urls:
            category = article.get('category', 'General')
            if category not in report['categories']:
                report['categories'][category] = 0
            report['categories'][category] += 1
        
        # Save report
        report_path = os.path.join(self.output_dir, 'scraping_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Generated summary report: {report_path}")
        return report
    
    def run(self):
        """Run the complete enhanced scraping process."""
        try:
            # Step 1: Find all article URLs
            self.scrape_all_docs()
            
            # Step 2: Save URLs to JSON
            self.save_urls_to_json()
            
            # Step 3: Download all articles
            self.download_all_articles()
            
            # Step 4: Generate summary report
            report = self.generate_summary_report()
            
            logging.info("Enhanced scraping completed successfully!")
            logging.info(f"Summary: {report['total_articles']} articles found across {len(report['categories'])} categories")
            
        except Exception as e:
            logging.error(f"Error during scraping: {e}")
            raise

def main():
    """Main function to run the enhanced scraper."""
    scraper = EnhancedOverviewScraper()
    scraper.run()

if __name__ == "__main__":
    main() 