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
    ## On définit la méthode create pour créer un nouvel emprunt
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
    ## On doit vérifier les champs qui sont mis à jour pour ne pas écraser les valeurs existantes avec des None
    def update(
        self,
        id_emprunt: int,
        data: EmpruntUpdate
        ) -> Emprunt | None:
        emprunt = self.get_by_id(id_emprunt)
        if emprunt is None:
            return None
        if data.date_debut is not None:
            emprunt.date_debut = data.date_debut
        if data.date_retour_prevue is not None:
            emprunt.date_retour_prevue = data.date_retour_prevue
        if data.date_retour_effective is not None:
            emprunt.date_retour_effective = data.date_retour_effective
        if data.id_adherent is not None:
            emprunt.id_adherent = data.id_adherent
        if data.id_ouvrage is not None:
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
    ### On définit la méthode get_by_adherent pour récupérer les emprunts d'un adhérent
    def get_by_adherent(self, id_adherent: int) -> list[Emprunt]:
        statement = select(Emprunt).where(Emprunt.id_adherent == id_adherent).order_by(Emprunt.id_emprunt)
        return list(self.db.scalars(statement).all())
    
    ### On définit la méthode get_by_ouvrage pour récupérer les emprunts d'un ouvrage
    def get_by_ouvrage(self, id_ouvrage: int) -> list[Emprunt]:
        statement = select(Emprunt).where(Emprunt.id_ouvrage == id_ouvrage).order_by(Emprunt.id_emprunt)
        return list(self.db.scalars(statement).all())