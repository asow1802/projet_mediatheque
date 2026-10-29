from datetime import date
from pydantic import BaseModel, Field

class OuvrageCreate(BaseModel):
    isbn: str = Field(min_length=10, max_length=13)
    date_publication: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    titre: str = Field(min_length=2)
    nombre_de_pages: int = Field(gt=0)
    editeur: str = Field(min_length=2)
    id_auteur: int
class OuvrageUpdate(BaseModel):
    isbn: str = Field(min_length=10, max_length=13)
    date_publication: date = Field(
        ge=date(1900, 1, 1), le=date.today()
    )
    titre: str = Field(min_length=2)
    nombre_de_pages: int = Field(gt=0)
    editeur: str = Field(min_length=2)
    id_auteur: int
