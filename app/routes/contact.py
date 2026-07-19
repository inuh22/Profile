from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from app.config import templates
from app.services.mailer import contact_mailer
from typing import Annotated
from pydantic import EmailStr


router = APIRouter()


@router.get('/mail-form')
async def mail_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='fragments/mail_form.html',
        context={}
    )

@router.post('/send-mail-form')
async def contact_form(
        request:Request,
        name : Annotated[str, Form()],
        email : Annotated[EmailStr, Form()],
        message : Annotated[str, Form()]
    ):

    if not name or not email or not message:
        return templates.TemplateResponse(
            request=request,
            name='fragments/unexpected.html',
            context={}
        )

    try:
        await contact_mailer(name, email, message)
    except Exception:
        return templates.TemplateResponse(
            request=request,
            name="fragments/unexpected.html",
            context={},
            status_code=500
        )

    return templates.TemplateResponse(
        request=request,
        name='fragments/sent_success.html',
        context={}
    )