from typing import List, Optional
from pydantic import BaseModel


class UploadRequest(BaseModel):
    blob_name: str
    organization:str
    person:str
    
