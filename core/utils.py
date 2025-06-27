import os

from ninja import Schema
from pydantic import EmailStr
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv(override=True)

GOOGLE_OAUTH_SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
  ]
 

credentials = {
    "type": os.getenv("SHEET_TYPE"),
    "project_id": os.getenv("SHEET_PROJECT_ID"),
    "private_key_id": os.getenv("SHEET_PRIVATE_KEY_ID"),
    "private_key": os.getenv("SHEET_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("SHEET_CLIENT_EMAIL"),
    "client_id": os.getenv("SHEET_CLIENT_ID"),
    "auth_uri": os.getenv("SHEET_AUTH_URI"),
    "token_uri": os.getenv("SHEET_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("SHEET_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("SHEET_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("SHEET_UNIVERSE_DOMAIN"),
}




class DetailSchema(Schema):
  name: str
  email: EmailStr
  gender: str
  dob: date
  lc: str
  year_joined: str
  role: str
  first_time: str
  expect: str
  social: str
  allergies: str
  antidote: str
  room_with_opps: str
  emergency: str
  related_by: str
  aob: str
  registered_at: datetime = datetime.utcnow()
  