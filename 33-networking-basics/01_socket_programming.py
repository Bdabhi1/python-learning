"""
Socket Programming in Python

This file demonstrates the fundamental concepts of socket programming.
"""

import socket
import threading
import time

# ============================================================================
# 1. WHAT ARE SOCKETS?
# ============================================================================
print("=" * 60)
print("1. WHAT ARE SOCKETS?")
print("=" * 60)

print("  Sockets are endpoints for network communication.")
print("  They allow programs to send and receive data over a network.")
print("  ")
print("  Types of sockets:")
print("    - TCP (SOCK_STREAM): Reliable, connection-oriented")
print("    - UDP (SOCK_DGRAM): Fast, connectionless")
print("  ")
print("  Socket addresses:")
print("    - IP address: Identifies the host")
print("    - Port number: Identifies the service")

print()  # Empty line


# ============================================================================
# 2. TCP SOCKET SERVER
# ============================================================================
print("=" * 60)
print("2. TCP SOCKET SERVER")
print("=" * 60)

def tcp_server_example():
    """Example TCP server"""
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket option to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to address and port
    server_socket.bind(('localhost', 12345))
    
    # Listen for connections (max 5 pending)
    server_socket.listen(5)
    print("    TCP Server listening on localhost:12345...")
    print("    (This is a demonstration - server not started)")
    
    # In real usage:
    # while True:
    #     client_socket, address = server_socket.accept()
    #     data = client_socket.recv(1024)
    #     client_socket.send(b"Message received!")
    #     client_socket.close()
    
    server_socket.close()

tcp_server_example()

print()  # Empty line


# ============================================================================
# 3. TCP SOCKET CLIENT
# ============================================================================
print("=" * 60)
print("3. TCP SOCKET CLIENT")
print("=" * 60)

def tcp_client_example():
    """Example TCP client"""
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to server
        print("    Attempting to connect to server...")
        # client_socket.connect(('localhost', 12345))
        print("    (Server not running - this is a demonstration)")
        
        # In real usage:
        # message = "Hello, Server!"
        # client_socket.send(message.encode())
        # response = client_socket.recv(1024)
        # print(f"    Server response: {response.decode()}")
        
    except ConnectionRefusedError:
        print("    Connection refused - server not running")
    finally:
        client_socket.close()

tcp_client_example()

print()  # Empty line


# ============================================================================
# 4. UDP SOCKET SERVER
# ============================================================================
print("=" * 60)
print("4. UDP SOCKET SERVER")
print("=" * 60)

def udp_server_example():
    """Example UDP server"""
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind to address and port
    server_socket.bind(('localhost', 12346))
    print("    UDP Server listening on localhost:12346...")
    print("    (This is a demonstration - server not started)")
    
    # In real usage:
    # while True:
    #     data, address = server_socket.recvfrom(1024)
    #     print(f"Received from {address}: {data.decode()}")
    #     response = "Message received!"
    #     server_socket.sendto(response.encode(), address)
    
    server_socket.close()

udp_server_example()

print()  # Empty line


# ============================================================================
# 5. UDP SOCKET CLIENT
# ============================================================================
print("=" * 60)
print("5. UDP SOCKET CLIENT")
print("=" * 60)

def udp_client_example():
    """Example UDP client"""
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send data (no connection needed)
        message = "Hello, UDP Server!"
        print(f"    Sending: {message}")
        # client_socket.sendto(message.encode(), ('localhost', 12346))
        print("    (Server not running - this is a demonstration)")
        
        # In real usage:
        # response, server_address = client_socket.recvfrom(1024)
        # print(f"    Server response: {response.decode()}")
        
    except Exception as e:
        print(f"    Error: {e}")
    finally:
        client_socket.close()

udp_client_example()

print()  # Empty line


# ============================================================================
# 6. SOCKET WITH CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("6. SOCKET WITH CONTEXT MANAGER")
print("=" * 60)

def socket_context_example():
    """Example using socket with context manager"""
    print("    Using context manager for automatic cleanup...")
    
    # Using context manager
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('localhost', 12347))
        s.listen(5)
        print("    Socket created and bound")
        print("    Socket will be automatically closed")
    
    print("    Socket closed automatically")

socket_context_example()

print()  # Empty line


# ============================================================================
# 7. SOCKET OPTIONS
# ============================================================================
print("=" * 60)
print("7. SOCKET OPTIONS")
print("=" * 60)

def socket_options_example():
    """Example of socket options"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket options
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("    Set SO_REUSEADDR: Allows reuse of address")
    
    # Set timeout
    s.settimeout(5.0)
    print("    Set timeout: 5 seconds")
    
    # Get socket options
    timeout = s.gettimeout()
    print(f"    Current timeout: {timeout} seconds")
    
    s.close()

socket_options_example()

print()  # Empty line


# ============================================================================
# 8. SOCKET ADDRESS FAMILIES
# ============================================================================
print("=" * 60)
print("8. SOCKET ADDRESS FAMILIES")
print("=" * 60)

print("  Common address families:")
print("    - AF_INET: IPv4 (most common)")
print("    - AF_INET6: IPv6")
print("    - AF_UNIX: Unix domain sockets (local)")
print("  ")
print("  Socket types:")
print("    - SOCK_STREAM: TCP (reliable, connection-oriented)")
print("    - SOCK_DGRAM: UDP (fast, connectionless)")
print("    - SOCK_RAW: Raw sockets (advanced)")

print()  # Empty line


# ============================================================================
# 9. GETTING HOST INFORMATION
# ============================================================================
print("=" * 60)
print("9. GETTING HOST INFORMATION")
print("=" * 60)

def host_info_example():
    """Example of getting host information"""
    hostname = socket.gethostname()
    print(f"    Hostname: {hostname}")
    
    ip_address = socket.gethostbyname(hostname)
    print(f"    IP Address: {ip_address}")
    
    try:
        host_info = socket.gethostbyaddr(ip_address)
        print(f"    Host info: {host_info}")
    except socket.herror:
        print("    Could not resolve host info")

host_info_example()

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SOCKET PROGRAMMING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Sockets are endpoints for network communication")
print("  - TCP: Reliable, connection-oriented")
print("  - UDP: Fast, connectionless")
print("  - Use socket.socket() to create sockets")
print("  - bind() to set address and port")
print("  - listen() for servers, connect() for clients")
print("  - Use context managers for automatic cleanup")
print("  - Set socket options for better control")
print("=" * 60)

