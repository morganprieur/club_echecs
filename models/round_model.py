


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
tournament_table = db.table('tournament') 

# un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 
# Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, 
# qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. 
# Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.

class Round_model(): 

    def __init__(self, round_name, round_matches, start_datetime, end_datetime):  ### datetime automatique ### 
        self.round_name = round_name 
        self.round_matches = round_matches 
        self.start_datetime = start_datetime 
        self.end_datetime = end_datetime 
    

    def __str__(self):
        round_matchesList = f'' 
        for m in range(len(self.round_matches)): 
            round_matchesList += f' {str(self.round_matches[m])} \n' 

        return f'Nom du round : {self.round_name} \nListe des matches : \n{round_matchesList}début : {self.start_datetime} \nfin : {self.end_datetime}' 


    # def print_round(self): 

    #     self.round_x = Round_model( 
    #         round = [
    #                 (
    #                     [1, 0], [2, 0]
    #                 ), 
    #                 (
    #                     [3, 0], [4, 0]
    #                 ), 
    #                 (
    #                     [5, 0], [6, 0]
    #                 ),
    #                  (
    #                     [7, 0], [8, 0]
    #                 ) 
    #             ] 
    #     ) 
    #     print(f'self.round_x RM39 : \n{self.round_x}') 

    #     return self.round_x 

    
    def instantiate_round(self, roundDicts): 

        # roundDict = { 
        #     'round_name': 'round 1', 
        #     'round_matches': [
        #         (
        #             [1, 0], [2, 0]
        #         ), (
        #             [3, 0], [4, 0]
        #         ), (
        #             [5, 0], [6, 0]
        #         ), (
        #             [7, 0], [8, 0]
        #         ) 
        #     ], 
        #     'start_datetime': '02/12/22 - 07:23', 
        #     'end_datetime': '02/12/22 - 09:23' 
        # } 

        for r in roundDicts: 

            self.round_x = Round_model( 
                # round_name = r['round_name'],  ### 
                round_name = roundDicts[0][1]['round_name'], 
                round_matches = roundDicts[0][1]['round_matches'], 
                start_datetime = roundDicts[0][1]['start_datetime'], 
                end_datetime = roundDicts[0][1]['end_datetime'] 
            ) 
        # print(f'tournament_x TM97 : {self.round_x}') 
        # print(f'type(self.tournament_x) TM98 : {type(self.round_x)}') 

        return self.round_x 

    def instantiate_rounds(self, roundDicts): 

        self.rounds = [] 

        for i in range(len(roundDicts)): 
            self.instantiate_round(self, roundDicts) 
            self.rounds.append(self.round_x) 
        
        return self.rounds 
    

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

