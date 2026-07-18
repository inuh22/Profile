from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from app.config import templates
from typing import Annotated

router = APIRouter()

@router.post('/contact-form')
async def contact_form(
        request:Request,
        name : Annotated[str, Form()],
        email : Annotated[str, Form()],
        message : Annotated[str, Form()]
    ):
    print(name)
    print(email)
    print(message)

    return HTMLResponse(
        "<p>Message Sent!!!</p>"
    )