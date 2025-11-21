# Concurrency and Asyncio in Python

Concurrency allows programs to handle multiple tasks simultaneously, improving performance and responsiveness. Python provides several approaches: threading, multiprocessing, and asyncio. This guide covers these concurrency models and when to use each.

## Table of Contents
1. [What is Concurrency?](#what-is-concurrency)
2. [Threading](#threading)
3. [Multiprocessing](#multiprocessing)
4. [Asyncio and Async/Await](#asyncio-and-asyncawait)
5. [Choosing the Right Approach](#choosing-the-right-approach)
6. [Synchronization Primitives](#synchronization-primitives)
7. [Best Practices](#best-practices)

---

## What is Concurrency?

**Concurrency** is the ability of a program to handle multiple tasks at the same time. It doesn't necessarily mean tasks run simultaneously (that's parallelism), but rather that tasks can make progress in overlapping time periods.

**Key Concepts:**
- **Concurrency**: Multiple tasks making progress (may or may not run simultaneously)
- **Parallelism**: Multiple tasks running simultaneously (requires multiple CPUs)
- **Threading**: Lightweight, shared memory concurrency
- **Multiprocessing**: Separate processes with independent memory
- **Asyncio**: Single-threaded, event-driven concurrency

**Why Use Concurrency?**
- **Performance**: Utilize multiple CPU cores or I/O waiting time
- **Responsiveness**: Keep UI responsive while processing
- **Efficiency**: Better resource utilization
- **Scalability**: Handle more requests/tasks

---

## Threading

**Threading** allows multiple threads to run within a single process, sharing the same memory space.

### Basic Threading

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(0.5)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(0.5)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Done!")
```

### Thread with Arguments

```python
import threading

def worker(name, delay):
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished")

# Create threads with arguments
thread1 = threading.Thread(target=worker, args=("Alice", 2))
thread2 = threading.Thread(target=worker, args=("Bob", 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### Thread Class

```python
import threading

class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(f"Thread {self.name} is running")
        time.sleep(2)
        print(f"Thread {self.name} finished")

# Create and start threads
thread1 = WorkerThread("Thread-1")
thread2 = WorkerThread("Thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### Thread Pool

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} starting")
    time.sleep(1)
    return f"Task {n} completed"

# Use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = [executor.submit(task, i) for i in range(5)]
    
    # Get results
    for future in futures:
        print(future.result())
```

---

## Multiprocessing

**Multiprocessing** uses separate processes, each with its own memory space. This avoids Python's Global Interpreter Lock (GIL) limitations.

### Basic Multiprocessing

```python
import multiprocessing
import time

def worker(name):
    print(f"Process {name} starting")
    time.sleep(2)
    print(f"Process {name} finished")

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=worker, args=("Process-1",))
    process2 = multiprocessing.Process(target=worker, args=("Process-2",))
    
    # Start processes
    process1.start()
    process2.start()
    
    # Wait for processes to complete
    process1.join()
    process2.join()
    
    print("All processes completed")
```

### Process Pool

```python
from concurrent.futures import ProcessPoolExecutor
import time

def compute_square(n):
    print(f"Computing square of {n}")
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(compute_square, numbers)
        
        for result in results:
            print(f"Result: {result}")
```

### Sharing Data Between Processes

```python
import multiprocessing

def worker(shared_dict, shared_value):
    shared_dict['count'] += 1
    shared_value.value += 1

if __name__ == '__main__':
    # Shared dictionary
    manager = multiprocessing.Manager()
    shared_dict = manager.dict({'count': 0})
    
    # Shared value
    shared_value = multiprocessing.Value('i', 0)
    
    # Create processes
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(shared_dict, shared_value))
        processes.append(p)
        p.start()
    
    # Wait for all processes
    for p in processes:
        p.join()
    
    print(f"Final count (dict): {shared_dict['count']}")
    print(f"Final count (value): {shared_value.value}")
```

---

## Asyncio and Async/Await

**Asyncio** provides single-threaded, event-driven concurrency using `async` and `await` keywords. It's ideal for I/O-bound operations.

### Basic Async Function

```python
import asyncio

async def say_hello(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # Simulate I/O operation
    print(f"Goodbye, {name}!")

async def main():
    await say_hello("Alice")
    await say_hello("Bob")

# Run async function
asyncio.run(main())
```

### Concurrent Async Tasks

```python
import asyncio

async def fetch_data(url, delay):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)  # Simulate network request
    print(f"Fetched {url}")
    return f"Data from {url}"

async def main():
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("url1", 2),
        fetch_data("url2", 1),
        fetch_data("url3", 3)
    )
    print("All tasks completed:", results)

asyncio.run(main())
```

### Async with Tasks

```python
import asyncio

async def task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Result from {name}"

async def main():
    # Create tasks
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))
    task3 = asyncio.create_task(task("C", 3))
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    print("Results:", results)

asyncio.run(main())
```

### Async Context Manager

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource...")
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource...")
        await asyncio.sleep(0.5)

async def main():
    async with AsyncResource() as resource:
        print("Using resource...")
        await asyncio.sleep(1)

asyncio.run(main())
```

### Async Generators

```python
import asyncio

async def async_counter(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.5)

async def main():
    async for value in async_counter(5):
        print(f"Received: {value}")

asyncio.run(main())
```

---

## Choosing the Right Approach

### Threading
**Use for:**
- I/O-bound operations (network requests, file I/O)
- Tasks that spend time waiting
- When you need shared memory

**Don't use for:**
- CPU-bound tasks (limited by GIL)
- Tasks requiring true parallelism

### Multiprocessing
**Use for:**
- CPU-bound tasks
- Tasks that need true parallelism
- When you need to bypass the GIL

**Don't use for:**
- Simple I/O-bound tasks (overhead)
- When you need shared state easily

### Asyncio
**Use for:**
- I/O-bound operations
- Network programming
- When you have many concurrent connections
- Single-threaded event loops

**Don't use for:**
- CPU-bound tasks
- When you need true parallelism

---

## Synchronization Primitives

### Locks (Threading)

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final counter: {counter}")  # Should be 200000
```

### Semaphores

```python
import threading
import time

semaphore = threading.Semaphore(2)  # Allow 2 threads at a time

def worker(name):
    with semaphore:
        print(f"{name} acquired semaphore")
        time.sleep(2)
        print(f"{name} released semaphore")

threads = [threading.Thread(target=worker, args=(f"Thread-{i}",)) 
           for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

### Queues

```python
import threading
import queue
import time

def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")
        time.sleep(0.5)

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Poison pill
            break
        print(f"Consumed: {item}")
        q.task_done()

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal consumer to stop
consumer_thread.join()
```

### Event

```python
import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for event...")
    event.wait()
    print("Event received!")

def setter():
    time.sleep(2)
    print("Setting event...")
    event.set()

thread1 = threading.Thread(target=waiter)
thread2 = threading.Thread(target=setter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

---

## Best Practices

### 1. Use ThreadPoolExecutor for Threading

```python
from concurrent.futures import ThreadPoolExecutor

# Good
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    results = [f.result() for f in futures]

# Less preferred
threads = [threading.Thread(target=task, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### 2. Use ProcessPoolExecutor for CPU-Bound Tasks

```python
from concurrent.futures import ProcessPoolExecutor

# Good for CPU-bound tasks
with ProcessPoolExecutor() as executor:
    results = executor.map(cpu_intensive_function, data)
```

### 3. Use Asyncio for I/O-Bound Operations

```python
import asyncio

# Good for I/O-bound
async def fetch_urls(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)
```

### 4. Always Use Locks for Shared State

```python
import threading

# Good
lock = threading.Lock()
with lock:
    shared_variable += 1

# Bad - race condition
shared_variable += 1
```

### 5. Use Context Managers for Resources

```python
# Good
with ThreadPoolExecutor() as executor:
    # Use executor
    pass
# Automatically cleaned up

# Less preferred
executor = ThreadPoolExecutor()
# Use executor
executor.shutdown()  # Must remember to shutdown
```

### 6. Handle Exceptions in Threads/Processes

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    if n == 5:
        raise ValueError("Error!")
    return n * 2

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in futures:
        try:
            result = future.result()
            print(result)
        except Exception as e:
            print(f"Error: {e}")
```

---

## Common Mistakes to Avoid

1. **Using threading for CPU-bound tasks**
   ```python
   # Wrong - GIL prevents true parallelism
   import threading
   def cpu_task():
       sum(i**2 for i in range(1000000))
   
   # Correct - use multiprocessing
   from multiprocessing import Process
   ```

2. **Not using locks for shared state**
   ```python
   # Wrong - race condition
   counter = 0
   def increment():
       global counter
       counter += 1
   
   # Correct
   lock = threading.Lock()
   def increment():
       global counter
       with lock:
           counter += 1
   ```

3. **Forgetting to join threads/processes**
   ```python
   # Wrong - main may exit before threads finish
   thread = threading.Thread(target=task)
   thread.start()
   # Missing thread.join()
   
   # Correct
   thread = threading.Thread(target=task)
   thread.start()
   thread.join()
   ```

4. **Blocking in async functions**
   ```python
   # Wrong - blocks event loop
   async def fetch():
       time.sleep(5)  # Blocking!
   
   # Correct
   async def fetch():
       await asyncio.sleep(5)  # Non-blocking
   ```

5. **Creating too many threads/processes**
   ```python
   # Wrong - too many threads
   threads = [threading.Thread(target=task) for _ in range(1000)]
   
   # Correct - use thread pool
   with ThreadPoolExecutor(max_workers=10) as executor:
       executor.map(task, range(1000))
   ```

---

## Summary

- **Concurrency** allows handling multiple tasks simultaneously
- **Threading** is good for I/O-bound tasks with shared memory
- **Multiprocessing** is good for CPU-bound tasks requiring parallelism
- **Asyncio** is ideal for I/O-bound operations with many concurrent connections
- **Use locks** to protect shared state in threads
- **Use thread/process pools** to limit resource usage
- **Choose the right approach** based on your task type

**Remember**: Concurrency can improve performance, but it adds complexity. Use it when the benefits outweigh the costs!

---

## Next Steps

Now that you understand concurrency and asyncio:
1. Practice with the examples in this folder
2. Use threading for I/O-bound tasks
3. Use multiprocessing for CPU-bound tasks
4. Use asyncio for async I/O operations
5. Move on to **33-networking-basics** to learn about network programming

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_threading_basics.py`: Understanding threading - start here!
2. `02_multiprocessing_basics.py`: Working with multiple processes
3. `03_asyncio_basics.py`: Introduction to async/await
4. `04_synchronization.py`: Locks, semaphores, and queues
5. `05_advanced_concurrency.py`: Advanced concurrency patterns
6. `06_practical_examples.py`: Real-world concurrency examples

Run these files in order to see concurrency in action!

