"""
Contains the configuration to work on the PostgresSQL db
"""
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:password@localhost:5432/ci_debugger"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# pylint: disable=too-few-public-methods
class CiCdPlatform(Base):
    """Represents a Continuous Integration/Continuous Deployment platform configuration."""
    __tablename__ = "ci_cd_platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, nullable=False)
    apikey = Column(String, nullable=False)

def init_db():
    """Initialize the database and add default platforms if not exist."""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    if not session.query(CiCdPlatform).first():
        default_platforms = [
            CiCdPlatform(name="GitHub Actions", url="https://github.com", apikey="default_key"),
            CiCdPlatform(name="GitLab CI", url="https://gitlab.com", apikey="default_key"),
            CiCdPlatform(name="Jenkins", url="https://jenkins.io", apikey="default_key")
        ]
        session.add_all(default_platforms)
        session.commit()
    session.close()

def update_platform(identifier, new_values):
    """Update a platform's attributes by ID or name."""
    session = SessionLocal()
    platform = session.query(CiCdPlatform).filter(
        (CiCdPlatform.id == identifier) | (CiCdPlatform.name == identifier)
    ).first()

    if platform:
        for key, value in new_values.items():
            if hasattr(platform, key):
                setattr(platform, key, value)
        session.commit()
        session.close()
        return True
    session.close()
    return False

def get_all_platforms():
    """Retrieve all CI/CD platforms."""
    session = SessionLocal()
    platforms = session.query(CiCdPlatform).all()
    session.close()
    return platforms

def get_platform_by_name(name):
    """Retrieve a platform by name."""
    session = SessionLocal()
    platform = session.query(CiCdPlatform).filter(CiCdPlatform.name == name).first()
    session.close()
    return platform
