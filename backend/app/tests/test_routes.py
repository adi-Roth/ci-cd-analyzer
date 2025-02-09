"""Unitests for app/routers/*.py"""
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

with patch("app.database.init_db", return_value=None):
    from app.main import app

client = TestClient(app)

def test_ldap_route_success(override_ldap_auth):
    """Testing login to ldap server, result need to be 200"""
    _ = override_ldap_auth
    user_data = {"username": "e029863", "password": "e029863"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 200
    assert response.cookies.get("access_token") is not None
    assert response.json() == {"message": "Login successful"}

def test_ldap_route_failure(override_ldap_auth):
    """Testing login to ldap server, result need to be 401"""
    _ = override_ldap_auth
    user_data = {"username": "e012345", "password": "somePass"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
