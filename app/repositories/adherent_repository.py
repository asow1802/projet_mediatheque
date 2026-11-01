from sqlalchemy import select
from datetime import date
from sqlalchemy.orm import Session
from app.models.adherent import Adherent
from app.schemas.adherent import AdherentCreate, AdherentUpdate

class AdherentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, id_adherent: int) -> Adherent | None:
        return self.db.get(Adherent, id_adherent)

    def get_all(self) -> list[Adherent]:
        statement = select(Adherent).order_by(Adherent.id_adherent)
        return list(self.db.scalars(statement).all())

    def create(
        self,
        data: AdherentCreate
        ) -> Adherent:
        adherent = Adherent(
            nom=data.nom,
            prenom=data.prenom,
            adresse=data.adresse,
            date_inscription=data.date_inscription,
            telephone=data.telephone,
            email=data.email
        )
        self.db.add(adherent)
        self.db.commit()
        self.db.refresh(adherent)
        return adherent
    ## On doit vérifier les champs qui sont mis à jour pour ne pas écraser les valeurs existantes avec des None
    def update(
        self,
        id_adherent: int,
        data: AdherentUpdate
        ) -> Adherent | None:
        adherent = self.get_by_id(id_adherent)
        if adherent is None:
            return None
        if data.nom is not None:
            adherent.nom = data.nom
        if data.prenom is not None:
            adherent.prenom = data.prenom
        if data.adresse is not None:
            adherent.adresse = data.adresse
        if data.date_inscription is not None:
            adherent.date_inscription = data.date_inscription
        if data.telephone is not None:
            adherent.telephone = data.telephone
        if data.email is not None:
            adherent.email = data.email
        self.db.commit()
        self.db.refresh(adherent)
        return adherent
    
    def delete(self, id_adherent: int) -> bool:
        adherent = self.get_by_id(id_adherent)
        if adherent is None:
            return False
        self.db.delete(adherent)
        self.db.commit()
        return True
    ### On définit la méthode get_by_email pour récupérer un adhérent par son email
    def get_by_email(self, email: str) -> Adherent | None:
        statement = select(Adherent).where(Adherent.email == email)
        return self.db.scalars(statement).first()