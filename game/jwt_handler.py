from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC

from . import schemas

SECRET_KEY = "4d9e4cf0d55d66b519e9d0d6073cf4d5ef7d93a682e4d7e1a0d4d0d8efefef78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = payload.get("sub")
        role = payload.get("role")

        if username is None or role is None:
            raise credentials_exception

        token_data = schemas.TokenData(
            username=username,
            role=role
        )

        return token_data

    except JWTError:
        raise credentials_exception













