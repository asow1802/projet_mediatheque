from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import EmpruntRepository, AdherentRepository, OuvrageRepository
from app.schemas.__init__ import EmpruntCreate
from app.database import get_db
router = APIRouter()

## Créer un emprunt
@router.post("/emprunts", status_code=201)
def create_emprunt(emp : EmpruntCreate, db : Session = Depends(get_db)):
    adh_repo = AdherentRepository(db)
    ouv_repo = OuvrageRepository(db)
    adherent = adh_repo.get_by_id(emp.id_adherent)
    ouvrage = ouv_repo.get_by_id(emp.id_ouvrage)
    if adherent is None:
        raise HTTPException(status_code=404, detail="Adhérent introuvable, veuillez renseigner un identifiant valide")
    if ouvrage is None:
        raise HTTPException(status_code=404, detail="Ouvrage introuvable, veuillez renseigner un identifiant valide")
    
    emprunts_en_cours = EmpruntRepository(db).get_by_ouvrage(emp.id_ouvrage)
    for emprunt in emprunts_en_cours:
        if emprunt.date_retour_effective is None:
            raise HTTPException(status_code=409, detail="L'ouvrage est actuellement emprunté et indisponible.")
    
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