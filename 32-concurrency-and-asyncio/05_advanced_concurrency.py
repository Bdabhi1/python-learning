"""
Advanced Concurrency Patterns in Python

This file demonstrates advanced concurrency patterns and techniques.
"""

import threading
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import queue

# ============================================================================
# 1. FUTURES AND PROMISES
# ============================================================================
print("=" * 60)
print("1. FUTURES AND PROMISES")
print("=" * 60)

def long_running_task(n):
    """Long running task"""
    time.sleep(1)
    return n * n

print("  Using futures with ThreadPoolExecutor...")
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks and get futures
    futures = {executor.submit(long_running_task, i): i for i in range(5)}
    
    # Process results as they complete
    for future in as_completed(futures):
        task_id = futures[future]
        try:
            result = future.result()
            print(f"    Task {task_id} completed: {result}")
        except Exception as e:
            print(f"    Task {task_id} failed: {e}")

print()  # Empty line


# ============================================================================
# 2. PRODUCER-CONSUMER WITH QUEUE
# ============================================================================
print("=" * 60)
print("2. PRODUCER-CONSUMER WITH QUEUE")
print("=" * 60)

def producer_advanced(queue, items):
    """Advanced producer"""
    for item in items:
        print(f"    Producing: {item}")
        queue.put(item)
        time.sleep(0.2)
    queue.put(None)  # Signal completion

def consumer_advanced(queue, name):
    """Advanced consumer"""
    while True:
        item = queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"    {name} consuming: {item}")
        time.sleep(0.3)
        queue.task_done()

q = queue.Queue()

print("  Multiple consumers with single producer...")
producer = threading.Thread(target=producer_advanced, args=(q, ['A', 'B', 'C', 'D', 'E']))
consumer1 = threading.Thread(target=consumer_advanced, args=(q, "Consumer-1"))
consumer2 = threading.Thread(target=consumer_advanced, args=(q, "Consumer-2"))

producer.start()
consumer1.start()
consumer2.start()

producer.join()
q.put(None)  # Signal consumers to stop
q.put(None)
consumer1.join()
consumer2.join()

print()  # Empty line


# ============================================================================
# 3. WORKER POOL PATTERN
# ============================================================================
print("=" * 60)
print("3. WORKER POOL PATTERN")
print("=" * 60)

class WorkerPool:
    """Worker pool class"""
    def __init__(self, num_workers):
        self.task_queue = queue.Queue()
        self.workers = []
        self.num_workers = num_workers
    
    def start(self):
        """Start worker threads"""
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker, args=(i,))
            worker.start()
            self.workers.append(worker)
    
    def _worker(self, worker_id):
        """Worker thread"""
        while True:
            task = self.task_queue.get()
            if task is None:
                self.task_queue.task_done()
                break
            print(f"    Worker {worker_id} processing: {task}")
            time.sleep(0.5)
            self.task_queue.task_done()
    
    def submit(self, task):
        """Submit task to queue"""
        self.task_queue.put(task)
    
    def shutdown(self):
        """Shutdown worker pool"""
        for _ in range(self.num_workers):
            self.task_queue.put(None)
        for worker in self.workers:
            worker.join()

print("  Using worker pool pattern...")
pool = WorkerPool(3)
pool.start()

for i in range(10):
    pool.submit(f"Task-{i}")

pool.shutdown()

print()  # Empty line


# ============================================================================
# 4. ASYNC WITH SEMAPHORE
# ============================================================================
print("=" * 60)
print("4. ASYNC WITH SEMAPHORE")
print("=" * 60)

async def fetch_with_semaphore(semaphore, url, delay):
    """Fetch with semaphore limiting"""
    async with semaphore:
        print(f"    Fetching {url}...")
        await asyncio.sleep(delay)
        print(f"    Fetched {url}")
        return f"Data from {url}"

async def main_semaphore():
    """Main with semaphore"""
    semaphore = asyncio.Semaphore(2)  # Limit to 2 concurrent
    
    urls = [f"url{i}" for i in range(5)]
    delays = [1, 2, 1, 3, 1]
    
    print("  Limiting concurrent fetches to 2...")
    results = await asyncio.gather(
        *[fetch_with_semaphore(semaphore, url, delay) 
          for url, delay in zip(urls, delays)]
    )
    print(f"  All fetched: {len(results)} items")

asyncio.run(main_semaphore())

print()  # Empty line


# ============================================================================
# 5. ASYNC QUEUE
# ============================================================================
print("=" * 60)
print("5. ASYNC QUEUE")
print("=" * 60)

async def producer_async(queue, items):
    """Async producer"""
    for item in items:
        await queue.put(item)
        print(f"    Produced: {item}")
        await asyncio.sleep(0.2)

async def consumer_async(queue, name):
    """Async consumer"""
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"    {name} consumed: {item}")
        await asyncio.sleep(0.3)
        queue.task_done()

async def main_async_queue():
    """Main with async queue"""
    q = asyncio.Queue()
    
    print("  Async producer-consumer...")
    producer_task = asyncio.create_task(
        producer_async(q, ['A', 'B', 'C', 'D', 'E'])
    )
    consumer_task = asyncio.create_task(consumer_async(q, "Consumer"))
    
    await producer_task
    await q.put(None)  # Signal completion
    await consumer_task

asyncio.run(main_async_queue())

print()  # Empty line


# ============================================================================
# 6. THREADING VS MULTIPROCESSING VS ASYNCIO
# ============================================================================
print("=" * 60)
print("6. THREADING VS MULTIPROCESSING VS ASYNCIO")
print("=" * 60)

print("  Threading:")
print("    - Shared memory")
print("    - Good for I/O-bound")
print("    - Limited by GIL")
print("  ")
print("  Multiprocessing:")
print("    - Separate memory")
print("    - Good for CPU-bound")
print("    - True parallelism")
print("  ")
print("  Asyncio:")
print("    - Single-threaded")
print("    - Good for I/O-bound")
print("    - Many concurrent connections")

print()  # Empty line


# ============================================================================
# 7. MIXED CONCURRENCY
# ============================================================================
print("=" * 60)
print("7. MIXED CONCURRENCY")
print("=" * 60)

def blocking_io():
    """Blocking I/O operation"""
    time.sleep(1)
    return "Blocking I/O result"

async def async_with_threading():
    """Async function using thread pool"""
    loop = asyncio.get_event_loop()
    
    print("  Running blocking I/O in thread pool from async...")
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, blocking_io)
        print(f"    Result: {result}")

asyncio.run(async_with_threading())

print()  # Empty line


# ============================================================================
# 8. RATE LIMITING
# ============================================================================
print("=" * 60)
print("8. RATE LIMITING")
print("=" * 60)

class RateLimiter:
    """Rate limiter class"""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = threading.Lock()
    
    def wait_if_needed(self):
        """Wait if rate limit exceeded"""
        with self.lock:
            now = time.time()
            # Remove old calls
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < self.period]
            
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    self.calls = []
            else:
                self.calls.append(time.time())

def rate_limited_task(name, limiter):
    """Task with rate limiting"""
    limiter.wait_if_needed()
    print(f"    {name} executed")

print("  Rate limiting to 2 calls per second...")
limiter = RateLimiter(max_calls=2, period=1.0)

threads = [threading.Thread(target=rate_limited_task, args=(f"Task-{i}", limiter))
           for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ADVANCED CONCURRENCY SUMMARY:")
print("=" * 60)
print("Key Patterns:")
print("  - Futures for async task results")
print("  - Producer-consumer with queues")
print("  - Worker pool pattern")
print("  - Async with semaphores")
print("  - Async queues")
print("  - Mix threading and asyncio")
print("  - Rate limiting")
print("  - Choose right concurrency model for task")
print("=" * 60)

