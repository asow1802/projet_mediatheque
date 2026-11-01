from datetime import date
from pydantic import BaseModel, Field, model_validator

class EmpruntCreate(BaseModel):
    date_debut: date = Field(
        ge=date(1900, 1, 1)
    )
    date_retour_prevue: date = Field(
        ge=date(1900, 1, 1)
    )
    id_adherent: int = Field(gt=0)
    id_ouvrage: int  = Field(gt=0)
    
    
    @model_validator(mode="after")
    def validation_age(self):
        if self.date_retour_prevue <= self.date_debut:
            raise ValueError(
            "La date de retour prévue doit etre postérieure à la date de début."
            )
        elif self.date_retour_prevue < date.today():
            raise ValueError(
                        "La date de retour prévue doit etre dans le futur"
                        )
        return self
    def validation_date_debut(self):
        if self.date_debut > date.today():
            raise ValueError(
            "La date de début ne peut pas etre dans le futur"
            )
        return self
class EmpruntUpdate(BaseModel):
    date_debut: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    date_retour_prevue: date = Field(
        ge=date(1900, 1, 1)
    )
    date_retour_effective: date | None = None
    id_adherent: int = Field(gt=0)
    id_ouvrage: int  = Field(gt=0)
    
    
    @model_validator(mode="after")
    def validation_age(self):
        if self.date_retour_effective is not None and self.date_retour_effective < self.date_debut:
            raise ValueError(
            "La date de retour effective doit etre postérieure à la date de début."
            )
        elif self.date_retour_effective is not None and self.date_retour_effective > date.today():
            raise ValueError(
                        "La date de retour effective ne peut pas etre dans le futur"
                        )
        elif self.date_retour_prevue <= self.date_debut:
            raise ValueError(
                        "La date de retour prévue doit etre postérieure à la date de début."
                        )
        return self
    def validation_date_debut(self):
        if self.date_debut > date.today():
            raise ValueError(
            "La date de début ne peut pas etre dans le futur"
            )
        return self
