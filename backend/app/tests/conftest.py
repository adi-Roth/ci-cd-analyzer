"""conftest file to override functions in my app"""
import pytest
from unittest.mock import patch
from app.tests.mock_data import mock_authenticate_with_ldap

@pytest.fixture
def override_ldap_auth():
    """Override for app.dependencies.get_ldap_connection in a mock function"""
    with patch("app.dependencies.get_ldap_connection", new=mock_authenticate_with_ldap):
        yield
