
from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from models.player_model import Player_model 
from models.tournament_model import Tournament_model 


class Main_controller(): 

    def __init__( 
        self, 
        board: Dashboard_view, 
        in_view: Input_view, 
        report_view: Report_view 
    ): 
        self.board = board 
        self.in_view = in_view 
        self.report_view = report_view 
        self.tournament = None 
        # self.last_tournament = None 
        self.player = None 


    def start(self): 
        # print("\nStart main controller") 
        self.board.display_welcome() 
        self.board.display_first_menu() 

        if self.board.ask_for_menu_action == '1': 
            # menu "saisir" :
            self.board.register() 

            if self.board.ask_for_register == '1': 
                # saisir un joueur : 
                self.enter_new_player() 
            if self.board.ask_for_register == '2': 
                # saisir un joueur : 
                self.enter_new_tournament() 
            if self.board.ask_for_register == '*': 
                return True 
                # self.board.display_first_menu() 

        if self.board.ask_for_menu_action == '2': 
            # menu "afficher" : 
            self.board.report() 

            # print('control menu 2 : ', self.board.ask_for_report)    
            if self.board.ask_for_report == '1': 
                # afficher les joueurs : 
                self.report_players('alphabétique') 
            if self.board.ask_for_report == '2': 
                # afficher les joueurs : 
                self.report_players('classement') 
            if self.board.ask_for_report == '8': 
                # afficher les tournois : 
                self.report_tournament() 
            if self.board.ask_for_report == '*': 
                return True 
                # self.board.display_first_menu() 

        
        if self.board.ask_for_menu_action == '*': 
            return True 
            # self.board.display_first_menu() 

        return False 
            # if self.board.ask_for_menu_action == '1': 
            #     # menu "saisir" :
            #     self.board.register() 

            #     if self.board.ask_for_register == '1': 
            #         # saisir un joueur : 
            #         self.enter_new_player() 
            #     if self.board.ask_for_register == '2': 
            #         # saisir un joueur : 
            #         self.enter_new_tournament() 
            #     if self.board.ask_for_register == '*': 
            #         self.board.display_first_menu() 

            # if self.board.ask_for_menu_action == '2': 
            #     # menu "afficher" : 
            #     self.board.report() 

            #     # print('control menu 2 : ', self.board.ask_for_report)    
            #     if self.board.ask_for_report == '1': 
            #         # afficher les joueurs : 
            #         self.report_players('alphabétique') 
            #     if self.board.ask_for_report == '2': 
            #         # afficher les joueurs : 
            #         self.report_players('classement') 
            #     if self.board.ask_for_report == '8': 
            #         # afficher les tournois : 
            #         self.report_tournament() 
            #     if self.board.ask_for_report == '*': 
            #         self.board.display_first_menu() 

        # print(f'ask_for_menu_action : {self.board.ask_for_menu_action}') 


    def enter_new_tournament(self): 
        print('\nEnter new tournament') 
        tournament_data = self.in_view.input_tournament() 
        self.tournament = Tournament_model(**tournament_data) 
        print(f'self.tournament MC59 : {self.tournament}') 
        self.tournament.serialize() 
    
    def report_tournament(self): 
        print('\nTous les tournois : ') 
        tournaments = Tournament_model.get_registered_all('t_table') 
        tournaments_obj = [] 
        for tournament in tournaments: 
            self.tournament = Tournament_model(**tournament) 
            tournaments_obj.append(self.tournament) 
        self.report_view.display_all_tournaments(tournaments_obj) 


    def enter_new_player(self): 
        print('\nEnter new player') 
        player_data = self.in_view.input_player() 
        self.player = Player_model(**player_data) 
        print(f'self.player MC65 : {self.player}') 
        self.player.serialize() 


    def report_players(self, sort): 
        players = Player_model.get_registered_all('p_table') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 
        
        if sort == 'alphabétique': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.report_view.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'classement': 
            print('\nJoueurs par classement : ') 
            self.report_view.sort_objects_by_field(players_obj, 'rank') 


    
    


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


