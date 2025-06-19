from fastapi import APIRouter

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/repos")
def list_repos():
    return {"message": "This will list GitHub repos"}