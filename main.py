from fastapi import FastAPI
from app.database import Base,engine
from app.model import role
import app.model.user 
from app.router.authentication import router as auth_router

app=FastAPI()
app.include_router(auth_router)

Base.metadata.create_all(engine) 