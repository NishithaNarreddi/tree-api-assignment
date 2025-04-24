# Importing necessary sqlalchemy column types and difining relationships
from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship  
from app.database import Base  

# TreeNode model
class TreeNode(Base):  
    __tablename__ = "tree_nodes"

    # Setting up id as Primary key
    id = Column(Integer, primary_key=True, index=True) 
    # Node label
    label = Column(String, index=True) 
    # Foreign key to parent
    parent_id = Column(Integer, ForeignKey("tree_nodes.id"), nullable=True)
    # Self-referential relationship to children
    children = relationship("TreeNode")  