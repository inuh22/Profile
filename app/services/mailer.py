from fastapi_mail import FastMail, MessageSchema
from app.config import mail_config

fast_mail = FastMail(mail_config)


async def contact_mailer(name: str, email: str, message:str):
    html = f"""
    <h2>New Contact Form Submission</h2>

    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>

    <p><strong>Message:</strong></p>
    <p>{message}</p>
    """

    msg = MessageSchema(
        subject="New Portfolio Contact",
        recipients=[mail_config.MAIL_FROM],
        body=html,
        subtype="html",
    )

    await fast_mail.send_message(msg)