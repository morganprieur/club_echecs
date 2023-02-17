
# from .abstract_model import AbstractModel  
# for tests : 
from models.abstract_model import AbstractModel 

import json 


# class Player(Persist_entity): 
class Player_model(AbstractModel): 

    def __init__(self, lastname:str, firstname:str, rank: int):  # , age, genre, rank, global_score 
        super().__init__('p_table') 
        self.lastname = lastname  
        self.firstname = firstname 
        self.rank = rank 
        # self.age = age 
        # self.genre = genre 
        # self.rank = rank 
        # self.global_score = global_score 
        # players.append(self)   # pas bonnes pratiques 

    # def __str__(self): 
    #     # born = '' 
    #     # if self.genre == 'M\n' or self.genre == 'M': 
    #     #     born = 'né'
    #     # elif self.genre == 'F\n' or self.genre == 'F': 
    #     #     born = 'née' 
    #     # elif self.genre == 'A\n' or self.genre == 'A': 
    #     #     born = 'né.e' 
    #     # return f'{self.firstname} {self.lastname} {born} on {self.age} range: {self.rank}.'  # , global score: {self.global_score}.' 
    #     return f'{self.firstname} {self.lastname} classement : {self.rank}.'  # , global score: {self.global_score}.' 


    def to_dict(self): 
        return { 
            'lastname': self.lastname, 
            'firstname': self.firstname, 
            'rank': self.rank 
        } 
    



if __name__ == "__main__": 
    # import site 
    # site.addsitedir('abstract_model') 
    new_player = {
        'lastname': 'Nom 130', 
        'firstname': 'Prénom 130', 
        'rank': 30 
    } 
    one_player = Player_model(**new_player) 
    print(f'new_player PM80 : {new_player}') 
    # print(f'type(new_player) PM66 : {type(new_player)}') 
    one_player.serialize() 


    # def register_players(self, serialized_players): 
    #     with open('p_table.json', 'w') as file:
    #         json.dump(serialized_players, file) 
    #         return serialized_players 
    

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



