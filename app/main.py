from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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

