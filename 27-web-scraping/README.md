# Web Scraping in Python

Web scraping is the process of extracting data from websites. Python provides excellent libraries like `requests` for fetching web pages and `BeautifulSoup` for parsing HTML content.

## Table of Contents
1. [What is Web Scraping?](#what-is-web-scraping)
2. [The `requests` Library](#the-requests-library)
3. [Parsing HTML with BeautifulSoup](#parsing-html-with-beautifulsoup)
4. [Finding Elements](#finding-elements)
5. [Extracting Data](#extracting-data)
6. [Handling Forms and Authentication](#handling-forms-and-authentication)
7. [Best Practices and Ethics](#best-practices-and-ethics)
8. [Error Handling](#error-handling)

---

## What is Web Scraping?

**Web scraping** is the process of:
- **Fetching** web pages from the internet
- **Parsing** HTML/XML content
- **Extracting** specific data
- **Storing** or processing the extracted data

**Common Use Cases:**
- Price monitoring
- News aggregation
- Research data collection
- Social media analysis
- Job listings aggregation

**Important Notes:**
- Always check website's `robots.txt`
- Respect rate limits
- Follow terms of service
- Use APIs when available (preferred over scraping)

---

## The `requests` Library

The `requests` library makes HTTP requests simple.

### Basic GET Request

```python
import requests

# Simple GET request
response = requests.get('https://example.com')
print(response.status_code)  # 200
print(response.text)  # HTML content
```

### Response Object

```python
import requests

response = requests.get('https://example.com')

# Status code
print(response.status_code)

# Headers
print(response.headers)

# Content
print(response.text)  # Text content
print(response.content)  # Binary content
```

### Error Handling

```python
import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raises exception for bad status codes
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## Parsing HTML with BeautifulSoup

BeautifulSoup makes parsing HTML easy.

### Basic Parsing

```python
from bs4 import BeautifulSoup
import requests

# Fetch webpage
response = requests.get('https://example.com')
html = response.text

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Get page title
title = soup.title.string
print(title)
```

### Installing BeautifulSoup

```bash
pip install beautifulsoup4
pip install requests
```

---

## Finding Elements

### Finding by Tag Name

```python
from bs4 import BeautifulSoup

html = '<div class="content">Hello</div>'
soup = BeautifulSoup(html, 'html.parser')

# Find first div
div = soup.find('div')
print(div.text)  # Hello

# Find all divs
divs = soup.find_all('div')
```

### Finding by Class and ID

```python
from bs4 import BeautifulSoup

html = '<div class="content" id="main">Hello</div>'
soup = BeautifulSoup(html, 'html.parser')

# Find by class
content = soup.find('div', class_='content')

# Find by ID
main = soup.find(id='main')

# Find by multiple attributes
element = soup.find('div', class_='content', id='main')
```

### CSS Selectors

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# Use CSS selectors
elements = soup.select('.content')  # By class
elements = soup.select('#main')  # By ID
elements = soup.select('div.content')  # Tag with class
```

---

## Extracting Data

### Extracting Text

```python
from bs4 import BeautifulSoup

html = '<div>Hello <span>World</span></div>'
soup = BeautifulSoup(html, 'html.parser')

div = soup.find('div')
print(div.text)  # Hello World
print(div.get_text())  # Hello World
print(div.string)  # None (has child elements)
```

### Extracting Attributes

```python
from bs4 import BeautifulSoup

html = '<a href="https://example.com">Link</a>'
soup = BeautifulSoup(html, 'html.parser')

link = soup.find('a')
print(link['href'])  # https://example.com
print(link.get('href'))  # https://example.com (safer)
```

### Extracting Links

```python
from bs4 import BeautifulSoup
import requests

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f"{text}: {href}")
```

---

## Handling Forms and Authentication

### POST Requests

```python
import requests

# POST request with data
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://example.com/login', data=data)
```

### Headers

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html'
}
response = requests.get('https://example.com', headers=headers)
```

### Sessions

```python
import requests

# Use session to maintain cookies
session = requests.Session()
session.post('https://example.com/login', data={'user': 'alice'})
response = session.get('https://example.com/dashboard')
```

---

## Best Practices and Ethics

### 1. Check robots.txt

```python
import requests
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://example.com/robots.txt')
rp.read()

if rp.can_fetch('*', 'https://example.com/page'):
    # Scrape page
    pass
```

### 2. Use Rate Limiting

```python
import time
import requests

def scrape_with_delay(url, delay=1):
    response = requests.get(url)
    time.sleep(delay)  # Be polite
    return response
```

### 3. Set User-Agent

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Educational Bot)'
}
response = requests.get(url, headers=headers)
```

### 4. Handle Errors Gracefully

```python
import requests

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError:
    print("HTTP error occurred")
```

---

## Error Handling

### Common Exceptions

```python
import requests

try:
    response = requests.get('https://example.com')
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError:
    print("HTTP error")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
```

### Retry Logic

```python
import requests
import time

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
```

---

## Common Mistakes to Avoid

1. **Not checking robots.txt**
   ```python
   # Always check robots.txt first
   # Respect website policies
   ```

2. **Too aggressive scraping**
   ```python
   # Bad - no delay
   for url in urls:
       requests.get(url)
   
   # Good - with delay
   for url in urls:
       requests.get(url)
       time.sleep(1)
   ```

3. **Not handling errors**
   ```python
   # Bad
   response = requests.get(url)
   data = response.text
   
   # Good
   try:
       response = requests.get(url)
       response.raise_for_status()
       data = response.text
   except requests.exceptions.RequestException as e:
       print(f"Error: {e}")
   ```

---

## Summary

- **Web scraping** extracts data from websites
- Use `requests` for fetching web pages
- Use `BeautifulSoup` for parsing HTML
- **Always respect** robots.txt and rate limits
- **Handle errors** gracefully
- **Use APIs** when available (preferred)
- **Be ethical** and follow terms of service

**Remember**: Web scraping should be done responsibly. Always check if an API is available first!

---

## Next Steps

Now that you understand web scraping:
1. Practice with the examples in this folder
2. Learn about more advanced techniques
3. Explore Selenium for JavaScript-heavy sites
4. Move on to **28-api-development** to learn API development

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_web_scraping_basics.py`: Understanding web scraping concepts
2. `02_requests_library.py`: Using the requests library
3. `03_beautifulsoup_parsing.py`: Parsing HTML with BeautifulSoup
4. `04_finding_elements.py`: Finding and selecting elements
5. `05_extracting_data.py`: Extracting text, links, and attributes
6. `06_practical_examples.py`: Real-world web scraping examples

Run these files in order to see web scraping in action!

