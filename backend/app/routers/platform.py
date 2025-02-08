from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, get_all_platforms, get_platform_by_name, update_platform

router = APIRouter()

# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/platforms")
def read_platforms(db: Session = Depends(get_db)):
    platforms = get_all_platforms()
    return [{"id": p.id, "name": p.name, "url": p.url, "apikey": p.apikey} for p in platforms]

@router.get("/platform/{platform_name}")
def read_platform(platform_name: str, db: Session = Depends(get_db)):
    platform = get_platform_by_name(platform_name)
    if not platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    return {"id": platform.id, "name": platform.name, "url": platform.url, "apikey": platform.apikey}

@router.put("/platform/{platform_name}")
def update_platform_route(platform_name: str, update_data: dict, db: Session = Depends(get_db)):
    updated = update_platform(platform_name, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Platform not found or no changes made")
    return {"message": "Platform updated successfully"}
