"""
Repository for Project database operations.
"""

from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project_schema import ProjectCreate


class ProjectRepository:

    @staticmethod
    def create(db: Session, project: ProjectCreate) -> Project:

        db_project = Project(
            name=project.name,
            description=project.description,
            problem_statement=project.problem_statement,
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project

    @staticmethod
    def get_all(db: Session):

        return db.query(Project).all()

    @staticmethod
    def get_by_id(db: Session, project_id: int):

        return db.query(Project).filter(Project.id == project_id).first()

    @staticmethod
    def delete(db: Session, project: Project):

        db.delete(project)
        db.commit()