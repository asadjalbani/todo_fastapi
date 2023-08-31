from fastapi import FastAPI
from models import Todo
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []

# get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# get single todo
@app.get("/todos/{todo_id}")
async def get_todo_by_id(todo_id: int):
    return todos[todo_id-1]

# create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"todo": "Todo has been added."}


# delete the todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
    return {"todo": "Todo has been deleted."}


# update the todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_obj.item
        else:
            return {"error": "Todo does not exist."}
    return {"todo": "Todo has been updated."}