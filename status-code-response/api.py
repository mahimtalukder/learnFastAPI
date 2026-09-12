from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create-user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }

@app.get("/user")
def get_users():
    return {
        "status": "Success",
        "message": "User Fetch",
        "data": {
            "name": "Mahim"
        }
    }

@app.get("/users/{id}")
def get_user(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id":1,
        "name": "Mahim"
    }