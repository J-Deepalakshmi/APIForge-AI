from fastapi import FastAPI
from app.api.project_routes import router as project_router

from app.config import settings
from app.db.init_db import init_database

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)
app.include_router(project_router)

@app.on_event("startup")
def startup() -> None:
    """
    Initialize application resources.
    """
    init_database()


@app.get("/")
def root():
    return {
        "message": "Welcome to APIForge AI 🚀",
        "status": "Backend Running Successfully",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
    }