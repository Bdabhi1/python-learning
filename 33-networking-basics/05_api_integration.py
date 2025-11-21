"""
API Integration in Python

This file demonstrates how to work with REST APIs.
"""

import json

# ============================================================================
# 1. WHAT IS API INTEGRATION?
# ============================================================================
print("=" * 60)
print("1. WHAT IS API INTEGRATION?")
print("=" * 60)

print("  API integration involves:")
print("    - Making requests to REST APIs")
print("    - Handling responses")
print("    - Error handling")
print("    - Authentication")
print("    - Rate limiting")
print("    - Pagination")

print()  # Empty line


# ============================================================================
# 2. BASIC API CLIENT
# ============================================================================
print("=" * 60)
print("2. BASIC API CLIENT")
print("=" * 60)

class APIClient:
    """Simple API client"""
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        url = f"{self.base_url}/{endpoint}"
        print(f"    GET {url}")
        print(f"    Headers: {self.headers}")
        if params:
            print(f"    Params: {params}")
        return {"status": "success", "data": "example"}
    
    def post(self, endpoint, data=None):
        """Make POST request"""
        url = f"{self.base_url}/{endpoint}"
        print(f"    POST {url}")
        print(f"    Data: {data}")
        return {"status": "created", "data": data}

print("  Basic API client example:")
client = APIClient('https://api.example.com', api_key='your-key')
result = client.get('users', params={'page': 1})
print(f"    Result: {result}")

print()  # Empty line


# ============================================================================
# 3. API CLIENT WITH requests
# ============================================================================
print("=" * 60)
print("3. API CLIENT WITH requests")
print("=" * 60)

try:
    import requests
    
    class RequestsAPIClient:
        """API client using requests"""
        def __init__(self, base_url, api_key=None):
            self.base_url = base_url
            self.session = requests.Session()
            if api_key:
                self.session.headers.update({'Authorization': f'Bearer {api_key}'})
        
        def get(self, endpoint, params=None):
            """GET request"""
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        
        def post(self, endpoint, data=None):
            """POST request"""
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data, timeout=5)
            response.raise_for_status()
            return response.json()
        
        def close(self):
            """Close session"""
            self.session.close()
    
    print("  API client with requests library:")
    print("    - Session for connection pooling")
    print("    - Automatic JSON handling")
    print("    - Error handling with raise_for_status()")
    print("    - Timeout support")
    
except ImportError:
    print("  requests library not installed")
    print("  Install with: pip install requests")

print()  # Empty line


# ============================================================================
# 4. HANDLING PAGINATION
# ============================================================================
print("=" * 60)
print("4. HANDLING PAGINATION")
print("=" * 60)

def get_all_pages(base_url, endpoint, max_pages=10):
    """Fetch all pages from paginated API"""
    all_data = []
    page = 1
    
    print(f"    Fetching pages from {endpoint}...")
    
    while page <= max_pages:
        print(f"    Fetching page {page}...")
        # Simulate API call
        # response = requests.get(f"{base_url}/{endpoint}", params={'page': page})
        # data = response.json()
        
        # Simulated response
        if page > 3:  # Simulate no more pages
            break
        
        data = [{'id': i, 'page': page} for i in range(10)]
        all_data.extend(data)
        page += 1
    
    print(f"    Fetched {len(all_data)} items from {page-1} pages")
    return all_data

result = get_all_pages('https://api.example.com', 'users')
print(f"  Total items: {len(result)}")

print()  # Empty line


# ============================================================================
# 5. RATE LIMITING
# ============================================================================
print("=" * 60)
print("5. RATE LIMITING")
print("=" * 60)

import time

class RateLimitedClient:
    """API client with rate limiting"""
    def __init__(self, requests_per_second=10):
        self.requests_per_second = requests_per_second
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0
    
    def request(self, method, url, **kwargs):
        """Make request with rate limiting"""
        # Wait if necessary
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_interval:
            sleep_time = self.min_interval - elapsed
            print(f"    Rate limiting: waiting {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
        print(f"    {method} {url}")
        return {"status": "success"}

print("  Rate limiting example:")
client = RateLimitedClient(requests_per_second=2)
for i in range(5):
    client.request('GET', f'https://api.example.com/data/{i}')

print()  # Empty line


# ============================================================================
# 6. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("6. ERROR HANDLING")
print("=" * 60)

try:
    import requests
    from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
    
    def safe_api_call(url):
        """Make API call with error handling"""
        try:
            # response = requests.get(url, timeout=5)
            # response.raise_for_status()
            # return response.json()
            print(f"    Making request to {url}...")
            return {"status": "success"}
        except ConnectionError:
            print("    Error: Could not connect to server")
            return None
        except Timeout:
            print("    Error: Request timed out")
            return None
        except HTTPError as e:
            print(f"    Error: HTTP {e.response.status_code}")
            return None
        except RequestException as e:
            print(f"    Error: {e}")
            return None
    
    result = safe_api_call('https://api.example.com/data')
    
except ImportError:
    print("  requests library not installed")

print()  # Empty line


# ============================================================================
# 7. AUTHENTICATION
# ============================================================================
print("=" * 60)
print("7. AUTHENTICATION")
print("=" * 60)

print("  Common authentication methods:")
print("    - API Key: X-API-Key header")
print("    - Bearer Token: Authorization: Bearer <token>")
print("    - Basic Auth: username:password")
print("    - OAuth: Token-based authentication")
print("  ")
print("  Example with API key:")
print("    headers = {'X-API-Key': 'your-api-key'}")
print("    response = requests.get(url, headers=headers)")
print("  ")
print("  Example with Bearer token:")
print("    headers = {'Authorization': 'Bearer your-token'}")
print("    response = requests.get(url, headers=headers)")

print()  # Empty line


# ============================================================================
# 8. ASYNC API REQUESTS
# ============================================================================
print("=" * 60)
print("8. ASYNC API REQUESTS")
print("=" * 60)

try:
    import asyncio
    import aiohttp
    
    async def fetch_url_async(session, url):
        """Async fetch URL"""
        async with session.get(url) as response:
            return await response.json()
    
    async def fetch_multiple_apis(urls):
        """Fetch multiple APIs concurrently"""
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url_async(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            return results
    
    print("  Async API requests with aiohttp:")
    print("    - Concurrent requests")
    print("    - Better performance for multiple APIs")
    print("    - Install: pip install aiohttp")
    
except ImportError:
    print("  aiohttp not installed")
    print("  Install with: pip install aiohttp")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("API INTEGRATION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use requests library for HTTP requests")
print("  - Handle errors properly (ConnectionError, Timeout, HTTPError)")
print("  - Implement rate limiting to avoid API limits")
print("  - Handle pagination for large datasets")
print("  - Use authentication (API keys, Bearer tokens)")
print("  - Use sessions for multiple requests")
print("  - Consider async requests for concurrent calls")
print("  - Always set timeouts")
print("=" * 60)

