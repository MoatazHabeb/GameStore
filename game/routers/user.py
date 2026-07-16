from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import user

router = APIRouter(
    prefix="/users"
)

@router.post("/", response_model=schemas.UserShow,status_code=status.HTTP_201_CREATED)
def create(request: schemas.UserCreate,db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get("/",response_model=list[schemas.UserShow])
def get_all(db: Session = Depends(database.get_db)):
    return user.get_all(db)



@router.get("/{id}",response_model=schemas.UserShow)
def get_by_id(id: int,db: Session = Depends(database.get_db)):
    result = user.get_by_id(id, db)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result


@router.put("/{id}", response_model=schemas.UserShow)
def update(id: int,request: schemas.UserCreate,db: Session = Depends(database.get_db)):
    result = user.update(id, request, db)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int,db: Session = Depends(database.get_db)):
    deleted = user.delete(id, db)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )