from fastapi import Request, APIRouter
from app.config import templates

router = APIRouter()

@router.get('/data-privacy')
async def data_privacy(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="fragments/data_privacy.html",
        context={}
    )