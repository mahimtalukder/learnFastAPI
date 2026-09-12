from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_handlar(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "Error",
            "message": f"User {exc.name} not found"
        }
    )

@app.get("/users/{name}")
def get_user(name: str):
    if name != "mahim":
        raise UserNotFoundException(name)

    return {
        "name": name
    }

