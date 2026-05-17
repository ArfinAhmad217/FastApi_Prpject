from fastapi import APIRouter, Depends

from auth.Oauth2 import get_current_user

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students(
    current_user = Depends(get_current_user)
):

    return {
        "message": "Protected route working",
        "user": current_user.email
    }