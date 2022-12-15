


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

    def __str__(self):  # , roundDicts        
        begin_phrase = f'\nNom du tournoi : {self.name} \nlieu : {self.site} \ndate(s) : {self.t_date} \n{self.nb_rounds} tours \nliste des tours : \n' # (instances de tours à mettre ici ###)  
        # roundsList = '' 
        round_name = '' 
        round_matches = '' 
        start_datetime = '' 
        end_datetime = '' 
        middle_phrase = f'\njoueurs de ce tournoi : (instances de joueurs à mettre ici ###) \n' 
        playersList = [] 
        end_phrase = f'temps de jeu : {self.duration}. \nDescription : {self.description}' 
        # print(f'rounds TM28 : {self.rounds}')
        # rounds = { 
        #     'round_name': roundDict['round_name'], 
        #     'matches': roundDict['round_matches'], 
        #     'date-heure début': roundDict['start_datetime'], 
        #     'date-heure fin': roundDict['start_datetime']
        # }, round_number 
        # for i in round_number: 
        #     pass 
        # print(f'len(self.rounds) : {len(self.rounds)}') 
        for r in range(len(self.rounds)): 
            for i in self.rounds[r]: 
                # round_name += f'{i["round_name"]}\n'  ###  
                round_name += f'{self.rounds[r][int(i)]["round_name"]}\n' 
                round_matches += f'{self.rounds[r][int(i)]["round_matches"]}\n' 
                start_datetime += f'{self.rounds[r][int(i)]["start_datetime"]}\n' 
                end_datetime += f'{self.rounds[r][int(i)]["end_datetime"]}\n' 
        # print(f'len(self.players) TM49 : {len(self.players)}')  # str # object of type 'Tournament_model' has no len() 
        # if self.players:  # TypeError: 'Tournament_model' object is not iterable ### 
        #     for p in self.players: 
        #         playersList.append(p) 
        return f'{begin_phrase}\nnom : {round_name}matches : {round_matches}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}'  # {playersList} 
        # return f'{begin_phrase}{roundsList}{middle_phrase}{playersList}{end_phrase}' 

    # 'rounds': { 
    #     1: roundDicts[0][1], 
    #     2: roundDicts[0][2],  
    # }, ### comment intégrer l'objet Round ici ? 


    def instantiate_tournament(self, tournaments, roundDicts): 
        print(f'type(tournaments) TM63 : {type(tournaments)}') 
        print(f'tournaments TM64 : {tournaments}')  # tounrament == déjà un objet 
        # for t in tournaments: 
        #     self.tournament_x = Tournament_model( 
        #         lastname=p, 
        #         firstname=p, 
        #         age=p, 
        #         genre=p, 
        #         rank=p 
        #     ) 

        # for p in players: 
        #     self.player_x = Player_model( 
        #         lastname=p, 

        for t in tournaments: 
            print(f't TM63 : {t}') 
            # print(f'type(tournaments[t]) TM61 : {type(tournaments[t])}') 
            self.tournament_x = Tournament_model( 
                name=t,  
                site=t,  
                t_date=t,  
                nb_rounds=t, 
                # rounds = tournaments['rounds'], 
                rounds= # [ 
                    roundDicts, 
                    # {      # key=1/2...: value='round_name'... 
                    # 'round_name' = roundDicts[0]["1"]['round_name'],  ### TypeError: tuple indices must be integers or slices, not str 
                    # 'round_matches' = roundDicts[0]["1"]['round_matches'], 
                    # 'start_datetime' = roundDicts[0]["1"]['start_datetime'], 
                    # 'end_datetime' = roundDicts[0]["1"]['end_datetime'] 
                    # }, 
                # ], 
                players=t, 
                duration=t, 
                description=t 
            ) 
            print(f'tournament_x.name TM95 : {self.tournament_x.name}') 
            print(f'type(self.tournament_x.name) TM96 : {type(self.tournament_x.name)}') 

        return self.tournament_x 
    

    # def serialize_tournament(self): 
    def serialize_tournament(tournaments): 

        print(f'type(tournaments[0]) TM109 : {type(tournaments[0])}') 
        # print(f'dir(self) TM104 : {dir(self)}')  # inception 
        # print(f'type(self.tournament_x) TM105 : {type(self.tournament_x)}') 

        # serialized_players = [] 
        # # print(f'players C48 : {players}')   # inversés 
        # # print(f'players C48 : {players[0].lastname}') 
        # for p_obj in range(len(players)): 
        #     # print(f'type(p_obj) : {type(p_obj)}\n') 
        #     # print(f'p_obj : {p_obj}\n') 
        #     # print(f'players[{p_obj}] : {players[p_obj]}\n') 
        #     serialized_player_data = {
        #         'lastname': players[p_obj].lastname, 

        # for t in self.tournament_x: 
            # print(f't TM109 : {t}') 
        serialized_tournaments = [] 

        for t_obj in tournaments: 
            serialized_tournament = {
                'name': t_obj.name, 
                'site': t_obj.site, 
                't_date': t_obj.t_date, 
                'nb_rounds': t_obj.nb_rounds, 
                'rounds': t_obj.rounds, 
                'players': t_obj.players,
                'duration': t_obj.duration, 
                'description': t_obj.description 
            } 
            serialized_tournaments.append(serialized_tournament) 
            print(f'type(serialized_tournament["name"]) TM116 : {type(serialized_tournament["name"])}') 

        print(f'serialized_tournament TM118 : {serialized_tournament}')         

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

