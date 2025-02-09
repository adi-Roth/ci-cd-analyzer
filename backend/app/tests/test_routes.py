# backend/app/tests/test_routes.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.database import get_db
from app.tests.mock_data import mock_authenticate_with_ldap, override_get_db

# Override dependencies
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def override_ldap_auth():
    with patch("app.dependencies.get_ldap_connection", new=mock_authenticate_with_ldap):
        yield

def test_ldap_route_success(override_ldap_auth):
    user_data = {"username": "e029863", "password": "e029863"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 200
    assert response.cookies.get("access_token") is not None
    assert response.json() == {"message": "Login successful"}

def test_ldap_route_failure(override_ldap_auth):
    user_data = {"username": "e012345", "password": "somePass"}
    response = client.post("/login", json=user_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

