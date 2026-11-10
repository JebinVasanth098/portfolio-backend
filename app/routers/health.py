from fastapi import APIRouter  # type: ignore[import-not-found]

router = APIRouter(prefix = "/api", tags=["health"])


@router.get("/health")
async def health_check() -> dict[str, str]:
	return {"status": "ok"}
