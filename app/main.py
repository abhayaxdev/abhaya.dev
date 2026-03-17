from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from app.dependencies import get_templates

from .routers.homepage_router import router as homepage_router
from .routers.blogs_router import router as blogs_router
from .routers.books_router import router as books_router
from .routers.photos_router import router as photos_router



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name='static')

app.include_router(homepage_router)
app.include_router(blogs_router, prefix='/blogs')
app.include_router(photos_router, prefix='/photos')
app.include_router(books_router, prefix='/books')

