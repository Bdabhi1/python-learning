"""
Practical Concurrency Examples

This file demonstrates real-world concurrency scenarios.
"""

import threading
import asyncio
import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import queue

# ============================================================================
# 1. WEB SCRAPER WITH THREADING
# ============================================================================
print("=" * 60)
print("1. WEB SCRAPER WITH THREADING")
print("=" * 60)

def fetch_url(url):
    """Fetch URL (simulated)"""
    print(f"    Fetching {url}...")
    time.sleep(1)  # Simulate network delay
    print(f"    Fetched {url}")
    return f"Content from {url}"

def scrape_urls_threading(urls):
    """Scrape multiple URLs using threading"""
    results = []
    threads = []
    
    def worker(url):
        result = fetch_url(url)
        results.append(result)
    
    for url in urls:
        thread = threading.Thread(target=worker, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results

urls = ["url1", "url2", "url3", "url4"]
print("  Scraping URLs with threading...")
results = scrape_urls_threading(urls)
print(f"  Scraped {len(results)} URLs")

print()  # Empty line


# ============================================================================
# 2. ASYNC WEB SCRAPER
# ============================================================================
print("=" * 60)
print("2. ASYNC WEB SCRAPER")
print("=" * 60)

async def fetch_url_async(url):
    """Async fetch URL"""
    print(f"    Fetching {url}...")
    await asyncio.sleep(1)  # Simulate network delay
    print(f"    Fetched {url}")
    return f"Content from {url}"

async def scrape_urls_async(urls):
    """Scrape URLs using asyncio"""
    print("  Scraping URLs with asyncio...")
    tasks = [fetch_url_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

urls = ["url1", "url2", "url3", "url4"]
results = asyncio.run(scrape_urls_async(urls))
print(f"  Scraped {len(results)} URLs")

print()  # Empty line


# ============================================================================
# 3. PARALLEL DATA PROCESSING
# ============================================================================
print("=" * 60)
print("3. PARALLEL DATA PROCESSING")
print("=" * 60)

def process_data_chunk(chunk):
    """Process a chunk of data"""
    print(f"    Processing chunk of size {len(chunk)}...")
    time.sleep(0.5)  # Simulate processing
    return sum(x**2 for x in chunk)

def process_data_parallel(data, num_workers=4):
    """Process data in parallel"""
    chunk_size = len(data) // num_workers
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    print(f"  Processing {len(data)} items with {num_workers} workers...")
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_data_chunk, chunks))
    
    return sum(results)

data = list(range(1000))
result = process_data_parallel(data, num_workers=4)
print(f"  Final result: {result}")

print()  # Empty line


# ============================================================================
# 4. DOWNLOAD MANAGER
# ============================================================================
print("=" * 60)
print("4. DOWNLOAD MANAGER")
print("=" * 60)

class DownloadManager:
    """Download manager with rate limiting"""
    def __init__(self, max_concurrent=3):
        self.max_concurrent = max_concurrent
        self.semaphore = threading.Semaphore(max_concurrent)
        self.downloads = []
    
    def download(self, url):
        """Download a file"""
        with self.semaphore:
            print(f"    Downloading {url}...")
            time.sleep(1)  # Simulate download
            print(f"    Downloaded {url}")
            return f"File from {url}"
    
    def download_all(self, urls):
        """Download all URLs"""
        threads = []
        results = []
        
        def worker(url):
            result = self.download(url)
            results.append(result)
        
        for url in urls:
            thread = threading.Thread(target=worker, args=(url,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return results

manager = DownloadManager(max_concurrent=3)
urls = [f"file{i}.zip" for i in range(10)]
print(f"  Downloading {len(urls)} files with max 3 concurrent...")
results = manager.download_all(urls)
print(f"  Downloaded {len(results)} files")

print()  # Empty line


# ============================================================================
# 5. ASYNC API CLIENT
# ============================================================================
print("=" * 60)
print("5. ASYNC API CLIENT")
print("=" * 60)

async def fetch_api_data(endpoint, delay=1):
    """Fetch data from API"""
    print(f"    Fetching {endpoint}...")
    await asyncio.sleep(delay)  # Simulate API call
    print(f"    Fetched {endpoint}")
    return {"endpoint": endpoint, "data": f"Data from {endpoint}"}

async def fetch_multiple_apis(endpoints):
    """Fetch from multiple APIs concurrently"""
    print(f"  Fetching from {len(endpoints)} APIs...")
    tasks = [fetch_api_data(endpoint) for endpoint in endpoints]
    results = await asyncio.gather(*tasks)
    return results

endpoints = ["/api/users", "/api/posts", "/api/comments", "/api/likes"]
results = asyncio.run(fetch_multiple_apis(endpoints))
print(f"  Fetched from {len(results)} APIs")

print()  # Empty line


# ============================================================================
# 6. TASK QUEUE WITH WORKERS
# ============================================================================
print("=" * 60)
print("6. TASK QUEUE WITH WORKERS")
print("=" * 60)

class TaskQueue:
    """Task queue with worker threads"""
    def __init__(self, num_workers=3):
        self.queue = queue.Queue()
        self.workers = []
        self.num_workers = num_workers
        self.running = False
    
    def start(self):
        """Start workers"""
        self.running = True
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker, args=(i,))
            worker.start()
            self.workers.append(worker)
    
    def _worker(self, worker_id):
        """Worker thread"""
        while self.running:
            try:
                task = self.queue.get(timeout=1)
                if task is None:
                    break
                print(f"    Worker {worker_id} processing: {task}")
                time.sleep(0.5)  # Simulate work
                self.queue.task_done()
            except queue.Empty:
                continue
    
    def add_task(self, task):
        """Add task to queue"""
        self.queue.put(task)
    
    def wait_completion(self):
        """Wait for all tasks to complete"""
        self.queue.join()
    
    def shutdown(self):
        """Shutdown workers"""
        self.running = False
        for _ in range(self.num_workers):
            self.queue.put(None)
        for worker in self.workers:
            worker.join()

queue_manager = TaskQueue(num_workers=3)
queue_manager.start()

print("  Adding tasks to queue...")
for i in range(10):
    queue_manager.add_task(f"Task-{i}")

queue_manager.wait_completion()
queue_manager.shutdown()

print()  # Empty line


# ============================================================================
# 7. MONITORING AND LOGGING
# ============================================================================
print("=" * 60)
print("7. MONITORING AND LOGGING")
print("=" * 60)

class MonitoredTask:
    """Task with monitoring"""
    def __init__(self):
        self.completed = 0
        self.failed = 0
        self.lock = threading.Lock()
    
    def execute_task(self, task_id):
        """Execute a task"""
        try:
            print(f"    Executing task {task_id}...")
            time.sleep(0.5)
            with self.lock:
                self.completed += 1
            print(f"    Task {task_id} completed")
        except Exception as e:
            with self.lock:
                self.failed += 1
            print(f"    Task {task_id} failed: {e}")
    
    def get_stats(self):
        """Get statistics"""
        with self.lock:
            return {"completed": self.completed, "failed": self.failed}

monitor = MonitoredTask()

print("  Executing tasks with monitoring...")
threads = [threading.Thread(target=monitor.execute_task, args=(i,))
           for i in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

stats = monitor.get_stats()
print(f"  Statistics: {stats}")

print()  # Empty line


# ============================================================================
# 8. BATCH PROCESSING
# ============================================================================
print("=" * 60)
print("8. BATCH PROCESSING")
print("=" * 60)

def process_batch(batch, batch_id):
    """Process a batch of items"""
    print(f"    Processing batch {batch_id} with {len(batch)} items...")
    time.sleep(0.5)  # Simulate processing
    return sum(batch)

def process_in_batches(items, batch_size=100, num_workers=4):
    """Process items in batches"""
    batches = [items[i:i+batch_size] for i in range(0, len(items), batch_size)]
    
    print(f"  Processing {len(items)} items in {len(batches)} batches...")
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(process_batch, batch, i) 
                   for i, batch in enumerate(batches)]
        results = [f.result() for f in futures]
    
    return sum(results)

items = list(range(1000))
result = process_in_batches(items, batch_size=100, num_workers=4)
print(f"  Final result: {result}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL CONCURRENCY EXAMPLES SUMMARY:")
print("=" * 60)
print("Real-world Patterns:")
print("  - Web scraping with threading/asyncio")
print("  - Parallel data processing")
print("  - Download managers with rate limiting")
print("  - Async API clients")
print("  - Task queues with workers")
print("  - Monitoring and logging")
print("  - Batch processing")
print("  - Choose concurrency model based on task type")
print("=" * 60)

