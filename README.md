# Projet :

API REST de gestion des auteurs, ouvrages, adhérents et emprunts d'une médiathèque.

Elle repose sur FastAPI, SQLAlchemy, Alembic, Pydantic et SQLite.

# Prérequis

Afin de pouvour exécuter le projet important de disposer :

* python 3.12
* pip

Un dépot git est aussi disponible pour retrouver le projet en ligne. ``git clone https://github.com/asow1802/projet_mediatheque.git  ``

---

# Installations

On commence d'abord par mettre en place un environnement python dédié au packages du projet.

```bash
python3 -m venv .projet_mediatheque
source .projet_mediatheque/bin/activate
pip install -r requirements.txt
```

# Configuration de la base de données

Le projet utilise SQLite : aucun serveur n'est à installer, tout est en local.

L'adresse de la base est définie par `DATABASE_URL` dans `app/database.py`.

Le fichier `mediatheque.db` est créé à la racine du projet lors de la première migration.

---

# Migrations

Alembic versionne la structure de la base. Le contenu est géré séparément par les fixtures.

Pour créer la base ou la mettre à jour : ``python -m alembic upgrade head``

# Migration 1 : création des tables

Fichier : `alembic/versions/a258a68d6289_creation_des_tables.py`

Elle crée les tables `auteurs`, `ouvrages`, `adherents` et `emprunts`, avec leurs clés primaires, leurs clés étrangères et l'unicité de l'ISBN et de l'email.

Elle a été générée avec `--autogenerate` à partir des modèles SQLAlchemy, puis relue.

---

# Migration 2 : ajout du genre des ouvrages

Fichier : `alembic/versions/ed3d12536601_ajout_du_genre_des_ouvrages.py`

La médiathèque souhaite classer ses ouvrages par genre. Cette migration ajoute une colonne `genre` facultative à la table `ouvrages`.

Elle est facultative car les ouvrages déjà enregistrés n'ont pas de genre.

La migration a été appliquée à une base existante et remplie, sans la supprimer ni la recréer : les 10 ouvrages et les 9 emprunts ont été conservés.

---

# Quelques commandes utiles

Vérifier qu'il n'y a aucun écart entre les modèles et le schéma de la base :
`python -m alembic check`

Afficher la version actuelle de la base :

`python -m alembic current`

Annuler la dernière migration :
`python -m alembic downgrade -1`

---

# Fixtures

À lancer après les migrations :
`python -m app.fixtures`

Le jeu de données contient 5 auteurs, 10 ouvrages, 10 adhérents et plusieurs emprunts : emprunts terminés, en cours et en retard, auteur sans ouvrage, ouvrage sans genre.

Ici il est impotant de noter que cette commande remplace les données déjà présentes dans la base.

# Lancement de l'API

`uvicorn app.main:app --reload`

une fois lien géréré, on peut ajouter /docs pour avoir une interface beaucoup agréable à manier avec tous les endpoints visibles.

- API : http://127.0.0.1:8000
- Documentation interactive : http://127.0.0.1:8000/docs

# Endpoints

* Lister les auteurs

GET `/auteurs`

* Créer un auteur

POST `/auteurs`

* Consulter un auteur

GET `/auteurs/{id}`

* Lister les ouvrages d'un auteur

GET `/auteurs/{id}/ouvrages`

* Lister les ouvrages

GET `/ouvrages`

* Créer un ouvrage

POST `/ouvrages`

* Consulter un ouvrage

GET `/ouvrages/{id}`

* Supprimer un ouvrage

DELETE `/ouvrages/{id}`

* Lister les adhérents

GET `/adherents`

* Créer un adhérent

POST `/adherents`

* Lister les emprunts d'un adhérent

GET `/adherents/{id}/emprunts`

* Créer un emprunt

POST `/emprunts`

# Architecture du projet

* `app/models` : modèles SQLAlchemy, issus du MLD.
* `app/repositories` : accès aux données (requêtes, création, mise à jour, suppression).
* `app/schemas` : validation des données reçues avec Pydantic.
* `app/main.py` : création de l'application et inclusion des routers.
* `app/fixtures.py` : chargement du jeu de données.
* `alembic/` : configuration et fichiers de migration.
* `app/routers` : vérifient ce qui nécessite la base : existence des ressources et disponibilité d'un ouvrage.

# Règles de gestion

- Un emprunt est en cours tant que `date_retour_effective` est vide : la date effective n'est pas incluse à la création d'un emprunt.
- Un ouvrage ne peut avoir qu'un seul emprunt en cours.
- Un ouvrage qui a des emprunts ne peut pas être supprimé, afin de conserver l'historique.

**Genre** : lors de notre deuxième migration, nous avons considéré le genre comme un attribut facultatif.

**ISBN** : validé avec `pydantic_extra_types`, à saisir sans tirets ni espaces.

**Téléphone** : validé comme numéro français et enregistré au format international à l'aide de la classe PhoneNumber avec les paramètres bien précisés.

**EnpruntUpdate** : tous les champs sont modifiables : cela permettra à l'administrateur de pouvoir corriger une erreur de saisie.

---

# Wébographie

* https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_phone_numbers/
* https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_isbn/#_top
* https://fastapi.tiangolo.com/reference/exceptions/?h=http+e#fastapi.HTTPException
