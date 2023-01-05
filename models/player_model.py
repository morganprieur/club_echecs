


# from Models.abstract_model_classes import Persist_entity 

# TinyDB 
from tinydb import TinyDB
db = TinyDB('db.json') 
players_table = db.table('players') 
import json 


# class Player(Persist_entity): 
class Player_model(): 

    # players = [] 
    # serialized_players = [] 

    def __init__(self, lastname, firstname, age, genre, rank):  # , global_score 
        self.lastname = lastname  
        self.firstname = firstname 
        self.age = age 
        self.genre = genre 
        self.rank = rank 
        # self.global_score = global_score 
        # players.append(self)   # pas bonnes pratiques 

    def __str__(self): 
        born = '' 
        if self.genre == 'M\n' or self.genre == 'M': 
            born = 'né'
        elif self.genre == 'F\n' or self.genre == 'F': 
            born = 'née' 
        elif self.genre == 'A\n' or self.genre == 'A': 
            born = 'né.e' 
        return f'{self.firstname} {self.lastname} {born} on {self.age} range: {self.rank}.'  # , global score: {self.global_score}.' 


    # def instantiate_player(self, players): 

    #     # playerDict = { 
    #     #     'lastname': 'nom 1',  
    #     #     'firstname': 'prénom 1', 
    #     #     'birthdate': '02/12/2001', 
    #     #     'genre': 'F', 
    #     #     'classement': '41' 
    #     # } 

    #     for p in players: 
    #         self.player_x = Player_model( 
    #             lastname=p, 
    #             firstname=p, 
    #             age=p, 
    #             genre=p, 
    #             rank=p 
    #             # lastname=players['lastname'], 
    #             # firstname=players['firstname'], 
    #             # birthdate=players['birthdate'], 
    #             # genre=players['genre'], 
    #             # classement=players['classement'] 
    #         ) 
    #         # print(f'\nPlayer_model.player_x PM60 : \n{Player_model.player_x}') 
        

    # # def instantiate_player(self, playerDict): 

    # #     playerDict = { 
    # #         'lastname': 'nom 1',  
    # #         'firstname': 'prénom 1', 
    # #         'birthdate': '02/12/2001', 
    # #         'genre': 'F', 
    # #         'classement': '41' 
    # #     } 

    # #     self.player_x = Player_model( 
    # #         lastname=playerDict['lastname'], 
    # #         firstname=playerDict['firstname'], 
    # #         birthdate=playerDict['birthdate'], 
    # #         genre=playerDict['genre'], 
    # #         classement=playerDict['classement'] 
    # #     ) 
    #         # print(f'\nPlayer_model.player_x PM80 : \n{Player_model.player_x}') 

    #     return self.player_x 



    # def instantiate_players(formated_players):  # , players 
    #     """ Instantiate the players in a list of object Players. 
    #     Args:
    #         formated_players (list): the list of the players formated data 
    #     Returns:
    #         players (list): the players in form of object Player 
    #     """ 
    #     # Liste pour les joueurs objets 
    #     players = [] 

    #     print(f'formated_players ln M42 : {formated_players}')  # inversés 

    #     for data_dict in range(len(formated_players)): 
    #         player_x = Player_model( 
    #             lastname=formated_players[data_dict]['lastname'], 
    #             firstname=formated_players[data_dict]['firstname'], 
    #             birthdate=formated_players[data_dict]['birthdate'], 
    #             genre=formated_players[data_dict]['genre'], 
    #             classement=formated_players[data_dict]['classement']  # , 
    #             # global_score=formated_players[data_dict]['global_score'] 
    #         ) 
    #         print(f'player_x ln M52 :  {player_x}') 

    #         players.append(player_x) 

    #     print(f'players PM60 :  {players}') 
    #     print(f'players[0].lastname PM61 :  {players[0].lastname}') 
        
    #     return players 

    ### Voir pour sérialiser : 
    def to_dict(self, exclude=None): 
        print(f'self PM119 : {self}') 
        print(f'dir(self) PM120 : {dir(self)}') 
        exclude = exclude or []
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and key not in exclude
            and not callable(getattr(self, key))
            and isinstance(getattr(self, key), (str, int, float))
      } 


    def serialize_multi_players(self, players):  # , serialized_players 
        """ Serialization of the players data in order to register them 
            in the DB. 
        Args:
            players (list): list of object Players 
        Returns:
            serialized_players (list): the players in the expected format for the DB 
        """ 
        print(f'self PM141 : {self}') 
        print(f'dir(self) PM142 : {dir(self)}') 
        self.serialized_players = [] 

        # print(f'players C48 : {players}')   # inversés 
        # print(f'players C48 : {players[0].lastname}') 
        for p_obj in players: 
            # print(f'type(p_obj) : {type(p_obj)}\n') 
            # print(f'p_obj : {p_obj}\n') 
            # print(f'players[{p_obj}] : {players[p_obj]}\n') 
            serialized_player_data = {
                'lastname': p_obj.lastname, 
                'firstname': p_obj.firstname, 
                'age': p_obj.age, 
                'genre': p_obj.genre, 
                'rank': p_obj.rank, 
                # 'global_score': players[p_obj].global_score 
            } 

            self.serialized_players.append(serialized_player_data) 

        # print(f'serialized_players M88 : {serialized_players}') 

        # players_table.truncate() 
        # # # Enregistrer les joueurs sérialisés dans la bdd : 
        # players_table.insert_multiple(serialized_players) 

        return self.serialized_players 
    
    def register_players(self, serialized_players): 
        with open('p_table.json', 'w') as file:
            json.dump(serialized_players, file) 
            return serialized_players 
    

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


    # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # (ne pas le faire pour les tournois, si on doit garder un historique des tournois) 
    # players_table.truncate() 
    # Enregistrer les joueurs sérialisés dans la bdd : 
    ### à décommenter pour enregistrer dans la DB 
    # players_table.insert_multiple(serialized_players) 


