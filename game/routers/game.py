from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, schemas,oauth
from ..repository import game

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)



@router.post(
    "/",
    response_model=schemas.GameShow,
    status_code=status.HTTP_201_CREATED
)
def create(
    request: schemas.GameCreate,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_admin)
):
    return game.create(request, db)


@router.get(
    "/",
    response_model=list[schemas.GameShow]
)
def get_all(
    db: Session = Depends(database.get_db) ,  current_user: schemas.TokenData = Depends(oauth.get_admin_or_client)

):
    return game.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.GameShow
)
def get_by_id(
    id: int,
    db: Session = Depends(database.get_db) ,  current_user: schemas.TokenData = Depends(oauth.get_current_admin)

):

    result = game.get_by_id(id, db)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return result


@router.put(
    "/{id}",
    response_model=schemas.GameShow
)
def update(
    id: int,
    request: schemas.GameCreate,
    db: Session = Depends(database.get_db) ,  current_user: schemas.TokenData = Depends(oauth.get_current_admin)
):

    result = game.update(id, request, db)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return result


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int,
    db: Session = Depends(database.get_db) , current_user: schemas.TokenData = Depends(oauth.get_current_admin)
):

    deleted = game.delete(id, db)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )