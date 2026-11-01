from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from app.repositories.__init__ import AuteurRepository, AdherentRepository, OuvrageRepository, EmpruntRepository
from app.schemas.__init__ import AuteurCreate, AdherentCreate, OuvrageCreate, EmpruntCreate
from app.database import get_db
app = FastAPI()

## liste des auteurs
@app.get("/auteurs")
def read_auteurs(db : Session = Depends(get_db)):
    repos = AuteurRepository(db)
    return repos.get_all()

## création d'un auteur
@app.post("/auteurs", status_code=201)
def create_auteur(aut : AuteurCreate, db : Session = Depends(get_db)):
    new_aut = AuteurRepository(db)
    return new_aut.create(aut)

# ## consulter un auteur
@app.get("/auteurs/{id_auteur}")
def get_auteur(id_auteur : int, db : Session = Depends(get_db)):
    aut_repo = AuteurRepository(db)
    aut = aut_repo.get_by_id(id_auteur)
    if aut is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable, veuillez renseigner un identifiant valide")
    else:
        return aut
## Lister les ouvrages
@app.get("/ouvrages")
def read_ouvrages(db : Session = Depends(get_db)):
    repos = OuvrageRepository(db)
    return repos.get_all()

## Créer un ouvrage
@app.post("/ouvrages", status_code=201)
def create_ouvrage(ouv : OuvrageCreate, db : Session = Depends(get_db)):
    new_ouv = OuvrageRepository(db)
    return new_ouv.create(ouv)

## Consulter un ouvrage
@app.get("/ouvrages/{id_ouvrage}")
def get_ouvrage(id_ouvrage : int, db : Session = Depends(get_db)):
    ouv_repo = OuvrageRepository(db)
    ouv = ouv_repo.get_by_id(id_ouvrage)
    if ouv is None:
        raise HTTPException(status_code=404, detail="Ouvrage introuvable, veuillez renseigner un identifiant valide")
    else:
        return ouv

## Supprimer un ouvrage
@app.delete("/ouvrages/{id_ouvrage}", status_code=204)
def delete_ouvrage(id_ouvrage : int, db : Session = Depends(get_db)):
    ouv_repo = OuvrageRepository(db)
    ouv = ouv_repo.get_by_id(id_ouvrage)
    if ouv is None:
        raise HTTPException(status_code=404, detail="Ouvrage introuvable, veuillez renseigner un identifiant valide")
    else:
        ouv_repo.delete(id_ouvrage)
        return {"message": "Ouvrage supprimé avec succès."}

## Rechercher les ouvrages d'un auteur
@app.get("/auteurs/{id_auteur}/ouvrages")
def get_ouvrages_by_auteur(id_auteur : int, db : Session = Depends(get_db)):
    aut_repo = AuteurRepository(db)
    aut = aut_repo.get_by_id(id_auteur)
    if aut is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable, veuillez renseigner un identifiant valide")
    else:
        ouv_repo = OuvrageRepository(db)
        ouvrages = ouv_repo.get_by_auteur(id_auteur)
        return ouvrages

## Créer un adherent
@app.post("/adherents", status_code=201)
def create_adherent(adh : AdherentCreate, db : Session = Depends(get_db)):
    new_adh = AdherentRepository(db)
    return new_adh.create(adh)

## Lister les adherents
@app.get("/adherents")
def read_adherents(db : Session = Depends(get_db)): 
    repos = AdherentRepository(db)
    return repos.get_all()

## Créer un emprunt
@app.post("/emprunts", status_code=201)
def create_emprunt(emp : EmpruntCreate, db : Session = Depends(get_db)):
    new_emp = EmpruntRepository(db)
    return new_emp.create(emp)  

## Consulter les emprunts d'un adherent
@app.get("/adherents/{id_adherent}/emprunts")
def get_emprunts_by_adherent(id_adherent : int, db : Session = Depends(get_db)):
    adh_repo = AdherentRepository(db)
    adh = adh_repo.get_by_id(id_adherent)
    if adh is None:
        raise HTTPException(status_code=404, detail="Adhérent introuvable, veuillez renseigner un identifiant valide")
    else:
        emp_repo = EmpruntRepository(db)
        emprunts = emp_repo.get_by_adherent(id_adherent)
        return emprunts