
# Projet 4 - Développer un programme logiciel en python 
Logiciel MVC en python pour gestion de tournois d'échecs. 


## Créer un environnement virtuel 

*  Installer la version de Python indiquée sur le repo du projet     
<!-- *  Copier le dossier téléchargé et extrait   -->
*  Depuis le dossier du projet, créer un environnement virtuel : `python -m venv <nom_env_virtuel>`     
*  Activer l'environnement virtuel :      
Linux --> `source bin/activate`        
Windows --> `source <nom_env_virtuel>/Scripts/activate` (ne pas taper "python" au début de la commande)     
     
L'invite de commande commence maintenant par 
`(<nom_env_virtuel>)`, ce qui signifie qu'on se trouve bien dans l'environnement virtuel. 
A noter que dans l'arborescence de l'IDE, les dossiers et fichiers de travail apparaissent au même niveau que le dossier `<nom_env_virtuel>`. 

zebboudjalexandre@gmail.com


## Fichiers des données 
*  Créer un dossier `data` 
*  A l'intérieur créer 2 fichiers json : 
    - `players.json` 
    - `tournaments.json` 
*  Dans chacun des fichiers, ajouter une liste vide : `[]`, qui recevra les données enregistrées. 


## Installer les dépendances 
Taper la commande :     
`pip install -r requirements.txt` 


## Arborescence du projet 

<racine du projet>/ 
    |-- controllers/
        |-- main_controller.py 
        |-- register_controller.py 
        |-- report_controller.py 
    |-- data/ 
        |-- players.json 
        |-- tournaments.json 
    |-- flake-reports/ 
        |-- ***  
    |-- models/ 
        |-- abstract_model.py 
        |-- match_model.py 
        |-- player_model.py 
        |-- round_model.py 
        |-- tournament_model.py 
    |-- utils/ 
        |-- helpers.py 
    |-- views/ 
        |-- dashboard_view.py 
        |-- input_view.py 
        |-- report_view.py 
    |-- .gitignore 
    |-- project.py          <-- entrée du programme 
    |-- README.md 
    |-- requirements.txt 
    |-- setup.cfg  <!-- config flake8 --> 


## Fonctionnalités / Menus 

**Enregistrer** 
* Enregistrer un joueur 
* Enregistrer plusieurs joueurs 
* Enregistrer un nouveau tournoi 
* Enregistrer des scores et clôturer le round (et le tournoi) 
* Clôturer un round 
* Clôturer un tournoi 

**Afficher** 
* Tous les joueurs par ordre alphabétique 
* Tous les joueurs par classement  <!-- pas demandé mais c'est fait --> 
* Tous les tournois 
* Un tournoi 
* Nom et dates d'un tournoi 
* Les joueurs du tournoi par ordre alphabétique 
* Les tours et matches d'un tournoi 

**Commandes de secours** 
* "*" : revenir au menu principal 
* "0" : sortir et fermer l'application  


## Lancer le programme 
*  Dans le terminal lancer le script : 
`python project.py` 


## Feedbacks 
En cas de mauvais fonctionnement ou si vous voulez suggérer des fonctionnalités, écrivez à morgan@chatnoir.lautre.net 


## Flake 8 
Lancer un rapport du projet complet : 
`flake8 --format=html --htmldir=flake-report/` (AttributeError) ou 
`flake8 path/to/the/file.py` (ne retourne rien) ou 
`flake8 path/to/the/folder` (ne retourne rien) ou 
`flake8` sans paramètres  
[Doc](https://flake8.pycqa.org/en/latest/)

*Ne crée pas de fichier html si pas d'erreur à signaler, crée le dossier avec uniquement des fichiers de mise en page* 

