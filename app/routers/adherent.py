from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import AdherentRepository
from app.schemas.__init__ import AdherentCreate
from app.database import get_db
router = APIRouter()

## Créer un adherent
@router.post("/adherents", status_code=201)
def create_adherent(adh : AdherentCreate, db : Session = Depends(get_db)):
    new_adh = AdherentRepository(db)
    return new_adh.create(adh)

## Lister les adherents
@router.get("/adherents")
def read_adherents(db : Session = Depends(get_db)): 
    repos = AdherentRepository(db)
    return repos.get_all()