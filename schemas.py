from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: uuid.UUID
    username: str
    name: str
    email: str
    password: str
    created_at: datetime.time
    token: str
    updated_at: datetime.time


class ReadUsers(BaseModel):
    id: uuid.UUID
    username: str
    name: str
    email: str
    password: str
    created_at: datetime.time
    token: str
    updated_at: datetime.time
    class Config:
        from_attributes = True


class Assignees(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    task_id: int
    team_id: int
    user_id: uuid.UUID
    user_name: str


class ReadAssignees(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    task_id: int
    team_id: int
    user_id: uuid.UUID
    user_name: str
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    task_id: str
    task_name: str
    ask_description: str
    priority: str
    visibility: str
    tags: str


class ReadTasks(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    task_id: str
    task_name: str
    ask_description: str
    priority: str
    visibility: str
    tags: str
    class Config:
        from_attributes = True


class Team(BaseModel):
    id: int
    created_at: datetime.time
    team_name: str
    limit: int


class ReadTeam(BaseModel):
    id: int
    created_at: datetime.time
    team_name: str
    limit: int
    class Config:
        from_attributes = True


class TeamUsers(BaseModel):
    team_id: int
    user_id: uuid.UUID
    can_view: str
    can_comment: str
    can_edit: str
    created_at: datetime.time
    id: int


class ReadTeamUsers(BaseModel):
    team_id: int
    user_id: uuid.UUID
    can_view: str
    can_comment: str
    can_edit: str
    created_at: datetime.time
    id: int
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    username: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PostAssignees(BaseModel):
    task_id: int
    team_id: int
    user_id: str
    user_name: str

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    task_id: str
    task_name: str
    ask_description: str
    priority: str
    visibility: str

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: int
    task_id: str
    task_name: str
    ask_description: str
    priority: str
    visibility: str
    tags: str

    class Config:
        from_attributes = True



class PostTeam(BaseModel):
    team_name: str
    limit: int

    class Config:
        from_attributes = True



class PostTeamUsers(BaseModel):
    team_id: int
    user_id: str
    can_view: str
    can_comment: str
    can_edit: str

    class Config:
        from_attributes = True



class PatchUpdateTags(BaseModel):
    task_id: int
    tag: str

    class Config:
        from_attributes = True



class PostUserLogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class PostTaskChangeVisibility(BaseModel):
    task_id: int
    visibility: str

    class Config:
        from_attributes = True



class PostTaskChangeVisibility(BaseModel):
    task_id: int
    visibility: str

    class Config:
        from_attributes = True



class PostTaskChangePriority(BaseModel):
    task_id: int
    priority: str

    class Config:
        from_attributes = True



class PutUserId(BaseModel):
    email: str
    name: str
    username: str
    uuid: str

    class Config:
        from_attributes = True

