Ce projet utilise Python et MySQL

md5sum des scripts pertinents:
- 77d2b171693857522cc01484e870da03  dbsetup.sql
- 4e7b00c6770df76306381163e3ee4f20  API.py
- adac5281d35a0160cc1c7be34e827dd0  utilities.py


Prérequis pour python:
- python version 3
- module flask

Pour lancer:
- accéder à votre serveur mysql local dans le fichier qui contient tout les scripts (dbsetup.sql, API.py, etc)
- créer une base de données vide (CREATE DATABASE exemple;)
- sélectionner la base de données vide (USE exemple;)
- exécuter dbsetup.sql (source ./dbsetup.sql;)
- retourner dans le fichier qui contient tout les scripts
- modifier la valeur de 'database' du ligne 5 au nom du base de données que vous avez choisi (exemple si vous suivez l'instruction au-dessus)
- modifier la valeur de 'port' du ligne 8 au port de mysql selon votre configuration
- modifier la valeur de 'user' du ligne 9 au nom d'utilisateur selon votre configuration
- modifier la valeur de 'password' du ligne 10 au mot de passe selon votre configuration
- exécuter API.py (python3 API.py)
- naviguer sur http://localhost:5000/ ou http://127.0.0.1:5000/
