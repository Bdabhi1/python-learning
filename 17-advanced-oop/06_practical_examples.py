"""
Practical Advanced OOP Examples

This file demonstrates real-world examples using advanced OOP concepts.
"""

from abc import ABC, abstractmethod

# ============================================================================
# 1. SINGLETON PATTERN
# ============================================================================
print("=" * 60)
print("1. SINGLETON PATTERN")
print("=" * 60)

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"  s1 is s2: {s1 is s2}")

print()  # Empty line


# ============================================================================
# 2. FACTORY PATTERN
# ============================================================================
print("=" * 60)
print("2. FACTORY PATTERN")
print("=" * 60)

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal")

dog = AnimalFactory.create("dog")
print(f"  {dog.speak()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Advanced OOP patterns help solve common design problems.")
print("=" * 60)

