from .database import Base

from sqlalchemy import (
    Column,
    Integer,
    String,
    Identity,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship





# ------------------------
# User
# ------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Identity(start=1), primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    number = Column(String(255))
    avatar = Column(String(255))

    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False
    )

    role = relationship(
        "Role",
        back_populates="users"
    )


# ------------------------
# Role
# ------------------------

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    users = relationship(
        "User",
        back_populates="role"
    )

# ------------------------
# Game
# ------------------------

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    price = Column(Integer, nullable=False)
    photo = Column(String(255))

    order_items = relationship(
        "OrderItem",
        back_populates="game"
    )


# ------------------------
# Order
# ------------------------

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, Identity(start=1), primary_key=True)

    total_price = Column(Integer, default=0)

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )


# ------------------------
# Order Item
# ------------------------

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, Identity(start=1), primary_key=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    game_id = Column(
        Integer,
        ForeignKey("games.id")
    )

    quantity = Column(Integer, nullable=False)

    order = relationship(
        "Order",
        back_populates="items"
    )

    game = relationship(
        "Game",
        back_populates="order_items"
    )