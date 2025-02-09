"""Unitests for app/routers/*.py"""
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import HTTPException
from app.config import LDAP_BASE_DN

def mock_get_ldap_connection(user_dn: str, password: str):
    """Mocked LDAP function to replace `get_ldap_connection`."""
    print(f"🔥 Mocked LDAP called: user_dn={user_dn}, password={password}")
    if user_dn == f"uid=e029863,{LDAP_BASE_DN}" and password == "e029863":
        return True
    raise HTTPException(status_code=401, detail="Incorrect username or password")

with patch("app.database.init_db", return_value=None), \
    patch("app.dependencies.get_ldap_connection", side_effect=mock_get_ldap_connection):
    from app.main import app

client = TestClient(app)

def test_ldap_route_success():
    """Testing login to LDAP server, expecting 200 OK"""
    user_data = {"username": "e029863", "password": "e029863"}

    response = client.post("/login", json=user_data)

    print("🔥 Response JSON:", response.json())  # ✅ Debugging output

    assert response.status_code == 200  # ✅ Should return 200 OK
    assert response.cookies.get("access_token") is not None
    assert response.json() == {"message": "Login successful"}

def test_ldap_route_failure():
    """Testing login to ldap server, result need to be 401"""
    user_data = {"username": "e012345", "password": "somePass"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
