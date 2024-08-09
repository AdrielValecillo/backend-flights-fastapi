import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv("./.env")






class EmailSender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")

    def send_email(self, sender_email, receiver_email, subject, html_content):
        message = EmailMessage()
        message.set_content(html_content, subtype='html')
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(message)


