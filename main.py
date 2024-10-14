from fastapi import FastAPI

app = FastAPI(title="Trading App")


@app.get("/")
def print_hello():
    return "hello world"
