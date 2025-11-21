"""
Asyncio Basics in Python

This file demonstrates the fundamental concepts of asyncio and async/await.
"""

import asyncio
import time

# ============================================================================
# 1. WHAT IS ASYNCIO?
# ============================================================================
print("=" * 60)
print("1. WHAT IS ASYNCIO?")
print("=" * 60)

print("  Asyncio provides single-threaded, event-driven concurrency")
print("  using async and await keywords.")
print("  ")
print("  Key concepts:")
print("    - Single-threaded (no GIL issues)")
print("    - Event loop manages tasks")
print("    - Non-blocking I/O operations")
print("    - Ideal for I/O-bound operations")
print("    - Can handle many concurrent connections")

print()  # Empty line


# ============================================================================
# 2. BASIC ASYNC FUNCTION
# ============================================================================
print("=" * 60)
print("2. BASIC ASYNC FUNCTION")
print("=" * 60)

async def say_hello(name):
    """Simple async function"""
    print(f"    Hello, {name}!")
    await asyncio.sleep(1)  # Simulate I/O operation
    print(f"    Goodbye, {name}!")

async def main():
    """Main async function"""
    print("  Running async functions sequentially...")
    await say_hello("Alice")
    await say_hello("Bob")

# Run async function
print("  Example 1: Sequential execution")
asyncio.run(main())

print()  # Empty line


# ============================================================================
# 3. CONCURRENT ASYNC TASKS
# ============================================================================
print("=" * 60)
print("3. CONCURRENT ASYNC TASKS")
print("=" * 60)

async def fetch_data(url, delay):
    """Simulate fetching data from URL"""
    print(f"    Fetching {url}...")
    await asyncio.sleep(delay)  # Simulate network request
    print(f"    Fetched {url}")
    return f"Data from {url}"

async def main_concurrent():
    """Main function with concurrent tasks"""
    print("  Running async functions concurrently...")
    
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("url1", 2),
        fetch_data("url2", 1),
        fetch_data("url3", 3)
    )
    
    print(f"  All tasks completed: {results}")

asyncio.run(main_concurrent())

print()  # Empty line


# ============================================================================
# 4. ASYNC WITH TASKS
# ============================================================================
print("=" * 60)
print("4. ASYNC WITH TASKS")
print("=" * 60)

async def task(name, delay):
    """Task function"""
    print(f"    Task {name} starting")
    await asyncio.sleep(delay)
    print(f"    Task {name} completed")
    return f"Result from {name}"

async def main_tasks():
    """Main function creating tasks"""
    print("  Creating and running tasks...")
    
    # Create tasks
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))
    task3 = asyncio.create_task(task("C", 3))
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    print(f"  Results: {results}")

asyncio.run(main_tasks())

print()  # Empty line


# ============================================================================
# 5. ASYNC CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("5. ASYNC CONTEXT MANAGER")
print("=" * 60)

class AsyncResource:
    """Async context manager"""
    async def __aenter__(self):
        print("    Acquiring resource...")
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("    Releasing resource...")
        await asyncio.sleep(0.5)

async def main_context():
    """Main function using async context manager"""
    print("  Using async context manager...")
    
    async with AsyncResource() as resource:
        print("    Using resource...")
        await asyncio.sleep(1)

asyncio.run(main_context())

print()  # Empty line


# ============================================================================
# 6. ASYNC GENERATORS
# ============================================================================
print("=" * 60)
print("6. ASYNC GENERATORS")
print("=" * 60)

async def async_counter(n):
    """Async generator"""
    for i in range(n):
        yield i
        await asyncio.sleep(0.3)

async def main_generator():
    """Main function using async generator"""
    print("  Using async generator...")
    
    async for value in async_counter(5):
        print(f"    Received: {value}")

asyncio.run(main_generator())

print()  # Empty line


# ============================================================================
# 7. ASYNC WITH TIMEOUT
# ============================================================================
print("=" * 60)
print("7. ASYNC WITH TIMEOUT")
print("=" * 60)

async def slow_task():
    """Slow task that might timeout"""
    print("    Starting slow task...")
    await asyncio.sleep(5)
    return "Task completed"

async def main_timeout():
    """Main function with timeout"""
    print("  Running task with timeout...")
    
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Task timed out!")

asyncio.run(main_timeout())

print()  # Empty line


# ============================================================================
# 8. ASYNC EVENT LOOP
# ============================================================================
print("=" * 60)
print("8. ASYNC EVENT LOOP")
print("=" * 60)

async def periodic_task():
    """Task that runs periodically"""
    for i in range(3):
        print(f"    Periodic task iteration {i+1}")
        await asyncio.sleep(1)

async def main_event_loop():
    """Main function demonstrating event loop"""
    print("  Event loop manages all async tasks")
    print("  Tasks are scheduled and executed concurrently")
    
    await periodic_task()

asyncio.run(main_event_loop())

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ASYNCIO BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Asyncio provides single-threaded concurrency")
print("  - Use async/await for async functions")
print("  - Use asyncio.gather() for concurrent execution")
print("  - Use asyncio.create_task() to create tasks")
print("  - Use async context managers for resource management")
print("  - Use async generators for async iteration")
print("  - Ideal for I/O-bound operations")
print("  - Event loop manages all async operations")
print("=" * 60)

