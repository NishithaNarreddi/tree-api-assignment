from sqlalchemy.orm import Session
from app import models, schemas  

 # Adds a new tree node to the database
def create_node(db: Session, node: schemas.TreeNodeCreate): 
    # Create instance with keys
    db_node = models.TreeNode(label=node.label, parent_id=node.parentId)
    # Add to session
    db.add(db_node)
    # Commit to DB
    db.commit()
    # Refreshing the DB 
    db.refresh(db_node)
    return db_node

# Get all root nodes(Gets all top-level nodes (i.e., nodes with no parent))
def get_all_roots(db: Session):
    # Filter root nodes
    return db.query(models.TreeNode).filter(models.TreeNode.parent_id == None).all()  

# Recursively fetching children(Builds a nested JSON representation of a tree)
def get_children_recursive(node):  
    return {
        "id": node.id,
        "label": node.label,
        "parentId": node.parent_id,
        "children": [get_children_recursive(child) for child in node.children]
    }