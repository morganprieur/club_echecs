


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
tournament_table = db.table('tournament') 


class Round_model(): 

    def __init__(self, round):  # ? 
        self.round = round 
        
        
    def __str__(self):
        roundList = f'Liste des matches : \n' 
        for m in self.round: 
            roundList += f'{str(m)}\n' 

        return f'{roundList}' 


    def print_round(self): 

        self.round_x = Round_model( 
            round = [
                    (
                        [1, 0], [2, 0]
                    ), (
                        [3, 0], [4, 0]
                    ), (
                        [5, 0], [6, 0]
                    ), (
                        [7, 0], [8, 0]
                    ) 
                ] 
        ) 
        print(f'self.round_x RM39 : \n{self.round_x}') 

        return self.round_x 




    
    # def instantiate_tournoi(self):  # tournamentDict 

    #     tournamentDict = {
    #         'name': 'nom', 
    #         'site': 'lieu', 
    #         't_date': '01/12/2022', 
    #         'nb_rounds': 4, 
    #         'rounds': {
    #             'matches': [
    #                 (
    #                     [1, 0], [2, 0]
    #                 ), (
    #                     [3, 0], [4, 0]
    #                 ), (
    #                     [5, 0], [6, 0]
    #                 ), (
    #                     [7, 0], [8, 0]
    #                 ) 
    #             ] 
    #         }, 
    #         'players': {
    #             1: 1, 
    #             2: 2, 
    #             3: 3, 
    #             4: 4, 
    #             5: 5, 
    #             6: 6, 
    #             7: 7, 
    #             8: 8, 
    #         }, 
    #         'duration': 'blitz', 
    #         'description': 'Observations du directeur du tournoi.' 
    #     }

    #     self.tournament_x = Tournament_model( 
    #         name = tournamentDict['name'],  
    #         site = tournamentDict['site'],  
    #         t_date = tournamentDict['t_date'],  
    #         nb_rounds = tournamentDict['nb_rounds'], 
    #         rounds = tournamentDict['rounds'], 
    #         players = tournamentDict['players'], 
    #         duration = tournamentDict['duration'], 
    #         description = tournamentDict['description'] 
    #     ) 
    #     # print(f'tournament_x TM97 : {self.tournament_x}') 
    #     # print(f'type(self.tournament_x) TM98 : {type(self.tournament_x)}') 

    #     return self.tournament_x 
    

    # def serialize_tournament(self): 

    #     # print(f'tournament_x TM103 : {self.tournament_x}') 

    #     serialized_tournament = {
    #         'name': self.tournament_x.name, 
    #         'site': self.tournament_x.site, 
    #         't_date': self.tournament_x.t_date, 
    #         'nb_rounds': self.tournament_x.nb_rounds, 
    #         'rounds': self.tournament_x.rounds, 
    #         'players': self.tournament_x.players,
    #         'duration': self.tournament_x.duration, 
    #         'description': self.tournament_x.description 
    #     }

    #     tournament_table.truncate() 
    #     # # Enregistrer les joueurs sérialisés dans la bdd : 
    #     tournament_table.insert(serialized_tournament) 

    #     return serialized_tournament 




    # def serialize_multi_players(players, serialized_players): 
    #     """ Serialization of the players data in order to register them 
    #         in the DB. 
    #     Args:
    #         players (list): list of object Players 
    #     Returns:
    #         serialized_players (list): the players in the expected format for the DB 
    #     """
    #     # serialized_players = [] 

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

""" 
    Chaque tournoi doit contenir au moins les informations suivantes :
    • Nom
    • Lieu :
    • Date
        ◦ Jusqu'à présent, tous nos tournois sont des événements d'un jour, mais nous pourrions en organiser de plusieurs jours à l'avenir, ce qui devrait donc permettre de varier les dates.
    • Nombre de tours
        ◦ Réglez la valeur par défaut sur 4.
    • Tournées
        ◦ La liste des instances rondes.
    • Joueurs
        ◦ Liste des indices correspondant aux instances du joueur stockées en mémoire.
    • Contrôle du temps
        ◦ C'est toujours un bullet, un blitz ou un coup rapide.
    • Description
        ◦ Les remarques générales du directeur du tournoi vont ici.
""" 

