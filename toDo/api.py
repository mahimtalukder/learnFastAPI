from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/")
def welcome():
    return {
        "message": "Welcome to the project"
    }

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Task added",
        "data": todo
    }

@app.get("/todos")
def get_todos():
    return {
        "todos": todos
    }

@app.get("/todos/{id}")
def get_by_id(id:int):
    for todo in todos:
        if todo.id == id:
            return {
                "todo": todo
            }

    return {
        "error": "Todo not found"
    }

@app.put("/todos/{id}")
def update_todo(id:int, updated: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated
            return {
                "message": "data updated",
                "data": updated
            }

    return {
        "error" : "Todo not found"
    }

@app.delete("/todos/{id}")
def delete_todo(id:int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
            return {
                "message": "Todo deleted"
            }

    return {
        "error": "Todo not found"
    }