"""
Error Handling in APIs

This file demonstrates error handling and validation in APIs.
"""

# ============================================================================
# 1. CUSTOM ERROR HANDLERS
# ============================================================================
print("=" * 60)
print("1. CUSTOM ERROR HANDLERS")
print("=" * 60)

print("  Define error handlers:")
print("    @app.errorhandler(404)")
print("    def not_found(error):")
print("        return jsonify({'error': 'Not found'}), 404")
print("    ")
print("    @app.errorhandler(500)")
print("    def internal_error(error):")
print("        return jsonify({'error': 'Internal server error'}), 500")

print()  # Empty line


# ============================================================================
# 2. INPUT VALIDATION
# ============================================================================
print("=" * 60)
print("2. INPUT VALIDATION")
print("=" * 60)

print("  Validate input data:")
print("    @app.route('/api/users', methods=['POST'])")
print("    def create_user():")
print("        data = request.get_json()")
print("        ")
print("        if not data:")
print("            return jsonify({'error': 'No data'}), 400")
print("        ")
print("        if 'name' not in data:")
print("            return jsonify({'error': 'Name required'}), 400")
print("        ")
print("        # Process valid data")

print()  # Empty line


# ============================================================================
# 3. TRY-EXCEPT BLOCKS
# ============================================================================
print("=" * 60)
print("3. TRY-EXCEPT BLOCKS")
print("=" * 60)

print("  Handle exceptions:")
print("    try:")
print("        user = get_user(user_id)")
print("        return jsonify(user)")
print("    except UserNotFound:")
print("        return jsonify({'error': 'User not found'}), 404")
print("    except Exception as e:")
print("        return jsonify({'error': str(e)}), 500")

print()  # Empty line


# ============================================================================
# 4. PROPER STATUS CODES
# ============================================================================
print("=" * 60)
print("4. PROPER STATUS CODES")
print("=" * 60)

print("  Use appropriate status codes:")
print("    - 200: Success")
print("    - 201: Created")
print("    - 400: Bad Request (validation error)")
print("    - 404: Not Found")
print("    - 500: Internal Server Error")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ERROR HANDLING SUMMARY:")
print("=" * 60)
print("  - Use @app.errorhandler() for custom error pages")
print("  - Validate all input data")
print("  - Use try-except for exception handling")
print("  - Return appropriate status codes")
print("=" * 60)

