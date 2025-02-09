"""Unitests for app/routers/*.py"""
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from app.tests.conftest import override_ldap_auth

with patch("app.database.init_db", return_value=None):
    from app.main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def force_override_ldap_auth(override_ldap_auth):
    """Manually apply override_ldap_auth fixture."""
    _ = override_ldap_auth  # ✅ Ensure it's applied

def test_ldap_route_success():
    """Testing login to ldap server, result need to be 200"""
    user_data = {"username": "e029863", "password": "e029863"}
    response = client.post("/login", json=user_data)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.cookies.get("access_token") is not None
    assert response.json() == {"message": "Login successful"}

def test_ldap_route_failure():
    """Testing login to ldap server, result need to be 401"""
    user_data = {"username": "e012345", "password": "somePass"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
