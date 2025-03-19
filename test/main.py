from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_hello():
    return {"message": "Hello world"}


@app.get("/feature")
def read_feature():
    return {"message": "Enhanced feature"}
