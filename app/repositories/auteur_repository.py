from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.auteur import Auteur
from app.schemas.auteur import AuteurCreate, AuteurUpdate

class AuteurRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, id_auteur: int) -> Auteur | None:
        return self.db.get(Auteur, id_auteur)

    def get_all(self) -> list[Auteur]:
        statement = select(Auteur).order_by(Auteur.id_auteur)
        return list(self.db.scalars(statement).all())

    def create(
        self,
        data: AuteurCreate
        ) -> Auteur:
        auteur = Auteur(
            nom=data.nom,
            prenom=data.prenom,
            date_naissance=data.date_naissance,
            lieu_naissance=data.lieu_naissance
        )
        self.db.add(auteur)
        self.db.commit()
        self.db.refresh(auteur)
        return auteur
    ## On doit vérifier les champs qui sont mis à jour pour ne pas écraser les valeurs existantes avec des None
    def update(
        self,
        id_auteur: int,
        data: AuteurUpdate
        ) -> Auteur | None:
        auteur = self.get_by_id(id_auteur)
        if auteur is None:
            return None
        if data.nom is not None:
            auteur.nom = data.nom
        if data.prenom is not None:
            auteur.prenom = data.prenom
        if data.date_naissance is not None:
            auteur.date_naissance = data.date_naissance
        if data.lieu_naissance is not None:
            auteur.lieu_naissance = data.lieu_naissance
        self.db.commit()
        self.db.refresh(auteur)
        return auteur
        
    def delete(self, id_auteur: int) -> bool:
        auteur = self.get_by_id(id_auteur)
        if auteur is None:
            return False
        self.db.delete(auteur)
        self.db.commit()
        return True