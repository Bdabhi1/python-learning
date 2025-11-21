"""
HTTP Clients in Python

This file demonstrates how to make HTTP requests using various methods.
"""

import urllib.request
import urllib.parse
import json

# ============================================================================
# 1. WHAT IS AN HTTP CLIENT?
# ============================================================================
print("=" * 60)
print("1. WHAT IS AN HTTP CLIENT?")
print("=" * 60)

print("  HTTP clients are programs that make requests to web servers.")
print("  ")
print("  Common use cases:")
print("    - Fetching web pages")
print("    - Calling REST APIs")
print("    - Downloading files")
print("    - Submitting forms")
print("  ")
print("  Python libraries:")
print("    - urllib: Built-in library")
print("    - requests: Popular third-party library")

print()  # Empty line


# ============================================================================
# 2. USING urllib FOR GET REQUESTS
# ============================================================================
print("=" * 60)
print("2. USING urllib FOR GET REQUESTS")
print("=" * 60)

def urllib_get_example():
    """Example using urllib for GET request"""
    try:
        url = 'https://httpbin.org/get'
        print(f"    Making GET request to {url}...")
        
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(f"    Status Code: {response.getcode()}")
            print(f"    Response length: {len(data)} bytes")
            print("    (Response received successfully)")
    except Exception as e:
        print(f"    Error: {e}")

urllib_get_example()

print()  # Empty line


# ============================================================================
# 3. USING urllib FOR POST REQUESTS
# ============================================================================
print("=" * 60)
print("3. USING urllib FOR POST REQUESTS")
print("=" * 60)

def urllib_post_example():
    """Example using urllib for POST request"""
    try:
        url = 'https://httpbin.org/post'
        data = {'key': 'value', 'name': 'Python'}
        data_encoded = urllib.parse.urlencode(data).encode()
        
        print(f"    Making POST request to {url}...")
        print(f"    Data: {data}")
        
        request = urllib.request.Request(url, data=data_encoded, method='POST')
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode())
            print(f"    Status Code: {response.getcode()}")
            print("    (POST request successful)")
    except Exception as e:
        print(f"    Error: {e}")

urllib_post_example()

print()  # Empty line


# ============================================================================
# 4. USING requests LIBRARY
# ============================================================================
print("=" * 60)
print("4. USING requests LIBRARY")
print("=" * 60)

print("  The requests library is more user-friendly than urllib.")
print("  Install with: pip install requests")
print("  ")
print("  Basic usage:")
print("    import requests")
print("    response = requests.get('https://api.example.com/data')")
print("    data = response.json()")

# Check if requests is available
try:
    import requests
    
    def requests_get_example():
        """Example using requests for GET"""
        try:
            url = 'https://httpbin.org/get'
            print(f"    Making GET request to {url}...")
            
            response = requests.get(url, timeout=5)
            print(f"    Status Code: {response.status_code}")
            print(f"    Response: {len(response.text)} characters")
            print("    (Request successful)")
        except Exception as e:
            print(f"    Error: {e}")
    
    requests_get_example()
    
except ImportError:
    print("    requests library not installed")
    print("    Install with: pip install requests")

print()  # Empty line


# ============================================================================
# 5. POST REQUEST WITH requests
# ============================================================================
print("=" * 60)
print("5. POST REQUEST WITH requests")
print("=" * 60)

try:
    import requests
    
    def requests_post_example():
        """Example using requests for POST"""
        try:
            url = 'https://httpbin.org/post'
            data = {'name': 'John', 'age': 30}
            
            print(f"    Making POST request to {url}...")
            print(f"    Data: {data}")
            
            response = requests.post(url, json=data, timeout=5)
            print(f"    Status Code: {response.status_code}")
            print("    (POST request successful)")
        except Exception as e:
            print(f"    Error: {e}")
    
    requests_post_example()
    
except ImportError:
    print("    requests library not installed")

print()  # Empty line


# ============================================================================
# 6. REQUEST HEADERS
# ============================================================================
print("=" * 60)
print("6. REQUEST HEADERS")
print("=" * 60)

try:
    import requests
    
    def headers_example():
        """Example with custom headers"""
        try:
            url = 'https://httpbin.org/headers'
            headers = {
                'User-Agent': 'MyApp/1.0',
                'Authorization': 'Bearer token123'
            }
            
            print("    Making request with custom headers...")
            response = requests.get(url, headers=headers, timeout=5)
            print(f"    Status Code: {response.status_code}")
            print("    (Request with headers successful)")
        except Exception as e:
            print(f"    Error: {e}")
    
    headers_example()
    
except ImportError:
    print("    requests library not installed")

print()  # Empty line


# ============================================================================
# 7. REQUEST PARAMETERS
# ============================================================================
print("=" * 60)
print("7. REQUEST PARAMETERS")
print("=" * 60)

try:
    import requests
    
    def parameters_example():
        """Example with URL parameters"""
        try:
            url = 'https://httpbin.org/get'
            params = {'page': 1, 'limit': 10, 'sort': 'name'}
            
            print("    Making request with parameters...")
            print(f"    Parameters: {params}")
            
            response = requests.get(url, params=params, timeout=5)
            print(f"    Status Code: {response.status_code}")
            print("    (Request with parameters successful)")
        except Exception as e:
            print(f"    Error: {e}")
    
    parameters_example()
    
except ImportError:
    print("    requests library not installed")

print()  # Empty line


# ============================================================================
# 8. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("8. ERROR HANDLING")
print("=" * 60)

try:
    import requests
    from requests.exceptions import RequestException, HTTPError, ConnectionError
    
    def error_handling_example():
        """Example of error handling"""
        try:
            response = requests.get('https://httpbin.org/status/404', timeout=5)
            response.raise_for_status()  # Raises HTTPError for bad status codes
            print("    Request successful")
        except HTTPError as e:
            print(f"    HTTP Error: {e}")
        except ConnectionError:
            print("    Connection error - could not reach server")
        except RequestException as e:
            print(f"    Request failed: {e}")
    
    error_handling_example()
    
except ImportError:
    print("    requests library not installed")

print()  # Empty line


# ============================================================================
# 9. SESSIONS
# ============================================================================
print("=" * 60)
print("9. SESSIONS")
print("=" * 60)

try:
    import requests
    
    def session_example():
        """Example using sessions"""
        print("    Sessions maintain cookies and connection pooling")
        print("    More efficient for multiple requests")
        
        session = requests.Session()
        session.headers.update({'User-Agent': 'MyApp/1.0'})
        
        print("    Session created with default headers")
        print("    (Use session.get/post for multiple requests)")
        
        session.close()
    
    session_example()
    
except ImportError:
    print("    requests library not installed")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("HTTP CLIENTS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - urllib is built-in but more verbose")
print("  - requests is more user-friendly (needs installation)")
print("  - Use GET for retrieving data")
print("  - Use POST for sending data")
print("  - Set headers for authentication and metadata")
print("  - Use parameters for URL query strings")
print("  - Always handle errors properly")
print("  - Use sessions for multiple requests")
print("  - Set timeouts to prevent hanging")
print("=" * 60)

