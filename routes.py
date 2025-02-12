from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: str, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: str, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/assignees/')
async def get_assignees(db: Session = Depends(get_db)):
    try:
        return await service.get_assignees(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/assignees/')
async def post_assignees(raw_data: schemas.PostAssignees, db: Session = Depends(get_db)):
    try:
        return await service.post_assignees(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/assignees/id')
async def delete_assignees_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_assignees_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(raw_data: schemas.PutTasksId, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team/id')
async def get_team_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_team_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/team/')
async def post_team(raw_data: schemas.PostTeam, db: Session = Depends(get_db)):
    try:
        return await service.post_team(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/team/id')
async def delete_team_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_team_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_users/')
async def get_team_users(team_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_team_users(db, team_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/team_users/')
async def post_team_users(raw_data: schemas.PostTeamUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_team_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/team_users/id')
async def delete_team_users_id(user_id: str, db: Session = Depends(get_db)):
    try:
        return await service.delete_team_users_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.patch('/update-tags')
async def patch_update_tags(raw_data: schemas.PatchUpdateTags, db: Session = Depends(get_db)):
    try:
        return await service.patch_update_tags(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user/login')
async def post_user_login(raw_data: schemas.PostUserLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_user_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task/change-visibility')
async def post_task_change_visibility(raw_data: schemas.PostTaskChangeVisibility, db: Session = Depends(get_db)):
    try:
        return await service.post_task_change_visibility(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task/get-tags')
async def get_task_get_tags(task_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_task_get_tags(db, task_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task/change-visibility')
async def post_task_change_visibility(db: Session = Depends(get_db)):
    try:
        return await service.post_task_change_visibility(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task/change-visibility')
async def post_task_change_visibility(raw_data: schemas.PostTaskChangeVisibility, db: Session = Depends(get_db)):
    try:
        return await service.post_task_change_visibility(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.patch('/task/change-visibility')
async def patch_task_change_visibility(db: Session = Depends(get_db)):
    try:
        return await service.patch_task_change_visibility(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task/change-priority')
async def post_task_change_priority(raw_data: schemas.PostTaskChangePriority, db: Session = Depends(get_db)):
    try:
        return await service.post_task_change_priority(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_user/user_id')
async def get_team_user_user_id(user_id: str, db: Session = Depends(get_db)):
    try:
        return await service.get_team_user_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams')
async def get_teams(db: Session = Depends(get_db)):
    try:
        return await service.get_teams(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_users/team_id')
async def get_team_users_team_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_team_users_team_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/update-tags')
async def get_update_tags(db: Session = Depends(get_db)):
    try:
        return await service.get_update_tags(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/get-all-tasks')
async def get_get_all_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_get_all_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/upload-document')
async def post_upload_document(doc: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_upload_document(db, doc)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/assignee/task_id')
async def get_assignee_task_id(task_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_assignee_task_id(db, task_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task/user_id')
async def get_task_user_id(user_id: str, db: Session = Depends(get_db)):
    try:
        return await service.get_task_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user/id')
async def put_user_id(raw_data: schemas.PutUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

