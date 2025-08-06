import smtplib
from email.message import EmailMessage
from flask import flash
import os 
from dotenv import load_dotenv

load_dotenv()
# This script sends an email using the SMTP protocol.
fluentories_email = os.getenv("FLUENTORY_EMAIL")
system_email = os.getenv("SYSTEM_EMAIL")
system_password = os.getenv("SYSTEM_PASSWORD")

def send_email(subject, body):
    """
    Sends an email using Gmail's SMTP server with TLS and shows flash messages in Flask.
    """
    if subject == "Appointment":
        subject = f"New Appointment Scheduled"
    else:
        subject = "New Registration"

    message = EmailMessage()
    message["From"] = system_email
    message["To"] = fluentories_email
    message["Subject"] = subject
    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            # Start Transport Layer Security (TLS) for security
            smtp.starttls()
            # Login to the email account
            smtp.login(system_email, system_password)
            smtp.send_message(message)
    except Exception as e:
        flash("❌ Something went wrong. Please try again.")

def send_email_to_user(subject ,user_email):
    email_subject = f"Thank You for {subject} with Fluentory"
    
    body = f"""
Hi there,

Thank you for {subject} with Fluentory!

We’re thrilled to have you on board. Our team has received your information and will be reaching out to you shortly with more details tailored to your learning goals.

Whether you're here to improve your Business English, help your child gain confidence in public speaking, or explore other language skills, Fluentory is committed to making your journey impactful and inspiring.

If you have any questions in the meantime, feel free to reply to this email or visit our website.

Warm regards,  
The Fluentory Team  
📍 Based in Amman, Jordan  
🌐 www.fluentory.com  
📧 support@fluentory.com

------------------------------------------------------------

مرحبًا،

شكرًا لانضمامك إلى منصة Fluentory!

يسعدنا أن نرحب بك في مجتمعنا التعليمي. لقد تم استلام تسجيلك بنجاح، وسيقوم أحد أعضاء فريقنا بالتواصل معك قريبًا لمساعدتك في بدء رحلتك التعليمية.

في Fluentory، نؤمن بأن تعلّم اللغات يجب أن يكون عمليًا، وشخصيًا، ومؤثرًا. سواء كنت تسعى لتطوير مهاراتك في التواصل المهني أو دعم طفلك في تنمية ثقته في التحدث أمام الجمهور، فنحن هنا لنقدّم لك الدعم الكامل.

إذا كان لديك أي استفسار، لا تتردد في الرد على هذا البريد الإلكتروني أو زيارة موقعنا الإلكتروني.

مع خالص التحيات،  
فريق Fluentory  
📍 عمان، الأردن  
🌐 www.fluentory.com  
📧 support@fluentory.com

"""

    message = EmailMessage()
    message["From"] = system_email
    message["To"] = user_email
    message["Subject"] = email_subject
    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(system_email, system_password)
            smtp.send_message(message)
    except Exception as e:
        flash("❌ Something went wrong. Please try again.")
