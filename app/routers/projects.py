from typing import Any

from fastapi import APIRouter  # type: ignore[import-not-found]

router = APIRouter(prefix="/api", tags=["projects"])


@router.get("/projects")
async def get_projects() -> list[dict[str, Any]]:
    return [
        {
          "slug": "portfolio-site",
          "name": "Portfolio Website",
          "summary": "A personal portfolio showcasing projects, writing, and experience.",
          "stack": ["React", "FastAPI", "Python"],
          "links": [
            {
              "label": "Source",
              "href": "https://github.com/your-handle/portfolio-site"
            }
          ]
        },
        {
          "slug": "task-manager",
          "name": "Task Manager",
          "summary": "A simple app for creating and tracking tasks.",
          "stack": ["JavaScript", "FastAPI"],
          "links": []
        }
    ]      

