from ldap3 import Server, Connection, SIMPLE, ALL
from fastapi import HTTPException
from .config import LDAP_SERVER_URL, LDAP_BASE_DN

def get_ldap_connection(user_dn: str, password: str):
    server = Server(LDAP_SERVER_URL, get_info=ALL)
    try:
        conn = Connection(
            server,
            user=user_dn,
            password=password,
            authentication=SIMPLE,
            auto_bind=True
        )
        return conn
    except Exception:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
