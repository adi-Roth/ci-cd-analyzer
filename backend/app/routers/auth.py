"""
This module defines routes for the application.
"""
from datetime import timedelta
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from ..models import User
from ..schemas import Token
from ..services import create_access_token
from ..dependencies import get_ldap_connection
from ..config import LDAP_BASE_DN
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(user: User, response: Response):
    """
    Authenticate the user, generate an access token, and store it in an HTTP-only cookie.

    This function verifies the user's credentials against an LDAP directory. If authentication
    is successful, it generates a JWT token and sets it as an HTTP-only cookie in the response.

    Args:
        user (User): The user object containing the username and password.
        
        response (Response): The HTTP response object used to set the authentication cookie.

    Returns:
        JSONResponse: A response indicating successful login with an HTTP-only cookie set.
    """
    user_dn = f"uid={user.username},{LDAP_BASE_DN}"
    get_ldap_connection(user_dn, user.password)
    token_data = {"sub": user.username}
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data=token_data, expires_delta=access_token_expires)
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="Lax")
    return response

@router.post('/logout')
async def logout(response: Response):
    """
    Log the user out by clearing the authentication cookie.

    This function removes the HTTP-only access token cookie from the client's browser,
    effectively logging the user out.

    Args:
        response (Response): The HTTP response object used to delete the authentication cookie.

    Returns:
        JSONResponse: A response indicating successful logout.
    """
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(key="access_token")
    return response
