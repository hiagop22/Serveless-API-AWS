from fastapi import APIRouter, Depends
from api.models import User
from api.auth import get_current_active_user

router = APIRouter(tags=["users"],
                   prefix="/users",
                   )

@router.get("/me", response_model=User)
async def read_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/me/items")
async def read_user(current_user: User = Depends(get_current_active_user)):
    return [{"item": "Foo", "owner": current_user.username}]