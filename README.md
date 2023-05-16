
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




## Lancer le programme 

*  Dans le terminal lancer le script : 
`python project.py` 

<!-- La console n'affiche aucun retour, pour vérifier que ça fonctionne, il faut ouvrir le dossier `data` pour voir si un fichier `Travel.csv` est créé, puis les suivants. Ouvrir le fichier avec Excel ou LibreOffice pour vérifier son contenu.  -->






## Flake 8 

Lancer un rapport du projet complet : 
`flake8 --format=html --htmldir=flake-report/` 


