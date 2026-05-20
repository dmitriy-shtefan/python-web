from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from .data import users
from .schemas import User

bearer_scheme = HTTPBearer()

# Demo-only token storage. Tokens disappear when the app restarts.
active_tokens: dict[str, str] = {}


def authenticate_user(username: str, password: str) -> User | None:
    user = users.get(username)

    if user is None:
        return None

    if user['password'] != password:
        return None

    return User(username=user['username'])


def create_access_token(username: str) -> str:
    token = f'demo-token-for-{username}'
    active_tokens[token] = username
    return token


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> User:
    token = credentials.credentials
    username = active_tokens.get(token)

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token',
            headers={'Auth': 'Bearer'},
        )

    return User(username=username)
