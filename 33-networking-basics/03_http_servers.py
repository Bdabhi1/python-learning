"""
HTTP Servers in Python

This file demonstrates how to create HTTP servers in Python.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# ============================================================================
# 1. WHAT IS AN HTTP SERVER?
# ============================================================================
print("=" * 60)
print("1. WHAT IS AN HTTP SERVER?")
print("=" * 60)

print("  HTTP servers handle incoming HTTP requests and send responses.")
print("  ")
print("  Python options:")
print("    - http.server: Built-in simple server")
print("    - Flask: Lightweight web framework")
print("    - FastAPI: Modern async web framework")
print("    - Django: Full-featured web framework")

print()  # Empty line


# ============================================================================
# 2. SIMPLE HTTP SERVER
# ============================================================================
print("=" * 60)
print("2. SIMPLE HTTP SERVER")
print("=" * 60)

class SimpleHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler"""
    
    def do_GET(self):
        """Handle GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, World!</h1>')
        print("    GET request handled")
    
    def do_POST(self):
        """Handle POST requests"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'status': 'received', 'data': post_data.decode()})
        self.wfile.write(response.encode())
        print("    POST request handled")
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        pass  # Suppress default logging

print("  Simple HTTP server example:")
print("    class SimpleHandler(BaseHTTPRequestHandler):")
print("        def do_GET(self):")
print("            # Handle GET request")
print("    ")
print("    server = HTTPServer(('localhost', 8000), SimpleHandler)")
print("    server.serve_forever()")
print("  ")
print("  (Server not started - this is a demonstration)")

print()  # Empty line


# ============================================================================
# 3. REST API SERVER
# ============================================================================
print("=" * 60)
print("3. REST API SERVER")
print("=" * 60)

class APIHandler(BaseHTTPRequestHandler):
    """REST API handler"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/api/users':
            users = [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'}
            ]
            self._send_json_response(200, users)
        elif self.path.startswith('/api/users/'):
            user_id = self.path.split('/')[-1]
            user = {'id': int(user_id), 'name': f'User {user_id}'}
            self._send_json_response(200, user)
        else:
            self._send_json_response(404, {'error': 'Not found'})
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/api/users':
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length).decode())
            new_user = {'id': 3, 'name': post_data.get('name', 'Unknown')}
            self._send_json_response(201, new_user)
        else:
            self._send_json_response(404, {'error': 'Not found'})
    
    def _send_json_response(self, status_code, data):
        """Helper to send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        pass

print("  REST API server example:")
print("    - GET /api/users - Get all users")
print("    - GET /api/users/1 - Get user by ID")
print("    - POST /api/users - Create new user")
print("  ")
print("  (Server not started - this is a demonstration)")

print()  # Empty line


# ============================================================================
# 4. FLASK WEB FRAMEWORK
# ============================================================================
print("=" * 60)
print("4. FLASK WEB FRAMEWORK")
print("=" * 60)

print("  Flask is a lightweight web framework.")
print("  Install with: pip install flask")
print("  ")
print("  Basic Flask example:")
print("    from flask import Flask, jsonify")
print("    ")
print("    app = Flask(__name__)")
print("    ")
print("    @app.route('/')")
print("    def home():")
print("        return '<h1>Welcome</h1>'")
print("    ")
print("    @app.route('/api/users', methods=['GET'])")
print("    def get_users():")
print("        return jsonify([{'id': 1, 'name': 'Alice'}])")
print("    ")
print("    if __name__ == '__main__':")
print("        app.run(debug=True, port=5000)")

# Check if Flask is available
try:
    from flask import Flask, jsonify, request
    print("  ")
    print("    Flask is available!")
except ImportError:
    print("  ")
    print("    Flask not installed (install with: pip install flask)")

print()  # Empty line


# ============================================================================
# 5. FASTAPI WEB FRAMEWORK
# ============================================================================
print("=" * 60)
print("5. FASTAPI WEB FRAMEWORK")
print("=" * 60)

print("  FastAPI is a modern, fast web framework.")
print("  Install with: pip install fastapi uvicorn")
print("  ")
print("  Basic FastAPI example:")
print("    from fastapi import FastAPI")
print("    ")
print("    app = FastAPI()")
print("    ")
print("    @app.get('/')")
print("    def read_root():")
print("        return {'message': 'Hello, World!'}")
print("    ")
print("    @app.get('/users/{user_id}')")
print("    def get_user(user_id: int):")
print("        return {'user_id': user_id}")
print("  ")
print("    Run with: uvicorn main:app --reload")

# Check if FastAPI is available
try:
    from fastapi import FastAPI
    print("  ")
    print("    FastAPI is available!")
except ImportError:
    print("  ")
    print("    FastAPI not installed (install with: pip install fastapi uvicorn)")

print()  # Empty line


# ============================================================================
# 6. HANDLING DIFFERENT HTTP METHODS
# ============================================================================
print("=" * 60)
print("6. HANDLING DIFFERENT HTTP METHODS")
print("=" * 60)

class MethodHandler(BaseHTTPRequestHandler):
    """Handler for different HTTP methods"""
    
    def do_GET(self):
        """Handle GET"""
        self._send_response(200, {'method': 'GET', 'message': 'Retrieve data'})
    
    def do_POST(self):
        """Handle POST"""
        self._send_response(201, {'method': 'POST', 'message': 'Create resource'})
    
    def do_PUT(self):
        """Handle PUT"""
        self._send_response(200, {'method': 'PUT', 'message': 'Update resource'})
    
    def do_DELETE(self):
        """Handle DELETE"""
        self._send_response(200, {'method': 'DELETE', 'message': 'Delete resource'})
    
    def _send_response(self, status, data):
        """Helper method"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        pass

print("  HTTP methods:")
print("    - GET: Retrieve data")
print("    - POST: Create new resource")
print("    - PUT: Update entire resource")
print("    - PATCH: Partial update")
print("    - DELETE: Delete resource")

print()  # Empty line


# ============================================================================
# 7. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("7. ERROR HANDLING")
print("=" * 60)

class ErrorHandler(BaseHTTPRequestHandler):
    """Handler with error handling"""
    
    def do_GET(self):
        """Handle GET with error handling"""
        try:
            if self.path == '/error':
                raise ValueError("Intentional error")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok'}).encode())
        except Exception as e:
            self.send_error(500, str(e))
    
    def log_message(self, format, *args):
        pass

print("  Error handling in servers:")
print("    - Use try-except blocks")
print("    - Send appropriate status codes")
print("    - Return error messages in JSON")
print("    - Log errors for debugging")

print()  # Empty line


# ============================================================================
# 8. STATIC FILES
# ============================================================================
print("=" * 60)
print("8. STATIC FILES")
print("=" * 60)

print("  Serving static files:")
print("    - HTML files")
print("    - CSS files")
print("    - JavaScript files")
print("    - Images")
print("  ")
print("  Using http.server:")
print("    python -m http.server 8000")
print("  ")
print("  Or with custom handler:")
print("    class StaticHandler(BaseHTTPRequestHandler):")
print("        def do_GET(self):")
print("            # Serve static files")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("HTTP SERVERS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - http.server: Built-in simple server")
print("  - Flask: Lightweight framework")
print("  - FastAPI: Modern async framework")
print("  - Handle different HTTP methods (GET, POST, PUT, DELETE)")
print("  - Return appropriate status codes")
print("  - Handle errors gracefully")
print("  - Use JSON for API responses")
print("  - Serve static files when needed")
print("=" * 60)

