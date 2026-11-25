from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.ouvrage import Ouvrage
from app.schemas.ouvrage import OuvrageCreate, OuvrageUpdate

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
            nombre_de_pages=data.nombre_de_pages,
            editeur=data.editeur,
            genre=data.genre,
            id_auteur=data.id_auteur
        )
        self.db.add(ouvrage)
        self.db.commit()
        self.db.refresh(ouvrage)
        return ouvrage
    ## On doit vérifier les champs qui sont mis à jour pour ne pas écraser les valeurs existantes avec des None
    def update(
        self,
        id_ouvrage: int,
        data: OuvrageUpdate
        ) -> Ouvrage | None:
        ouvrage = self.get_by_id(id_ouvrage)
        if ouvrage is None:
            return None
        if data.isbn is not None:
            ouvrage.isbn = data.isbn
        if data.date_publication is not None:
            ouvrage.date_publication = data.date_publication
        if data.titre is not None:
            ouvrage.titre = data.titre
        if data.nombre_de_pages is not None:
            ouvrage.nombre_de_pages = data.nombre_de_pages
        if data.editeur is not None:
            ouvrage.editeur = data.editeur
        if data.genre is not None:
            ouvrage.genre = data.genre
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
    ## On définit la méthode get_by_auteur pour récupérer les ouvrages d'un auteur
    def get_by_auteur(self, id_auteur: int) -> list[Ouvrage]:
        statement = select(Ouvrage).where(Ouvrage.id_auteur == id_auteur).order_by(Ouvrage.id_ouvrage)
        return list(self.db.scalars(statement).all())
    ### On définit la méthode get_by_isbn pour récupérer un ouvrage par son ISBN
    def get_by_isbn(self, isbn: str) -> Ouvrage | None:
        statement = select(Ouvrage).where(Ouvrage.isbn == isbn)
        return self.db.scalars(statement).first()