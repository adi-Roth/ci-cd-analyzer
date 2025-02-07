"""
This module defines all the models for the application
"""
from pydantic import BaseModel, Field

class User(BaseModel):
    """
    Represents a user with a username and password.

    Attributes:
        username (str): The user's username, which must be 7 characters long and follow the pattern 'dpXXXXX' or 'e0XXXXX'.
        password (str): The user's password.
    """
    username: str = Field(
        ...,
        min_length=7,
        max_length=7,
        pattern=r'^(?:[dD][pP]|[eE]0)\d{5}$'
    )
    password: str = Field(..., min_length=1)
