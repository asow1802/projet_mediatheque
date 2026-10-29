from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.ouvrage import Ouvrage
from app.schemas import OuvrageCreate, OuvrageUpdate

class OuvrageRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, id_ouvrage: int) -> Ouvrage | None:
        return self.db.get(Ouvrage, id_ouvrage)

    def get_all(self) -> list[Ouvrage]:
        statement = select(Ouvrage).order_by(Ouvrage.id_ouvrage)
        return list(self.db.scalars(statement).all())

    def create(
        self,
        data : OuvrageCreate
        ) -> Ouvrage:
        ouvrage = Ouvrage(
            isbn=data.isbn,
            date_publication=data.date_publication,
            titre=data.titre,
            nombre_de_page=data.nombre_de_page,
            id_ouvrage=data.id_ouvrage,
            editeur=data.editeur,
            id_auteur=data.id_auteur
        )
        self.db.add(ouvrage)
        self.db.commit()
        self.db.refresh(ouvrage)
        return ouvrage
    
    def update(
        self,
        id_ouvrage: int,
        data: OuvrageUpdate
        ) -> Ouvrage | None:
        ouvrage = self.get_by_id(id_ouvrage)
        if ouvrage is None:
            return None
        ouvrage.isbn = data.isbn
        ouvrage.date_publication = data.date_publication
        ouvrage.titre = data.titre
        ouvrage.nombre_de_page = data.nombre_de_page
        ouvrage.editeur = data.editeur
        ouvrage.id_auteur = data.id_auteur
        self.db.commit()
        self.db.refresh(ouvrage)
        return ouvrage  
        
    def delete(self, id_ouvrage: int) -> bool:
        ouvrage = self.get_by_id(id_ouvrage)
        if ouvrage is None:
            return False
        self.db.delete(ouvrage)
        self.db.commit()
        return True