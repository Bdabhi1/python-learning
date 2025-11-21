"""
Threading Basics in Python

This file demonstrates the fundamental concepts of threading in Python.
"""

import threading
import time

# ============================================================================
# 1. WHAT IS THREADING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS THREADING?")
print("=" * 60)

print("  Threading allows multiple threads to run within a single process,")
print("  sharing the same memory space.")
print("  ")
print("  Key concepts:")
print("    - Threads run concurrently (not necessarily in parallel)")
print("    - Threads share memory space")
print("    - Good for I/O-bound operations")
print("    - Limited by GIL (Global Interpreter Lock) for CPU-bound tasks")

print()  # Empty line


# ============================================================================
# 2. CREATING A SIMPLE THREAD
# ============================================================================
print("=" * 60)
print("2. CREATING A SIMPLE THREAD")
print("=" * 60)

def print_numbers():
    """Function that prints numbers"""
    for i in range(5):
        print(f"    Number: {i}")
        time.sleep(0.3)

def print_letters():
    """Function that prints letters"""
    for letter in 'ABCDE':
        print(f"    Letter: {letter}")
        time.sleep(0.3)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

print("  Creating two threads...")
print("  Starting threads...")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("  Both threads completed!")

print()  # Empty line


# ============================================================================
# 3. THREAD WITH ARGUMENTS
# ============================================================================
print("=" * 60)
print("3. THREAD WITH ARGUMENTS")
print("=" * 60)

def worker(name, delay):
    """Worker function that takes arguments"""
    print(f"    Worker {name} starting")
    time.sleep(delay)
    print(f"    Worker {name} finished")

# Create threads with arguments
print("  Creating threads with arguments...")
thread1 = threading.Thread(target=worker, args=("Alice", 1))
thread2 = threading.Thread(target=worker, args=("Bob", 0.5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("  All workers completed!")

print()  # Empty line


# ============================================================================
# 4. THREAD CLASS
# ============================================================================
print("=" * 60)
print("4. THREAD CLASS")
print("=" * 60)

class WorkerThread(threading.Thread):
    """Custom thread class"""
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        """Method that runs when thread starts"""
        print(f"    Thread {self.name} is running")
        time.sleep(self.delay)
        print(f"    Thread {self.name} finished")

# Create and start threads
print("  Creating custom thread classes...")
thread1 = WorkerThread("Thread-1", 1)
thread2 = WorkerThread("Thread-2", 0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("  All threads completed!")

print()  # Empty line


# ============================================================================
# 5. THREAD POOL EXECUTOR
# ============================================================================
print("=" * 60)
print("5. THREAD POOL EXECUTOR")
print("=" * 60)

from concurrent.futures import ThreadPoolExecutor

def task(n):
    """Task function"""
    print(f"    Task {n} starting")
    time.sleep(0.5)
    result = n * 2
    print(f"    Task {n} completed: {result}")
    return result

# Use ThreadPoolExecutor
print("  Using ThreadPoolExecutor with 3 workers...")
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = [executor.submit(task, i) for i in range(5)]
    
    # Get results
    results = []
    for future in futures:
        result = future.result()
        results.append(result)
    
    print(f"  All results: {results}")

print()  # Empty line


# ============================================================================
# 6. THREAD NAMING
# ============================================================================
print("=" * 60)
print("6. THREAD NAMING")
print("=" * 60)

def named_worker():
    """Worker with thread name"""
    print(f"    Thread name: {threading.current_thread().name}")
    print(f"    Thread ID: {threading.current_thread().ident}")
    time.sleep(0.5)

# Create named threads
print("  Creating named threads...")
thread1 = threading.Thread(target=named_worker, name="Worker-1")
thread2 = threading.Thread(target=named_worker, name="Worker-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print()  # Empty line


# ============================================================================
# 7. DAEMON THREADS
# ============================================================================
print("=" * 60)
print("7. DAEMON THREADS")
print("=" * 60)

def daemon_worker():
    """Daemon thread worker"""
    while True:
        print("    Daemon thread running...")
        time.sleep(1)

print("  Daemon threads:")
print("    - Exit when main program exits")
print("    - Don't prevent program termination")
print("    - Useful for background tasks")

# Create daemon thread
daemon = threading.Thread(target=daemon_worker, daemon=True)
daemon.start()

print("    Daemon thread started (will exit with main program)")
time.sleep(2)  # Let it run briefly

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("THREADING BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Threads allow concurrent execution")
print("  - Use threading.Thread for simple threads")
print("  - Use ThreadPoolExecutor for thread pools")
print("  - Threads share memory space")
print("  - Good for I/O-bound operations")
print("  - Use join() to wait for threads")
print("  - Daemon threads exit with main program")
print("=" * 60)

