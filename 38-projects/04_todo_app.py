"""
To-Do List Application

This file demonstrates a simple to-do list application.
"""

import json
from datetime import datetime
from typing import List, Dict

# ============================================================================
# 1. TASK MODEL
# ============================================================================
print("=" * 60)
print("1. TASK MODEL")
print("=" * 60)

class Task:
    """Task model"""
    
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.id = id(self)  # Simple ID generation
    
    def mark_complete(self):
        """Mark task as complete"""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark task as incomplete"""
        self.completed = False
    
    def to_dict(self):
        """Convert task to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    def __repr__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title}"

task = Task("Learn Python", "Complete Python tutorial")
print(f"  Task: {task}")
task.mark_complete()
print(f"  After completion: {task}")

print()  # Empty line


# ============================================================================
# 2. TODO LIST MANAGER
# ============================================================================
print("=" * 60)
print("2. TODO LIST MANAGER")
print("=" * 60)

class TodoList:
    """To-do list manager"""
    
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: str = ""):
        """Add a new task"""
        task = Task(title, description)
        self.tasks.append(task)
        return task
    
    def remove_task(self, task_id: int):
        """Remove a task by ID"""
        self.tasks = [t for t in self.tasks if t.id != task_id]
    
    def get_task(self, task_id: int):
        """Get task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self, show_completed: bool = True):
        """List all tasks"""
        tasks = self.tasks if show_completed else [t for t in self.tasks if not t.completed]
        return tasks
    
    def complete_task(self, task_id: int):
        """Mark task as complete"""
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
    
    def get_stats(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        return {
            'total': total,
            'completed': completed,
            'pending': total - completed
        }

todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build projects")
todo.add_task("Write documentation")
print(f"  Tasks: {len(todo.list_tasks())}")
stats = todo.get_stats()
print(f"  Stats: {stats}")

print()  # Empty line


# ============================================================================
# 3. FILE PERSISTENCE
# ============================================================================
print("=" * 60)
print("3. FILE PERSISTENCE")
print("=" * 60)

class PersistentTodoList(TodoList):
    """To-do list with file persistence"""
    
    def __init__(self, filename: str = "todos.json"):
        super().__init__()
        self.filename = filename
        self.load()
    
    def save(self):
        """Save tasks to file"""
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        """Load tasks from file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    task = Task(item['title'], item.get('description', ''))
                    task.id = item['id']
                    task.completed = item['completed']
                    task.created_at = item['created_at']
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # File doesn't exist yet
    
    def add_task(self, title: str, description: str = ""):
        """Add task and save"""
        task = super().add_task(title, description)
        self.save()
        return task
    
    def remove_task(self, task_id: int):
        """Remove task and save"""
        super().remove_task(task_id)
        self.save()

print("  PersistentTodoList saves to JSON file")
print("  Tasks persist between sessions")

print()  # Empty line


# ============================================================================
# 4. SEARCH AND FILTER
# ============================================================================
print("=" * 60)
print("4. SEARCH AND FILTER")
print("=" * 60)

class AdvancedTodoList(TodoList):
    """Advanced to-do list with search and filter"""
    
    def search(self, query: str):
        """Search tasks by title or description"""
        query_lower = query.lower()
        return [
            task for task in self.tasks
            if query_lower in task.title.lower() or query_lower in task.description.lower()
        ]
    
    def filter_by_status(self, completed: bool):
        """Filter tasks by completion status"""
        return [task for task in self.tasks if task.completed == completed]
    
    def filter_by_date(self, date: str):
        """Filter tasks by creation date"""
        return [task for task in self.tasks if task.created_at.startswith(date)]

adv_todo = AdvancedTodoList()
adv_todo.add_task("Learn Python", "Complete tutorial")
adv_todo.add_task("Learn JavaScript", "Frontend basics")
results = adv_todo.search("Python")
print(f"  Search 'Python': {len(results)} results")

print()  # Empty line


# ============================================================================
# 5. TODO APP INTERFACE
# ============================================================================
print("=" * 60)
print("5. TODO APP INTERFACE")
print("=" * 60)

class TodoApp:
    """Complete to-do application"""
    
    def __init__(self):
        self.todo_list = PersistentTodoList()
    
    def display_menu(self):
        """Display menu options"""
        print("  To-Do App Menu:")
        print("    1. Add task")
        print("    2. List tasks")
        print("    3. Complete task")
        print("    4. Remove task")
        print("    5. Show stats")
        print("    6. Search tasks")
        print("    0. Exit")
    
    def run(self):
        """Run the application"""
        print("  To-Do Application")
        print("  (This is a demonstration)")
        print("  ")
        print("  In real implementation:")
        print("    while True:")
        print("        self.display_menu()")
        print("        choice = input('Choose option: ')")
        print("        # Handle user input")

app = TodoApp()
app.display_menu()

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TODO APP SUMMARY:")
print("=" * 60)
print("Key Features:")
print("  - Task model with properties")
print("  - Add/remove/list tasks")
print("  - Mark tasks as complete")
print("  - File persistence (JSON)")
print("  - Search and filter")
print("  - Statistics")
print("  - User interface")
print("=" * 60)

