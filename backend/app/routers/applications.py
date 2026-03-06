from fastapi import APIRouter, HTTPException, Query, Body
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["nariconnect"]
applications_collection = db["user_applications"]

router = APIRouter()

class ApplicationCreate(BaseModel):
    user_id: str
    scheme_slug: str
    scheme_name: str
    ministry_name: Optional[str] = None
    status: str = "Saved"

class ApplicationResponse(ApplicationCreate):
    id: str
    applied_at: datetime

@router.post("/applications", response_model=dict)
async def save_application(app: ApplicationCreate):
    # Check if already saved
    existing = applications_collection.find_one({
        "user_id": app.user_id,
        "scheme_slug": app.scheme_slug
    })
    
    if existing:
        return {"message": "Application already saved", "id": str(existing["_id"])}
    
    application_dict = app.dict()
    application_dict["applied_at"] = datetime.utcnow()
    
    result = applications_collection.insert_one(application_dict)
    
    return {
        "message": "Application saved successfully",
        "id": str(result.inserted_id)
    }

@router.get("/applications")
async def get_user_applications(user_id: str = Query(..., description="The Clerk User ID")):
    cursor = applications_collection.find({"user_id": user_id}).sort("applied_at", -1)
    apps = []
    for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        apps.append(doc)
    
    return apps

@router.delete("/applications/{scheme_slug}")
async def remove_application(scheme_slug: str, user_id: str = Query(..., description="The Clerk User ID")):
    result = applications_collection.delete_one({
        "user_id": user_id,
        "scheme_slug": scheme_slug
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Application not found")
        
    return {"message": "Application removed successfully"}
