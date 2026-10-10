from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def get_keyword(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}
