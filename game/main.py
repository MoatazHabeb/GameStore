from fastapi import FastAPI


from .database import engine, SessionLocal
from .routers import user,game,authentication,order
from sqlalchemy.orm import Session
from . import models

app = FastAPI()



def seed_roles(db: Session):

    admin = db.query(models.Role).filter(
        models.Role.name == "admin"
    ).first()

    if not admin:
        db.add(models.Role(name="admin"))

    client = db.query(models.Role).filter(
        models.Role.name == "client"
    ).first()

    if not client:
        db.add(models.Role(name="client"))

    db.commit()




models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

seed_roles(db)

db.close()

app.include_router(user.router, tags=["User"])
app.include_router(game.router)

app.include_router(authentication.api_router,tags=["Authentication"])
app.include_router(order.router)