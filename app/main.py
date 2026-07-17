from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

# Templates
templates = Jinja2Templates(directory='templates')

# Static File
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name = "static"    
)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={}
    )

@app.post("/contact-form")
async def contact_form(
    request: Request,
    name : Annotated[str, Form()] ,
    email : Annotated[str, Form()],
    message : Annotated[str, Form()]
    ):
    print(name)
    print(email)
    print(message)
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={}
    )