from fastapi import FastAPI
from src.api.app import tdl

app = FastAPI()


@app.get("/", include_in_schema=False)
def health_check():
    return {"This page is for health check."}


app.include_router(tdl)
