from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import AuteurRepository, OuvrageRepository, EmpruntRepository
from app.schemas.__init__ import OuvrageCreate
from app.database import get_db
router = APIRouter()


## Lister les ouvrages
@router.get("/ouvrages")
def read_ouvrages(db : Session = Depends(get_db)):
    repos = OuvrageRepository(db)
    return repos.get_all()

## Créer un ouvrage
@router.post("/ouvrages", status_code=201)
def create_ouvrage(ouv : OuvrageCreate, db : Session = Depends(get_db)):
    aut_repo = AuteurRepository(db)
    auteur = aut_repo.get_by_id(ouv.id_auteur)
    if auteur is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable, veuillez renseigner un identifiant valide")
    new_ouv = OuvrageRepository(db)
    
    existing_ouvrage = new_ouv.get_by_isbn(ouv.isbn)
    if existing_ouvrage:
        raise HTTPException(status_code=409, detail="Un ouvrage avec ce numéro ISBN existe déjà.")  
    return new_ouv.create(ouv)

## Consulter un ouvrage
@router.get("/ouvrages/{id_ouvrage}")
def get_ouvrage(id_ouvrage : int, db : Session = Depends(get_db)):
    ouv_repo = OuvrageRepository(db)
    ouv = ouv_repo.get_by_id(id_ouvrage)
    if ouv is None:
        raise HTTPException(status_code=404, detail="Ouvrage introuvable, veuillez renseigner un identifiant valide")
    else:
        return ouv

## Supprimer un ouvrage
@router.delete("/ouvrages/{id_ouvrage}", status_code=204)
def delete_ouvrage(id_ouvrage : int, db : Session = Depends(get_db)):
    ouv_repo = OuvrageRepository(db)
    ouv = ouv_repo.get_by_id(id_ouvrage)
    emprunt_repo = EmpruntRepository(db)
    
    if ouv is None:
        raise HTTPException(status_code=404, detail="Ouvrage introuvable, veuillez renseigner un identifiant valide")
    else:
        emprunts_en_cours = emprunt_repo.get_by_ouvrage(id_ouvrage)
        if emprunts_en_cours:
            raise HTTPException(status_code=409, detail="Cet ouvrage a des enprunts et ne peut pas être supprimé.")
        ouv_repo.delete(id_ouvrage)

## Rechercher les ouvrages d'un auteur
@router.get("/auteurs/{id_auteur}/ouvrages")
def get_ouvrages_by_auteur(id_auteur : int, db : Session = Depends(get_db)):
    aut_repo = AuteurRepository(db)
    aut = aut_repo.get_by_id(id_auteur)
    if aut is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable, veuillez renseigner un identifiant valide")
    else:
        ouv_repo = OuvrageRepository(db)
        ouvrages = ouv_repo.get_by_auteur(id_auteur)
        return ouvrages

