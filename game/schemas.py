from typing import List, Optional

from pydantic import BaseModel




               # User Schemas
class UserBase(BaseModel):
    username: str
    email: str
    number: str
    avatar: str


class RoleBase(BaseModel):
    name: str


class RoleShow(RoleBase):
    id: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    number: str
    avatar: str


class UserShow(BaseModel):
    id: int
    username: str
    email: str
    number: str
    avatar: str | None = None
    role: RoleShow

    class Config:
        from_attributes = True





                 # Game Schemas


class GameBase(BaseModel):
    name: str
    description: str
    price: int
    photo: str


class GameCreate(GameBase):
    pass


class GameShow(GameBase):
    id: int

    class Config:
        from_attributes = True

        # -----------------------
        # Order Item
        # -----------------------
class OrderItemCreate(BaseModel):
        game_id: int
        quantity: int

class OrderItemShow(BaseModel):
            id: int
            game: GameShow
            quantity: int

            class Config:
                from_attributes = True

        # -----------------------
        # Order
        # -----------------------

class OrderCreate(BaseModel):
        items: list[OrderItemCreate]

class OrderShow(BaseModel):
        id: int
        total_price: int
        items: list[OrderItemShow]

        class Config:
            from_attributes = True


#  Role with User

class UserSimple(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class RoleWithUsers(RoleBase):
    id: int
    users: List[UserSimple]

    class Config:
        from_attributes = True





class LoginUser(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str]
    role: str