from fastapi import APIRouter  # type: ignore[import-not-found]

router = APIRouter(tags=["health"])


@router.get("/contact")
async def contact_info() -> dict[str, str]:
	return {"message": "This is the contact page"}