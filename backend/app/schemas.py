"""
Contains schemas for request and response bodies
"""
from pydantic import BaseModel

class Token(BaseModel):
    """
    Represents an authentication token.

    Attributes:
        access_token (str): The JWT access token issued upon successful authentication.
        token_type (str): The type of token, typically "bearer".
    """
    access_token: str
    token_type: str
