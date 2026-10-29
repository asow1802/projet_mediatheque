from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from app.repositories import __init__ as repository
from app.schemas.auteur import AuteurCreate
app = FastAPI()

## liste des auteurs
@app.get("/auteurs")
def read_auteurs():
    return repository.AuteurRepository.get_all()

## création d'un auteur
@app.post("/auteurs")
def create_auteur(aut : AuteurCreate):
    return repository.AuteurRepository.create(aut)

## consulter un auteur
@app.get("/auteurs/{id_auteur}")
def get_auteur(id_auteur : int):
    return repository.AuteurRepository.get_by_id(id_auteur)