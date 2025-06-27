import os
import requests

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_mail(email, attachment):
  html_content = render_to_string("emails/confirm_register.html")  # Optional context

  msg = EmailMessage(
        subject="Your ticket to NC Akure'25",
        body=html_content,
        from_email=None,  # Uses DEFAULT_FROM_EMAIL
        to=[email],
    )
  msg.content_subtype = "html"

    # Attach PDF
  msg.attach('ticket.pdf', attachment.read(), 'application/pdf')
    
  msg.send()