"""
Module for handling platform-related routes.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, get_all_platforms, get_platform_by_name, update_platform

router = APIRouter()

# Dependency to get a session
def get_db():
    """Open a db session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# pylint: disable=unused-argument
@router.get("/platforms")
def read_platforms(db: Session = Depends(get_db)):
    """
    Getting all the avilable ci/cd platforms 

    Args:
        db (Session): the db's session if the db is up

    Returns:
        all the platform as json list
    """
    platforms = get_all_platforms()
    return [{"id": p.id, "name": p.name, "url": p.url, "apikey": p.apikey} for p in platforms]

# pylint: disable=unused-argument
@router.get("/platform/{platform_name}")
def read_platform(platform_name: str, db: Session = Depends(get_db)):
    """
    Getting a platform based on his name

    Args:
        platform_name (str): the platform's name
        db (Session): the db's session if the db is up

    Returns:
        200 - details about platform_name
        404 - platform_name is not exist error
    """
    platform = get_platform_by_name(platform_name)
    if not platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    return {"id": platform.id,
            "name": platform.name,
            "url": platform.url,
            "apikey": platform.apikey
    }

# pylint: disable=unused-argument
@router.put("/platform/{platform_name}")
def update_platform_route(platform_name: str, update_data: dict, db: Session = Depends(get_db)):
    """
    Update platform data by name
    Args:
        platform_name (str): the platform's name
        update_data (dict): the data's platform for the update
        db (Session): the db's session if the db is up

    Returns:
        200 - platform_name is updated
        404 - platform_name is not exist error
    """
    updated = update_platform(platform_name, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Platform not found or no changes made")
    return {"message": "Platform updated successfully"}
