"""
This module represent the main for the application
"""
from fastapi import FastAPI
from .routers import auth

app = FastAPI()

app.include_router(auth.router)
