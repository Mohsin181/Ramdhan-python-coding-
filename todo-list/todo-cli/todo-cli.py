import click  # To create a CLI
import json  # To save and load tasks from a file
import os  # To check if file exists

TODO_FILE = "todo.json"

# Function to load tasks
def load_todo_task():
    if not os.path.exists(TODO_FILE):
        return []
    
    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # Handle empty/corrupt JSON file

# Function to save tasks
def save_task(task_list):
    with open(TODO_FILE, "w") as file:
        json.dump(task_list, file, indent=4)

@click.group()
def cli():
    """Simple TODO LIST MANAGER"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    task_list = load_todo_task()
    task_list.append({"task": task, "done": False})
    save_task(task_list)
    click.echo(f"Task added successfully: {task}")

@click.command()
def list():
    """List all the tasks"""
    tasks = load_todo_task()
    if not tasks:
        click.echo("No tasks found")
        return

    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark task as completed"""
    tasks = load_todo_task()
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Task {task_number} marked as completed ✅")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_todo_task()
    
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_task(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}")

# Register the commands
cli.add_command(add)  
cli.add_command(list)
cli.add_command(complete)  # ✅ Fixed command registration
cli.add_command(remove)

if __name__ == "__main__":
    cli()
 