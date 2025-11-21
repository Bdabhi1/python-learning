"""
Practical File Handling Examples

This file demonstrates real-world examples of file handling for
common programming tasks and scenarios.
"""

# ============================================================================
# 1. LOG FILE WRITER
# ============================================================================
print("=" * 60)
print("1. LOG FILE WRITER")
print("=" * 60)

from datetime import datetime

def write_log(message, log_file="app.log"):
    """Write log entry with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        with open(log_file, "a") as file:
            file.write(log_entry)
        return True
    except Exception as e:
        print(f"  Error writing log: {e}")
        return False

# Write some log entries
write_log("Application started")
write_log("Processing data")
write_log("Application finished")

# Read log file
if os.path.exists("app.log"):
    with open("app.log", "r") as file:
        print("  Log entries:")
        for line in file:
            print(f"    {line.strip()}")

print()  # Empty line


# ============================================================================
# 2. CONFIGURATION FILE HANDLER
# ============================================================================
print("=" * 60)
print("2. CONFIGURATION FILE HANDLER")
print("=" * 60)

def write_config(config_dict, filename="config.txt"):
    """Write configuration to file."""
    try:
        with open(filename, "w") as file:
            for key, value in config_dict.items():
                file.write(f"{key}={value}\n")
        return True
    except Exception as e:
        print(f"  Error writing config: {e}")
        return False

def read_config(filename="config.txt"):
    """Read configuration from file."""
    config = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line and "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value
        return config
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"  Error reading config: {e}")
        return {}

# Write config
config = {
    "host": "localhost",
    "port": "8080",
    "debug": "True",
    "database": "app.db"
}
write_config(config)

# Read config
loaded_config = read_config()
print("  Configuration:")
for key, value in loaded_config.items():
    print(f"    {key} = {value}")

print()  # Empty line


# ============================================================================
# 3. CSV DATA PROCESSOR
# ============================================================================
print("=" * 60)
print("3. CSV DATA PROCESSOR")
print("=" * 60)

def write_csv(data, filename="data.csv"):
    """Write data to CSV file."""
    try:
        with open(filename, "w") as file:
            # Write header
            if data:
                header = ",".join(data[0].keys())
                file.write(header + "\n")
                
                # Write rows
                for row in data:
                    values = [str(v) for v in row.values()]
                    file.write(",".join(values) + "\n")
        return True
    except Exception as e:
        print(f"  Error writing CSV: {e}")
        return False

def read_csv(filename="data.csv"):
    """Read data from CSV file."""
    data = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                return data
            
            # Parse header
            header = lines[0].strip().split(",")
            
            # Parse rows
            for line in lines[1:]:
                values = line.strip().split(",")
                row = dict(zip(header, values))
                data.append(row)
        return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"  Error reading CSV: {e}")
        return []

# Write CSV data
csv_data = [
    {"name": "Alice", "age": "25", "city": "New York"},
    {"name": "Bob", "age": "30", "city": "London"},
    {"name": "Charlie", "age": "28", "city": "Tokyo"}
]
write_csv(csv_data)

# Read CSV data
loaded_data = read_csv()
print("  CSV Data:")
for row in loaded_data:
    print(f"    {row}")

print()  # Empty line


# ============================================================================
# 4. JSON DATA HANDLER
# ============================================================================
print("=" * 60)
print("4. JSON DATA HANDLER")
print("=" * 60)

import json

def save_json(data, filename="data.json"):
    """Save data to JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"  Error saving JSON: {e}")
        return False

def load_json(filename="data.json"):
    """Load data from JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"  Error: Invalid JSON in {filename}")
        return {}
    except Exception as e:
        print(f"  Error loading JSON: {e}")
        return {}

# Save JSON data
json_data = {
    "users": [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": 30, "email": "bob@example.com"}
    ],
    "settings": {
        "theme": "dark",
        "language": "en"
    }
}
save_json(json_data)

# Load JSON data
loaded_json = load_json()
print("  JSON Data:")
print(f"    Users: {len(loaded_json.get('users', []))}")
print(f"    Settings: {loaded_json.get('settings', {})}")

print()  # Empty line


# ============================================================================
# 5. FILE BACKUP UTILITY
# ============================================================================
print("=" * 60)
print("5. FILE BACKUP UTILITY")
print("=" * 60)

import shutil
from datetime import datetime

def backup_file(filename):
    """Create backup of file."""
    if not os.path.exists(filename):
        print(f"  File '{filename}' does not exist")
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"
    
    try:
        shutil.copy2(filename, backup_name)
        print(f"  Backup created: {backup_name}")
        return True
    except Exception as e:
        print(f"  Error creating backup: {e}")
        return False

# Create a test file and backup it
test_file = "important.txt"
with open(test_file, "w") as f:
    f.write("Important data\n")

backup_file(test_file)

print()  # Empty line


# ============================================================================
# 6. FILE SEARCH UTILITY
# ============================================================================
print("=" * 60)
print("6. FILE SEARCH UTILITY")
print("=" * 60)

def search_in_file(filename, search_term):
    """Search for term in file."""
    try:
        with open(filename, "r") as file:
            matches = []
            for line_num, line in enumerate(file, 1):
                if search_term.lower() in line.lower():
                    matches.append((line_num, line.strip()))
            return matches
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"  Error searching file: {e}")
        return []

# Search in test file
matches = search_in_file(test_file, "Important")
print(f"  Found {len(matches)} matches:")
for line_num, line in matches:
    print(f"    Line {line_num}: {line}")

print()  # Empty line


# ============================================================================
# 7. FILE STATISTICS
# ============================================================================
print("=" * 60)
print("7. FILE STATISTICS")
print("=" * 60)

def file_stats(filename):
    """Get statistics about file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")
            
            stats = {
                "size": os.path.getsize(filename),
                "characters": len(content),
                "lines": len(lines),
                "words": len(content.split()),
                "non_empty_lines": len([l for l in lines if l.strip()])
            }
            return stats
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"  Error getting stats: {e}")
        return None

stats = file_stats(test_file)
if stats:
    print("  File statistics:")
    for key, value in stats.items():
        print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 8. MULTI-FILE OPERATIONS
# ============================================================================
print("=" * 60)
print("8. MULTI-FILE OPERATIONS")
print("=" * 60)

def merge_files(filenames, output_file="merged.txt"):
    """Merge multiple files into one."""
    try:
        with open(output_file, "w") as outfile:
            for filename in filenames:
                if os.path.exists(filename):
                    with open(filename, "r") as infile:
                        outfile.write(f"=== {filename} ===\n")
                        outfile.write(infile.read())
                        outfile.write("\n")
        return True
    except Exception as e:
        print(f"  Error merging files: {e}")
        return False

# Create test files
with open("file1.txt", "w") as f:
    f.write("Content from file 1\n")
with open("file2.txt", "w") as f:
    f.write("Content from file 2\n")

# Merge files
merge_files(["file1.txt", "file2.txt"])

if os.path.exists("merged.txt"):
    with open("merged.txt", "r") as f:
        print("  Merged content:")
        print(f"    {f.read().strip()}")

print()  # Empty line


# ============================================================================
# 9. CLEANUP
# ============================================================================
print("=" * 60)
print("9. CLEANUP")
print("=" * 60)

# Clean up test files
import os
files_to_remove = [
    "app.log", "config.txt", "data.csv", "data.json",
    test_file, "file1.txt", "file2.txt", "merged.txt"
]

# Also remove backup files
for f in os.listdir("."):
    if f.startswith("important.txt.backup_"):
        files_to_remove.append(f)

for filename in files_to_remove:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  Removed: {filename}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL FILE HANDLING EXAMPLES SUMMARY:")
print("=" * 60)
print("Key Applications:")
print("  - Log files: Record application events")
print("  - Configuration: Store app settings")
print("  - Data storage: CSV, JSON formats")
print("  - File backup: Create copies of important files")
print("  - File search: Find content in files")
print("  - File statistics: Analyze file content")
print("  - Multi-file operations: Merge, split files")
print("\nRemember:")
print("  - Always handle errors")
print("  - Use appropriate file formats")
print("  - Clean up temporary files")
print("  - Use context managers (with statement)")
print("=" * 60)

