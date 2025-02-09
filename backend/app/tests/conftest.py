"""conftest file to override functions in my app"""
from unittest.mock import patch
import pytest
from app.tests.mock_data import mock_authenticate_with_ldap

@pytest.fixture
def override_ldap_auth():
    """Override for app.dependencies.get_ldap_connection in a mock function"""
    with patch("app.dependencies.get_ldap_connection", new=mock_authenticate_with_ldap):
        yield

@pytest.fixture(scope="session", autouse=True)
def mock_init_db():
    """Mock the init_db function to prevent database connection issues."""
    with patch("app.database.init_db", return_value=None):
        yield
