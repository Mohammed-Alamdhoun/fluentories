import smtplib
from email.message import EmailMessage
from flask import flash

# This script sends an email using the SMTP protocol.
fluentories_email = "mohammedalmadhoum@gmail.com"
my_email = "almadhounmohammed.2002@gmail.com"
password = "nxaa dlic cnwy cvnu"
connection = smtplib.SMTP('smtp.gmail.com', 587)
# Start Transport Layer Security (TLS) for security
connection.starttls()
# Login to the email account
connection.login(user= my_email, password=password)

def send_email(subject, body):
    """
    Sends an email using Gmail's SMTP server with TLS and shows flash messages in Flask.
    """
    message = EmailMessage()
    message["From"] = my_email
    message["To"] = fluentories_email
    message["Subject"] = subject
    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(my_email, password)
            smtp.send_message(message)
    except Exception as e:
        flash(f"❌ Failed register")

