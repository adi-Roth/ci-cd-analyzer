"""Unitests for app/routers/*.py"""
from fastapi.testclient import TestClient
from app.main import app
from app.routers.platform import get_db
from app.tests.mock_data import override_get_db

app.dependency_overrides[get_db] = override_get_db

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
