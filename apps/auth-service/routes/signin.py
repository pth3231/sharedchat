from fastapi import APIRouter, status

router = APIRouter(
    prefix="/signin",
    tags=["signin"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/")
async def signin_root():
    return "This is the signin API"