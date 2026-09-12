from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

#home Route
@app.get("/")
def home():
    return {"message": "Welcome to Mahim Words!"}

#about route
@app.get("/about")
def about():
    return {
        "message" : "This is about page"
    }

#Owner info
@app.get("/users-info")
def userInfo():
    return {
        "owner": ["Mahim", "Oishi"]
    }

#Dynamic Routes
#user get
#
# @app.get("/user/{user_id}")
# def get_user(user_id):
#     return {
#         "user_id": user_id
#     }

# #Dynamic Routes
# #user get
# @app.get("/user-int-only/{user_id}")
# def get_user(user_id:int):
#     return {
#         "user_id": user_id
#     }

#query parameter

@app.get("/users")
def get_users(name: str = None): #name: str = None this is optional parameter
    return {
        "Name": name
    }


@app.get("/products")
def get_users(limit: int = 10): #this is for defult value
    return {
        "limi": limit
    }

@app.get("/items")
def get_items(name: str = None, limit: int =10):
    return {
        "name": name,
        "limit": limit
    }

@app.post("/create-user")
def create_user(name: str, age: int):
    return {
        "Name": name,
        "Age": age
    }

#with dictonary without validation
@app.post("/create-userV2")
def create_user(user: dict):
    return {
        "message": "User Created",
        "data": user
    }

#Pydantic validation
@app.post("/create-userV3")
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
    }

class Address(BaseModel):
    city:str
    pincode: int

class Student(BaseModel):
    name: str
    age: int
    email: str
    address: Address

@app.post("/create-student")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "data": student
    }

