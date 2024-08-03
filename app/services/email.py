import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self):
        self.smtp_server = "sandbox.smtp.mailtrap.io"
        self.smtp_port = 2525
        self.smtp_user = "10c60c5b4898bb"
        self.smtp_password = "ad9d381b4d9f26"

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



