from datetime import timedelta
from fastapi import APIRouter, Depends
from ..models import User
from ..schemas import Token
from ..services import create_access_token
from ..dependencies import get_ldap_connection
from ..config import LDAP_BASE_DN
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(user: User):
    user_dn = f"uid={user.username},{LDAP_BASE_DN}"
    conn = get_ldap_connection(user_dn, user.password)
    token_data = {"sub": user.username}
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data=token_data, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
