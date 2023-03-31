
# from .abstract_model import AbstractModel  
# for tests : 
from models.abstract_model import AbstractModel 

import json 


# class Player(Persist_entity): 
class Player_model(AbstractModel): 

    def __init__(self, id:int, lastname:str, firstname:str, rank: int, global_score:float):  # , age, genre, rank 
        super().__init__('players') 
        self.id = id  
        self.lastname = lastname  
        self.firstname = firstname 
        self.rank = rank 
        self.global_score = global_score 
        # self.age = age 
        # self.genre = genre 
        # players.append(self)   # pas bonnes pratiques 

    def __str__(self): 
        return f'\nJoueur {self.id} : {self.firstname} {self.lastname} classement : {self.rank}, global score: {self.global_score}.' 


    def to_dict(self): 
        return { 
            'id': self.id, 
            'lastname': self.lastname, 
            'firstname': self.firstname, 
            'rank': self.rank, 
            'global_score': self.global_score  
        } 
    
""" Enoncé : 
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
""" 
    

    ### Python forge : écrire dans fichier JSON : 
    # import json

    # employee = {
    #     "nom": "Marie Richardson",
    #     "id": 1,
    #     "recrutement": True,
    #     "department": "Ventes"
    # }

    # with open('data.json', 'w') as mon_fichier:
    #     json.dump(employee, mon_fichier) 
    ### FIN Python forge : écrire dans fichier JSON 
    
    ### Python forge : lire un fichier JSON : 
    # import json

    # with open('data.json') as mon_fichier:
    #     data = json.load(mon_fichier)

    # print(data) 
    ### FIN Python forge : lire un fichier JSON 



