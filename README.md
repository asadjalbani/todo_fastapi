# FastAPI ToDo App

This is a simple ToDo app built with FastAPI that allows you to manage tasks efficiently. It includes basic CRUD (Create, Read, Update, Delete) operations for your tasks.

## Features

- **Create Task**: Add new tasks with a unique ID and a description.
- **Read Tasks**: Retrieve a list of all tasks and individual tasks by their ID.
- **Update Task**: Modify the description of an existing task by its ID.
- **Delete Task**: Remove a task from the list by its ID.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Pydantic

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/asadjalbani/todo_api.git
   
## API Endpoints

- **GET /todos:** Retrieve a list of all tasks.
- **GET /todos/{todo_id}:** Retrieve an individual task by its ID.
- **POST /todos:** Create a new task.
- **PUT /todos/{todo_id}:** Update a task by its ID.
- **DELETE /todos/{todo_id}:** Delete a task by its ID.

## Data Model

The data model for tasks is defined using Pydantic:

```python
class Todo(BaseModel):
    id: int
    item: str
```
This Pydantic model defines the structure of tasks in your application, with an integer field for the task's ID and a string field for the task description (item).

## Contributing

Contributions to this project are welcome. If you find any issues, have suggestions for improvements, or would like to add new features, please feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Asad Ahmed](https://github.com/asadjalbani)

## Acknowledgments

- Thanks to the FastAPI and Pydantic communities for their excellent tools and documentation.
