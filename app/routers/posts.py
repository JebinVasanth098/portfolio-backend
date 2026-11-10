from fastapi import APIRouter, HTTPException

from app.schemas.content import Post, PostSummary
from app.services import content

router = APIRouter(prefix="/api")


@router.get("/posts", response_model=list[PostSummary])
def list_posts():
    return content.get_posts()


@router.get("/posts/{slug}", response_model=Post)
def read_post(slug: str):
    post = content.get_post(slug)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post