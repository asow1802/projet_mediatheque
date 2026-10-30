from datetime import date
from sqlalchemy import String, Integer, Date
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.emprunt import Emprunt
from app.schemas.emprunt import EmpruntCreate, EmpruntUpdate

class EmpruntRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, id_emprunt: int) -> Emprunt | None:
        return self.db.get(Emprunt, id_emprunt)

    def get_all(self) -> list[Emprunt]:
        statement = select(Emprunt).order_by(Emprunt.id_emprunt)
        return list(self.db.scalars(statement).all())

    def create(
            self,
            data: EmpruntCreate
            ) -> Emprunt:
            emprunt = Emprunt(
                date_debut=data.date_debut,
                date_retour_prevue=data.date_retour_prevue,
                id_adherent=data.id_adherent,
                id_ouvrage=data.id_ouvrage
            )
            self.db.add(emprunt)
            self.db.commit()
            self.db.refresh(emprunt)
            return emprunt

    def update(
        self,
        id_emprunt: int,
        data: EmpruntUpdate
        ) -> Emprunt | None:
        emprunt = self.get_by_id(id_emprunt)
        if emprunt is None:
            return None
        emprunt.date_debut = data.date_debut
        emprunt.date_retour_prevue = data.date_retour_prevue
        emprunt.date_retour_effective = data.date_retour_effective
        emprunt.id_adherent = data.id_adherent
        emprunt.id_ouvrage = data.id_ouvrage
        self.db.commit()
        self.db.refresh(emprunt)
        return emprunt
        
    def delete(self, id_emprunt: int) -> bool:
        emprunt = self.get_by_id(id_emprunt)
        if emprunt is None:
            return False
        self.db.delete(emprunt)
        self.db.commit()
        return True