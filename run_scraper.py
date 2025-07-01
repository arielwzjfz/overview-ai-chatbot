#!/usr/bin/env python3
"""
Simple script to run the Overview AI documentation scraper
"""

import sys
import argparse
from overview_docs_scraper import OverviewDocsScraper
from enhanced_overview_scraper import EnhancedOverviewScraper

def main():
    parser = argparse.ArgumentParser(description='Scrape Overview AI documentation')
    parser.add_argument('--mode', choices=['basic', 'enhanced'], default='enhanced',
                       help='Scraping mode: basic or enhanced (default: enhanced)')
    parser.add_argument('--urls-only', action='store_true',
                       help='Only extract URLs, do not download content')
    parser.add_argument('--output-dir', default=None,
                       help='Custom output directory')
    
    args = parser.parse_args()
    
    if args.mode == 'basic':
        scraper = OverviewDocsScraper()
    else:
        scraper = EnhancedOverviewScraper()
    
    if args.output_dir:
        scraper.output_dir = args.output_dir
        import os
        os.makedirs(args.output_dir, exist_ok=True)
    
    try:
        if args.urls_only:
            # Only extract URLs
            print("Extracting article URLs...")
            articles = scraper.scrape_all_docs()
            scraper.save_urls_to_json()
            print(f"Found {len(articles)} articles. URLs saved to JSON file.")
        else:
            # Full scraping
            print("Starting full scraping process...")
            scraper.run()
            print("Scraping completed successfully!")
            
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error during scraping: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 