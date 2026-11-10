import json
from pathlib import Path


CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
POSTS_DIR = CONTENT_DIR / "posts"
SUPPORTED_CONTENT_SUFFIXES = {".json", ".md"}


def get_site_context() -> str:
    files = sorted(
        path
        for path in CONTENT_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_CONTENT_SUFFIXES
    ) if CONTENT_DIR.exists() else []
    if not files:
        return "No site content is configured yet."

    return "\n\n".join(
        f"## {path.stem}\n{path.read_text(encoding='utf-8')}"
        for path in files
    )


def _load_posts() -> list[dict]:
    if not POSTS_DIR.exists():
        return []

    posts = []
    for path in sorted(POSTS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as post_file:
            post = json.load(post_file)
        if not isinstance(post, dict):
            raise ValueError(f"Post file must contain a JSON object: {path}")
        posts.append(post)
    return posts


def get_posts() -> list[dict]:
    posts = _load_posts()
    posts.sort(key=lambda post: post.get("date", ""), reverse=True)
    summary_fields = ("slug", "title", "date", "summary", "tags", "readTime")
    return [
        {field: post[field] for field in summary_fields if field in post}
        for post in posts
    ]


def get_post(slug: str) -> dict | None:
    return next(
        (post for post in _load_posts() if post.get("slug") == slug),
        None,
    )


def body_to_text(body):
    parts = []
    for b in body:
        if b["type"] == "list":
            parts.extend(f"- {item}" for item in b["items"])
        else:
            parts.append(b["content"])
    return "\n".join(parts)