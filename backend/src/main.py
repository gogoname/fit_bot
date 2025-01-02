from fastapi import FastAPI

from src.models.queries import TextQuery, ImageQuery

app = FastAPI()

@app.post("/text")
def text_query(query: TextQuery):
    return {"text": query.text}

@app.post("/image")
def image_query(query: ImageQuery):
    return {"image": query.image.filename or "no filename"}
