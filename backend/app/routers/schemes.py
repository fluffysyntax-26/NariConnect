from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.scheme_models import Scheme
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["nariconnect"]
schemes_collection = mongo_db["detailed_schemes"]

router = APIRouter()

@router.get("/schemes")
async def get_schemes(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    search: Optional[str] = None,
    sector: Optional[str] = None,
    state: Optional[str] = None,
    level: Optional[str] = None
):
    query = {}
    
    if search:
        query["$or"] = [
            {"basicDetails.schemeName": {"$regex": search, "$options": "i"}},
            {"schemeContent.briefDescription": {"$regex": search, "$options": "i"}}
        ]
    
    if sector:
        # Assuming sector maps to schemeCategory
        query["basicDetails.schemeCategory.label"] = {"$regex": sector, "$options": "i"}

    if state:
        query["basicDetails.state"] = {"$regex": state, "$options": "i"}

    if level:
         query["basicDetails.level.label"] = {"$regex": level, "$options": "i"}

    total_count = schemes_collection.count_documents(query)
    skip = (page - 1) * limit
    
    cursor = schemes_collection.find(query).skip(skip).limit(limit)
    schemes = list(cursor)
    
    result = []
    for scheme in schemes:
        if "_id" in scheme:
            scheme["_id"] = str(scheme["_id"])
        result.append(scheme)
            
    return {
        "data": result,
        "page": page,
        "limit": limit,
        "total": total_count,
        "total_pages": (total_count + limit - 1) // limit
    }

@router.get("/schemes/{slug}")
async def get_scheme_details(slug: str):
    scheme = schemes_collection.find_one({"slug": slug})
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    
    if "_id" in scheme:
        scheme["_id"] = str(scheme["_id"])
        
    return scheme
