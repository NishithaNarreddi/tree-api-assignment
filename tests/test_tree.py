# FastAPI test client
from fastapi.testclient import TestClient  
from app.main import app 
from app.database import Base, engine 
import pytest

# Initialize test client
client = TestClient(app)  

@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)  
    Base.metadata.create_all(bind=engine)

# Test case
def test_create_and_get_tree():  
    # Create root
    response = client.post("/api/tree", json={"label": "root"})  
    # Checking response
    assert response.status_code == 200 
    # Get root ID 
    root_id = response.json()["id"]  

    # Create first child
    bear_resp = client.post("/api/tree", json={"label": "bear", "parentId": root_id})  
    assert bear_resp.status_code == 200
    # Get bear ID
    bear_id = bear_resp.json()["id"]  

    # Create grandchild
    cat_resp = client.post("/api/tree", json={"label": "cat", "parentId": bear_id})  
    assert cat_resp.status_code == 200

    # Another child
    frog_resp = client.post("/api/tree", json={"label": "frog", "parentId": root_id})  
    assert frog_resp.status_code == 200

    # Getting the whole tree
    response = client.get("/api/tree")  
    assert response.status_code == 200
    tree = response.json() 

    # One root
    assert len(tree) == 1  
    assert tree[0]["label"] == "root"
    # Two children 
    assert len(tree[0]["children"]) == 2  
    labels = sorted(child["label"] for child in tree[0]["children"])
    # Checking if both children are present
    assert labels == ["bear", "frog"]  

    bear_node = next(child for child in tree[0]["children"] if child["label"] == "bear")
    assert len(bear_node["children"]) == 1
    # Grandchild
    assert bear_node["children"][0]["label"] == "cat"  