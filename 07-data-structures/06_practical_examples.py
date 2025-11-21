"""
Practical Data Structure Examples

This file demonstrates real-world examples using different data structures
to solve common programming problems.
"""

# ============================================================================
# 1. STUDENT GRADEBOOK
# ============================================================================
print("=" * 60)
print("1. STUDENT GRADEBOOK")
print("=" * 60)

# Using dictionary to store student data
gradebook = {
    "Alice": [85, 90, 88, 92],
    "Bob": [75, 80, 78, 82],
    "Charlie": [95, 98, 92, 96]
}

print("  Student Gradebook:")
print("  " + "-" * 50)
print(f"  {'Name':<15} {'Scores':<20} {'Average':>10}")
print("  " + "-" * 50)

for name, scores in gradebook.items():
    average = sum(scores) / len(scores)
    scores_str = ", ".join(map(str, scores))
    print(f"  {name:<15} {scores_str:<20} {average:>10.2f}")

print()  # Empty line


# ============================================================================
# 2. SHOPPING CART SYSTEM
# ============================================================================
print("=" * 60)
print("2. SHOPPING CART SYSTEM")
print("=" * 60)

# Using list for cart (allows duplicates, ordered)
cart = []

def add_to_cart(item):
    cart.append(item)
    print(f"    Added: {item}")

def remove_from_cart(item):
    if item in cart:
        cart.remove(item)
        print(f"    Removed: {item}")
    else:
        print(f"    {item} not in cart")

def show_cart():
    print("    Cart contents:")
    for i, item in enumerate(cart, 1):
        print(f"      {i}. {item}")

print("  Shopping Cart Operations:")
add_to_cart("Apple")
add_to_cart("Banana")
add_to_cart("Apple")
show_cart()
remove_from_cart("Banana")
show_cart()

print()  # Empty line


# ============================================================================
# 3. USER AUTHENTICATION SYSTEM
# ============================================================================
print("=" * 60)
print("3. USER AUTHENTICATION SYSTEM")
print("=" * 60)

# Using dictionary for user database
users = {
    "alice": {"password": "pass123", "email": "alice@example.com", "role": "admin"},
    "bob": {"password": "secret456", "email": "bob@example.com", "role": "user"},
    "charlie": {"password": "mypass789", "email": "charlie@example.com", "role": "user"}
}

def authenticate(username, password):
    if username in users:
        if users[username]["password"] == password:
            return True, users[username]
    return False, None

# Test authentication
username = "alice"
password = "pass123"
success, user_data = authenticate(username, password)

if success:
    print(f"  Login successful!")
    print(f"    Username: {username}")
    print(f"    Email: {user_data['email']}")
    print(f"    Role: {user_data['role']}")
else:
    print("  Login failed!")

print()  # Empty line


# ============================================================================
# 4. TAG SYSTEM
# ============================================================================
print("=" * 60)
print("4. TAG SYSTEM")
print("=" * 60)

# Using set for unique tags
all_tags = set()
articles = [
    {"title": "Python Basics", "tags": ["python", "tutorial", "beginner"]},
    {"title": "Advanced Python", "tags": ["python", "advanced", "tutorial"]},
    {"title": "Web Development", "tags": ["web", "javascript", "tutorial"]}
]

# Collect all unique tags
for article in articles:
    all_tags.update(article["tags"])

print(f"  All unique tags: {sorted(all_tags)}")

# Find articles with specific tag
search_tag = "python"
matching_articles = [a["title"] for a in articles if search_tag in a["tags"]]
print(f"\n  Articles tagged '{search_tag}': {matching_articles}")

# Find common tags between articles
tags1 = set(articles[0]["tags"])
tags2 = set(articles[1]["tags"])
common = tags1 & tags2
print(f"\n  Common tags between article 1 and 2: {common}")

print()  # Empty line


# ============================================================================
# 5. CONFIGURATION MANAGER
# ============================================================================
print("=" * 60)
print("5. CONFIGURATION MANAGER")
print("=" * 60)

# Using dictionary for configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
        "credentials": ("admin", "secret123")  # Tuple for credentials
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "debug": True
    },
    "allowed_hosts": ["localhost", "127.0.0.1", "example.com"]  # List
}

print("  Configuration:")
print(f"    Database host: {config['database']['host']}")
print(f"    Database port: {config['database']['port']}")
print(f"    Server port: {config['server']['port']}")
print(f"    Allowed hosts: {config['allowed_hosts']}")

# Update configuration
config["server"]["port"] = 9000
print(f"\n  Updated server port: {config['server']['port']}")

print()  # Empty line


# ============================================================================
# 6. INVENTORY SYSTEM
# ============================================================================
print("=" * 60)
print("6. INVENTORY SYSTEM")
print("=" * 60)

# Using dictionary for inventory
inventory = {
    "apple": {"quantity": 50, "price": 0.99},
    "banana": {"quantity": 30, "price": 0.79},
    "orange": {"quantity": 40, "price": 1.29}
}

def check_stock(item):
    if item in inventory:
        return inventory[item]["quantity"]
    return 0

def update_stock(item, quantity):
    if item in inventory:
        inventory[item]["quantity"] += quantity
        return True
    return False

def get_price(item):
    if item in inventory:
        return inventory[item]["price"]
    return None

print("  Inventory:")
for item, info in inventory.items():
    print(f"    {item}: {info['quantity']} units @ ${info['price']:.2f}")

# Check stock
item = "apple"
print(f"\n  Stock of {item}: {check_stock(item)}")

# Update stock
update_stock("apple", -5)
print(f"  After selling 5 {item}s: {check_stock(item)}")

print()  # Empty line


# ============================================================================
# 7. CONTACT BOOK
# ============================================================================
print("=" * 60)
print("7. CONTACT BOOK")
print("=" * 60)

# Using dictionary for contacts
contacts = {
    "Alice": {"phone": "555-0101", "email": "alice@example.com"},
    "Bob": {"phone": "555-0102", "email": "bob@example.com"},
    "Charlie": {"phone": "555-0103", "email": "charlie@example.com"}
}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def find_contact(name):
    return contacts.get(name)

def list_contacts():
    return list(contacts.keys())

print("  Contacts:")
for name, info in contacts.items():
    print(f"    {name}: {info['phone']}, {info['email']}")

# Add contact
add_contact("David", "555-0104", "david@example.com")
print(f"\n  Added David")
print(f"  All contacts: {list_contacts()}")

print()  # Empty line


# ============================================================================
# 8. DATA ANALYSIS
# ============================================================================
print("=" * 60)
print("8. DATA ANALYSIS")
print("=" * 60)

# Using multiple structures for data analysis
sales_data = [
    {"product": "Laptop", "category": "Electronics", "sales": 150},
    {"product": "Mouse", "category": "Electronics", "sales": 200},
    {"product": "Desk", "category": "Furniture", "sales": 80},
    {"product": "Chair", "category": "Furniture", "sales": 120},
    {"product": "Keyboard", "category": "Electronics", "sales": 180}
]

# Group by category (using dictionary)
category_sales = {}
for item in sales_data:
    category = item["category"]
    if category not in category_sales:
        category_sales[category] = []
    category_sales[category].append(item)

# Calculate totals
print("  Sales by Category:")
for category, items in category_sales.items():
    total = sum(item["sales"] for item in items)
    print(f"    {category}: ${total}")

# Find unique categories (using set)
categories = {item["category"] for item in sales_data}
print(f"\n  Unique categories: {categories}")

# Top selling product
top_product = max(sales_data, key=lambda x: x["sales"])
print(f"\n  Top product: {top_product['product']} (${top_product['sales']})")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("These examples demonstrate:")
print("  - Lists: Shopping carts, ordered data")
print("  - Tuples: Fixed data, credentials")
print("  - Dictionaries: User data, configurations, lookups")
print("  - Sets: Unique tags, set operations")
print("\nKey Patterns:")
print("  - Use dictionaries for key-value mappings")
print("  - Use lists for ordered, modifiable sequences")
print("  - Use sets for unique elements and operations")
print("  - Use tuples for immutable data")
print("  - Combine structures for complex data")
print("=" * 60)

