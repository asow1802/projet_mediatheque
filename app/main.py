from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.repositories import __init__ as repository

app = FastAPI()

## liste des auteurs
@get("/auteurs")
def read_auteurs():
    return repository.AuteurRepository.get_all()

## création d'un auteur
@post("/auteurs")
def create_auteur():
    return 0

## consulter un auteur
@get("auteurs/{id_auteur}")
def get_auteur(id_auteur : int):
    return repository.AuteurRepository.get_by_id(id_auteur)