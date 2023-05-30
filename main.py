from app import gcs, schemas
from fastapi import FastAPI, HTTPException, Header, Depends, Request, File, UploadFile, Form
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
import base64
import json
from typing import Optional
import os
from datetime import date



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    'https://halcyon-api-gateway-bm6h3c7g.uc.gateway.dev'
    'http://halcyon-api-gateway-bm6h3c7g.uc.gateway.dev',
    'https://api-gateway-tj76tt6qmq-uc.a.run.app',
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.put("/document/upload")
async def get_upload_url(
    document_type: str,
    body: schemas.UploadRequest 
):  
    try:
        today = date.today()
        currentDate = today.strftime("%d-%m-%Y")
        organzation = body.organization
        person = body.person
        blob_name = body.blob_name
        document_path = organzation + '/' + person + '/' + currentDate + '/'+ blob_name
        bucket_name = document_type + "_raw"
        service_account = os.environ['Service_Account']
        url = gcs.generate_signed_url(
           service_account,bucket_name,document_path
        )
        return {"signed_url": url}
    except Exception as e:
        print(e)
    raise HTTPException(status_code=403, detail="failed to validate request")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Halcyon API",
        version="0.0.1",
        description="The Halcyon API gateway for uploading documents with a signed url.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi