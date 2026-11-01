from app.database import SessionLocal
from app.models.auteur import Auteur
from app.models.adherent import Adherent
from app.models.emprunt import Emprunt
from app.models.ouvrage import Ouvrage
from datetime import date

def load_fixtures():
    db = SessionLocal()
    Auteurs = [
        Auteur(id_auteur=1,nom="LeCun", prenom="Yann", date_naissance=date(1980,1,1), lieu_naissance="Paris"),
        Auteur(id_auteur=2,nom="Bengio", prenom="Yoshua", date_naissance=date(1985,5,15), lieu_naissance="Lyon"),
        Auteur(id_auteur=3,nom="Julia", prenom="Luc", date_naissance=date(1988,12,5), lieu_naissance="Bordeaux"),
        Auteur(id_auteur=4,nom="Ponce", prenom="Jean", date_naissance=date(1992,9,25), lieu_naissance="Lille"),
        Auteur(id_auteur=5,nom="Bach", prenom="Francis", date_naissance=date(1983,4,18), lieu_naissance="Strasbourg"),
    ]
    
    
    Ouvrages = [
        Ouvrage(id_ouvrage=1,titre="Réseaux de neurones convolutifs", date_publication=date(2020,1,1), nombre_de_pages=200, editeur="Editeur A", genre ="Informatique", isbn="9780000000026", id_auteur=1),
        Ouvrage(id_ouvrage=2,titre="Deep learnig", date_publication=date(2021,2,15), nombre_de_pages=150, editeur="Editeur B",genre = "Informatique", isbn="9780000000033", id_auteur=2),
        Ouvrage(id_ouvrage=3,titre="Reconnaissance vocale", date_publication=date(2019,5,10), nombre_de_pages=300, editeur="Editeur C",genre="Informatique", isbn="9780000000040", id_auteur=3),
        Ouvrage(id_ouvrage=4,titre="Apprentissage automatique", date_publication=date(2022,8,20), nombre_de_pages=250, editeur="Editeur D",genre="Informatique", isbn="9780000000057", id_auteur=4),
        Ouvrage(id_ouvrage=5,titre="Optimisation", date_publication=date(2020,11,5), nombre_de_pages=180, editeur="Editeur E",genre="Mathématiques", isbn="9780000000064", id_auteur=5),
        Ouvrage(id_ouvrage=6,titre="Réseaux de neurones récurrents", date_publication=date(2021,3,12), nombre_de_pages=220, editeur="Editeur F",genre="Mathématiques", isbn="9780000000071", id_auteur=1),
        Ouvrage(id_ouvrage=7,titre="Apprentissage par renforcement", date_publication=date(2019,7,18), nombre_de_pages=280, editeur="Editeur G",genre="Informatique", isbn="9780000000088", id_auteur=2),
        Ouvrage(id_ouvrage=8,titre="Vision par ordinateur", date_publication=date(2022,10,25), nombre_de_pages=320, editeur="Editeur H",genre="Informatique", isbn="9780000000095", id_auteur=3),
        Ouvrage(id_ouvrage=9,titre="Traitement du langage naturel", date_publication=date(2020,6,30), nombre_de_pages=260, editeur="Editeur I",genre="Informatique", isbn="9780000000101", id_auteur=4),
        Ouvrage(id_ouvrage=10,titre="Apprentissage profond", date_publication=date(2021,9,15), nombre_de_pages=240, editeur="Editeur J", genre="Informatique", isbn="9780000000118", id_auteur=5)
    ]   
    
    Emprunts = [
        Emprunt(id_emprunt=1,date_debut=date(2023,1,1), date_retour_prevue=date(2023,1,15), date_retour_effective=date(2023,1,14), id_adherent=1, id_ouvrage=1),
        Emprunt(id_emprunt=2,date_debut=date(2023,2,10), date_retour_prevue=date(2023,2,24), date_retour_effective=date(2023,2,23), id_adherent=2, id_ouvrage=2),
        Emprunt(id_emprunt=3,date_debut=date(2023,3,5), date_retour_prevue=date(2023,3,19), date_retour_effective=date(2023,3,18), id_adherent=3, id_ouvrage=3),
        Emprunt(id_emprunt=4,date_debut=date(2023,4,15), date_retour_prevue=date(2023,4,29), date_retour_effective=date(2023,4,28), id_adherent=4, id_ouvrage=4),
        Emprunt(id_emprunt=5,date_debut=date(2023,5,20), date_retour_prevue=date(2023,6,3), date_retour_effective=date(2023,6,2), id_adherent=5, id_ouvrage=5),
        Emprunt(id_emprunt=6,date_debut=date(2023,6,10), date_retour_prevue=date(2023,6,24), date_retour_effective=date(2023,6,23), id_adherent=6, id_ouvrage=6),
        Emprunt(id_emprunt=7,date_debut=date(2023,7,5), date_retour_prevue=date(2023,7,19), date_retour_effective=date(2023,7,18), id_adherent=7, id_ouvrage=7),
        Emprunt(id_emprunt=8,date_debut=date(2023,8,15), date_retour_prevue=date(2023,8,29), date_retour_effective=date(2023,8,28), id_adherent=8, id_ouvrage=8),
        Emprunt(id_emprunt=9,date_debut=date(2023,9,20), date_retour_prevue=date(2023,10,4), date_retour_effective=date(2023,10,3), id_adherent=9, id_ouvrage=9),
    ]   
    
    Adherents = [
        Adherent(id_adherent=1,nom="Adherent A", prenom="Adam", adresse="Adresse A", date_inscription=date(2022,1,1), telephone="+330723456789", email="AA@gmail.com"),
        Adherent(id_adherent=2,nom="Adherent B", prenom="Babs", adresse="Adresse B", date_inscription=date(2022,2,15), telephone="0687654321", email="AB@gmail.com"),
        Adherent(id_adherent=3,nom="Adherent C", prenom="Carlos", adresse="Adresse C", date_inscription=date(2022,3,10), telephone="0723987654", email="AC@gmail.com"),
        Adherent(id_adherent=4,nom="Adherent D", prenom="David", adresse="Adresse D", date_inscription=date(2022,4,20), telephone="0687123456", email="AD@gmail.com"),
        Adherent(id_adherent=5,nom="Adherent E", prenom="Eva", adresse="Adresse E", date_inscription=date(2022,5,5), telephone="0723456780", email="AE@gmail.com"),
        Adherent(id_adherent=6,nom="Adherent F", prenom="Fanta", adresse="Adresse F", date_inscription=date(2022,6,12), telephone="0787654321", email="AF@gmail.com"),
        Adherent(id_adherent=7,nom="Adherent G", prenom="Georges", adresse="Adresse G", date_inscription=date(2022,7,18), telephone="0623987651", email="AG@gmail.com"),
        Adherent(id_adherent=8,nom="Adherent H", prenom="Hugo", adresse="Adresse H", date_inscription=date(2022,8,18), telephone="0723983654", email="AH@gmail.com"),
        Adherent(id_adherent=9,nom="Adherent I", prenom="Inas", adresse="Adresse I", date_inscription=date(2023,7,18), telephone="330723987604", email="AI@gmail.com"),
        Adherent(id_adherent=10,nom="Adherent J", prenom="Jack", adresse="Adresse J", date_inscription=date(2022,7,19), telephone="0624987650", email="AJ@gmail.com"),
    ]
    try:
        # on supprime les données existantes pour éviter de faire planter la base
        db.query(Emprunt).delete()
        db.query(Adherent).delete()
        db.query(Ouvrage).delete()
        db.query(Auteur).delete()
        # On insert le jeu de données dans la base
        db.add_all(Auteurs)
        db.add_all(Ouvrages)
        db.add_all(Adherents)
        db.add_all(Emprunts)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    load_fixtures()