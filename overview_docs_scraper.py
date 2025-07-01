#!/usr/bin/env python3
"""
Overview AI Documentation Scraper
Scrapes all article URLs from https://docs.overview.ai/docs and downloads their HTML content.
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import json
from urllib.parse import urljoin, urlparse
import re
from typing import List, Dict, Set
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

class OverviewDocsScraper:
    def __init__(self, base_url: str = "https://docs.overview.ai/docs"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.visited_urls: Set[str] = set()
        self.article_urls: List[Dict] = []
        self.output_dir = "overview_docs"
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
    def get_page_content(self, url: str) -> BeautifulSoup:
        """Fetch and parse a web page."""
        try:
            logging.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_article_urls_from_page(self, soup: BeautifulSoup, page_url: str) -> List[Dict]:
        """Extract article URLs from a documentation page."""
        articles = []
        
        # Look for various patterns that might contain article links
        selectors = [
            'a[href*="/docs/"]',  # Links containing /docs/
            'a[href*="article"]',  # Links containing "article"
            '.article-link',       # Common article link class
            '.docs-link',          # Common docs link class
            'nav a',               # Navigation links
            '.sidebar a',          # Sidebar links
            '.menu a',             # Menu links
        ]
        
        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(page_url, href)
                    
                    # Skip if already visited or not a valid docs URL
                    if full_url in self.visited_urls:
                        continue
                    
                    # Check if it's a valid documentation URL
                    if self.is_valid_docs_url(full_url):
                        title = link.get_text(strip=True) or link.get('title', '')
                        articles.append({
                            'url': full_url,
                            'title': title,
                            'source_page': page_url
                        })
                        self.visited_urls.add(full_url)
        
        return articles
    
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
            '.pdf',
            '.zip',
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.svg'
        ]
        
        for pattern in skip_patterns:
            if pattern in url.lower():
                return False
        
        return True
    
    def find_navigation_links(self, soup: BeautifulSoup, page_url: str) -> List[str]:
        """Find navigation links to other documentation pages."""
        nav_urls = []
        
        # Look for pagination, next/previous links, or category links
        nav_selectors = [
            'a[href*="page"]',
            'a[href*="category"]',
            '.pagination a',
            '.next',
            '.prev',
            '.category-link'
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
        logging.info("Starting documentation scraping...")
        
        # Start with the main docs page
        pages_to_visit = [self.base_url]
        
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
        
        logging.info(f"Found {len(self.article_urls)} article URLs")
        return self.article_urls
    
    def download_article_content(self, article: Dict) -> bool:
        """Download HTML content for a single article."""
        try:
            soup = self.get_page_content(article['url'])
            if not soup:
                return False
            
            # Create a safe filename
            safe_title = re.sub(r'[^\w\s-]', '', article['title'])
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            filename = f"{safe_title[:50]}.html"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save the HTML content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
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
    
    def save_urls_to_json(self, filename: str = "article_urls.json"):
        """Save all found URLs to a JSON file."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.article_urls, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Saved URLs to {filepath}")
    
    def run(self):
        """Run the complete scraping process."""
        try:
            # Step 1: Find all article URLs
            self.scrape_all_docs()
            
            # Step 2: Save URLs to JSON
            self.save_urls_to_json()
            
            # Step 3: Download all articles
            self.download_all_articles()
            
            logging.info("Scraping completed successfully!")
            
        except Exception as e:
            logging.error(f"Error during scraping: {e}")
            raise

def main():
    """Main function to run the scraper."""
    scraper = OverviewDocsScraper()
    scraper.run()

if __name__ == "__main__":
    main() 