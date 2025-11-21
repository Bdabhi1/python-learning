"""
Practical API Examples

This file demonstrates real-world API development patterns.
"""

# ============================================================================
# 1. COMPLETE CRUD API EXAMPLE
# ============================================================================
print("=" * 60)
print("1. COMPLETE CRUD API EXAMPLE")
print("=" * 60)

print("  Full CRUD API structure:")
print("    GET    /api/users          # List all users")
print("    GET    /api/users/<id>     # Get specific user")
print("    POST   /api/users          # Create user")
print("    PUT    /api/users/<id>     # Update user")
print("    DELETE /api/users/<id>     # Delete user")

print()  # Empty line


# ============================================================================
# 2. PAGINATION
# ============================================================================
print("=" * 60)
print("2. PAGINATION")
print("=" * 60)

print("  Implement pagination:")
print("    @app.route('/api/users')")
print("    def get_users():")
print("        page = request.args.get('page', 1, type=int)")
print("        per_page = request.args.get('per_page', 10, type=int)")
print("        # Fetch paginated data")
print("        return jsonify({")
print("            'data': users,")
print("            'page': page,")
print("            'per_page': per_page")
print("        })")

print()  # Empty line


# ============================================================================
# 3. SEARCH AND FILTERING
# ============================================================================
print("=" * 60)
print("3. SEARCH AND FILTERING")
print("=" * 60)

print("  Add search functionality:")
print("    @app.route('/api/users')")
print("    def get_users():")
print("        search = request.args.get('search')")
print("        age_min = request.args.get('age_min', type=int)")
print("        # Filter users based on parameters")
print("        return jsonify(filtered_users)")

print()  # Empty line


# ============================================================================
# 4. API DOCUMENTATION
# ============================================================================
print("=" * 60)
print("4. API DOCUMENTATION")
print("=" * 60)

print("  Document your API:")
print("    - Use docstrings for endpoints")
print("    - Document request/response formats")
print("    - List all available endpoints")
print("    - Include example requests/responses")
print("    - Consider using Swagger/OpenAPI")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("API development best practices:")
print("  - Implement full CRUD operations")
print("  - Add pagination for large datasets")
print("  - Support search and filtering")
print("  - Document your API")
print("  - Use consistent response format")
print("=" * 60)

