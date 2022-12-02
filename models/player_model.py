


# from Models.abstract_model_classes import Persist_entity 

# TinyDB 
from tinydb import TinyDB
db = TinyDB('db.json') 
players_table = db.table('players') 


# class Player(Persist_entity): 
class Player_model(): 

    # players = [] 
    # serialized_players = [] 

    def __init__(self, lastname, firstname, birthdate, genre, classement):  # , global_score 
        self.lastname = lastname  
        self.firstname = firstname 
        self.birthdate = birthdate 
        self.genre = genre 
        self.classement = classement 
        # self.global_score = global_score 

    def __str__(self): 
        born = '' 
        if self.genre == 'M\n' or self.genre == 'M': 
            born = 'né'
        elif self.genre == 'F\n' or self.genre == 'F': 
            born = 'née' 
        elif self.genre == 'A\n' or self.genre == 'A': 
            born = 'né.e' 
        return f'{self.firstname} {self.lastname} {born} on {self.birthdate} range: {self.classement}.'  # , global score: {self.global_score}.' 


    def instantiate_player(self, playerDict): 

        playerDict = { 
            'lastname': 'nom 1',  
            'firstname': 'prénom 1', 
            'birthdate': '02/12/2001', 
            'genre': 'F', 
            'classement': '41' 
        } 

        self.player_x = Player_model( 
            lastname=playerDict['lastname'], 
            firstname=playerDict['firstname'], 
            birthdate=playerDict['birthdate'], 
            genre=playerDict['genre'], 
            classement=playerDict['classement'] 
        ) 

        return self.player_x 



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


    # def serialize_multi_players(players):  # , serialized_players 
    #     """ Serialization of the players data in order to register them 
    #         in the DB. 
    #     Args:
    #         players (list): list of object Players 
    #     Returns:
    #         serialized_players (list): the players in the expected format for the DB 
    #     """
    #     serialized_players = [] 

    #     # print(f'players C48 : {players}')   # inversés 
    #     # print(f'players C48 : {players[0].lastname}') 
    #     for p_obj in range(len(players)): 
    #         # print(f'type(p_obj) : {type(p_obj)}\n') 
    #         # print(f'p_obj : {p_obj}\n') 
    #         # print(f'players[{p_obj}] : {players[p_obj]}\n') 
    #         serialized_player_data = {
    #             'lastname': players[p_obj].lastname, 
    #             'firstname': players[p_obj].firstname, 
    #             'birthdate': players[p_obj].birthdate, 
    #             'genre': players[p_obj].genre, 
    #             'classement': players[p_obj].classement, 
    #             'global_score': players[p_obj].global_score 
    #         } 

    #         serialized_players.append(serialized_player_data) 

    #     # print(f'serialized_players M88 : {serialized_players}')     # ok 

    #     players_table.truncate() 
    #     # # Enregistrer les joueurs sérialisés dans la bdd : 
    #     players_table.insert_multiple(serialized_players) 

    #     return serialized_players 


    # Vider la BDD avant d'enregistrer les nouveaux joueurs 
    # (ne pas le faire pour les tournois, si on doit garder un historique des tournois) 
    # players_table.truncate() 
    # Enregistrer les joueurs sérialisés dans la bdd : 
    ### à décommenter pour enregistrer dans la DB 
    # players_table.insert_multiple(serialized_players) 


