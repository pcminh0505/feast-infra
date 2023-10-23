from typing import Union

from pydantic import BaseModel

class ProjectBase(BaseModel):
    project_id: str
    name: str
    description: Union[str, None] = None
    registryPath: str


class ProjectCreate(ProjectBase):
    project_id: str
    name: str
    description: Union[str, None] = None


class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
