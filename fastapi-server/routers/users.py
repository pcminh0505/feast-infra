from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models, schemas
from config import config
from connection_pool import database_instance

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{id}")
def get_user(id: str):
    return {"username": id}


@router.get("/{id}/projects")
def get_user(id: str):
    return {"projects": [
        {
            "name": "Credit Score Project",
            "description": "Project for credit scoring team and associated models.",
            "id": "credit_scoring_aws",
            "registryPath": f"{config.host_url}/projects/credit_scoring_aws/registry"
        },
        {
            "name": "Driver Ranking Project",
            "description": "Project for driver ranking team and associated models.",
            "id": "driver_ranking",
            "registryPath": f"{config.host_url}/projects/driver_ranking/registry"
        }
    ]
    }


def get_user(db: Session, user_id: int):
    return database_instance.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_project(db: Session, project: schemas.projectCreate, user_id: int):
    db_project = models.project(**project.dict(), owner_id=user_id)
    db_project.registryPath = f"{config.host_url}/projects/{db_project.project_id}/registry"
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
