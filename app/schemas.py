# base model for data validation
from pydantic import BaseModel  
from typing import Optional, List

class TreeNodeBase(BaseModel): 
    label: str
    # camelCase for JSON request
    parentId: Optional[int] = None  

# Model for POST input
class TreeNodeCreate(TreeNodeBase):  
    pass

# Model for response
class TreeNodeRead(TreeNodeBase):  
    id: int
    # Recursive field for children
    children: List['TreeNodeRead'] = []  

    class Config:
        from_attributes = True  
        populate_by_name = True

# Handling forward reference
TreeNodeRead.model_rebuild()  