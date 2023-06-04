# Projet de base de donnée - Centre de jeux vidéo

## Ce projet utilise Python et MySQL

### Prérequis pour python:
- python version 3
- module Flask (pip install Flask)
- module MySQL-connector-python (pip install mysql-connector-python)

### Pour lancer le service:
- Accéder à votre serveur mysql local dans le fichier qui contient tout les scripts (dbsetup.sql, API.py, utilities.py etc)
- Créer une base de données vide (CREATE DATABASE exemple;)
- Sélectionner la base de données vide (USE exemple;)
- Exécuter dbsetup.sql (source ./dbsetup.sql;)
- Retourner dans le fichier qui contient tout les scripts
- Ouvriri utilites.py
- Modifier la valeur de 'database' du ligne 5 au nom du base de données que vous avez choisi (exemple si vous suivez l'instruction au-dessus)
- Modifier la valeur de 'port' du ligne 8 au port de mysql selon votre configuration
- Modifier la valeur de 'user' du ligne 9 au nom d'utilisateur selon votre configuration
- Modifier la valeur de 'password' du ligne 10 au mot de passe selon votre configuration
- Exécuter API.py (python3 API.py)
- Naviguer sur http://localhost:5000/ ou http://127.0.0.1:5000/


### md5sum des scripts pertinents:
- 77d2b171693857522cc01484e870da03  dbsetup.sql
- 4e7b00c6770df76306381163e3ee4f20  API.py
- adac5281d35a0160cc1c7be34e827dd0  utilities.py
