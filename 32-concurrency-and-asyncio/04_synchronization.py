"""
Synchronization in Python

This file demonstrates synchronization primitives for threads and processes.
"""

import threading
import time
import queue

# ============================================================================
# 1. WHAT IS SYNCHRONIZATION?
# ============================================================================
print("=" * 60)
print("1. WHAT IS SYNCHRONIZATION?")
print("=" * 60)

print("  Synchronization ensures that multiple threads/processes")
print("  can safely access shared resources.")
print("  ")
print("  Common primitives:")
print("    - Locks: Mutual exclusion")
print("    - Semaphores: Limit concurrent access")
print("    - Events: Signal between threads")
print("    - Queues: Thread-safe communication")
print("    - Conditions: Wait for conditions")

print()  # Empty line


# ============================================================================
# 2. LOCKS
# ============================================================================
print("=" * 60)
print("2. LOCKS")
print("=" * 60)

counter = 0
lock = threading.Lock()

def increment_without_lock():
    """Increment without lock (unsafe)"""
    global counter
    for _ in range(1000):
        counter += 1

def increment_with_lock():
    """Increment with lock (safe)"""
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

# Test without lock (may have race conditions)
counter = 0
thread1 = threading.Thread(target=increment_without_lock)
thread2 = threading.Thread(target=increment_without_lock)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"  Without lock: {counter} (may not be 2000)")

# Test with lock
counter = 0
thread1 = threading.Thread(target=increment_with_lock)
thread2 = threading.Thread(target=increment_with_lock)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"  With lock: {counter} (always 2000)")

print()  # Empty line


# ============================================================================
# 3. SEMAPHORES
# ============================================================================
print("=" * 60)
print("3. SEMAPHORES")
print("=" * 60)

semaphore = threading.Semaphore(2)  # Allow 2 threads at a time

def worker_with_semaphore(name):
    """Worker that uses semaphore"""
    with semaphore:
        print(f"    {name} acquired semaphore")
        time.sleep(1)
        print(f"    {name} releasing semaphore")

print("  Semaphore allows 2 threads at a time...")
threads = [threading.Thread(target=worker_with_semaphore, args=(f"Thread-{i}",)) 
           for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print()  # Empty line


# ============================================================================
# 4. EVENTS
# ============================================================================
print("=" * 60)
print("4. EVENTS")
print("=" * 60)

event = threading.Event()

def waiter():
    """Thread that waits for event"""
    print("    Waiter: Waiting for event...")
    event.wait()
    print("    Waiter: Event received!")

def setter():
    """Thread that sets event"""
    time.sleep(2)
    print("    Setter: Setting event...")
    event.set()

print("  Using events to signal between threads...")
thread1 = threading.Thread(target=waiter)
thread2 = threading.Thread(target=setter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print()  # Empty line


# ============================================================================
# 5. QUEUES
# ============================================================================
print("=" * 60)
print("5. QUEUES")
print("=" * 60)

q = queue.Queue()

def producer():
    """Producer thread"""
    for i in range(5):
        print(f"    Producing: {i}")
        q.put(i)
        time.sleep(0.3)
    q.put(None)  # Signal completion

def consumer():
    """Consumer thread"""
    while True:
        item = q.get()
        if item is None:
            break
        print(f"    Consuming: {item}")
        q.task_done()

print("  Producer-consumer pattern with queue...")
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print()  # Empty line


# ============================================================================
# 6. CONDITIONS
# ============================================================================
print("=" * 60)
print("6. CONDITIONS")
print("=" * 60)

condition = threading.Condition()
items = []

def producer_condition():
    """Producer with condition"""
    global items
    with condition:
        print("    Producer: Adding items...")
        items.append(1)
        items.append(2)
        condition.notify()  # Notify waiting threads

def consumer_condition():
    """Consumer with condition"""
    global items
    with condition:
        while not items:
            print("    Consumer: Waiting for items...")
            condition.wait()
        item = items.pop(0)
        print(f"    Consumer: Got {item}")

print("  Using conditions for producer-consumer...")
consumer_thread = threading.Thread(target=consumer_condition)
producer_thread = threading.Thread(target=producer_condition)

consumer_thread.start()
time.sleep(0.5)  # Let consumer start first
producer_thread.start()

consumer_thread.join()
producer_thread.join()

print()  # Empty line


# ============================================================================
# 7. RLock (Reentrant Lock)
# ============================================================================
print("=" * 60)
print("7. RLOCK (REENTRANT LOCK)")
print("=" * 60)

rlock = threading.RLock()

def recursive_function(n):
    """Function that calls itself"""
    with rlock:
        if n > 0:
            print(f"    Recursive call: {n}")
            recursive_function(n - 1)

print("  RLock allows same thread to acquire lock multiple times...")
thread = threading.Thread(target=recursive_function, args=(3,))
thread.start()
thread.join()

print()  # Empty line


# ============================================================================
# 8. THREAD-SAFE COUNTER
# ============================================================================
print("=" * 60)
print("8. THREAD-SAFE COUNTER")
print("=" * 60)

class ThreadSafeCounter:
    """Thread-safe counter class"""
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def decrement(self):
        with self._lock:
            self._value -= 1
    
    def get_value(self):
        with self._lock:
            return self._value

counter = ThreadSafeCounter()

def increment_counter_multiple():
    for _ in range(100):
        counter.increment()

print("  Using thread-safe counter...")
threads = [threading.Thread(target=increment_counter_multiple) 
           for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"  Final counter value: {counter.get_value()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SYNCHRONIZATION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Locks provide mutual exclusion")
print("  - Semaphores limit concurrent access")
print("  - Events signal between threads")
print("  - Queues provide thread-safe communication")
print("  - Conditions allow waiting for conditions")
print("  - RLock allows reentrant locking")
print("  - Always use synchronization for shared state")
print("=" * 60)

