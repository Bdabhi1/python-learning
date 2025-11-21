"""
Multiprocessing Basics in Python

This file demonstrates the fundamental concepts of multiprocessing in Python.
"""

import multiprocessing
import time
import os

# ============================================================================
# 1. WHAT IS MULTIPROCESSING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS MULTIPROCESSING?")
print("=" * 60)

print("  Multiprocessing uses separate processes, each with its own")
print("  memory space. This avoids Python's GIL limitations.")
print("  ")
print("  Key concepts:")
print("    - Each process has independent memory")
print("    - True parallelism (uses multiple CPU cores)")
print("    - Good for CPU-bound tasks")
print("    - More overhead than threading")
print("    - Requires if __name__ == '__main__' guard")

print()  # Empty line


# ============================================================================
# 2. BASIC MULTIPROCESSING
# ============================================================================
print("=" * 60)
print("2. BASIC MULTIPROCESSING")
print("=" * 60)

def worker(name, delay):
    """Worker function for multiprocessing"""
    print(f"    Process {name} (PID: {os.getpid()}) starting")
    time.sleep(delay)
    print(f"    Process {name} (PID: {os.getpid()}) finished")

if __name__ == '__main__':
    print("  Creating processes...")
    
    # Create processes
    process1 = multiprocessing.Process(target=worker, args=("Process-1", 1))
    process2 = multiprocessing.Process(target=worker, args=("Process-2", 0.5))
    
    # Start processes
    process1.start()
    process2.start()
    
    # Wait for processes to complete
    process1.join()
    process2.join()
    
    print("  All processes completed!")

print()  # Empty line


# ============================================================================
# 3. PROCESS POOL EXECUTOR
# ============================================================================
print("=" * 60)
print("3. PROCESS POOL EXECUTOR")
print("=" * 60)

def compute_square(n):
    """Compute square of a number"""
    print(f"    Computing square of {n} (PID: {os.getpid()})")
    time.sleep(0.5)
    return n * n

if __name__ == '__main__':
    from concurrent.futures import ProcessPoolExecutor
    
    numbers = [1, 2, 3, 4, 5]
    
    print(f"  Computing squares of {numbers} using ProcessPoolExecutor...")
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(compute_square, numbers))
        
        print(f"  Results: {results}")

print()  # Empty line


# ============================================================================
# 4. SHARING DATA BETWEEN PROCESSES
# ============================================================================
print("=" * 60)
print("4. SHARING DATA BETWEEN PROCESSES")
print("=" * 60)

def increment_counter(shared_dict, shared_value, lock):
    """Increment shared counter"""
    for _ in range(5):
        with lock:
            shared_dict['count'] += 1
            shared_value.value += 1
        time.sleep(0.1)

if __name__ == '__main__':
    # Shared dictionary using Manager
    manager = multiprocessing.Manager()
    shared_dict = manager.dict({'count': 0})
    
    # Shared value
    shared_value = multiprocessing.Value('i', 0)
    
    # Lock for synchronization
    lock = manager.Lock()
    
    print("  Creating processes to increment shared counter...")
    
    # Create processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(
            target=increment_counter,
            args=(shared_dict, shared_value, lock)
        )
        processes.append(p)
        p.start()
    
    # Wait for all processes
    for p in processes:
        p.join()
    
    print(f"  Final count (dict): {shared_dict['count']}")
    print(f"  Final count (value): {shared_value.value}")

print()  # Empty line


# ============================================================================
# 5. PROCESS COMMUNICATION WITH QUEUE
# ============================================================================
print("=" * 60)
print("5. PROCESS COMMUNICATION WITH QUEUE")
print("=" * 60)

def producer(queue, items):
    """Producer process"""
    for item in items:
        print(f"    Producing: {item}")
        queue.put(item)
        time.sleep(0.2)
    queue.put(None)  # Signal completion

def consumer(queue):
    """Consumer process"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"    Consuming: {item}")
        time.sleep(0.3)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    
    print("  Creating producer and consumer processes...")
    
    # Create processes
    producer_process = multiprocessing.Process(
        target=producer,
        args=(queue, ['A', 'B', 'C', 'D', 'E'])
    )
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    
    # Start processes
    producer_process.start()
    consumer_process.start()
    
    # Wait for completion
    producer_process.join()
    consumer_process.join()
    
    print("  Producer-consumer completed!")

print()  # Empty line


# ============================================================================
# 6. PROCESS POOL WITH MAP
# ============================================================================
print("=" * 60)
print("6. PROCESS POOL WITH MAP")
print("=" * 60)

def cpu_intensive_task(n):
    """CPU-intensive task"""
    result = sum(i**2 for i in range(n))
    print(f"    Task {n} completed: {result}")
    return result

if __name__ == '__main__':
    print("  Using ProcessPool with map...")
    
    with multiprocessing.Pool(processes=3) as pool:
        numbers = [1000, 2000, 3000, 4000, 5000]
        results = pool.map(cpu_intensive_task, numbers)
        
        print(f"  All results: {results}")

print()  # Empty line


# ============================================================================
# 7. PROCESS VS THREAD
# ============================================================================
print("=" * 60)
print("7. PROCESS VS THREAD")
print("=" * 60)

print("  Processes:")
print("    - Separate memory space")
print("    - True parallelism")
print("    - Good for CPU-bound tasks")
print("    - More overhead")
print("  ")
print("  Threads:")
print("    - Shared memory space")
print("    - Limited by GIL")
print("    - Good for I/O-bound tasks")
print("    - Less overhead")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MULTIPROCESSING BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Multiprocessing uses separate processes")
print("  - Each process has independent memory")
print("  - True parallelism for CPU-bound tasks")
print("  - Use ProcessPoolExecutor for process pools")
print("  - Use Manager for shared data")
print("  - Use Queue for inter-process communication")
print("  - Always use if __name__ == '__main__' guard")
print("=" * 60)

