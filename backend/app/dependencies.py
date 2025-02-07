"""
This module contains reusable dependencies
"""
from ldap3 import Server, Connection, SIMPLE, ALL
from fastapi import HTTPException
from .config import LDAP_SERVER_URL

def get_ldap_connection(user_dn: str, password: str):
    """
    Establish and return an LDAP connection using the provided user distinguished name (DN) and password.

    Args:
        user_dn (str): The distinguished name of the user for LDAP authentication.
        password (str): The password associated with the user DN.

    Returns:
        Connection: An active LDAP connection object.

    Raises:
        HTTPException: If authentication fails due to incorrect username or password.
    """
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
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Incorrect username or password") from exc
