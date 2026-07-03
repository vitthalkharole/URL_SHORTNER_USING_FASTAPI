from fastapi import FastAPI ,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from sqlalchemy import Engine, create_engine,Column,Integer,String
from websockets import Router
from api_service import router
from database import Base
from sqlalchemy import create_engine
from database import Base, engine



app = FastAPI(title="URL Shortener API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
Base.metadata.create_all(bind=engine)

app.include_router(router)