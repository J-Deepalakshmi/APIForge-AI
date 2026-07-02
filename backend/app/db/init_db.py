"""
Initialize the database.
"""


from app.db.base import Base
from app.db.database import engine

# Import all models here
from app.models.project import Project


def init_database() -> None:
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)