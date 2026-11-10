# app/main.py
from fastapi import FastAPI  # type: ignore[import-not-found]
from fastapi.middleware.cors import CORSMiddleware  # type: ignore[import-not-found]
from config import settings
from app.routers import ask, contact, health, posts, projects

app = FastAPI(title="Portfolio API")

@app.get("/")
def read_root():
    return {"message": "Welcome to my portfolio backend!"}

# Only needed when the site and API are on different origins (production).
# In development the Vite proxy makes everything same-origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(posts.router)
app.include_router(contact.router)
app.include_router(ask.router)