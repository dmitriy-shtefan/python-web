from fastapi import APIRouter, HTTPException, status

from ..auth import authenticate_user, create_access_token
from ..schemas import LoginRequest, TokenResponse

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):

    user = authenticate_user(credentials.username, credentials.password)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    token = create_access_token(user.username)

    return {"access_token": token}
