from datetime import date
from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict

class AuteurCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    nom: str = Field(min_length=2, max_length=20)
    prenom: str = Field(min_length=3, max_length=50)
    date_naissance: date = Field(
        ge =date(1900, 1, 1)
    )
    lieu_naissance: str = Field(min_length=3, max_length=100)
    
    # @model_validator(mode="before")
    # def validation_nomComplet(self):
    #         if len(self.nom)<2  or len(self.prenom) < 3:
    #             raise ValueError(
    #             "Le nom de l'auteur est invalide"
    #             )
    #         return self
    
    @model_validator(mode="after")
    def validation_age(self):
        age = date.today().year - self.date_naissance.year
        if age < 10:
            raise ValueError(
            "Veuillez vérifier l'age de l'auteur."
            )
        return self
class AuteurUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    nom: str = Field(min_length=2, max_length=20)
    prenom: str = Field(min_length=3, max_length=50)
    date_naissance: date = Field(
        ge =date(1900, 1, 1), le=date.today()
    )
    lieu_naissance: str = Field(min_length=3, max_length=100)
    
    
    
    @model_validator(mode="after")
    def validation_age(self):
        age = date.today().year - self.date_naissance.year
        if age < 10:
            raise ValueError(
            "Veuillez vérifier l'age de l'auteur."
            )
        return self
