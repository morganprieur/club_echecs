


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
tournament_table = db.table('tournament') 


class Tournament_model(): 

    def __init__(self, name, site, t_date, nb_rounds, rounds, players, duration, description): 
        self.name = name 
        self.site = site 
        self.t_date = t_date 
        self.nb_rounds = nb_rounds 
        self.rounds = rounds 
        self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):
        begin_phrase = f'Nom du tournoi : {self.name} \nlieu : {self.site} \ndate(s) : {self.t_date} \n{self.nb_rounds} tours \nliste des tours : (instances de tours à mettre ici ###) \n' 
        # roundsList = '' 
        round_name = '' 
        round_matches = '' 
        start_datetime = '' 
        end_datetime = '' 
        middle_phrase = f'\njoueurs de ce tournoi : (instances de joueurs à mettre ici ###) \n' 
        playersList = '' 
        end_phrase = f'temps de jeu : {self.duration}. \nDescription : {self.description}' 
        # print(f'rounds TM28 : {self.rounds}')
        # rounds = { 
        #     'round_name': roundDict['round_name'], 
        #     'matches': roundDict['round_matches'], 
        #     'date-heure début': roundDict['start_datetime'], 
        #     'date-heure fin': roundDict['start_datetime']
        # }, 
        for r in range(len(self.rounds)): 
            # roundsList += f'{self.rounds[r]} \n' 
            round_name += f'{self.rounds[r+1]["round_name"]}\n' 
            round_matches += f'{self.rounds[r+1]["matches"]}\n' 
            start_datetime += f'{self.rounds[r+1]["date-heure début"]}\n' 
            end_datetime += f'{self.rounds[r+1]["date-heure fin"]}\n' 
        for p in self.players: 
            playersList += f'{p} \n' 
        return f'{begin_phrase}\nnom : {round_name}matches : {round_matches}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{playersList}{end_phrase}' 
        # return f'{begin_phrase}{roundsList}{middle_phrase}{playersList}{end_phrase}' 

    
    def instantiate_tournoi(self, tournamentDict, roundDict):  #  

        self.tournament_x = Tournament_model( 
            name = tournamentDict['name'],  
            site = tournamentDict['site'],  
            t_date = tournamentDict['t_date'],  
            nb_rounds = tournamentDict['nb_rounds'], 
            # rounds = tournamentDict['rounds'], 
            rounds = { 
                1: {
                    'round_name': roundDict['round_name'], 
                    'matches': roundDict['round_matches'], 
                    'date-heure début': roundDict['start_datetime'], 
                    'date-heure fin': roundDict['end_datetime']
                }  
            }, 
            players = tournamentDict['players'], 
            duration = tournamentDict['duration'], 
            description = tournamentDict['description'] 
        ) 
        # print(f'tournament_x TM97 : {self.tournament_x}') 
        # print(f'type(self.tournament_x) TM98 : {type(self.tournament_x)}') 

        return self.tournament_x 
    

    def serialize_tournament(self): 

        # print(f'tournament_x TM103 : {self.tournament_x}') 

        serialized_tournament = {
            'name': self.tournament_x.name, 
            'site': self.tournament_x.site, 
            't_date': self.tournament_x.t_date, 
            'nb_rounds': self.tournament_x.nb_rounds, 
            'rounds': self.tournament_x.rounds, 
            'players': self.tournament_x.players,
            'duration': self.tournament_x.duration, 
            'description': self.tournament_x.description 
        }

        tournament_table.truncate() 
        # # Enregistrer les joueurs sérialisés dans la bdd : 
        tournament_table.insert(serialized_tournament) 

        return serialized_tournament 




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

