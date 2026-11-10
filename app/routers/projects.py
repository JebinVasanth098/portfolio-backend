from typing import Any

from fastapi import APIRouter  # type: ignore[import-not-found]

router = APIRouter(prefix="/api", tags=["projects"])


@router.get("/projects")
async def get_projects() -> list[dict[str, Any]]:
    return [
        {
          "slug": "WIP",
          "name": "WIP(WORK IN PROGRESS!)",
          "summary": "",
          "stack": ["React", "FastAPI", "Python"],
          "links": [
            {
              "label": "Source",
              "href": ""
            }
          ]
        }
    ] 

