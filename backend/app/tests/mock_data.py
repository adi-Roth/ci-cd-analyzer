"""Contains deps for my unitests"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

# Mock LDAP authentication function
async def mock_authenticate_with_ldap(username: str, password: str):
    """Override function for ldap authentication"""
    if username == "e029863" and password == "e029863":
        return True
    return False

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override for my get_db() function"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
