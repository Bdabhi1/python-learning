"""
Practical OOP Examples

This file demonstrates real-world examples using object-oriented
programming concepts.
"""

# ============================================================================
# 1. LIBRARY MANAGEMENT SYSTEM
# ============================================================================
print("=" * 60)
print("1. LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

library = Library()
book1 = Book("Python Basics", "John Doe", "123456")
book2 = Book("Advanced Python", "Jane Smith", "789012")

library.add_book(book1)
library.add_book(book2)

found = library.find_book("Python Basics")
if found:
    found.borrow()
    print(f"  Borrowed: {found.title}")

print()  # Empty line


# ============================================================================
# 2. SHOPPING CART
# ============================================================================
print("=" * 60)
print("2. SHOPPING CART")
print("=" * 60)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        self.items.append((product, quantity))
    
    def total(self):
        return sum(product.price * quantity for product, quantity in self.items)
    
    def display(self):
        for product, quantity in self.items:
            print(f"    {product.name} x{quantity}: ${product.price * quantity:.2f}")

cart = ShoppingCart()
cart.add_item(Product("Laptop", 999.99), 1)
cart.add_item(Product("Mouse", 29.99), 2)

print("  Cart items:")
cart.display()
print(f"  Total: ${cart.total():.2f}")

print()  # Empty line


# ============================================================================
# 3. STUDENT GRADE SYSTEM
# ============================================================================
print("=" * 60)
print("3. STUDENT GRADE SYSTEM")
print("=" * 60)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, score):
        self.grades[subject] = score
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

student = Student("Alice", "S001")
student.add_grade("Math", 85)
student.add_grade("Science", 90)
student.add_grade("English", 88)

print(f"  Student: {student.name}")
print(f"  Grades: {student.grades}")
print(f"  Average: {student.get_average():.2f}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("OOP helps organize code into logical, reusable components.")
print("These examples show real-world applications of classes and objects.")
print("=" * 60)

