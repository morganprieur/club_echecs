



from models.tournament_model import Tournament_model 
from models.round_model import Round_model 
from models.match_model import Match_model 
from models.player_model import Player_model 


class Main_controller(): 
    
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
        with open("utils/players.csv", "r") as file:
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

        # Player_model.instantiate_player(Player_model, players) 
        Player_model.serialize_multi_players(players) 
        

        matches = [] 
        player1 = [] 
        player2 = [] 
        players = [] 
        match = tuple 
        print(f'type(match) MC148 : {type(match)}') 
        with open("utils/matches.csv", "r") as m_file: 
            for m_line in m_file: 
                if m_line.startswith("player1"): 
                    continue 

                player1, player2 = m_line.strip().split(";") 
                match = (player1, player2) 
                print(f'player1 MC151 : {player1}') 
                print(f'player2 MC152 : {player2}') 
                print(f'match MC153 : {match}') 
                print(f'type(match) MC153 : {type(match)}') 
                matches.append(Match_model(match)) 

        print(f'matches MC149 : {matches}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        Match_model.serialize_match(matches) 


        rounds = [] 
        with open("utils/rounds.csv", "r") as r_file: 
            for r_line in r_file: 
                if r_line.startswith("round_name"): 
                    continue 

                round_name, round_matches, start_datetime, end_datetime = r_line.strip().split(";") 
                rounds.append(Round_model(round_name, round_matches, start_datetime, end_datetime)) 
        print(f'rounds MC131 : {rounds}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        Round_model.serialize_round(rounds) 


        tournaments = [] 
        with open("utils/tournaments.csv", "r") as t_file: 
            for t_line in t_file: 
                if t_line.startswith("name"): 
                    continue 

                name, site, t_date, nb_rounds, rounds, players, duration, description = t_line.strip().split(";") 
                tournaments.append(Tournament_model(name, site, t_date, nb_rounds, rounds, players, duration, description)) 
        print(f'tournaments MC131 : {tournaments}') 

        # Tournament_model.instantiate_tournament(Tournament_model, tournaments, roundDicts) 
        # Tournament_model.serialize_tournament(Tournament_model) 
        Tournament_model.serialize_tournament(tournaments) 

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


