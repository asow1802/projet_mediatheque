from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import EmpruntRepository, AdherentRepository
from app.schemas.__init__ import EmpruntCreate
from app.database import get_db
router = APIRouter()

## Créer un emprunt
@router.post("/emprunts", status_code=201)
def create_emprunt(emp : EmpruntCreate, db : Session = Depends(get_db)):
    new_emp = EmpruntRepository(db)
    return new_emp.create(emp)  

## Consulter les emprunts d'un adherent
@router.get("/adherents/{id_adherent}/emprunts")
def get_emprunts_by_adherent(id_adherent : int, db : Session = Depends(get_db)):
    adh_repo = AdherentRepository(db)
    adh = adh_repo.get_by_id(id_adherent)
    if adh is None:
        raise HTTPException(status_code=404, detail="Adhérent introuvable, veuillez renseigner un identifiant valide")
    else:
        emp_repo = EmpruntRepository(db)
        emprunts = emp_repo.get_by_adherent(id_adherent)
        return emprunts