# API Development in Python

API (Application Programming Interface) development allows you to create web services that other applications can interact with. Python provides excellent frameworks like Flask and FastAPI for building REST APIs.

## Table of Contents
1. [What is an API?](#what-is-an-api)
2. [REST API Basics](#rest-api-basics)
3. [Flask Framework](#flask-framework)
4. [Creating Endpoints](#creating-endpoints)
5. [Request and Response](#request-and-response)
6. [Error Handling](#error-handling)
7. [API Best Practices](#api-best-practices)
8. [Testing APIs](#testing-apis)

---

## What is an API?

**API (Application Programming Interface)** is:
- A **contract** between applications
- A way for applications to **communicate**
- **Endpoints** that accept requests and return responses
- **Stateless** communication (each request is independent)

**Types of APIs:**
- **REST API**: Representational State Transfer (most common)
- **GraphQL**: Query language for APIs
- **SOAP**: XML-based protocol

**REST API Characteristics:**
- Uses HTTP methods (GET, POST, PUT, DELETE)
- Returns JSON (usually)
- Stateless
- Resource-based URLs

---

## REST API Basics

### HTTP Methods

- **GET**: Retrieve data
- **POST**: Create new resource
- **PUT**: Update entire resource
- **PATCH**: Partial update
- **DELETE**: Delete resource

### Status Codes

- **200**: OK (success)
- **201**: Created
- **400**: Bad Request
- **404**: Not Found
- **500**: Internal Server Error

---

## Flask Framework

Flask is a lightweight web framework for Python.

### Basic Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
```

### Installing Flask

```bash
pip install flask
```

---

## Creating Endpoints

### GET Endpoint

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ]
    return jsonify(users)
```

### POST Endpoint

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # Process data
    new_user = {'id': 3, 'name': data['name']}
    return jsonify(new_user), 201
```

### Dynamic Routes

```python
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = {'id': user_id, 'name': 'Alice'}
    return jsonify(user)
```

---

## Request and Response

### Reading Request Data

```python
from flask import request

# JSON data
data = request.get_json()

# Query parameters
name = request.args.get('name')

# Form data
email = request.form.get('email')

# Headers
token = request.headers.get('Authorization')
```

### Sending Responses

```python
from flask import jsonify

# JSON response
return jsonify({'message': 'Success'})

# With status code
return jsonify({'error': 'Not found'}), 404

# Custom headers
response = jsonify({'data': data})
response.headers['Custom-Header'] = 'value'
return response
```

---

## Error Handling

### Custom Error Handlers

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

### Validation

```python
from flask import request, jsonify

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    # Process valid data
    return jsonify({'message': 'User created'}), 201
```

---

## API Best Practices

### 1. Use Proper HTTP Methods

```python
# GET for retrieval
@app.route('/api/users', methods=['GET'])

# POST for creation
@app.route('/api/users', methods=['POST'])

# PUT for updates
@app.route('/api/users/<id>', methods=['PUT'])

# DELETE for deletion
@app.route('/api/users/<id>', methods=['DELETE'])
```

### 2. Return Proper Status Codes

```python
# Success
return jsonify(data), 200

# Created
return jsonify(data), 201

# Bad request
return jsonify({'error': 'Invalid data'}), 400

# Not found
return jsonify({'error': 'Not found'}), 404
```

### 3. Use JSON for Data Exchange

```python
# Always return JSON
return jsonify({'data': data})

# Accept JSON
data = request.get_json()
```

### 4. Version Your API

```python
# Version in URL
@app.route('/api/v1/users')

# Or in headers
version = request.headers.get('API-Version')
```

---

## Testing APIs

### Using requests Library

```python
import requests

# Test GET endpoint
response = requests.get('http://localhost:5000/api/users')
print(response.json())

# Test POST endpoint
data = {'name': 'Alice'}
response = requests.post('http://localhost:5000/api/users', json=data)
print(response.status_code)
```

### Using curl

```bash
# GET request
curl http://localhost:5000/api/users

# POST request
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
```

---

## Common Mistakes to Avoid

1. **Not validating input**
   ```python
   # Wrong
   data = request.get_json()
   name = data['name']  # May raise KeyError
   
   # Correct
   data = request.get_json()
   if not data or 'name' not in data:
       return jsonify({'error': 'Name required'}), 400
   ```

2. **Not using proper status codes**
   ```python
   # Wrong
   return jsonify({'error': 'Not found'}), 200
   
   # Correct
   return jsonify({'error': 'Not found'}), 404
   ```

3. **Not handling errors**
   ```python
   # Wrong
   user = get_user(id)  # May raise exception
   
   # Correct
   try:
       user = get_user(id)
   except UserNotFound:
       return jsonify({'error': 'User not found'}), 404
   ```

---

## Summary

- **APIs** allow applications to communicate
- **REST APIs** use HTTP methods and return JSON
- **Flask** is a lightweight framework for building APIs
- **Use proper HTTP methods** (GET, POST, PUT, DELETE)
- **Return appropriate status codes**
- **Validate input** and handle errors
- **Version your API** for compatibility

**Remember**: Good APIs are well-documented, consistent, and follow REST principles!

---

## Next Steps

Now that you understand API development:
1. Practice with the examples in this folder
2. Build your own REST API
3. Learn about API authentication and security
4. Explore FastAPI for modern async APIs

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_api_basics.py`: Understanding APIs and REST principles
2. `02_flask_setup.py`: Setting up Flask and basic routes
3. `03_creating_endpoints.py`: Creating GET, POST, PUT, DELETE endpoints
4. `04_request_response.py`: Handling requests and sending responses
5. `05_error_handling.py`: Error handling and validation
6. `06_practical_examples.py`: Real-world API examples

Run these files in order to see API development in action!

