# imports of SQLAlchemy for database
from sqlalchemy import create_engine  
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker 

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./tree.db"  

# Create engine for db
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  
# Session factory attaching to engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

# Base class for models
Base = declarative_base()  

def get_db():
    # Creating a session
    db = SessionLocal()  
    try:
        # Yield session to caller
        yield db  
    finally:
        # Making Sure session is closed
        db.close()  