from ninja import Schema
from pydantic import EmailStr
from datetime import date

class DetailSchema(Schema):
  name: str
  email: EmailStr
  gender: str
  #dob: date
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
  