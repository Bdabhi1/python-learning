"""
Web Scraper Project

This file demonstrates a simple web scraper implementation.
"""

# ============================================================================
# 1. BASIC WEB SCRAPER
# ============================================================================
print("=" * 60)
print("1. BASIC WEB SCRAPER")
print("=" * 60)

print("  Web scraper components:")
print("    - HTTP requests (requests library)")
print("    - HTML parsing (BeautifulSoup)")
print("    - Data extraction")
print("    - Data storage")
print("  ")
print("  Example structure:")
print("    ")
print("    import requests")
print("    from bs4 import BeautifulSoup")
print("    ")
print("    def scrape_url(url):")
print("        response = requests.get(url)")
print("        soup = BeautifulSoup(response.content, 'html.parser')")
print("        # Extract data")
print("        return data")

print()  # Empty line


# ============================================================================
# 2. SCRAPER CLASS
# ============================================================================
print("=" * 60)
print("2. SCRAPER CLASS")
print("=" * 60)

class WebScraper:
    """Basic web scraper"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    
    def fetch_page(self, url: str):
        """Fetch page content"""
        print(f"    Fetching: {url}")
        # In real implementation:
        # response = requests.get(url, headers=self.headers)
        # return response.content
        return "<html>...</html>"
    
    def parse_html(self, html: str):
        """Parse HTML content"""
        print("    Parsing HTML...")
        # In real implementation:
        # soup = BeautifulSoup(html, 'html.parser')
        # return soup
        return None
    
    def extract_data(self, soup):
        """Extract data from parsed HTML"""
        print("    Extracting data...")
        # Extract specific elements
        return []

scraper = WebScraper("https://example.com")
print("  WebScraper class created")
print("  (Install: pip install requests beautifulsoup4)")

print()  # Empty line


# ============================================================================
# 3. DATA EXTRACTION
# ============================================================================
print("=" * 60)
print("3. DATA EXTRACTION")
print("=" * 60)

class DataExtractor:
    """Extract specific data from HTML"""
    
    def extract_links(self, soup):
        """Extract all links"""
        # In real implementation:
        # links = soup.find_all('a')
        # return [link.get('href') for link in links]
        return []
    
    def extract_text(self, soup, selector: str):
        """Extract text by CSS selector"""
        # In real implementation:
        # elements = soup.select(selector)
        # return [elem.get_text() for elem in elements]
        return []
    
    def extract_attributes(self, soup, tag: str, attribute: str):
        """Extract specific attribute from tags"""
        # In real implementation:
        # elements = soup.find_all(tag)
        # return [elem.get(attribute) for elem in elements]
        return []

extractor = DataExtractor()
print("  DataExtractor for extracting specific data")

print()  # Empty line


# ============================================================================
# 4. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("4. ERROR HANDLING")
print("=" * 60)

class RobustScraper(WebScraper):
    """Scraper with error handling"""
    
    def fetch_page_safe(self, url: str, retries: int = 3):
        """Fetch page with retry logic"""
        for attempt in range(retries):
            try:
                print(f"    Attempt {attempt + 1}...")
                # response = requests.get(url, headers=self.headers, timeout=10)
                # response.raise_for_status()
                return "<html>...</html>"
            except Exception as e:
                print(f"    Error: {e}")
                if attempt == retries - 1:
                    raise
        return None
    
    def extract_safe(self, soup, selector: str):
        """Extract with error handling"""
        try:
            # elements = soup.select(selector)
            # return [elem.get_text() for elem in elements]
            return []
        except Exception as e:
            print(f"    Extraction error: {e}")
            return []

robust_scraper = RobustScraper("https://example.com")
print("  RobustScraper with error handling")

print()  # Empty line


# ============================================================================
# 5. DATA STORAGE
# ============================================================================
print("=" * 60)
print("5. DATA STORAGE")
print("=" * 60)

import json
import csv

class ScraperWithStorage(WebScraper):
    """Scraper with data storage"""
    
    def save_json(self, data: list, filename: str):
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"    Saved {len(data)} items to {filename}")
    
    def save_csv(self, data: list, filename: str):
        """Save data to CSV file"""
        if not data:
            return
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"    Saved {len(data)} items to {filename}")

storage_scraper = ScraperWithStorage("https://example.com")
print("  ScraperWithStorage can save to JSON/CSV")

print()  # Empty line


# ============================================================================
# 6. RATE LIMITING
# ============================================================================
print("=" * 60)
print("6. RATE LIMITING")
print("=" * 60)

import time

class RateLimitedScraper(WebScraper):
    """Scraper with rate limiting"""
    
    def __init__(self, base_url: str, delay: float = 1.0):
        super().__init__(base_url)
        self.delay = delay
        self.last_request_time = 0
    
    def fetch_with_delay(self, url: str):
        """Fetch with rate limiting"""
        # Wait if necessary
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            sleep_time = self.delay - elapsed
            print(f"    Rate limiting: waiting {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
        return self.fetch_page(url)

rate_limited = RateLimitedScraper("https://example.com", delay=2.0)
print("  RateLimitedScraper respects rate limits")
print("  Important: Be respectful when scraping!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("WEB SCRAPER SUMMARY:")
print("=" * 60)
print("Key Features:")
print("  - HTTP requests")
print("  - HTML parsing")
print("  - Data extraction")
print("  - Error handling")
print("  - Data storage (JSON/CSV)")
print("  - Rate limiting")
print("  - Respect robots.txt and terms of service")
print("=" * 60)

