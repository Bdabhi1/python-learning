"""
Practical Examples Using Collections Module

This file demonstrates real-world examples using various collections
from the collections module.
"""

from collections import Counter, defaultdict, deque, OrderedDict, namedtuple, ChainMap

# ============================================================================
# 1. TEXT ANALYSIS WITH COUNTER
# ============================================================================
print("=" * 60)
print("1. TEXT ANALYSIS WITH COUNTER")
print("=" * 60)

def analyze_text(text):
    """Analyze text for word and character frequencies"""
    words = text.lower().split()
    word_count = Counter(words)
    char_count = Counter(text.lower().replace(' ', ''))
    
    return {
        'word_freq': word_count.most_common(5),
        'char_freq': char_count.most_common(5),
        'total_words': len(words),
        'unique_words': len(word_count)
    }

text = "Python is great. Python is powerful. Python is versatile."
analysis = analyze_text(text)
print(f"  Text: '{text}'")
print(f"  Top 5 words: {analysis['word_freq']}")
print(f"  Top 5 characters: {analysis['char_freq']}")
print(f"  Total words: {analysis['total_words']}")
print(f"  Unique words: {analysis['unique_words']}")

print()  # Empty line


# ============================================================================
# 2. INVENTORY MANAGEMENT WITH DEFAULTDICT
# ============================================================================
print("=" * 60)
print("2. INVENTORY MANAGEMENT WITH DEFAULTDICT")
print("=" * 60)

class Inventory:
    def __init__(self):
        self.stock = defaultdict(int)
        self.categories = defaultdict(list)
    
    def add_item(self, name, quantity, category):
        self.stock[name] += quantity
        if name not in self.categories[category]:
            self.categories[category].append(name)
    
    def get_stock(self, name):
        return self.stock[name]
    
    def get_category_items(self, category):
        return self.categories[category]

inventory = Inventory()
inventory.add_item('laptop', 10, 'electronics')
inventory.add_item('mouse', 25, 'electronics')
inventory.add_item('desk', 5, 'furniture')
inventory.add_item('laptop', 5, 'electronics')  # Add more

print(f"  Laptop stock: {inventory.get_stock('laptop')}")
print(f"  Electronics: {inventory.get_category_items('electronics')}")
print(f"  Furniture: {inventory.get_category_items('furniture')}")

print()  # Empty line


# ============================================================================
# 3. TASK SCHEDULER WITH DEQUE
# ============================================================================
print("=" * 60)
print("3. TASK SCHEDULER WITH DEQUE")
print("=" * 60)

class TaskScheduler:
    def __init__(self):
        self.queue = deque()
        self.completed = []
    
    def add_task(self, task, priority='normal'):
        if priority == 'high':
            self.queue.appendleft(task)
        else:
            self.queue.append(task)
    
    def process_next(self):
        if self.queue:
            task = self.queue.popleft()
            self.completed.append(task)
            return task
        return None
    
    def get_queue_size(self):
        return len(self.queue)

scheduler = TaskScheduler()
scheduler.add_task('Task 1')
scheduler.add_task('Task 2')
scheduler.add_task('Urgent Task', priority='high')
scheduler.add_task('Task 3')

print(f"  Queue size: {scheduler.get_queue_size()}")
print(f"  Processing tasks:")
while scheduler.get_queue_size() > 0:
    task = scheduler.process_next()
    print(f"    - {task}")

print()  # Empty line


# ============================================================================
# 4. LRU CACHE WITH ORDEREDDICT
# ============================================================================
print("=" * 60)
print("4. LRU CACHE WITH ORDEREDDICT")
print("=" * 60)

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
    
    def display(self):
        return dict(self.cache)

cache = LRUCache(3)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
print(f"  After adding a, b, c: {cache.display()}")

cache.get('a')  # Access 'a' (moves to end)
print(f"  After get('a'): {cache.display()}")

cache.put('d', 4)  # Evicts 'b' (least recently used)
print(f"  After put('d'): {cache.display()}")

print()  # Empty line


# ============================================================================
# 5. DATABASE RECORDS WITH NAMEDTUPLE
# ============================================================================
print("=" * 60)
print("5. DATABASE RECORDS WITH NAMEDTUPLE")
print("=" * 60)

# Define record structure
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

employees = [
    Employee(1, 'Alice', 'Engineering', 95000),
    Employee(2, 'Bob', 'Sales', 75000),
    Employee(3, 'Charlie', 'Engineering', 100000),
    Employee(4, 'Diana', 'Marketing', 80000)
]

print("  Employees:")
for emp in employees:
    print(f"    {emp.name} ({emp.department}): ${emp.salary:,}")

# Calculate average salary by department
dept_salaries = defaultdict(list)
for emp in employees:
    dept_salaries[emp.department].append(emp.salary)

print("\n  Average salary by department:")
for dept, salaries in dept_salaries.items():
    avg = sum(salaries) / len(salaries)
    print(f"    {dept}: ${avg:,.2f}")

print()  # Empty line


# ============================================================================
# 6. CONFIGURATION MANAGEMENT WITH CHAINMAP
# ============================================================================
print("=" * 60)
print("6. CONFIGURATION MANAGEMENT WITH CHAINMAP")
print("=" * 60)

class ConfigManager:
    def __init__(self):
        self.defaults = {
            'host': 'localhost',
            'port': 8080,
            'debug': False,
            'timeout': 30
        }
        self.user_config = {}
        self.env_config = {}
        self.config = ChainMap(self.env_config, self.user_config, self.defaults)
    
    def set_user_config(self, **kwargs):
        self.user_config.update(kwargs)
    
    def set_env_config(self, **kwargs):
        self.env_config.update(kwargs)
    
    def get(self, key):
        return self.config[key]
    
    def display(self):
        return {key: self.config[key] for key in self.defaults.keys()}

config = ConfigManager()
config.set_user_config(port=9000, debug=True)
config.set_env_config(host='production.example.com')

print(f"  Configuration: {config.display()}")
print(f"  Priority: env_config > user_config > defaults")

print()  # Empty line


# ============================================================================
# 7. VOTING SYSTEM WITH COUNTER
# ============================================================================
print("=" * 60)
print("7. VOTING SYSTEM WITH COUNTER")
print("=" * 60)

def tally_votes(votes):
    """Tally votes and determine winner"""
    vote_count = Counter(votes)
    winner, winner_votes = vote_count.most_common(1)[0]
    total_votes = sum(vote_count.values())
    
    return {
        'winner': winner,
        'votes': winner_votes,
        'percentage': (winner_votes / total_votes) * 100,
        'all_results': dict(vote_count)
    }

votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Bob', 'Alice']
results = tally_votes(votes)

print(f"  Votes: {votes}")
print(f"  Results: {results['all_results']}")
print(f"  Winner: {results['winner']} with {results['votes']} votes ({results['percentage']:.1f}%)")

print()  # Empty line


# ============================================================================
# 8. SLIDING WINDOW WITH DEQUE
# ============================================================================
print("=" * 60)
print("8. SLIDING WINDOW WITH DEQUE")
print("=" * 60)

def sliding_window_average(data, window_size):
    """Calculate moving average using sliding window"""
    window = deque(maxlen=window_size)
    averages = []
    
    for value in data:
        window.append(value)
        if len(window) == window_size:
            avg = sum(window) / window_size
            averages.append(avg)
    
    return averages

data = [10, 20, 30, 40, 50, 60, 70, 80]
window_size = 3
averages = sliding_window_average(data, window_size)

print(f"  Data: {data}")
print(f"  Window size: {window_size}")
print(f"  Moving averages: {averages}")

print()  # Empty line


# ============================================================================
# 9. EVENT LOG WITH ORDEREDDICT
# ============================================================================
print("=" * 60)
print("9. EVENT LOG WITH ORDEREDDICT")
print("=" * 60)

class EventLog:
    def __init__(self, max_size=100):
        self.log = OrderedDict()
        self.max_size = max_size
    
    def add_event(self, timestamp, event):
        if len(self.log) >= self.max_size:
            self.log.popitem(last=False)  # Remove oldest
        self.log[timestamp] = event
    
    def get_recent(self, n=5):
        return list(self.log.items())[-n:]
    
    def get_oldest(self, n=5):
        return list(self.log.items())[:n]

log = EventLog(max_size=5)
for i in range(10):
    log.add_event(f't{i}', f'Event {i}')

print(f"  Recent events: {log.get_recent(3)}")
print(f"  Oldest events: {log.get_oldest(3)}")

print()  # Empty line


# ============================================================================
# 10. COMPREHENSIVE EXAMPLE: E-COMMERCE SYSTEM
# ============================================================================
print("=" * 60)
print("10. COMPREHENSIVE EXAMPLE: E-COMMERCE SYSTEM")
print("=" * 60)

# Product namedtuple
Product = namedtuple('Product', ['id', 'name', 'price', 'category'])

# Inventory with defaultdict
inventory = defaultdict(int)
products = {
    1: Product(1, 'Laptop', 999.99, 'Electronics'),
    2: Product(2, 'Mouse', 29.99, 'Electronics'),
    3: Product(3, 'Desk', 199.99, 'Furniture')
}

# Initialize inventory
for product_id in products:
    inventory[product_id] = 10

# Shopping cart with Counter
cart = Counter()

# Add items to cart
cart[1] += 2  # 2 laptops
cart[2] += 1  # 1 mouse

print("  Shopping Cart:")
total = 0
for product_id, quantity in cart.items():
    product = products[product_id]
    subtotal = product.price * quantity
    total += subtotal
    print(f"    {product.name} x{quantity}: ${subtotal:.2f}")

print(f"  Total: ${total:.2f}")

# Check inventory
print("\n  Inventory Check:")
for product_id, quantity in cart.items():
    product = products[product_id]
    available = inventory[product_id]
    if available >= quantity:
        print(f"    {product.name}: {quantity} requested, {available} available ✓")
    else:
        print(f"    {product.name}: {quantity} requested, {available} available ✗")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Collections module provides powerful data structures for:")
print("  - Counter: Counting and frequency analysis")
print("  - defaultdict: Grouping and indexing")
print("  - deque: Queue/stack operations and sliding windows")
print("  - OrderedDict: LRU caches and ordered data")
print("  - namedtuple: Structured data without classes")
print("  - ChainMap: Layered configuration")
print("\nThese collections make code more efficient and readable!")
print("=" * 60)

