# Tree API

A production-ready FastAPI service to manage tree data structures with relational modeling, persistence, testing, and Docker support.

## 📌 Technology Choices

| Technology     | Role                       | Why Chosen                                       |
|----------------|----------------------------|--------------------------------------------------|
| **FastAPI**    | API framework              | Fast, modern, built-in validation and docs       |
| **SQLite**     | Database                   | Lightweight and file-based                       |
| **SQLAlchemy** | ORM                        | Pythonic way to manage DB, supports relationships|
| **Pydantic**   | Data validation            | Clean schema definitions and error handling      |
| **Uvicorn**    | ASGI server                | Fast server for running the API                  |
| **Pytest**     | Testing framework          | Easy-to-use, supports fixtures and assertions    |
| **httpx**      | HTTP support for testing   | Used by FastAPI's test client                    |

---

## ⚙️ Three Ways to Set Up
- **Option 1:** Setup with [Poetry](https://python-poetry.org/)
- **Option 2:** Setup with `pip`
- **Option 3:** Setup with 🐳 Docker

### Prerequisites
- Python 3.12.10

### Option 1: Setup with Poetry

#### 1. Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
or
```bash
curl -sSL https://install.python-poetry.org | py -
```

#### 2. Verify Installation
```bash
poetry --version
```
If Poetry is not found, add this to your PATH:
```
C:\Users\<YourUsername>\AppData\Roaming\Python\Scripts
```

#### 3. Install Dependencies
```bash
poetry env use 3.12
poetry install
```

#### 4. Run the Server
```bash
poetry run uvicorn app.main:app --reload
```

#### 5. Run Tests
```bash
poetry run pytest
```

---

### Option 2: Setup with pip
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
## To test the testcases
pytest
```


### Option 3: Setup with 🐳 Docker

This is the easiest way to run the app if you have Docker installed.

#### 1. Build Docker Image
```bash
docker build -t tree-api .
```

#### 2. Run Docker Container
```bash
docker run -d -p 8000:8000 -v ${PWD}\tree.db:/app/tree.db tree-api

```

#### 3. Access the API (Swagger UI)
Open in browser:
```
Visit:
```
http://localhost:8000/docs
```
to explore the API with Swagger UI.
```

---

## 🚀 Endpoints

- `GET /api/tree` - Returns all trees
- `POST /api/tree` - Creates a node

### Example `GET /api/tree` Response
```json
[
  {
    "id": 1,
    "label": "root",
    "children": [
      {
        "id": 3,
        "label": "bear",
        "children": [
          {
            "id": 4,
            "label": "cat",
            "children": []
          }
        ]
      },
      {
        "id": 7,
        "label": "frog",
        "children": []
      }
    ]
  }
]
```

### Example `POST /api/tree` Request
```json
{
  "label": "cat's child",
  "parentId": 4
}
```

---

## 🧪 Testing

### Run All Tests
```bash
pytest
```

---

## 🌐 Example CURL Commands

### macOS / Linux / PowerShell

```bash
curl -X POST http://127.0.0.1:8000/api/tree -H 'Content-Type: application/json' -d '{"label": "root"}'
curl -X POST http://127.0.0.1:8000/api/tree -H 'Content-Type: application/json' -d '{"label": "bear", "parentId": 1}'
curl -X POST http://127.0.0.1:8000/api/tree -H 'Content-Type: application/json' -d '{"label": "cat", "parentId": 2}'
curl http://127.0.0.1:8000/api/tree
```

### Windows CMD

```cmd
curl -X POST http://127.0.0.1:8000/api/tree -H "Content-Type: application/json" -d "{"label": "root"}"
curl -X POST http://127.0.0.1:8000/api/tree -H "Content-Type: application/json" -d "{"label": "bear", "parentId": 1}"
curl -X POST http://127.0.0.1:8000/api/tree -H "Content-Type: application/json" -d "{"label": "cat", "parentId": 2}"
curl http://127.0.0.1:8000/api/tree
```

---

