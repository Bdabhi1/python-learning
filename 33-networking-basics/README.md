# Networking Basics in Python

Networking is fundamental to modern applications. Python provides excellent libraries for network programming, from low-level socket programming to high-level HTTP clients. This guide covers networking concepts, socket programming, HTTP clients and servers, and working with APIs.

## Table of Contents
1. [What is Networking?](#what-is-networking)
2. [Socket Programming](#socket-programming)
3. [HTTP Clients](#http-clients)
4. [HTTP Servers](#http-servers)
5. [Working with URLs](#working-with-urls)
6. [Working with APIs](#working-with-apis)
7. [Best Practices](#best-practices)

---

## What is Networking?

**Networking** is the practice of connecting computers to share resources and communicate. In Python, networking typically involves:
- **Sockets**: Low-level network communication
- **HTTP**: Web protocols for client-server communication
- **APIs**: Application Programming Interfaces for data exchange
- **Protocols**: Rules for data transmission (TCP, UDP, HTTP, HTTPS)

**Key Concepts:**
- **Client**: Requests data or services
- **Server**: Provides data or services
- **Socket**: Endpoint for network communication
- **Protocol**: Rules for communication
- **Port**: Number identifying a service
- **IP Address**: Unique identifier for a device

**Why Learn Networking?**
- **Web Development**: Build web applications
- **API Integration**: Connect to external services
- **Distributed Systems**: Build scalable applications
- **Data Exchange**: Share data between systems

---

## Socket Programming

**Sockets** are the fundamental building blocks of network communication in Python.

### TCP Socket Server

```python
import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address and port
server_socket.bind(('localhost', 12345))

# Listen for connections
server_socket.listen(5)
print("Server listening on port 12345...")

while True:
    # Accept connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")
    
    # Receive data
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    
    # Send response
    client_socket.send(b"Message received!")
    
    # Close connection
    client_socket.close()
```

### TCP Socket Client

```python
import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))

# Send data
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive response
response = client_socket.recv(1024)
print(f"Server response: {response.decode()}")

# Close connection
client_socket.close()
```

### UDP Socket Server

```python
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and port
server_socket.bind(('localhost', 12346))
print("UDP Server listening on port 12346...")

while True:
    # Receive data (no connection needed)
    data, address = server_socket.recvfrom(1024)
    print(f"Received from {address}: {data.decode()}")
    
    # Send response
    response = "Message received!"
    server_socket.sendto(response.encode(), address)
```

### UDP Socket Client

```python
import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data (no connection needed)
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), ('localhost', 12346))

# Receive response
response, server_address = client_socket.recvfrom(1024)
print(f"Server response: {response.decode()}")

# Close socket
client_socket.close()
```

### Socket with Context Manager

```python
import socket

# Using context manager for automatic cleanup
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 12347))
    s.listen(5)
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        conn.sendall(data)  # Echo back
```

---

## HTTP Clients

Python provides several ways to make HTTP requests.

### Using `urllib`

```python
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json

# Simple GET request
response = urlopen('https://api.github.com/users/octocat')
data = json.loads(response.read().decode())
print(data)

# POST request
url = 'https://httpbin.org/post'
data = {'key': 'value'}
data_encoded = urlencode(data).encode()

request = Request(url, data=data_encoded, method='POST')
response = urlopen(request)
print(response.read().decode())
```

### Using `requests` Library

```python
import requests

# GET request
response = requests.get('https://api.github.com/users/octocat')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# POST request
data = {'name': 'John', 'age': 30}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())

# With headers
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com/data', headers=headers)

# With parameters
params = {'page': 1, 'limit': 10}
response = requests.get('https://api.example.com/users', params=params)
```

### Handling Responses

```python
import requests

response = requests.get('https://api.github.com/users/octocat')

# Status code
print(f"Status: {response.status_code}")

# Headers
print(f"Headers: {response.headers}")

# Content
print(f"Text: {response.text}")
print(f"JSON: {response.json()}")

# Check if request was successful
if response.status_code == 200:
    print("Success!")
else:
    print(f"Error: {response.status_code}")
```

### Error Handling

```python
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad status codes
    data = response.json()
except ConnectionError:
    print("Connection error - could not reach server")
except HTTPError:
    print(f"HTTP error: {response.status_code}")
except RequestException as e:
    print(f"Request failed: {e}")
```

### Session for Multiple Requests

```python
import requests

# Session maintains cookies and connection pooling
session = requests.Session()

# Set default headers
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Make multiple requests
response1 = session.get('https://api.example.com/login')
response2 = session.get('https://api.example.com/data')  # Uses same session

session.close()
```

---

## HTTP Servers

Python provides tools to create HTTP servers.

### Simple HTTP Server

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, World!</h1>')
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "received"}')

# Start server
server = HTTPServer(('localhost', 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
```

### Using Flask (Simple Web Framework)

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My API</h1>'

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({'id': 3, 'name': data['name']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Using FastAPI (Modern Web Framework)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Alice"}

@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} created", "age": user.age}
```

---

## Working with URLs

Python provides tools to parse and manipulate URLs.

### URL Parsing

```python
from urllib.parse import urlparse, urlunparse, urljoin, urlencode

# Parse URL
url = "https://www.example.com:8080/path/to/page?param=value#fragment"
parsed = urlparse(url)

print(f"Scheme: {parsed.scheme}")      # https
print(f"Netloc: {parsed.netloc}")      # www.example.com:8080
print(f"Path: {parsed.path}")          # /path/to/page
print(f"Query: {parsed.query}")        # param=value
print(f"Fragment: {parsed.fragment}")  # fragment

# Reconstruct URL
reconstructed = urlunparse(parsed)
print(reconstructed)
```

### URL Encoding/Decoding

```python
from urllib.parse import urlencode, quote, unquote, parse_qs

# Encode parameters
params = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
encoded = urlencode(params)
print(encoded)  # name=John+Doe&age=30&city=New+York

# Quote individual values
name = quote("John Doe")
print(name)  # John%20Doe

# Decode
decoded = unquote("John%20Doe")
print(decoded)  # John Doe

# Parse query string
query_string = "name=John+Doe&age=30"
parsed = parse_qs(query_string)
print(parsed)  # {'name': ['John Doe'], 'age': ['30']}
```

### URL Joining

```python
from urllib.parse import urljoin

base = "https://www.example.com/path/"
relative = "to/page.html"

# Join URLs
full_url = urljoin(base, relative)
print(full_url)  # https://www.example.com/path/to/page.html

# Absolute URL
absolute = urljoin(base, "/absolute/path.html")
print(absolute)  # https://www.example.com/absolute/path.html
```

---

## Working with APIs

APIs (Application Programming Interfaces) allow applications to communicate.

### REST API Client

```python
import requests

class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def close(self):
        self.session.close()

# Usage
client = APIClient('https://api.example.com', api_key='your-key')
users = client.get('users', params={'page': 1})
new_user = client.post('users', data={'name': 'Alice'})
client.close()
```

### Handling Pagination

```python
import requests

def get_all_pages(base_url, endpoint):
    all_data = []
    page = 1
    
    while True:
        response = requests.get(f"{base_url}/{endpoint}", params={'page': page})
        data = response.json()
        
        if not data:  # No more data
            break
        
        all_data.extend(data)
        page += 1
    
    return all_data

# Usage
all_users = get_all_pages('https://api.example.com', 'users')
```

### Rate Limiting

```python
import requests
import time

class RateLimitedClient:
    def __init__(self, requests_per_second=10):
        self.requests_per_second = requests_per_second
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0
    
    def request(self, *args, **kwargs):
        # Wait if necessary
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        
        self.last_request_time = time.time()
        return requests.request(*args, **kwargs)

# Usage
client = RateLimitedClient(requests_per_second=5)
response = client.request('GET', 'https://api.example.com/data')
```

### Async HTTP Requests

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = [
    'https://api.example.com/users/1',
    'https://api.example.com/users/2',
    'https://api.example.com/users/3'
]

results = asyncio.run(fetch_multiple_urls(urls))
```

---

## Best Practices

### 1. Always Use Timeouts

```python
import requests

# Good - prevents hanging
response = requests.get('https://api.example.com/data', timeout=5)

# Bad - may hang indefinitely
response = requests.get('https://api.example.com/data')
```

### 2. Handle Errors Properly

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    # Handle error appropriately
```

### 3. Use Sessions for Multiple Requests

```python
import requests

# Good - reuses connections
session = requests.Session()
for url in urls:
    response = session.get(url)
# session.close()

# Less efficient - new connection each time
for url in urls:
    response = requests.get(url)
```

### 4. Validate and Sanitize URLs

```python
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

# Usage
if is_valid_url(user_input):
    response = requests.get(user_input)
```

### 5. Use Context Managers

```python
import socket

# Good - automatic cleanup
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345))
    s.sendall(b'Hello')

# Less preferred
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))
s.sendall(b'Hello')
s.close()  # Must remember to close
```

### 6. Don't Expose Sensitive Data

```python
import os

# Good - use environment variables
api_key = os.getenv('API_KEY')
headers = {'Authorization': f'Bearer {api_key}'}

# Bad - hardcoded
headers = {'Authorization': 'Bearer secret-key-12345'}
```

---

## Common Mistakes to Avoid

1. **Not handling connection errors**
   ```python
   # Wrong
   response = requests.get('https://api.example.com/data')
   data = response.json()
   
   # Correct
   try:
       response = requests.get('https://api.example.com/data', timeout=5)
       response.raise_for_status()
       data = response.json()
   except requests.exceptions.RequestException as e:
       print(f"Error: {e}")
   ```

2. **Not using timeouts**
   ```python
   # Wrong - may hang
   response = requests.get('https://api.example.com/data')
   
   # Correct
   response = requests.get('https://api.example.com/data', timeout=5)
   ```

3. **Not closing sockets**
   ```python
   # Wrong
   s = socket.socket()
   s.connect(('localhost', 12345))
   # Forgot to close
   
   # Correct
   with socket.socket() as s:
       s.connect(('localhost', 12345))
   ```

4. **Hardcoding URLs and credentials**
   ```python
   # Wrong
   api_key = "secret-key"
   url = "https://api.example.com"
   
   # Correct
   api_key = os.getenv('API_KEY')
   url = os.getenv('API_URL', 'https://api.example.com')
   ```

5. **Not validating responses**
   ```python
   # Wrong
   response = requests.get('https://api.example.com/data')
   data = response.json()  # May fail if status != 200
   
   # Correct
   response = requests.get('https://api.example.com/data')
   response.raise_for_status()
   data = response.json()
   ```

---

## Summary

- **Networking** enables communication between applications
- **Sockets** provide low-level network communication
- **HTTP clients** (requests, urllib) make web requests easy
- **HTTP servers** can be built with http.server, Flask, or FastAPI
- **URL parsing** helps work with web addresses
- **APIs** enable application-to-application communication
- **Always use timeouts** and handle errors
- **Use sessions** for multiple requests
- **Validate inputs** and sanitize URLs

**Remember**: Networking is powerful but requires careful error handling and security considerations!

---

## Next Steps

Now that you understand networking basics:
1. Practice with the examples in this folder
2. Build simple client-server applications
3. Work with real APIs (GitHub, Twitter, etc.)
4. Create your own REST API
5. Explore more advanced networking topics

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_socket_programming.py`: Understanding sockets - start here!
2. `02_http_clients.py`: Making HTTP requests with urllib and requests
3. `03_http_servers.py`: Creating HTTP servers
4. `04_url_handling.py`: Parsing and manipulating URLs
5. `05_api_integration.py`: Working with REST APIs
6. `06_practical_examples.py`: Real-world networking examples

Run these files in order to see networking in action!

