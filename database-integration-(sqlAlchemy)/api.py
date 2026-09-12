from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
    )

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    completed = Column(Boolean)

class TodoRequest(BaseModel):
    title: str
    completed: bool
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(title:str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo Created",
        "data": todo

    }

@app.get("/todos")
def get_all(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "message": "data get successfully",
        "total": len(todos),
        "data": todos
    }

@app.get("/todos/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": "Todo found successfully",
        "data": todo
    }

@app.put("/todos/{id}")
def update_todo(id: int, todo_update: TodoRequest, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = todo_update.title
    todo.completed = todo_update.completed

    db.commit()
    db.refresh(todo)
    
    return {
        "message": "Todo updated",
        "data": todo
    }

@app.delete("/todos/{id}")
def delete_todo(id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message": "TODO deleted"
    }

