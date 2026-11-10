import logging

from fastapi import APIRouter, HTTPException  # type: ignore[import-not-found]
from app.schemas.ask import AskIn, AskOut
from app.services import gemini, content

router = APIRouter(prefix="/api", tags=["ask"])
logger = logging.getLogger(__name__)


@router.post("/ask", response_model=AskOut)
async def ask(body: AskIn):
    try:
        answer = await gemini.answer(
            message=body.message.strip(),
            history=[item.model_dump() for item in body.history],
            site_context=content.get_site_context(),
        )
    except Exception:
        logger.exception("Error generating answer from Gemini API")
        raise HTTPException(
            status_code=500, detail="Error generating answer from Gemini API"
        )
    return {"answer": answer}
