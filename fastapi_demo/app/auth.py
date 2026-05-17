from datetime import datetime, timedelta, timezone
import base64
import hashlib
import hmac
import json

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.data import users
from app.schemas import User

SECRET_KEY = "demo-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

bearer_scheme = HTTPBearer()


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _base64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def _json_encode(data: dict) -> str:
    json_data = json.dumps(data, separators=(",", ":")).encode()
    return _base64url_encode(json_data)


def create_access_token(username: str) -> str:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    header = {"alg": ALGORITHM, "typ": "JWT"}
    payload = {"sub": username, "exp": int(expires_at.timestamp())}

    header_part = _json_encode(header)
    payload_part = _json_encode(payload)
    signing_input = f"{header_part}.{payload_part}".encode()
    signature = hmac.new(SECRET_KEY.encode(), signing_input, hashlib.sha256).digest()

    return f"{header_part}.{payload_part}.{_base64url_encode(signature)}"


def decode_access_token(token: str) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не вдалося перевірити токен",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        header_part, payload_part, signature_part = token.split(".")
        signing_input = f"{header_part}.{payload_part}".encode()
        expected_signature = hmac.new(
            SECRET_KEY.encode(),
            signing_input,
            hashlib.sha256,
        ).digest()
        received_signature = _base64url_decode(signature_part)

        if not hmac.compare_digest(expected_signature, received_signature):
            raise credentials_exception

        payload = json.loads(_base64url_decode(payload_part))
    except (ValueError, json.JSONDecodeError):
        raise credentials_exception

    if payload.get("exp", 0) < int(datetime.now(timezone.utc).timestamp()):
        raise credentials_exception

    return payload


def authenticate_user(username: str, password: str) -> User | None:
    user = users.get(username)
    if user is None or user["password"] != password:
        return None

    return User(username=user["username"])


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> User:
    payload = decode_access_token(credentials.credentials)
    username = payload.get("sub")

    if username not in users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Користувача не знайдено",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return User(username=username)
