from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Root url"}


@app.get("/test")
def home():
    return {"message": "Hello this is the test url"}
