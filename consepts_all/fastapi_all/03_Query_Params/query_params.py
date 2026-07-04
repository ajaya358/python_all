from fastapi import FastAPI

app = FastAPI()

# URL: /search?keyword=python&limit=5
@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}

# Optional query param
@app.get("/items")
def get_items(category: str = None):
    if category:
        return {"category": category}
    return {"message": "All items"}

# Run: uvicorn query_params:app --reload
