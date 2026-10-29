Ce fichier .md liste les différentes  étapes de la réalisation du projet

# Le projet est décomposé sous une arborescence de dossier dont chacun joue un role spécifique pour la réalisation du projet.

* **/app/models** : Ce dossier constitue la base de la modélisation de l'application avec sqlalchemy. Il contient l'ensemble des fichiers nécessaires pour la définition des entités issues du modèle logique des données(MLD).
* **/app/repositories :** contient les fichiers permettant de réaliser les opérations sur les entités( créer, supprimer, mis à jour, supprimer ...)
* **/app/fixtures.py** contient le programme nécessaire pour initialiser la base de données comme décrit dans le sujet.
* **/app/schemas** dossier contenant les fichiers de validation avec pydantic. Chaque création et mise à jour de nouvelles données devra respecter des contraintes de validités.

# Les Paquets

Environnement python pour installer les librairies nécessaires et spécifiques au projet :

* *python3 -m venv .projet_mediatheque*
* *source .projet_mediatheque/bin/activate*

Installation des paquets, puis remplissage de requirements.txt

* *pip install fastapi uvicorn alembic pydantic*
* *pip freeze > requirements.txt*
* *alembic init alembic*
