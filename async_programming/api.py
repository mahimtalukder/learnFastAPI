from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/home")
async def home():
    await asyncio.sleep(3)

    return {
        "message": "Async API"
    }