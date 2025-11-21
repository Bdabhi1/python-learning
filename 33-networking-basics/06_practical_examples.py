"""
Practical Networking Examples

This file demonstrates real-world networking scenarios.
"""

import socket
import time
import json

# ============================================================================
# 1. SIMPLE CHAT SERVER
# ============================================================================
print("=" * 60)
print("1. SIMPLE CHAT SERVER")
print("=" * 60)

print("  Chat server example:")
print("    - Multiple clients can connect")
print("    - Messages broadcast to all clients")
print("    - Thread per client")
print("  ")
print("  Implementation:")
print("    - Use threading for multiple clients")
print("    - Maintain list of connected clients")
print("    - Broadcast messages to all clients")
print("  ")
print("  (Server not started - this is a demonstration)")

print()  # Empty line


# ============================================================================
# 2. FILE TRANSFER SERVER
# ============================================================================
print("=" * 60)
print("2. FILE TRANSFER SERVER")
print("=" * 60)

print("  File transfer server example:")
print("    - Client sends file to server")
print("    - Server saves file")
print("    - Progress tracking")
print("  ")
print("  Implementation:")
print("    - Use TCP for reliable transfer")
print("    - Send file size first")
print("    - Transfer in chunks")
print("    - Verify file integrity")

print()  # Empty line


# ============================================================================
# 3. WEATHER API CLIENT
# ============================================================================
print("=" * 60)
print("3. WEATHER API CLIENT")
print("=" * 60)

class WeatherAPIClient:
    """Weather API client example"""
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com"
    
    def get_weather(self, city):
        """Get weather for city"""
        print(f"    Fetching weather for {city}...")
        # Simulated API call
        # response = requests.get(f"{self.base_url}/weather", 
        #                        params={'city': city, 'key': self.api_key})
        return {
            'city': city,
            'temperature': 22,
            'condition': 'Sunny',
            'humidity': 65
        }
    
    def get_forecast(self, city, days=5):
        """Get forecast for city"""
        print(f"    Fetching {days}-day forecast for {city}...")
        return [{'day': i+1, 'temp': 20+i, 'condition': 'Sunny'} 
                for i in range(days)]

print("  Weather API client example:")
client = WeatherAPIClient(api_key='your-key')
weather = client.get_weather('New York')
print(f"    Weather: {weather}")
forecast = client.get_forecast('New York', days=3)
print(f"    Forecast: {len(forecast)} days")

print()  # Empty line


# ============================================================================
# 4. DOWNLOAD MANAGER
# ============================================================================
print("=" * 60)
print("4. DOWNLOAD MANAGER")
print("=" * 60)

class DownloadManager:
    """Download manager with progress tracking"""
    def __init__(self, max_concurrent=3):
        self.max_concurrent = max_concurrent
        self.downloads = []
    
    def download_file(self, url, filename):
        """Download file with progress"""
        print(f"    Downloading {url} to {filename}...")
        # Simulated download
        time.sleep(0.5)
        print(f"    Downloaded {filename}")
        return True
    
    def download_multiple(self, urls):
        """Download multiple files"""
        print(f"  Downloading {len(urls)} files...")
        for i, url in enumerate(urls, 1):
            filename = f"file_{i}.zip"
            self.download_file(url, filename)
        print("  All downloads completed")

manager = DownloadManager()
urls = [f"https://example.com/file{i}.zip" for i in range(5)]
manager.download_multiple(urls)

print()  # Empty line


# ============================================================================
# 5. API MONITORING
# ============================================================================
print("=" * 60)
print("5. API MONITORING")
print("=" * 60)

class APIMonitor:
    """Monitor API health"""
    def __init__(self, endpoints):
        self.endpoints = endpoints
        self.stats = {}
    
    def check_endpoint(self, endpoint):
        """Check if endpoint is healthy"""
        print(f"    Checking {endpoint}...")
        # Simulated check
        # response = requests.get(endpoint, timeout=5)
        # return response.status_code == 200
        return True
    
    def monitor(self):
        """Monitor all endpoints"""
        print(f"  Monitoring {len(self.endpoints)} endpoints...")
        for endpoint in self.endpoints:
            is_healthy = self.check_endpoint(endpoint)
            self.stats[endpoint] = 'healthy' if is_healthy else 'down'
            print(f"    {endpoint}: {self.stats[endpoint]}")
    
    def get_stats(self):
        """Get monitoring statistics"""
        healthy = sum(1 for status in self.stats.values() if status == 'healthy')
        return {
            'total': len(self.stats),
            'healthy': healthy,
            'down': len(self.stats) - healthy
        }

monitor = APIMonitor([
    'https://api.example.com/health',
    'https://api.example.com/users',
    'https://api.example.com/posts'
])
monitor.monitor()
stats = monitor.get_stats()
print(f"  Stats: {stats}")

print()  # Empty line


# ============================================================================
# 6. WEBHOOK RECEIVER
# ============================================================================
print("=" * 60)
print("6. WEBHOOK RECEIVER")
print("=" * 60)

class WebhookReceiver:
    """Receive and process webhooks"""
    def __init__(self):
        self.webhooks = []
    
    def receive_webhook(self, payload):
        """Receive webhook payload"""
        print("    Received webhook:")
        print(f"      Event: {payload.get('event')}")
        print(f"      Data: {payload.get('data')}")
        self.webhooks.append(payload)
        return {'status': 'received'}
    
    def process_webhooks(self):
        """Process received webhooks"""
        print(f"  Processing {len(self.webhooks)} webhooks...")
        for webhook in self.webhooks:
            event = webhook.get('event')
            print(f"    Processing {event}...")
        print("  All webhooks processed")

receiver = WebhookReceiver()
receiver.receive_webhook({'event': 'user.created', 'data': {'id': 1}})
receiver.receive_webhook({'event': 'order.placed', 'data': {'id': 123}})
receiver.process_webhooks()

print()  # Empty line


# ============================================================================
# 7. API CACHING
# ============================================================================
print("=" * 60)
print("7. API CACHING")
print("=" * 60)

class CachedAPIClient:
    """API client with caching"""
    def __init__(self, ttl=300):  # 5 minutes default
        self.cache = {}
        self.ttl = ttl
    
    def get(self, endpoint):
        """Get with caching"""
        now = time.time()
        
        # Check cache
        if endpoint in self.cache:
            cached_time, cached_data = self.cache[endpoint]
            if now - cached_time < self.ttl:
                print(f"    Cache hit for {endpoint}")
                return cached_data
        
        # Fetch from API
        print(f"    Fetching {endpoint} from API...")
        # response = requests.get(endpoint)
        # data = response.json()
        data = {'endpoint': endpoint, 'data': 'example'}
        
        # Cache result
        self.cache[endpoint] = (now, data)
        return data
    
    def clear_cache(self):
        """Clear cache"""
        self.cache.clear()
        print("    Cache cleared")

client = CachedAPIClient(ttl=60)
print("  First request (cache miss):")
data1 = client.get('/api/users')
print("  Second request (cache hit):")
data2 = client.get('/api/users')

print()  # Empty line


# ============================================================================
# 8. NETWORK SCANNER
# ============================================================================
print("=" * 60)
print("8. NETWORK SCANNER")
print("=" * 60)

def scan_port(host, port, timeout=1):
    """Scan a single port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def scan_ports(host, ports):
    """Scan multiple ports"""
    print(f"  Scanning {host} on ports {ports}...")
    open_ports = []
    
    for port in ports:
        if scan_port(host, port):
            print(f"    Port {port}: OPEN")
            open_ports.append(port)
        else:
            print(f"    Port {port}: CLOSED")
    
    return open_ports

print("  Network port scanner example:")
print("    (Not scanning actual ports - this is a demonstration)")
print("    Use responsibly and only on systems you own!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL NETWORKING EXAMPLES SUMMARY:")
print("=" * 60)
print("Real-world Patterns:")
print("  - Chat servers with multiple clients")
print("  - File transfer with progress tracking")
print("  - API clients for external services")
print("  - Download managers")
print("  - API health monitoring")
print("  - Webhook receivers")
print("  - API response caching")
print("  - Network port scanning (use responsibly)")
print("=" * 60)

