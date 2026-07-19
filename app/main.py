from fastapi import FastAPI, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Annotated
from app.routes.home import router as home_router
from app.routes.contact import router as contact_router
from app.routes.data_privacy import router as dp_router


app = FastAPI()

# Static File
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name = "static"    
)

app.include_router(home_router)
app.include_router(contact_router)
app.include_router(dp_router)
