"""
REST API Project

This file demonstrates a simple REST API implementation.
"""

# ============================================================================
# 1. BASIC API STRUCTURE
# ============================================================================
print("=" * 60)
print("1. BASIC API STRUCTURE")
print("=" * 60)

print("  REST API components:")
print("    - Web framework (Flask/FastAPI)")
print("    - Routes/endpoints")
print("    - Request handling")
print("    - Response formatting")
print("    - Error handling")
print("  ")
print("  Example with Flask:")
print("    ")
print("    from flask import Flask, jsonify")
print("    ")
print("    app = Flask(__name__)")
print("    ")
print("    @app.route('/api/users', methods=['GET'])")
print("    def get_users():")
print("        return jsonify([{'id': 1, 'name': 'Alice'}])")

print()  # Empty line


# ============================================================================
# 2. API MODELS
# ============================================================================
print("=" * 60)
print("2. API MODELS")
print("=" * 60)

class User:
    """User model"""
    
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class UserRepository:
    """User data repository"""
    
    def __init__(self):
        self.users = []
        self.next_id = 1
    
    def create(self, name: str, email: str):
        """Create new user"""
        user = User(self.next_id, name, email)
        self.next_id += 1
        self.users.append(user)
        return user
    
    def get_all(self):
        """Get all users"""
        return self.users
    
    def get_by_id(self, user_id: int):
        """Get user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def update(self, user_id: int, name: str = None, email: str = None):
        """Update user"""
        user = self.get_by_id(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
        return user
    
    def delete(self, user_id: int):
        """Delete user"""
        self.users = [u for u in self.users if u.id != user_id]

repo = UserRepository()
repo.create("Alice", "alice@example.com")
repo.create("Bob", "bob@example.com")
print(f"  Users: {len(repo.get_all())}")

print()  # Empty line


# ============================================================================
# 3. API ENDPOINTS
# ============================================================================
print("=" * 60)
print("3. API ENDPOINTS")
print("=" * 60)

class APIHandler:
    """API request handler"""
    
    def __init__(self, repository: UserRepository):
        self.repo = repository
    
    def get_users(self):
        """GET /api/users"""
        users = self.repo.get_all()
        return {'users': [u.to_dict() for u in users]}
    
    def get_user(self, user_id: int):
        """GET /api/users/{id}"""
        user = self.repo.get_by_id(user_id)
        if user:
            return {'user': user.to_dict()}
        return {'error': 'User not found'}, 404
    
    def create_user(self, data: dict):
        """POST /api/users"""
        name = data.get('name')
        email = data.get('email')
        if not name or not email:
            return {'error': 'Name and email required'}, 400
        user = self.repo.create(name, email)
        return {'user': user.to_dict()}, 201
    
    def update_user(self, user_id: int, data: dict):
        """PUT /api/users/{id}"""
        user = self.repo.update(user_id, data.get('name'), data.get('email'))
        if user:
            return {'user': user.to_dict()}
        return {'error': 'User not found'}, 404
    
    def delete_user(self, user_id: int):
        """DELETE /api/users/{id}"""
        user = self.repo.get_by_id(user_id)
        if user:
            self.repo.delete(user_id)
            return {'message': 'User deleted'}, 200
        return {'error': 'User not found'}, 404

handler = APIHandler(repo)
print("  APIHandler with CRUD operations")
print(f"  GET users: {handler.get_users()}")

print()  # Empty line


# ============================================================================
# 4. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("4. ERROR HANDLING")
print("=" * 60)

class APIError(Exception):
    """Custom API error"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def handle_api_error(error: APIError):
    """Handle API errors"""
    return {'error': error.message}, error.status_code

print("  API error handling:")
print("    - Custom exceptions")
print("    - Proper status codes")
print("    - Error messages")
print("    - Validation errors")

print()  # Empty line


# ============================================================================
# 5. API WITH FLASK EXAMPLE
# ============================================================================
print("=" * 60)
print("5. API WITH FLASK EXAMPLE")
print("=" * 60)

print("  Flask API example structure:")
print("    ")
print("    from flask import Flask, request, jsonify")
print("    ")
print("    app = Flask(__name__)")
print("    handler = APIHandler(repo)")
print("    ")
print("    @app.route('/api/users', methods=['GET'])")
print("    def get_users():")
print("        return jsonify(handler.get_users())")
print("    ")
print("    @app.route('/api/users', methods=['POST'])")
print("    def create_user():")
print("        data = request.json")
print("        return jsonify(handler.create_user(data))")
print("    ")
print("    if __name__ == '__main__':")
print("        app.run(debug=True)")

print()  # Empty line


# ============================================================================
# 6. API WITH FASTAPI EXAMPLE
# ============================================================================
print("=" * 60)
print("6. API WITH FASTAPI EXAMPLE")
print("=" * 60)

print("  FastAPI example structure:")
print("    ")
print("    from fastapi import FastAPI")
print("    from pydantic import BaseModel")
print("    ")
print("    app = FastAPI()")
print("    ")
print("    class UserCreate(BaseModel):")
print("        name: str")
print("        email: str")
print("    ")
print("    @app.get('/api/users')")
print("    def get_users():")
print("        return handler.get_users()")
print("    ")
print("    @app.post('/api/users')")
print("    def create_user(user: UserCreate):")
print("        return handler.create_user(user.dict())")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("API PROJECT SUMMARY:")
print("=" * 60)
print("Key Features:")
print("  - RESTful API design")
print("  - CRUD operations")
print("  - Data models and repositories")
print("  - Error handling")
print("  - Request/response handling")
print("  - Framework integration (Flask/FastAPI)")
print("  - API documentation")
print("=" * 60)

