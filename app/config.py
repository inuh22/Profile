import os
from pydantic import SecretStr
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

load_dotenv()
router = APIRouter()
templates = Jinja2Templates(directory='templates')

mail_config = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=SecretStr(os.getenv("MAIL_PASSWORD")),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS") == "True",
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS") == "True",
)