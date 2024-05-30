import smtplib
from email.message import EmailMessage

# Información del remitente y destinatario
sender_email = "from@example.com"
receiver_email = "to@example.com"

# Creación del mensaje
message = EmailMessage()
message.set_content("This is a test e-mail message.")
message["Subject"] = "Hi Mailtrap"
message["From"] = "Private Person <from@example.com>"
message["To"] = "A Test User <to@example.com>"

# Configuración del servidor SMTP
smtp_server = "sandbox.smtp.mailtrap.io"
smtp_port = 2525
smtp_user = "10c60c5b4898bb"
smtp_password = "ad9d381b4d9f26"

# Envío del correo electrónico
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(message)
