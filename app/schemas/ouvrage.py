from datetime import date
from pydantic import BaseModel, Field, model_validator, ConfigDict
from pydantic_extra_types.isbn import ISBN


class OuvrageCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    isbn: ISBN
    date_publication: date = Field(
        ge=date(1900, 1, 1)
    )
    titre: str = Field(min_length=1, max_length=100)
    nombre_de_pages: int = Field(gt=0)
    editeur: str = Field(min_length=2, max_length=100)
    genre: str | None = Field(min_length=2, max_length=50, default=None)
    id_auteur: int = Field(gt=0)
    
    @model_validator(mode="after")
    def validation_date_publication(self):
        if self.date_publication > date.today():
            raise ValueError(
            "Veuillez vérifier la date de publication."
            )
        
        return self
class OuvrageUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    isbn: ISBN
    date_publication: date = Field(
        ge=date(1900, 1, 1)
    )
    titre: str = Field(min_length=1, max_length=100)
    nombre_de_pages: int = Field(gt=0)
    editeur: str = Field(min_length=2, max_length=100)
    genre: str = Field(min_length=2, max_length=50, default=None)
    id_auteur: int = Field(gt=0)
    @model_validator(mode="after")
    def validation_date_publication(self):
        if self.date_publication > date.today():
            raise ValueError(
            "Veuillez vérifier la date de publication."
            )
        
        return self