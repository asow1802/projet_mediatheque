from app.routers import adherent, auteur, ouvrage, emprunt
from fastapi import FastAPI

app = FastAPI()
app.include_router(adherent.router)
app.include_router(auteur.router)
app.include_router(ouvrage.router)
app.include_router(emprunt.router)