
# Projet 4 - Développer un programme logiciel en python 
Centre d'échecs 


## Créer un environnement virtuel 

*  Installer la version de Python indiquée sur le repo du projet     
<!-- *  Copier le dossier téléchargé et extrait   -->
*  Depuis le dossier du projet, créer un environnement virtuel : `python -m venv env`     
*  Activer l'environnement virtuel :      
Linux --> `source bin/activate`        
Windows --> `source env/Scripts/activate` (ne pas taper "python" au début de la commande)     
     
L'invite de commande commence maintenant par `(env)`, ce qui signifie qu'on se trouve bien dans l'environnement virtuel. 
A noter que dans l'arborescence de l'IDE, les dossiers et fichiers de travail apparaissent au même niveau que le dossier `env`.     
     
     
## Installer les dépendances 
Taper la commande :     
`pip install -r requirements.txt` 


## Arborescence du projet 

work 
 |--> env  
 |-- project.py (entrée du programme) 


## Fonctionnalités 

**Enregistrer** 
* Enregistrer un joueur 
* Enregistrer plusieurs joueurs 
* Enregistrer un nouveau tournoi 
* Attribuer des joueurs à un tournoi 
* Définir et enregistrer les matches pour le 1er round 
* Définir et enregistrer les matches pour les rounds 2 à 4 
* Clôturer un round 
* Clôturer un tournoi 
* Enregistrer des scores 

**Afficher** 
* Afficher tous les joueurs par ordre alphabétique 
* Afficher tous les joueurs par nombre de points 
* Afficher tous les joueurs d'un tournoi par ordre alphabétique 
* Afficher tous les tournois 
* Afficher un tournoi désiré 
* Afficher les nom et date d'un tournoi 
* Afficher tous les rounds et matches d'un tournoi désiré  

## Menus 

**Menu "Enregistrer"** 
* Enregistrer un joueur 
* Enregistrer plusieurs joueurs 
* Enregistrer un nouveau tournoi 
* Enregistrer des scores 

**Menu "Afficher"** 
* Tous les joueurs par ordre alphabétique 
* Tous les joueurs par classement (pas demandé mais c'est fait) 
* Tous les tournois 
* Nom et dates d'un tournoi 
* Les joueurs du tournoi par ordre alphabétique 
* Les tours et matches d'un tournoi 



## Lancer le programme 

*  Dans le terminal lancer le script : 
`python project.py` 

<!-- La console n'affiche aucun retour, pour vérifier que ça fonctionne, il faut ouvrir le dossier `data` pour voir si un fichier `Travel.csv` est créé, puis les suivants. Ouvrir le fichier avec Excel ou LibreOffice pour vérifier son contenu.  -->






## Flake 8 

Lancer un rapport du projet complet : 
`flake8 --format=html --htmldir=flake-report/` 


