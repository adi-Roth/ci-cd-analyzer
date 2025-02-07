"""
This module defines all the configuration for the app's modules
"""
# JWT configuration
SECRET_KEY = "ThisIsMyJWTPasswordToVerify"  # Use a secure secret in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expires in 60 minutes

# LDAP configuration
LDAP_SERVER_URL = "ldap://localhost:389"
LDAP_BASE_DN = "ou=users,dc=example,dc=com"
