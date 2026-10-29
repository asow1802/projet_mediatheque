from datetime import date
from pydantic import BaseModel, Field

class AuteurCreate(BaseModel):
    nom: str = Field(min_length=2)
    prenom: str = Field(min_length=3)
    date_naissance: date = Field(
        ge =date(1900, 1, 1), le=date.today()
    )
    lieu_naissance: str = Field(min_length=3, max_length=150)
class AuteurUpdate(BaseModel):
    nom: str = Field(min_length=2)
    prenom: str = Field(min_length=3)
    date_naissance: date = Field(
        ge =date(1900, 1, 1), le=date.today()
    )
    lieu_naissance: str = Field(min_length=3, max_length=150)
