from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/page/{page}")
async def getPage(page: str):
    try:
        page = open(f"src/pages/{page}/index.md", "r").read()
        return page
    except (OSError, IOError) as e:
        return "# 404 - Page not found"