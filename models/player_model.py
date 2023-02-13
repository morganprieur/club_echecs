
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 

import json 


# class Player(Persist_entity): 
class Player_model(AbstractModel): 

    def __init__(self, lastname:str, firstname:str):  # , age, genre, rank, global_score 
        super().__init__('p_table') 
        self.lastname = lastname  
        self.firstname = firstname 
        # self.age = age 
        # self.genre = genre 
        # self.rank = rank 
        # self.global_score = global_score 
        # players.append(self)   # pas bonnes pratiques 

    def __str__(self): 
        # born = '' 
        # if self.genre == 'M\n' or self.genre == 'M': 
        #     born = 'né'
        # elif self.genre == 'F\n' or self.genre == 'F': 
        #     born = 'née' 
        # elif self.genre == 'A\n' or self.genre == 'A': 
        #     born = 'né.e' 
        # return f'{self.firstname} {self.lastname} {born} on {self.age} range: {self.rank}.'  # , global score: {self.global_score}.' 
        return f'{self.firstname} {self.lastname}.'  # , global score: {self.global_score}.' 



    # def serialize(self): 
    #     # print(f'one_tournament TM172 : {self}') 
    #     # print(f'type(one_tournament) TP193 : {type(self)}') 
    #     # if not Player_model.check_if_json_empty('p_table'): 
    #     if not self.check_if_json_empty(): 
    #         # tournaments = Tournament_model.get_tournaments() 
    #         # players = Player_model.get_registered('p_table') 
    #         players = self.get_registered() 
    #     else: 
    #         players = [] 
    #     one_serialized_player = { 
    #         'lastname': self.lastname, 
    #         'firstname': self.firstname 
    #     } 
    #     # tournaments.append(self.to_dict()) 
    #     players.append(one_serialized_player) 
    #     with open("tables/p_table.json", "w") as file: 
    #         json.dump(players, file) 


    def to_dict(self): 
        return { 
            'lastname': self.lastname, 
            'firstname': self.firstname 
        } 


    
    # @staticmethod 
    # def check_if_json_empty(table): 
    #     # with open("tables/t_table.json",'rb') as f: 
    #     with open(f"tables/{table}.json",'rb') as f: 
    #         if len(f.read()) == 0: 
    #             print("The file is empty.") 
    #             return True 
    #         else: 
    #             print("The file is not empty.") 
    #             return False 


    # # Si le fichier JSON n'est pas vide : 
    # @staticmethod 
    # def get_tournaments(): 
    #     with open('tables/t_table.json', 'r') as file: 
    #         tournaments = json.load(file) 
    #     # print(f'type(self.registered) TM192 : {type(self.registered)}') 
    #     print(f'tournaments TM166 : {tournaments}') 
    #     print(f'type(tournaments) TM167 : {type(tournaments)}') 
    #     return tournaments 
    

    # @staticmethod 
    # def get_registered(table): 
    #     # with open('tables/t_table.json', 'r') as file: 
    #     with open(f'tables/{table}.json', 'r') as file: 
    #         registered = json.load(file) 
    #     # print(f'registered AC16 : {registered}') 
    #     # print(f'type(registered) AC17 : {type(registered)}') 
    #     return registered 


if __name__ == "__main__": 
    # import site 
    # site.addsitedir('abstract_model') 
    new_player = {
        "lastname": "Nom 130", 
        "firstname": "Prénom 130" 
    } 
    one_player = Player_model(**new_player) 
    print(f'new_player PM65 : {new_player}') 
    print(f'type(new_player) PM66 : {type(new_player)}') 
    one_player.serialize() 
    # print(f'get tournaments TM189 : {Tournament_model.get_tournaments()}') 
    # print(f'get registered TM189 : {Tournament_model.get_registered()}') 



    # def serialize_multi_players(self, players):  # , serialized_players 
    #     """ Serialization of the players data in order to register them 
    #         in the DB. 
    #     Args:
    #         players (list): list of object Players 
    #     Returns:
    #         serialized_players (list): the players in the expected format for the DB 
    #     """ 
    #     print(f'self PM141 : {self}') 
    #     print(f'dir(self) PM142 : {dir(self)}') 
    #     self.serialized_players = [] 

    #     # print(f'players C48 : {players}')   # inversés 
    #     # print(f'players C48 : {players[0].lastname}') 
    #     for p_obj in players: 
    #         # print(f'type(p_obj) : {type(p_obj)}\n') 
    #         # print(f'p_obj : {p_obj}\n') 
    #         # print(f'players[{p_obj}] : {players[p_obj]}\n') 
    #         serialized_player_data = {
    #             'lastname': p_obj.lastname, 
    #             'firstname': p_obj.firstname, 
    #             'age': p_obj.age, 
    #             'genre': p_obj.genre, 
    #             'rank': p_obj.rank, 
    #             # 'global_score': players[p_obj].global_score 
    #         } 

    #         self.serialized_players.append(serialized_player_data) 

    #     # print(f'serialized_players M88 : {serialized_players}') 

    #     # players_table.truncate() 
    #     # # # Enregistrer les joueurs sérialisés dans la bdd : 
    #     # players_table.insert_multiple(serialized_players) 

    #     return self.serialized_players 
    
    # def register_players(self, serialized_players): 
    #     with open('p_table.json', 'w') as file:
    #         json.dump(serialized_players, file) 
    #         return serialized_players 
    

    ### P2 write csv : 
    # Ouvre un fichier csv par catégorie, 
    # avec comme nom <nom de la catégorie>.csv, 
    # affiche les en-têtes des colones pour les livres 
    # et ferme le fichier 
    # def open_csv(cat_name): 
    #     """ Opens a file for the category,
    #         with <cat_name>.csv as name,
    #         displays books' headers for the columns 
    #         and closes the file  

    #     Args:
    #         cat_name (string): category name 
    #     """
    #     file_name = folder + '/data/' + cat_name + '.csv'
    #     books_headers = ['title', 'image url', 'upc', 'price excl tax', 'price', 'books availables', 'review', 'description'] 

    #     with open(file_name, 'w', encoding='utf-8') as csvfile: 
    #         writer = csv.writer(csvfile, delimiter = ',') 
    #         writer.writerow(books_headers) 

    # Affiche dans des fichiers CSV les infos des livres, 
    # à partir de leurs urls et en utilisant les retours des fonctions 
    # d'extraction des données 
    # def print_csv(book_data, cat_name): 
    #     """ Displays the books' data under the header into the files  

    #     Args:
    #         book_data (list): the extract functions' returns 
    #         cat_name (string): the category's name 
    #     """
    #     file_name = folder + '/data/' + cat_name + '.csv' 
    #     with open(file_name, 'a', encoding='utf-8') as csvfile: 
    #         writer = csv.writer(csvfile, delimiter = ',')  

    #         writer.writerow(book_data) 
    ### FIN P2 write csv 
    
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



