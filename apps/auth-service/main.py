from fastapi import FastAPI
from .src.routes import signin

app = FastAPI()

app.include_router(signin.router)

@app.get("/")
def root():
    return {"message": "Hello, this is auth service!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}