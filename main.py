from fastapi import FastAPI

app = FastAPI(
    title="Rangmanch FastAPI Application to provide feedback",
    description="This is a FastAPI application that provides feedback functionality for Rangmanch.",
    version="1.0.0",)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Rangmanch FastAPI Application!"}

