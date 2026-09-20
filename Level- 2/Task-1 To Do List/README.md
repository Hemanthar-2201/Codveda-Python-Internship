# To-Do List Application

## Description

This project is a command-line To-Do List application developed using Python.

The application allows users to add, view, delete, and mark tasks as completed. Tasks are stored in a JSON file so that they remain available even after the program is closed.

The application also includes additional task organization features such as short-term and long-term categories and different priority levels.

## Features

- Add new tasks
- View all tasks
- Delete tasks
- Mark tasks as completed
- Store tasks in a JSON file
- Load previously saved tasks when the program starts
- Short-term and long-term task categories
- High, Medium, and Low priority levels
- Prevent empty task names
- Handle invalid task numbers
- Handle invalid category and priority choices
- Handle missing or invalid JSON data

## Task Categories

Each task can be assigned to one of two categories:

- Short-term
- Long-term

This helps organize tasks based on how soon they need to be completed.

## Priority Levels

Each task can also have a priority level:

- High
- Medium
- Low

This helps users identify which tasks require more attention.

## Data Storage

Tasks are stored in a JSON file named:

`tasks.json`

Each task contains:

- Task name
- Category
- Priority
- Completion status

Example:

```json
{
    "name": "Complete Python assignment",
    "category": "Short-term",
    "priority": "High",
    "completed": false
}
```

## Technologies Used

- Python 3
- JSON
- Python os module
- Command-line interface

## How to Run

1. Make sure Python 3 is installed on your system.
2. Open the Task-1-To-Do-List folder in a terminal.
3. Run the following command:
```bash
python todo.py
```
4. Follow the instructions displayed in the terminal.

## Error Handling

The application handles common errors such as:

- Empty task names
- Invalid category choices
- Invalid priority choices
- Invalid task numbers
- Attempting to delete a task that does not exist
- Attempting to mark a non-existent task as completed
- Missing JSON file
- Invalid JSON data

## What I Learned

Through this project, I practiced:

- Python functions
- Lists and dictionaries
- Conditional statements
- Loops
- User input
- File handling
- JSON data storage
- Exception handling
- Working with Python modules
- Building a command-line application

## Additional Features

In addition to the basic requirements, I added:

- Short-term and long-term task categories
- High, Medium, and Low priority levels

These features were added to make the application more useful for organizing different types of tasks.

## Internship

This project was completed as part of my Python Development Internship at Codveda Technologies.