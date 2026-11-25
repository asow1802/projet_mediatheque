from datetime import date
from pydantic import BaseModel, Field, model_validator, EmailStr, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class telephoneFR(PhoneNumber):
    default_region_code = "FR"
    phone_format = "E164"
    
class AdherentCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    nom: str = Field(min_length=2, max_length=20)
    prenom: str = Field(min_length=3, max_length=50)
    adresse: str = Field(min_length=3, max_length=150)
    date_inscription: date = Field(
        ge=date(1900, 1, 1)
    )
    telephone: telephoneFR = Field(min_length=10, max_length=15)
    email: EmailStr = Field(min_length=5, max_length=100)
    
    
    @model_validator(mode="after")
    def validation_inscription(self):
        if self.date_inscription > date.today():
            raise ValueError(
            "Veuillez vérifier la date d'inscription."
            )
        
        return self
class AdherentUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    nom: str = Field(min_length=2, max_length=20)
    prenom: str = Field(min_length=3, max_length=50)
    adresse: str = Field(min_length=3, max_length=150)
    date_inscription: date = Field(
        ge=date(1900, 1, 1)
    )
    telephone: telephoneFR = Field(min_length=10, max_length=15)
    email: EmailStr = Field(min_length=5, max_length=100)
    @model_validator(mode="after")
    def validation_inscription(self):
        if self.date_inscription > date.today():
            raise ValueError(
            "Veuillez vérifier la date d'inscription."
            )
        
        return self
