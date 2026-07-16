from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from .. import database, models, jwt_handler
from ..hashing import Hash

api_router = APIRouter()


@api_router.post("/login")
async def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):

    user = db.query(models.User).filter(
        models.User.username == request.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = jwt_handler.create_access_token(
        data={
            "sub": user.username,
            "role": user.role.name
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role.name
    }