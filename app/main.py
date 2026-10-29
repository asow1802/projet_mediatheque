from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from app.repositories.__init__ import AuteurRepository, AdherentRepository, OuvrageRepository, EmpruntRepository
from app.schemas.auteur import AuteurCreate
app = FastAPI()

## liste des auteurs
@app.get("/auteurs")
def read_auteurs():
    return AuteurRepository.get_all()

## création d'un auteur
@app.post("/auteurs")
def create_auteur(aut : AuteurCreate):
    return AuteurRepository.create(aut)

## consulter un auteur
@app.get("/auteurs/{id_auteur}")
def get_auteur(id_auteur : int):
    return AuteurRepository.get_by_id(id_auteur)