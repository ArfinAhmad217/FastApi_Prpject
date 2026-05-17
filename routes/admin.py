from fastapi import APIRouter, Depends, HTTPException

from auth.Oauth2 import admin_only

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/")
def admin_route(
    current_user = Depends(admin_only)
):

    return {
        "message": "Welcome Admin"
    }