from app.database import SessionLocal
from app.models import __init__ as models
def load_fixtures():
    db = SessionLocal()
    Auteurs = [
    models.Auteur(nom="LeCun", prenom="Yann", date_naissance="1980-01-01", lieu_naissance="Paris"),
    models.Auteur(nom="Bengio", prenom="Yoshua", date_naissance="1985-05-15", lieu_naissance="Lyon"),
    models.Auteur(nom="Julia", prenom="Luc", date_naissance="1988-12-05", lieu_naissance="Bordeaux"),
    models.Auteur(nom="Ponce", prenom="Jean", date_naissance="1992-09-25", lieu_naissance="Lille"),
    models.Auteur(nom="Bach", prenom="Francis", date_naissance="1983-04-18", lieu_naissance="Strasbourg"),
    ]
    
    
    Ouvrages = [
    models.Ouvrage(titre="Réseaux de neurones convolutifs", date_publication="2020-01-01", nombre_de_pages=200, editeur="Editeur A", isbn="978-1234567890", id_auteur=1),
    models.Ouvrage(titre="Deep learnig", date_publication="2021-02-15", nombre_de_pages=150, editeur="Editeur B", isbn="978-0987654321", id_auteur=2),
    models.Ouvrage(titre="Reconnaissance vocale", date_publication="2019-05-10", nombre_de_pages=300, editeur="Editeur C", isbn="978-1122334455", id_auteur=3),
    models.Ouvrage(titre="Apprentissage automatique", date_publication="2022-08-20", nombre_de_pages=250, editeur="Editeur D", isbn="978-5566778899", id_auteur=4),
    models.Ouvrage(titre="Optimisation", date_publication="2020-11-05", nombre_de_pages=180, editeur="Editeur E", isbn="978-6677889900", id_auteur=5),
    models.Ouvrage(titre="Réseaux de neurones récurrents", date_publication="2021-03-12", nombre_de_pages=220, editeur="Editeur F", isbn="978-3344556677", id_auteur=1),
    models.Ouvrage(titre="Apprentissage par renforcement", date_publication="2019-07-18", nombre_de_pages=280, editeur="Editeur G", isbn="978-7788990011", id_auteur=2),
    models.Ouvrage(titre="Vision par ordinateur", date_publication="2022-10-25", nombre_de_pages=320, editeur="Editeur H", isbn="978-4455667788", id_auteur=3),
    models.Ouvrage(titre="Traitement du langage naturel", date_publication="2020-06-30", nombre_de_pages=260, editeur="Editeur I", isbn="978-8899001122", id_auteur=4),
    models.Ouvrage(titre="Apprentissage profond", date_publication="2021-09-15", nombre_de_pages=240, editeur="Editeur J", isbn="978-2233445566", id_auteur=5)
    ]   
    
    Emprunts = [
    models.Emprunt(date_debut="2023-01-01", date_retour_prevue="2023-01-15", date_retour_effective="2023-01-14", id_adherent=1, id_ouvrage=1),
    models.Emprunt(date_debut="2023-02-10", date_retour_prevue="2023-02-24", date_retour_effective="2023-02-23", id_adherent=2, id_ouvrage=2),
    models.Emprunt(date_debut="2023-03-05", date_retour_prevue="2023-03-19", date_retour_effective="2023-03-18", id_adherent=3, id_ouvrage=3),
    models.Emprunt(date_debut="2023-04-15", date_retour_prevue="2023-04-29", date_retour_effective="2023-04-28", id_adherent=4, id_ouvrage=4),
    models.Emprunt(date_debut="2023-05-20", date_retour_prevue="2023-06-03", date_retour_effective="2023-06-02", id_adherent=5, id_ouvrage=5),
    models.Emprunt(date_debut="2023-06-10", date_retour_prevue="2023-06-24", date_retour_effective="2023-06-23", id_adherent=6, id_ouvrage=6),
    models.Emprunt(date_debut="2023-07-05", date_retour_prevue="2023-07-19", date_retour_effective="2023-07-18", id_adherent=7, id_ouvrage=7),
    models.Emprunt(date_debut="2023-08-15", date_retour_prevue="2023-08-29", date_retour_effective="2023-08-28", id_adherent=8, id_ouvrage=8),
    models.Emprunt(date_debut="2023-09-20", date_retour_prevue="2023-10-04", date_retour_effective="2023-10-03", id_adherent=9, id_ouvrage=9),
    models.Emprunt(date_debut="2023-10-10", date_retour_prevue="2023-10-24", date_retour_effective="2023-10-23", id_adherent=10,id_ouvrage=10),
    models.Emprunt(date_debut="2023-11-05", date_retour_prevue="2023-11-19", date_retour_effective="2023-11-18", id_adherent=1, id_ouvrage=2),
    models.Emprunt(date_debut="2023-12-15", date_retour_prevue="2023-12-29", date_retour_effective="2023-12-28", id_adherent=2, id_ouvrage=3),
    models.Emprunt(date_debut="2024-01-20", date_retour_prevue="2024-02-03", date_retour_effective="2024-02-02", id_adherent=3, id_ouvrage=4)
    ]   
    
    Adherents = [
    models.Adherent(nom="Adherent A", prenom="A", adresse="Adresse A", date_inscription="2022-01-01", telephone="0123456789", email="AA@gmail.com"),
    models.Adherent(nom="Adherent B", prenom="B", adresse="Adresse B", date_inscription="2022-02-15", telephone="0987654321", email="AB@gmail.com"),
    models.Adherent(nom="Adherent C", prenom="C", adresse="Adresse C", date_inscription="2022-03-10", telephone="0123987654", email="AC@gmail.com"),
    models.Adherent(nom="Adherent D", prenom="D", adresse="Adresse D", date_inscription="2022-04-20", telephone="0987123456", email="AD@gmail.com"),
    models.Adherent(nom="Adherent E", prenom="E", adresse="Adresse E", date_inscription="2022-05-05", telephone="0123456789", email="AE@gmail.com"),
    models.Adherent(nom="Adherent F", prenom="F", adresse="Adresse F", date_inscription="2022-06-12", telephone="0987654321", email="AF@gmail.com"),
    models.Adherent(nom="Adherent G", prenom="G", adresse="Adresse G", date_inscription="2022-07-18", telephone="0123987654", email="AG@gmail.com"),
    ]
    
    db.add_all(Auteurs)
    db.add_all(Ouvrages)
    db.add_all(Adherents)
    db.add_all(Emprunts)
    db.commit()
    db.close()