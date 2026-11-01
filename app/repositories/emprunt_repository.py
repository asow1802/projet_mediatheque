from sqlalchemy import select
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.emprunt import Emprunt
from app.schemas.emprunt import EmpruntCreate, EmpruntUpdate
from app.models.__init__ import Ouvrage, Adherent

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
            id_adherent = data.id_adherent
            id_ouvrage = data.id_ouvrage
            adherent = self.db.get(Adherent, id_adherent)
            ouvrage = self.db.get(Ouvrage, id_ouvrage)
            all_emprunts = self.get_all()
            ## On vérifie si l'ouvrage est déjà emprunté et n'a pas encore été retourné
            for existing_emprunt in all_emprunts:
                if existing_emprunt.id_ouvrage == id_ouvrage and existing_emprunt.date_retour_effective is None:
                    raise ValueError(f"L'ouvrage avec l'identifiant {id_ouvrage} est déjà emprunté et n'a pas encore été retourné.")
            ## On vérifie si l'adhérent et l'ouvrage existent dans la base de données avant de créer l'emprunt
            if adherent is None:
                raise ValueError(f"L'adhérent avec l'identifiant {id_adherent} n'existe pas.")
            elif ouvrage is None:
                raise ValueError(f"L'ouvrage avec l'identifiant {id_ouvrage} n'existe pas.")
            self.db.add(emprunt)
            self.db.commit()
            self.db.refresh(emprunt)
            return emprunt
    ## On définit la méthode update pour mettre à jour un emprunt existant
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
    
    def get_by_adherent(self, id_adherent: int) -> list[Emprunt]:
        statement = select(Emprunt).where(Emprunt.id_adherent == id_adherent)
        return list(self.db.scalars(statement).all())