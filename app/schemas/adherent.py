from datetime import date
from pydantic import BaseModel, Field, EmailStr

class AdherentCreate(BaseModel):
    nom: str = Field(min_length=2)
    prenom: str = Field(min_length=3)
    adresse: str = Field(min_length=3, max_length=150)
    date_inscription: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    telephone: str = Field(min_length=10, max_length=15)
    email: str = EmailStr
class AdherentUpdate(BaseModel):
    nom: str = Field(min_length=2)
    prenom: str = Field(min_length=3)
    date_inscription: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    telephone: str = Field(min_length=10, max_length=15)
    email: str = EmailStr   
