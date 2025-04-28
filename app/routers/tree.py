# Required imports
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

# Create router instance
router = APIRouter()  

# # POST endpoint to create node from rquest body
# @router.post("/tree", response_model=schemas.TreeNodeRead)  
# def create_tree_node(node: schemas.TreeNodeCreate, db: Session = Depends(get_db)):
#     return crud.create_node(db, node)

def create_tree_node(node: schemas.TreeNodeCreate, db: Session = Depends(get_db)):
    # Validation step: if parentId is provided, check if it exists
    if node.parentId is not None:
        parent = db.query(schemas.TreeNode).filter(schemas.TreeNode.id == node.parentId).first()
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Parent node with ID {node.parentId} does not exist."
            )
    # Proceed with creation if validation passes
    return crud.create_node(db, node)

# GET endpoint to return all trees
@router.get("/tree")  
def read_tree(db: Session = Depends(get_db)):
    roots = crud.get_all_roots(db)
    return [crud.get_children_recursive(root) for root in roots]
