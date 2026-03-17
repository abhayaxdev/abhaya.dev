from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.dependencies import get_templates



router = APIRouter()
templates = get_templates()


@router.get("/", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse(
        request=request, name='blogs.html',
    )


@router.get("/blog/{id}")
async def get_blog_id(id: int):
    return {"blog_id": id}



