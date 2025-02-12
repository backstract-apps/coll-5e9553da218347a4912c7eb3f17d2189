from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: str):

    user = db.query(models.Users).filter(models.Users.id == id).first() 
    user = user.to_dict() if user else user


    

    try:
        user_data = {
            "uuid": user.get("id"),
            "username": user.get("username"),
            "name": user.get("name"),
            "email": user.get("email"),
        }
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'user': user_data,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    username:str = raw_data.username
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    import uuid

    try:
        generated_uuid = str(uuid.uuid4())
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'username': username, 'name': name, 'email': email, 'password': password, 'created_at': current_datetime, 'updated_at': current_datetime, 'id': generated_uuid}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    user_data = new_users.to_dict()


    user_record = db.query(models.Users).filter(models.Users.email == email).first() 
    user_record = user_record.to_dict() if user_record else user_record

    res = {
        'user': user_data,
    }
    return res

async def delete_users_id(db: Session, id: str):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_assignees(db: Session):

    assignees_all = db.query(models.Assignees).all()
    assignees_all = [new_data.to_dict() for new_data in assignees_all] if assignees_all else assignees_all

    res = {
        'assignees_all': assignees_all,
    }
    return res

async def post_assignees(db: Session, raw_data: schemas.PostAssignees):
    task_id:int = raw_data.task_id
    team_id:int = raw_data.team_id
    user_id:str = raw_data.user_id
    user_name:str = raw_data.user_name


    
    from datetime import datetime

    try:
        current_datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'task_id': task_id, 'team_id': team_id, 'user_id': user_id, 'created_at': current_datetime, 'updated_at': current_datetime, 'user_name': user_name}
    new_assignees = models.Assignees(**record_to_be_added)
    db.add(new_assignees)
    db.commit()
    db.refresh(new_assignees)
    added_assignee = new_assignees.to_dict()

    res = {
        'task_id': added_assignee['task_id'],
        'team_id': added_assignee['team_id'],
        'user_id': added_assignee['user_id'],
        'user_name': added_assignee['user_name'],
    }
    return res

async def delete_assignees_id(db: Session, id: int):

    assignees_deleted = None
    record_to_delete = db.query(models.Assignees).filter(models.Assignees.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        assignees_deleted = record_to_delete.to_dict() 

    res = {
        'assignees_deleted': assignees_deleted,
    }
    return res

async def get_tasks(db: Session, id: int):

    tasks_all = db.query(models.Tasks).all()
    tasks_all = [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all

    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first() 
    tasks_one = tasks_one.to_dict() if tasks_one else tasks_one

    res = {
        'task': tasks_one,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    task_id:str = raw_data.task_id
    task_name:str = raw_data.task_name
    ask_description:str = raw_data.ask_description
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'task_id': task_id, 'task_name': task_name, 'ask_description': ask_description, 'priority': priority, 'visibility': visibility, 'created_at': current_datetime, 'updated_at': current_datetime}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks.to_dict()

    res = {
        'task': tasks_inserted_record,
    }
    return res

async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id:int = raw_data.id
    task_id:str = raw_data.task_id
    task_name:str = raw_data.task_name
    ask_description:str = raw_data.ask_description
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility
    tags:str = raw_data.tags


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    updated_task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'updated_at': current_datetime, 'task_id': task_id, 'task_name': task_name, 'ask_description': ask_description, 'priority': priority, 'visibility': visibility, 'tags': tags}.items():
          setattr(updated_task, key, value)
    db.commit()
    db.refresh(updated_task)
    updated_task = updated_task.to_dict() 

    res = {
        'data': updated_task,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict() 

    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def get_team_id(db: Session, id: int):

    team_one = db.query(models.Team).filter(models.Team.id == id).first() 
    team_one = team_one.to_dict() if team_one else team_one

    res = {
        'team_one': team_one,
    }
    return res

async def post_team(db: Session, raw_data: schemas.PostTeam):
    team_name:str = raw_data.team_name
    limit:int = raw_data.limit


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'limit': limit, 'team_name': team_name, 'created_at': current_datetime}
    new_team = models.Team(**record_to_be_added)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    team = new_team.to_dict()

    res = {
        'id': team['id'],
        'name': team['team_name'],
        'members_limit': team['limit'],
    }
    return res

async def delete_team_id(db: Session, id: int):

    team_deleted = None
    record_to_delete = db.query(models.Team).filter(models.Team.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        team_deleted = record_to_delete.to_dict() 

    res = {
        'team_deleted': team_deleted,
    }
    return res

async def get_team_users(db: Session, team_id: int):

    team_users = db.query(models.TeamUsers).all()
    team_users = [new_data.to_dict() for new_data in team_users] if team_users else team_users

    res = {
        'team_users': team_users,
    }
    return res

async def post_team_users(db: Session, raw_data: schemas.PostTeamUsers):
    team_id:int = raw_data.team_id
    user_id:str = raw_data.user_id
    can_view:str = raw_data.can_view
    can_comment:str = raw_data.can_comment
    can_edit:str = raw_data.can_edit


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'team_id': team_id, 'user_id': user_id, 'can_view': can_view, 'can_comment': can_comment, 'can_edit': can_edit, 'created_at': current_datetime}
    new_team_users = models.TeamUsers(**record_to_be_added)
    db.add(new_team_users)
    db.commit()
    db.refresh(new_team_users)
    team_user = new_team_users.to_dict()

    res = {
        'teamId': team_user['team_id'],
        'userId': team_user['user_id'],
        'comment_rights': team_user['can_comment'],
        'edit_rights': team_user['can_edit'],
        'view_rights': team_user['can_view'],
    }
    return res

async def delete_team_users_id(db: Session, user_id: str):

    team_users_deleted = None
    record_to_delete = db.query(models.TeamUsers).filter(models.TeamUsers.user_id == user_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        team_users_deleted = record_to_delete.to_dict() 

    res = {
        'team_users_deleted': team_users_deleted,
    }
    return res

async def patch_update_tags(db: Session, raw_data: schemas.PatchUpdateTags):
    task_id:int = raw_data.task_id
    tag:str = raw_data.tag


    task_data = db.query(models.Tasks).filter(models.Tasks.id == task_id).first() 
    task_data = task_data.to_dict() if task_data else task_data


    # stores the task_data returned through get a record
    task_tags = []  # Creating new list


    

    try:
        def add_tag(tags: List[str], tag: str) -> List[str]:
            # tagArrayFromDB: List=tags[0].tags
            tag = tag.strip().lower()
            if tag and tag not in tags:
                tags.append(tag)
            return tags
        
        updated_tags:List[str] = add_tag(task_data.tags, tag)
    except Exception as e:
        raise HTTPException(500, str(e))



    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    query_updated_tags = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    for key, value in {'tags': task_tags, 'updated_at': current_datetime}.items():
          setattr(query_updated_tags, key, value)
    db.commit()
    db.refresh(query_updated_tags)
    query_updated_tags = query_updated_tags.to_dict() 

    res = {
        'task': query_updated_tags,
    }
    return res

async def post_user_login(db: Session, raw_data: schemas.PostUserLogin):
    email:str = raw_data.email
    password:str = raw_data.password


    user_data = db.query(models.Users).filter(models.Users.email == email).first() 
    user_data = user_data.to_dict() if user_data else user_data


    # dictionary that contains the user data
    user_data_dictionary = {}  # Creating new dict


    # useless variable, scared to delete
    data_to_encrypt = {}  # Creating new dict


    

    try:
        if user_data == {}:
            data_to_encrypt ={}
            user_data_dictionary = {}
        
        data_to_encrypt = {
            "uuid": user_data.get("id"),
            "username": user_data.get("username"),
            "email": user_data.get("email"),
            "name": user_data["name"]
        }
    except Exception as e:
        raise HTTPException(500, str(e))



    # generated jwt token
    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=36000)).timestamp()),
        'data': user_data
    }

    jwt_token = jwt.encode(bs_jwt_payload, 'kd+eW6DTE70JItoGyLZGJUFr4p4qGjJdgqIwymLtVGI=', algorithm='HS256')


    

    try:
        if password == user_data["password"]:
            user_data_dictionary = {
            "username" : user_data["username"],
            "email" : user_data["email"],
            "name" : user_data["name"],
            "token" : jwt_token,
            "uuid": user_data["id"]
        }
        else:
            user_data_dictionary = {
                "error": "password did not match"
            }
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'user_data': user_data_dictionary,
    }
    return res

async def post_task_change_visibility(db: Session, raw_data: schemas.PostTaskChangeVisibility):
    task_id:int = raw_data.task_id
    visibility:str = raw_data.visibility


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    updated_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    for key, value in {'visibility': visibility, 'updated_at': current_datetime, 'id': task_id}.items():
          setattr(updated_task, key, value)
    db.commit()
    db.refresh(updated_task)
    updated_task = updated_task.to_dict() 

    res = {
        'task': updated_task,
    }
    return res

async def get_task_get_tags(db: Session, task_id: int):

    task_record = db.query(models.Tasks).all()
    task_record = [new_data.to_dict() for new_data in task_record] if task_record else task_record


    

    try:
        tags = {
            
        }
    except Exception as e:
        raise HTTPException(500, str(e))



    res = {
    }
    return res

async def post_task_change_visibility(db: Session):
    res = {
    }
    return res

async def post_task_change_visibility(db: Session, raw_data: schemas.PostTaskChangeVisibility):
    task_id:int = raw_data.task_id
    visibility:str = raw_data.visibility


    
    from datetime import datetime

    try:
        current_datetime:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    updated_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    for key, value in {'visibility': visibility, 'updated_at': current_datetime, 'id': task_id}.items():
          setattr(updated_task, key, value)
    db.commit()
    db.refresh(updated_task)
    updated_task = updated_task.to_dict() 

    res = {
        'task': updated_task,
    }
    return res

async def patch_task_change_visibility(db: Session):
    res = {
    }
    return res

async def post_task_change_priority(db: Session, raw_data: schemas.PostTaskChangePriority):
    task_id:int = raw_data.task_id
    priority:str = raw_data.priority


    updated_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    for key, value in {'priority': priority}.items():
          setattr(updated_task, key, value)
    db.commit()
    db.refresh(updated_task)
    updated_task = updated_task.to_dict() 

    res = {
        'task': updated_task,
    }
    return res

async def get_team_user_user_id(db: Session, user_id: str):

    all_team_users = db.query(models.TeamUsers).all()
    all_team_users = [new_data.to_dict() for new_data in all_team_users] if all_team_users else all_team_users

    res = {
        'user_teams': all_team_users,
    }
    return res

async def get_teams(db: Session):
    res = {
    }
    return res

async def get_team_users_team_id(db: Session, id: int):


    query = db.query(models.TeamUsers)
    query = query.filter(
        
        and_(
            models.TeamUsers.team_id == id
        )
    )


    team_users = query.all()
    team_users = [new_data.to_dict() for new_data in team_users] if team_users else team_users

    res = {
        'team_users': team_users,
    }
    return res

async def get_update_tags(db: Session):
    res = {
    }
    return res

async def get_get_all_tasks(db: Session):


    query = db.query(models.Tasks)


    tasks = query.all()
    tasks = [new_data.to_dict() for new_data in tasks] if tasks else tasks

    res = {
        'all_tasks': tasks,
    }
    return res

async def post_upload_document(db: Session, doc: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CP6X5H4BNH",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await doc.read()

    name = doc.filename
    file_path = file_path  + '/' + name

    import mimetypes
    doc.file.seek(0)
    s3_client.upload_fileobj(
        doc.file,
        bucket_name,
        name,
        ExtraArgs={"ContentType": mimetypes.guess_type(name)[0]}

    )

    file_type = Path(doc.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    uploaded_url = file_url
    res = {
        'url': uploaded_url,
    }
    return res

async def get_assignee_task_id(db: Session, task_id: int):


    query = db.query(models.Assignees)
    query = query.filter(
        
        and_(
            models.Assignees.task_id == task_id
        )
    )


    all_assignees_for_task_id = query.all()
    all_assignees_for_task_id = [new_data.to_dict() for new_data in all_assignees_for_task_id] if all_assignees_for_task_id else all_assignees_for_task_id

    res = {
        'data': all_assignees_for_task_id,
    }
    return res

async def get_task_user_id(db: Session, user_id: str):


    query = db.query(models.Assignees)
    query = query.filter(
        
        and_(
            models.Assignees.user_id == user_id
        )
    )


    assignee_details = query.all()
    assignee_details = [new_data.to_dict() for new_data in assignee_details] if assignee_details else assignee_details


    # a list that contains all the task_ids for a user_id
    aassigned_tasks = []  # Creating new list

    res = {
        'data': assignee_details,
    }
    return res

async def put_user_id(db: Session, raw_data: schemas.PutUserId):
    email:str = raw_data.email
    name:str = raw_data.name
    username:str = raw_data.username
    uuid:str = raw_data.uuid


    user = db.query(models.Users).filter(models.Users.id == uuid).first()
    for key, value in {'username': username, 'name': name, 'email': email}.items():
          setattr(user, key, value)
    db.commit()
    db.refresh(user)
    user = user.to_dict() 

    res = {
        'user': user,
    }
    return res

