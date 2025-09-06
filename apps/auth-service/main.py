from fastapi import FastAPI
from routes import signin

app = FastAPI()

app.include_router(signin.router)


@app.get("/")
async def root():
    return {"message": "Hello, this is auth service!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}