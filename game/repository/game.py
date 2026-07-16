from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.GameCreate, db: Session):

    game = models.Game(
        name=request.name,
        description=request.description,
        price=request.price,
        photo=request.photo
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    return game


def get_all(db: Session):
    return db.query(models.Game).all()


def get_by_id(id: int, db: Session):
    return db.query(models.Game).filter(
        models.Game.id == id
    ).first()


def update(id: int, request: schemas.GameCreate, db: Session):

    game = db.query(models.Game).filter(
        models.Game.id == id
    ).first()

    if not game:
        return None

    game.name = request.name
    game.description = request.description
    game.price = request.price
    game.photo = request.photo

    db.commit()
    db.refresh(game)

    return game


def delete(id: int, db: Session):

    game = db.query(models.Game).filter(
        models.Game.id == id
    ).first()

    if not game:
        return False

    db.delete(game)
    db.commit()

    return True