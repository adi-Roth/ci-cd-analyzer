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

class CI_CD_Platform(Base):
    __tablename__ = "ci_cd_platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, nullable=False)
    apikey = Column(String, nullable=False)

def init_db():
    """Initialize the database and add default platforms if not exist."""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    if not session.query(CI_CD_Platform).first():
        default_platforms = [
            CI_CD_Platform(name="GitHub Actions", url="https://github.com", apikey="default_key"),
            CI_CD_Platform(name="GitLab CI", url="https://gitlab.com", apikey="default_key"),
            CI_CD_Platform(name="Jenkins", url="https://jenkins.io", apikey="default_key")
        ]
        session.add_all(default_platforms)
        session.commit()
    session.close()

def update_platform(identifier, new_values):
    """Update a platform's attributes by ID or name."""
    session = SessionLocal()
    platform = session.query(CI_CD_Platform).filter(
        (CI_CD_Platform.id == identifier) | (CI_CD_Platform.name == identifier)
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
    platforms = session.query(CI_CD_Platform).all()
    session.close()
    return platforms

def get_platform_by_name(name):
    """Retrieve a platform by name."""
    session = SessionLocal()
    platform = session.query(CI_CD_Platform).filter(CI_CD_Platform.name == name).first()
    session.close()
    return platform
