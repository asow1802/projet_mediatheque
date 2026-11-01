from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import AuteurRepository
from app.schemas.__init__ import AuteurCreate
from app.database import get_db
router = APIRouter()

## liste des auteurs
@router.get("/auteurs")
def read_auteurs(db : Session = Depends(get_db)):
    repos = AuteurRepository(db)
    return repos.get_all()

## création d'un auteur
@router.post("/auteurs", status_code=201)
def create_auteur(aut : AuteurCreate, db : Session = Depends(get_db)):
    new_aut = AuteurRepository(db)
    return new_aut.create(aut)

# ## consulter un auteur
@router.get("/auteurs/{id_auteur}")
def get_auteur(id_auteur : int, db : Session = Depends(get_db)):
    aut_repo = AuteurRepository(db)
    aut = aut_repo.get_by_id(id_auteur)
    if aut is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable, veuillez renseigner un identifiant valide")
    else:
        return aut






