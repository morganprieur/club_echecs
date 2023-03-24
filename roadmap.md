
TODO 

Tous les modèles 
    --> ajouter les props qui manquent 
    --> fichiers de données : data/tournaments 
    --> retirer input_data.csv 

Players 
    --> points au départ 
    --> mise à jour des points à chaque round 
    --> + identifiant national d'échecs (juste à stocker, pas à générer) 

Tournaments 
    --> date début automatique (retirer l'heure)
    --> date fin auto 
    V--> ID automatique 
    V--> check key 'rounds' avant instanciation et l'ajouter si elle manque 
        (voir dans MC.report_tournaments) 
    --> Ajouter les joueurs aux tournois 
    --> nb de rounds max 
    --> décrémenter nb de rounds 

WIP Rounds 
    --> datetime début et fin automatiques 
    V début ok 
    --> date + heure de fin : voir sur [add_missing_properties] **ajouter un flag pour "round terminé ou non"** 
        --> voir consigne 
            - Ajouter une prop "nb_de_rounds" à round_match 
            - Décrémenter "nb_de_rounds" à chaque nouveau round 
            ->quand c'est le dernier round : ajouter datetime de fin 
    V--> ID automatique 
    --> mc.report_rounds() : manque matches 

Matches 
    V--> model 
    V--> intégrer matches à round 
    V--> report matches one tournament 
    V--> main_controller menu 7 
    --> liste des matches dans chaque round 

--> définir les matches 


XX Facto méthode MC.select_one_obj() : voir si rentable ou pas (combien d'args il faut mettre) 
--> marche pas, il faut tjrs select un tournoi, puis un/des joueur/s et un/des round/s, puis des matches  

README 

black (config espaces en fin de lignes et ligne à la fin du doc) 

WIP Accueil 

========== 

## TOURNOIS
Le programme utilise les fichiers de données JSON pour la persistance des informations sur
les tournois. Les fichiers de données sont généralement situés dans le dossier
data/tournaments.  

### DÉROULEMENT DE BASE DU TOURNOI
● Un tournoi a un nombre de tours défini.
● Chaque tour est une liste de matchs.
    ○ Chaque match consiste en une paire de joueurs.
● À la fin du match, les joueurs reçoivent des points selon leurs résultats.
    ○ Le gagnant reçoit 1 point.
    ○ Le perdant reçoit 0 point.
○ Chaque joueur reçoit 0,5 point si le match se termine par un match nul.  

### SCHÉMA DES TOURNOIS
Chaque tournoi doit contenir au moins les informations suivantes :
● nom ;
● lieu ;
● date de début et de fin ;
● nombre de tours – réglez la valeur par défaut sur 4 ;
● numéro correspondant au tour actuel ;
● une liste des tours ;
● une liste des joueurs enregistrés ;
● description pour les remarques générales du directeur du tournoi.  

## TOURS / MATCHS
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous forme de liste dans l'instance du tour auquel ils appartiennent.
En plus de la liste des matchs, chaque instance du tour doit contenir un nom. 
Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé.

====  
## GÉNÉRATION DES PAIRES
● Au début du premier tour, mélangez tous les joueurs de façon aléatoire.
● Chaque tour est généré dynamiquement en fonction des résultats des joueurs dans le tournoi en cours.
○ Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
○ Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4 et ainsi de suite.)
○ Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
○ Lors de la génération des paires, évitez de créer des matchs identiques (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
■ Par exemple, si le joueur 1 a déjà joué contre le joueur 2,
associez-le plutôt au joueur 3.
● Mettez à jour les points de tous les joueurs après chaque tour et répétez le processus de triage et d’association jusqu'à ce que le tournoi soit terminé.
● Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ; il n'est donc pas nécessaire de mettre en place un équilibrage des couleurs.

====  
## RAPPORTS
Nous aimerions pouvoir afficher les rapports suivants dans le programme :
● liste de tous les joueurs par ordre alphabétique ;
● liste de tous les tournois ;
● nom et dates d’un tournoi donné ;
● liste des joueurs du tournoi par ordre alphabétique ;
● liste de tous les tours du tournoi et de tous les matchs du tour.
Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
Les rapports peuvent être en texte brut, à condition qu'ils soient bien formatés et faciles à lire. Vous pouvez même utiliser des modèles HTML !

====  
## SAUVEGARDE / CHARGEMENT DES DONNÉES
Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.
Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
charger toutes ses données à partir des fichiers JSON et **pouvoir restaurer son état entre les exécutions**.   

====  
**Si vous avez le choix entre la manipulation de dictionnaires ou d'instances de classe, choisissez toujours des instances de classe pour assurer la conformité avec le modèle de conception MVC.**  


