from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserApplication(BaseModel):
    user_id: str
    scheme_slug: str
    scheme_name: str
    ministry_name: Optional[str] = None
    status: str = "Saved"
    applied_at: datetime = datetime.utcnow()

class ApplicationResponse(UserApplication):
    id: str
