#Imports for FastAPI, routers and database modules
from fastapi import FastAPI
from app.routers import tree  
from app.database import Base, engine 

# Create database tables
Base.metadata.create_all(bind=engine)  

# Initialize FastAPI app
app = FastAPI() 

# Include tree router with prefix /api
app.include_router(tree.router, prefix="/api", tags=["Tree"])  

