"""conftest file to override functions in my app"""
from unittest.mock import AsyncMock, patch
import pytest
from app.tests.mock_data import mock_authenticate_with_ldap

@pytest.fixture(scope="function", autouse=True)
def override_ldap_auth():
    """Mock `get_ldap_connection` to use our fake LDAP authentication function."""
    with patch("app.dependencies.get_ldap_connection", new=AsyncMock(side_effect=mock_authenticate_with_ldap)):
        yield

@pytest.fixture(scope="session", autouse=True)
def mock_init_db():
    """Mock the init_db function to prevent database connection issues."""
    with patch("app.database.init_db", return_value=None):
        yield
