"""
Handling Requests and Responses

This file demonstrates reading request data and sending responses.
"""

# ============================================================================
# 1. READING REQUEST DATA
# ============================================================================
print("=" * 60)
print("1. READING REQUEST DATA")
print("=" * 60)

print("  Get request data:")
print("    from flask import request")
print("    ")
print("    # JSON data")
print("    data = request.get_json()")
print("    ")
print("    # Query parameters")
print("    name = request.args.get('name')")
print("    ")
print("    # Form data")
print("    email = request.form.get('email')")
print("    ")
print("    # Headers")
print("    token = request.headers.get('Authorization')")

print()  # Empty line


# ============================================================================
# 2. SENDING RESPONSES
# ============================================================================
print("=" * 60)
print("2. SENDING RESPONSES")
print("=" * 60)

print("  Return responses:")
print("    # JSON response")
print("    return jsonify({'message': 'Success'})")
print("    ")
print("    # With status code")
print("    return jsonify({'error': 'Not found'}), 404")
print("    ")
print("    # Custom headers")
print("    response = jsonify({'data': data})")
print("    response.headers['Custom-Header'] = 'value'")
print("    return response")

print()  # Empty line


# ============================================================================
# 3. QUERY PARAMETERS
# ============================================================================
print("=" * 60)
print("3. QUERY PARAMETERS")
print("=" * 60)

print("  Handle query parameters:")
print("    @app.route('/api/users')")
print("    def get_users():")
print("        page = request.args.get('page', 1, type=int)")
print("        limit = request.args.get('limit', 10, type=int)")
print("        # Use for pagination")

print()  # Empty line


# ============================================================================
# 4. REQUEST VALIDATION
# ============================================================================
print("=" * 60)
print("4. REQUEST VALIDATION")
print("=" * 60)

print("  Validate request data:")
print("    data = request.get_json()")
print("    ")
print("    if not data:")
print("        return jsonify({'error': 'No data provided'}), 400")
print("    ")
print("    if 'name' not in data:")
print("        return jsonify({'error': 'Name required'}), 400")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("REQUEST/RESPONSE SUMMARY:")
print("=" * 60)
print("  - request.get_json(): Get JSON data")
print("  - request.args: Query parameters")
print("  - request.form: Form data")
print("  - request.headers: Request headers")
print("  - jsonify(): Return JSON response")
print("=" * 60)

