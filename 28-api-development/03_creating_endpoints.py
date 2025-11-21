"""
Creating API Endpoints

This file demonstrates creating different types of API endpoints.
"""

# ============================================================================
# 1. GET ENDPOINT
# ============================================================================
print("=" * 60)
print("1. GET ENDPOINT")
print("=" * 60)

print("  GET endpoint (retrieve data):")
print("    @app.route('/api/users', methods=['GET'])")
print("    def get_users():")
print("        users = [{'id': 1, 'name': 'Alice'}]")
print("        return jsonify(users)")

print()  # Empty line


# ============================================================================
# 2. POST ENDPOINT
# ============================================================================
print("=" * 60)
print("2. POST ENDPOINT")
print("=" * 60)

print("  POST endpoint (create resource):")
print("    @app.route('/api/users', methods=['POST'])")
print("    def create_user():")
print("        data = request.get_json()")
print("        # Process and create user")
print("        return jsonify(new_user), 201")

print()  # Empty line


# ============================================================================
# 3. PUT ENDPOINT
# ============================================================================
print("=" * 60)
print("3. PUT ENDPOINT")
print("=" * 60)

print("  PUT endpoint (update resource):")
print("    @app.route('/api/users/<int:user_id>', methods=['PUT'])")
print("    def update_user(user_id):")
print("        data = request.get_json()")
print("        # Update user")
print("        return jsonify(updated_user)")

print()  # Empty line


# ============================================================================
# 4. DELETE ENDPOINT
# ============================================================================
print("=" * 60)
print("4. DELETE ENDPOINT")
print("=" * 60)

print("  DELETE endpoint (delete resource):")
print("    @app.route('/api/users/<int:user_id>', methods=['DELETE'])")
print("    def delete_user(user_id):")
print("        # Delete user")
print("        return '', 204  # No content")

print()  # Empty line


# ============================================================================
# 5. DYNAMIC ROUTES
# ============================================================================
print("=" * 60)
print("5. DYNAMIC ROUTES")
print("=" * 60)

print("  Route parameters:")
print("    @app.route('/api/users/<int:user_id>')")
print("    def get_user(user_id):")
print("        # user_id is automatically converted to int")
print("        return jsonify({'id': user_id})")
print("  ")
print("  Type converters:")
print("    <int:id>     # Integer")
print("    <string:name> # String (default)")
print("    <float:price> # Float")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CREATING ENDPOINTS SUMMARY:")
print("=" * 60)
print("  - GET: Retrieve data")
print("  - POST: Create resource")
print("  - PUT: Update resource")
print("  - DELETE: Delete resource")
print("  - Use dynamic routes with <parameter>")
print("=" * 60)

