"""
Flask Setup and Basic Routes

This file demonstrates setting up Flask and creating basic routes.
"""

# Note: Install Flask with: pip install flask

# ============================================================================
# 1. BASIC FLASK APP
# ============================================================================
print("=" * 60)
print("1. BASIC FLASK APP")
print("=" * 60)

print("  Basic Flask application:")
print("    from flask import Flask")
print("    ")
print("    app = Flask(__name__)")
print("    ")
print("    @app.route('/')")
print("    def hello():")
print("        return {'message': 'Hello, World!'}")
print("    ")
print("    if __name__ == '__main__':")
print("        app.run(debug=True)")

print()  # Empty line


# ============================================================================
# 2. ROUTE DECORATORS
# ============================================================================
print("=" * 60)
print("2. ROUTE DECORATORS")
print("=" * 60)

print("  @app.route() decorator:")
print("    @app.route('/')              # Root path")
print("    @app.route('/api/users')     # Specific path")
print("    @app.route('/api/users/<id>') # Dynamic path")

print()  # Empty line


# ============================================================================
# 3. RETURNING JSON
# ============================================================================
print("=" * 60)
print("3. RETURNING JSON")
print("=" * 60)

print("  Use jsonify for JSON responses:")
print("    from flask import jsonify")
print("    ")
print("    @app.route('/api/data')")
print("    def get_data():")
print("        return jsonify({'message': 'Success'})")

print()  # Empty line


# ============================================================================
# 4. RUNNING THE APP
# ============================================================================
print("=" * 60)
print("4. RUNNING THE APP")
print("=" * 60)

print("  Run Flask app:")
print("    app.run()                    # Default: localhost:5000")
print("    app.run(debug=True)          # Enable debug mode")
print("    app.run(host='0.0.0.0')      # Listen on all interfaces")
print("    app.run(port=8000)           # Custom port")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FLASK SETUP SUMMARY:")
print("=" * 60)
print("  - Flask is a lightweight web framework")
print("  - Use @app.route() to define endpoints")
print("  - Use jsonify() to return JSON")
print("  - Run with app.run()")
print("=" * 60)

