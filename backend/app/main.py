"""
This module represent the main for the application
"""
# pylint: disable=missing-final-newline
from fastapi import FastAPI
from .database import init_db
from .routers import auth, platform

app = FastAPI()

init_db()

app.include_router(auth.router)
app.include_router(platform.router)