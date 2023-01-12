



from views.input_view import Input_view 
from models.tournament_model import Tournament_model 
from models.round_model import Round_model 
from models.match_model import Match_model 
from models.player_model import Player_model 


class Main_controller(): 

    tournament = Tournament_model.instantiate_tournament(Tournament_model, Input_view.new_tournament) 
    tournaments = Tournament_model.serialize_tournaments(Tournament_model) 

    def __init__(self, tournament, serialized_tournament): 
        self.tournament = tournament 
        self.serialized_tournaments = [] 
        self.serialized_tournament = serialized_tournament 

    def tourn_stream(self): 

        print('tourn_stream main controller') 

        print(f'Main_controller.tournament MC26 : {self.tournament}') 
        print(f'Main_controller.tournaments MC27 : {self.tournaments}') 

        # Tournament_model.print_t(Tournament_model) 

        
        # print(f'dir(self) : {dir(self)}') 
        # print(f'self.variable : {self.variable}') 

        # print(f'report_tournament : {Report_view.report_tournament}') 
        
        # get tournament data : 
        # Input_view.get_input_tournament(Input_view) 
        Input_view.get_new_tourns(Input_view) 
        # Input_view.get_fct(Input_view) 
        # instancier le tournoi : 
        Tournament_model.instantiate_tournament(Tournament_model, Input_view.new_tournament) 
        # tournoi = Tournament_model(name, site, t_date, duration, description) 
        #### pouruqoi cette méthode n'est pas appelée quand décommentée : ??? #### 
        # self.serialized_tournament = Tournament_model.serialize_one_tournament(Tournament_model) 
        self.serialized_tournaments = Tournament_model.serialize_tournaments(Tournament_model) 
        # Tournament_model.register_tournaments(Tournament_model) 

        # Tournament_model.get_registered_tournaments(Tournament_model) 

        # Main_controller.display_tournaments(self.serialized_tournaments) 
        
        # Report_view.display_tournament(Main_controller.variable) 
        

        """ 
        RAPPORTS
        Nous aimerions pouvoir afficher les rapports suivants dans le programme :

            • Liste de tous les joueurs:
                ◦ par ordre alphabétique ;
                ◦ par classement.
            • Liste de tous les joueurs d'un tournoi :
                ◦ par ordre alphabétique ;
                ◦ par classement.
            • Liste de tous les tournois.
            • Liste de tous les tours d'un tournoi.
            • Liste de tous les matchs d'un tournoi.

        Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
        """ 

        # # Afficher un tournoi 
        # print(f'tournoi : {Tournament_model.tournament}') 
        # Afficher tous les tournois 
        # print('Tournois : ') 
        # for i in Tournament_model.tournaments: 
        #     print(f'{Tournament_model.tournament}') 
    

    def display_tournaments(serialized_tournaments): 
            # print(f'dir(Tournament_model) : {dir(Tournament_model)}') 
            print(f'serialized_tournaments MC91 : {serialized_tournaments}') 
            # print(f'self.variable : {self.variable}') 
            # print('Variables : ') 
            # for i in self.variable: 
            #     print(f'variable : {i}') 

    def start(): 

        print('start main controller') 






        playerDict = { 
            'lastname': 'nom 1',  
            'firstname': 'prénom 1', 
            'birthdate': '02/12/2001', 
            'genre': 'F', 
            'classement': '41' 
        } 

        roundDicts = { 
            1: { 
                'round_name': 'round 1', 
                'round_matches': [
                    (
                        [1, 0], [2, 0]
                    ), (
                        [3, 0], [4, 0]
                    ), (
                        [5, 0], [6, 0]
                    ), (
                        [7, 0], [8, 0]
                    ) 
                ], 
                'start_datetime': '02/12/22 - 07:23', 
                'end_datetime': '02/12/22 - 09:23' 
            }, 
            2: { 
                'round_name': 'round 2', 
                'round_matches': [
                    (
                        [1, 0], [3, 0]
                    ), (
                        [5, 0], [7, 0]
                    ), (
                        [2, 0], [4, 0]
                    ), (
                        [6, 0], [8, 0]
                    ) 
                ], 
                'start_datetime': '02/12/22 - 11:11', 
                'end_datetime': '02/12/22 - 13:11' 
            } 
        }, 
        # print(f'\roundDicts C58 : \n{roundDicts}') 
        # print(f'\nroundDicts[0][1] C59 : \n{roundDicts[0]["1"]}') 
        # print(f'roundDicts[0][2] C59 : \n{roundDicts[0][2]}\n') 

        # rounds = [ 
        #     {      # key=1/2...: value='round_name'... 
        #         'round_name': roundDicts[0]["1"]['round_name'],  ### TypeError: tuple indices must be integers or slices, not str 
        #         'round_matches': roundDicts[0]["1"]['round_matches'], 
        #         'start_datetime': roundDicts[0]["1"]['start_datetime'], 
        #         'end_datetime': roundDicts[0]["1"]['end_datetime'] 
        #     }, 
        # ], 

        tournamentDict = {
            'name': 'Tournoi 1', 
            'site': 'lieu 1', 
            't_date': ['01/12/2022',], 
            'nb_rounds': 4, 
            'rounds': # [ 
                roundDicts[0][1], 
            # ], ### comment intégrer l'objet Round ici ? 
            'players': {
                1: 1, 
                2: 2, 
                3: 3, 
                4: 4, 
                5: 5, 
                6: 6, 
                7: 7, 
                8: 8, 
            }, 
            'duration': 'blitz', 
            'description': 'Observations du directeur du tournoi.' 
        } 

        # # Round_model.instantiate_round(Round_model, roundDict) 
        # Round_model.instantiate_rounds(Round_model, roundDicts) 

        # # tournament_obj = 
        # Tournament_model.instantiate_tournament(Tournament_model, tournamentDict, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 

    #### PJ 
        players = []
        with open("utils/players.csv", "r", encoding='utf-8') as file:
            for line in file:
                if line.startswith("lastname"):
                    continue

                lastname, firstname, age, genre, rank = line.strip().split(";") 
                players.append(Player_model(lastname, firstname, age, genre, rank)) 
    #### PJ / 
        print("file C110 : ", players) 
        # for p in players: 
        #     print("file : ", p.lastname) 
        #     print("file : ", p.firstname) 
        #     print("file : ", p.age) 
        #     print("file : ", p.genre) 
        #     print("file : ", p.rank) 
        # print("player2.lastname : ", players[2].firstname) 

        # ser_players = Player_model.to_dict(players, exclude=None) 
        serial_players = Player_model.serialize_multi_players(Player_model, players) 
        print(f'ser_players MC124 : {serial_players}') 
        # Player_model.register_players(Player_model.serialized_players)
        Player_model.register_players(Player_model, Player_model.serialized_players) 
        

        matches = [] 
        player1 = [] 
        player2 = [] 
        players = [] 
        # match = tuple 
        match = () 
        print(f'type(match) MC148 : {type(match)}') 
        with open("utils/matches.csv", "r") as m_file: 
            for m_line in m_file: 
                if m_line.startswith("player1"): 
                    continue 

                player1, player2 = m_line.strip().split(";") 
                match = (player1, player2) 
                # print(f'player1 MC141 : {player1}') 
                # print(f'player2 MC142 : {player2}') 
                # print(f'match MC143 : {match}') 
                # print(f'type(match) MC144 : {type(match)}') 
                # matches.append(match) 
                matches.append(Match_model(match)) 

        # print(f'dir(match) 
        # MC155 : {dir(match)}') 
        # print(f'matches MC150 : {matches}') 
        # print(f'type(matches[0]) MC151 : {type(matches[0])}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        serialized_matches = Match_model.serialize_matches(matches)  # serialize dans un for pour 1 seul objet ### 


        # rounds = [] 
        with open("utils/round.csv", "r") as r_file: 
            for r_line in r_file: 
                if r_line.startswith("round_name"): 
                    continue 

                round_name, round_matches, start_datetime, end_datetime = r_line.strip().split(";") 
                # rounds.append(Round_model(round_name, round_matches, start_datetime, end_datetime)) 
                # rounds.append(Round_model(round_name, matches, start_datetime, end_datetime)) 
                round = Round_model(round_name, matches, start_datetime, end_datetime) 
        print(f'round MC131 : {round}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        # print(f'serialized_matches MC164 : {serialized_matches}') 
        # print(f'type(serialized_matches) MC165 : {type(serialized_matches)}') 
        serialized_round = Round_model.serialize_round(round, serialized_matches) 


        # tournaments = [] 
        rounds = [] 
        with open("utils/tournaments.csv", "r") as t_file: 
            for t_line in t_file: 
                if t_line.startswith("name"): 
                    continue 

                # rounds or round ? ### 
                name, site, t_date, nb_rounds, players, duration, description = t_line.strip().split(";")  # rounds, 
                # print(f'rounds MC178 : {rounds}') 
                rounds.append(serialized_round) 
                # print(f'rounds MC180 : {rounds}') 
                # tournaments.append(Tournament_model(name, site, t_date, nb_rounds, rounds, players, duration, description)) 
                tournament = Tournament_model(name, site, t_date, nb_rounds, rounds, players, duration, description) 
        print(f'tournament MC131 : {tournament}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        Tournament_model.serialize_tournament(Tournament_model, tournament) 

        # Round_model.print_round(Round_model) 

        # print(f'\nTournament_model.tournament_obj C95 : \n{Tournament_model.tournament_x}') 

        # print(f'\ntournament_obj C95 : \n{Tournament_model.__str__(tournament_obj, roundDicts)}') 
        # print(f'\ntournament_obj C95 : \n{tournament_obj, tournamentDict, roundDicts}') 
        # print(f'\nTournament_model.tournament_x C70 : \n{Tournament_model.tournament_x}') 
        # print(f'type(Tournament_model.tournament_x) TM18 : {type(Tournament_model.tournament_x)}') 
        
        # print(f'\nRound_model.round_x C98 : \n{Round_model.round_x}') 
        # print(f'\nPlayer_model.player_x C99 : \n{Player_model.player_x}') 
        


    """ 
    tournament_obj C95 : 
    ( 
        <models.tournament_model.Tournament_model object at 0x00000226BD6CEA10>,  # --> tournament_obj 
        { 
            'name': 'Tournoi 1', 
            'site': 'lieu 1', 
            't_date': ['01/12/2022'], 
            'nb_rounds': 4, 
            'rounds': { 
                1: { 
                    'round_name': 'round 1', 
                    'round_matches': [ 
                        ([1, 0], [2, 0]), 
                        ([3, 0], [4, 0]), 
                        ([5, 0], [6, 0]), 
                        ([7, 0], [8, 0]) 
                    ], 
                    'start_datetime': '02/12/22 - 07:23', 
                    'end_datetime': '02/12/22 - 09:23' 
                }, 
                2: { 
                    'round_name': 'round 1', 
                    'round_matches': [ 
                        ([1, 0], [3, 0]), 
                        ([5, 0], [7, 0]), 
                        ([2, 0], [4, 0]), 
                        ([6, 0], [8, 0]) 
                    ], 
                    'start_datetime': '02/12/22 - 11:11', 
                    'end_datetime': '02/12/22 - 13:11' 
                }  
            }, 
            'players': { 
                1: 1, 
                2: 2, 
                3: 3, 
                4: 4, 
                5: 5, 
                6: 6, 
                7: 7, 
                8: 8 
            }, 
            'duration': 'blitz', 
            'description': 'Observations du directeur du tournoi.' 
        },                                                                         # --> tournamentDict 

        ( 
            { 
                1: { 
                    'round_name': 'round 1', 
                    'round_matches': [ 
                        ([1, 0], [2, 0]), 
                        ([3, 0], [4, 0]), 
                        ([5, 0], [6, 0]), 
                        ([7, 0], [8, 0]) 
                    ], 
                    'start_datetime': '02/12/22 - 07:23', 
                    'end_datetime': '02/12/22 - 09:23' 
                }, 
                2: { 
                    'round_name': 'round 1', 
                    'round_matches': [ 
                        ([1, 0], [3, 0]), 
                        ([5, 0], [7, 0]), 
                        ([2, 0], [4, 0]), 
                        ([6, 0], [8, 0]) 
                    ], 
                    'start_datetime': '02/12/22 - 11:11', 
                    'end_datetime': '02/12/22 - 13:11' 
                } 
            }, 
        )                                                                           # --> roundDicts 
    ) 


    """

    

    """ 
        tournamentDict = {
            'name': 'Tournoi 1', 
            'site': 'lieu 1', 
            't_date': ['01/12/2022',], 
            'nb_rounds': 4, 
            'rounds': {  ### comment intégrer l'objet Round ici ? 
                '1': [
                    (
                        [1, 0], [2, 0]
                    ), (
                        [3, 0], [4, 0]
                    ), (
                        [5, 0], [6, 0]
                    ), (
                        [7, 0], [8, 0]
                    ) 
                ], 
                '2': [
                    (
                        [1, 0], [2, 0]
                    ), (
                        [3, 0], [4, 0]
                    ), (
                        [5, 0], [6, 0]
                    ), (
                        [7, 0], [8, 0]
                    ) 
                ], 
                '3': [
                    (
                        [1, 0], [2, 0]
                    ), (
                        [3, 0], [4, 0]
                    ), (
                        [5, 0], [6, 0]
                    ), (
                        [7, 0], [8, 0]
                    ) 
                ], 
                '4': [
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
            }, 
            'players': {
                1: 1, 
                2: 2, 
                3: 3, 
                4: 4, 
                5: 5, 
                6: 6, 
                7: 7, 
                8: 8, 
            }, 
            'duration': 'blitz', 
            'description': 'Observations du directeur du tournoi.' 
        } 
    """


