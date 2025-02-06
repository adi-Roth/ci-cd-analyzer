from fastapi import FastAPI
import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://admin:password@localhost/ci_debugger")
async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI Debugger API is running!!!"}
