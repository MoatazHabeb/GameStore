from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import models, schemas


def create(request: schemas.UserCreate, db: Session):
    client_role = db.query(models.Role).filter(
        models.Role.name == "client"
    ).first()

    new_user = models.User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        number=request.number,
        avatar=request.avatar,
        role=client_role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all(db: Session):
    return db.query(models.User).all()


def get_by_id(id: int, db: Session):
    return db.query(models.User).filter(models.User.id == id).first()


def update(id: int, request: schemas.UserCreate, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        return None

    user.update({
        "username": request.username,
        "email": request.email,
        "password": request.password,
        "number": request.number,
        "avatar": request.avatar
    })

    db.commit()

    return user.first()


def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        return False

    user.delete(synchronize_session=False)
    db.commit()

    return True