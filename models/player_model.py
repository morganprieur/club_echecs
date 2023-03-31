
# from .abstract_model import AbstractModel  
# for tests : 
from models.abstract_model import AbstractModel 

import json 


# class Player(Persist_entity): 
class Player_model(AbstractModel): 

    def __init__(self, lastname:str, firstname:str, rank: int, global_score:float):  # , age, genre, rank 
        super().__init__('players') 
        self.lastname = lastname  
        self.firstname = firstname 
        self.rank = rank 
        self.global_score = global_score 
        # self.age = age 
        # self.genre = genre 
        # players.append(self)   # pas bonnes pratiques 

    def __str__(self): 
        return f'{self.firstname} {self.lastname} classement : {self.rank}, global score: {self.global_score}.' 


    def to_dict(self): 
        return { 
            'lastname': self.lastname, 
            'firstname': self.firstname, 
            'rank': self.rank, 
            'global_score': self.global_score  
        } 
    

# if __name__ == "__main__": 
#     new_player = {
#         'lastname': 'Nom 130', 
#         'firstname': 'Prénom 130', 
#         'rank': 30, 
#         'global_score': 0 
#     } 
#     one_player = Player_model(**new_player) 
#     print(f'new_player PM80 : {new_player}') 
#     # print(f'type(new_player) PM66 : {type(new_player)}') 
#     one_player.serialize_new_object() 

    

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



