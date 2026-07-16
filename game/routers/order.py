from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, schemas, oauth
from ..repository import order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "/",
    response_model=schemas.OrderShow,
    status_code=status.HTTP_201_CREATED
)
def create(
    request: schemas.OrderCreate,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth.get_admin_or_client)
):
    return order.create(request, db)


@router.get(
    "/",
    response_model=list[schemas.OrderShow]
)
def get_all(
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_admin)
):
    return order.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.OrderShow
)
def get_by_id(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_user)
):

    result = order.get_by_id(id, db)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return result


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_admin)
):

    deleted = order.delete(id, db)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )