# Required imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

# Create router instance
router = APIRouter()  

# POST endpoint to create node from rquest body
@router.post("/tree", response_model=schemas.TreeNodeRead)  
def create_tree_node(node: schemas.TreeNodeCreate, db: Session = Depends(get_db)):
    return crud.create_node(db, node)

# GET endpoint to return all trees
@router.get("/tree")  
def read_tree(db: Session = Depends(get_db)):
    roots = crud.get_all_roots(db)
    return [crud.get_children_recursive(root) for root in roots]
