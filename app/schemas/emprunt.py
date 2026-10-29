from datetime import date
from pydantic import BaseModel, Field

class EmpruntCreate(BaseModel):
    date_debut: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    date_retour_prevue: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    date_retour_effective: date | None = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    id_adherent: int
    id_ouvrage: int
class EmpruntUpdate(BaseModel):
    date_debut: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    date_retour_prevue: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    date_retour_effective: date | None = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    id_adherent: int    
    id_ouvrage: int
