from fastapi import APIRouter, Request
from app.config import templates, router

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='pages/index.html',
        context={}
    )