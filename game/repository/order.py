from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.OrderCreate, db: Session):

    order = models.Order(total_price=0)

    db.add(order)
    db.flush()

    total = 0

    for item in request.items:

        game = db.query(models.Game).filter(
            models.Game.id == item.game_id
        ).first()

        if not game:
            continue

        order_item = models.OrderItem(
            order_id=order.id,
            game_id=game.id,
            quantity=item.quantity
        )

        db.add(order_item)

        total += game.price * item.quantity

    order.total_price = total

    db.commit()
    db.refresh(order)

    return order


def get_all(db: Session):
    return db.query(models.Order).all()


def get_by_id(id: int, db: Session):
    return db.query(models.Order).filter(
        models.Order.id == id
    ).first()


def delete(id: int, db: Session):

    order = db.query(models.Order).filter(
        models.Order.id == id
    ).first()

    if not order:
        return False

    db.delete(order)
    db.commit()

    return True