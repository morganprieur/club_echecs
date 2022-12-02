



from models.tournament_model import Tournament_model 
from models.round_model import Round_model 


class Main_controller(): 
    
    def start(): 

        print('start main controller') 

        roundDict = { 
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
        } 

        tournamentDict = {
            'name': 'Tournoi 1', 
            'site': 'lieu 1', 
            't_date': ['01/12/2022',], 
            'nb_rounds': 4, 
            'rounds': roundDict, ### comment intégrer l'objet Round ici ? 
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

        Tournament_model.instantiate_tournoi(Tournament_model, tournamentDict, roundDict) 
        Tournament_model.serialize_tournament(Tournament_model) 

        Round_model.instantiate_round(Round_model, roundDict) 

        # Round_model.print_round(Round_model) 

        print(f'\nTournament_model.tournament_x C104 : \n{Tournament_model.tournament_x}') 
        # print(f'type(Tournament_model.tournament_x) TM18 : {type(Tournament_model.tournament_x)}') 
        print(f'\nRound_model.round_x C106 : \n{Round_model.round_x}') 


    

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


