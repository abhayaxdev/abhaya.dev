from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.dependencies import get_templates



router = APIRouter()
templates = get_templates()


@router.get("/", response_class=HTMLResponse)
async def get_photos(request: Request):
    return templates.TemplateResponse(
        request=request, name='books.html',
    )


@router.get("/book/{id}")
def get_book_detail(id: int):
    return {"book_id": id}