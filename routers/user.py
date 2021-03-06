


from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, database , models
from sqlalchemy.orm  import Session
from blog.repositiry import user


router = APIRouter(
    prefix="/User",
     tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

    

@router.get('/{id}', response_model = schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db) ):
    return user.show(id, db)
         