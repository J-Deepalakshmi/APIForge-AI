from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)


@app.get("/")
def root():
    return {
        "message": "Welcome to APIForge AI 🚀",
        "status": "Backend Running Successfully"
    }