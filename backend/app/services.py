"""
This module provides utility functions for the app
"""
from datetime import datetime, timedelta
from jose import jwt
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a JWT from given data. If an expiration delta is provided, it uses that; otherwise, the function uses a default expiration time.
    Args:
        data (dict): Data to be encoded in the JWT.
        expires_delta (timedelta, optional): Time interval until the token expires. Defaults to None, which uses a configuration-defined value.
    Returns:
        str: The encoded JWT as a string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
