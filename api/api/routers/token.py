from fastapi import APIRouter, status, HTTPException, Depends

from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from api.auth import (ACCESS_TOKEN_EXPERIRE_MINUTES, 
                     create_access_token,
                     fake_users_db,
                     authenticate_user,
                     )

router = APIRouter(tags=["token"],
                   prefix="/token",
                   )

@router.post("/")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPERIRE_MINUTES)
    access_token = create_access_token(
        data = {"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}