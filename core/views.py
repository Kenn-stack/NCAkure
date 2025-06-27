import gspread
import base64

from pathlib import Path

from django.shortcuts import render
from ninja import NinjaAPI

from .utils import DetailSchema, credentials
from .email import send_mail
from .ticket import generate_delegate_ticket

api = NinjaAPI()

# Create your views here.
@api.post("/register")
def register(request, details: DetailSchema):
  email = details.email
  lc = details.lc
  attendee_name = details.name
  details.dob = details.dob.isoformat()
  details.registered_at = details.registered_at.isoformat()
  
  #save details to google sheets
  data = [d for d in details.dict().values()]
  gc = gspread.service_account_from_dict(credentials)
  
  
  '''json_path = Path(__file__).resolve().parent.parent / "aiesec-backend.json"
  gc = gspread.service_account(filename=str(json_path))'''
  worksheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1yTM-nJDspyO-DBuwvNa307cDECZs7XaRFTg4DbUE4dU/edit?usp=drivesdk").sheet1
  worksheet.append_row(data)
  
  # Get the ticket that will be attached to the mail
  pdf_bytes = generate_delegate_ticket(attendee_name, lc)
  
  send_mail(email, pdf_bytes)
  return {"message": "Success"}
  