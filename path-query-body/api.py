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

@app.put("/todos/{id}")
def update_todo(id:int, updated: Todo, notify: bool = False):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated
            return {
                "message": "data updated",
                "notify": notify,
                "data": updated
            }

    return {
        "error" : "Todo not found"
    }



