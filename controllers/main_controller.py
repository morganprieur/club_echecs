
from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from models.player_model import Player_model 
from models.tournament_model import Tournament_model 
from models.round_model import Round_model 

from prompt_toolkit import PromptSession 
session = PromptSession() 


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
        self.round = None 


    def start(self, tourn): 
        # print("\nStart main controller") 

        if tourn == True: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_player() 

            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_tournament() 

            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_round() 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                return True 
            
            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                # print(self.board.ask_for_menu_action) 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 

            # print('control menu 2 : ', self.board.ask_for_report)    
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('alphabétique') 

            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('classement') 

            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisi run tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 
            
            if self.board.ask_for_report == '8': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_tournaments() 


            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 
            
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
                # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            return True 
        
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
            # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
            print('Fermeture de l\'application. Bonne fin de journée !') 

        return False 


    def enter_new_tournament(self): 
        print('\nEnter new tournament') 
        tournament_data = self.in_view.input_tournament() 
        self.tournament = Tournament_model(**tournament_data) 
        print(f'self.tournament MC59 : {self.tournament}') 
        self.tournament.serialize() 
    

    # def check_key(self, key, model, objs, sub_obj): 
    #     print(f'objs MC130 : {objs}') 
    #     for o in objs: 
    #         print(f'o MC132 : {o}') 
    #         keys = [] 
    #         # for k,v in o.items(): 
    #         #     keys.append(k) 
    #         keys.append(o) 
    #         if key not in keys: 
    #             objs['rounds'] = [] 
    #             self.obj = model(**objs) 
    #             # self.obj = model(**objs, sub_obj=[]) 
    #         else: 
    #             self.obj = model(**objs) 

    #         return self.obj 


    def report_tournaments(self): 
        self.board.ask_for_report = None 

        # print('\nTous les tournois : ') 
        tournaments = Tournament_model.get_registered_all('t_table') 
        tournaments_obj = [] 
        # self.check_key(tournaments, 'round', Tournament_model, rounds)  ### corriger ou remplacer 
        for tournament in tournaments: 
            keys = [] 
            for k,v in tournament.items(): 
                keys.append(k) 
            # print(f'keys MC93 : {keys}') 
            if "rounds" not in keys:  
                # print(f'tournament MC90 : {tournament}') 
                self.tournament = Tournament_model(**tournament, rounds=[]) 
            else: 
                # print(f'tournament MC95 : {self.tournament}') 
                # rounds = [Round_model(**round_data) for round_data in tournament.rounds]
                self.tournament = Tournament_model(**tournament) 
            self.rounds = self.tournament.rounds 
            # print(f'self.rounds MC167 : {self.rounds}') 
            rounds = [] 
            # print(f'tournament.rounds MC162 : {self.tournament.rounds}') 
            
            for round_data in self.tournament.rounds: 
                # print(f'round_data mC170 : {round_data}') 
                keys = [] 
                for k,v in round_data.items(): 
                    keys.append(k) 
                if 'tournament_id' not in keys: 
                    rounds.append(Round_model(**round_data, tournament_id=None)) 
                else: 
                    rounds.append(Round_model(**round_data)) 
            
            self.tournament.rounds = rounds
            tournaments_obj.append(self.tournament) 
        # self.check_key('tournaments', 'round', 'Tournament_model') 
        # print(f'len(tournaments_obj) MC181 : {len(tournaments_obj)}') 
        # print(f'tournaments_obj MC182 : {tournaments_obj}') 
        self.report_view.display_all_tournaments(tournaments_obj) 
        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    def select_one_tournament(self, t_id): 
        # Récupérer tous les <obj> dans la liste <objs> (liste de dicts) : 
        t_objs = Tournament_model.get_registered_all('t_table') 
        # Sélectionner le <objet> indiqué dans id (dict) 
        t_obj = t_objs[t_id] 
        return t_obj 


    def enter_new_player(self): 
        print('\nEnter new player') 
        player_data = self.in_view.input_player() 
        self.player = Player_model(**player_data) 
        # print(f'self.player MC65 : {self.player}') 
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

        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    def enter_new_round(self): 
        print('\nEnter new round') 
        round_data = self.in_view.input_round() 
        self.round = Round_model(**round_data) 
        print(f'Le round : {self.round} a bien été enregistré (MC233)') 
        # self.round.serialize() 
        if self.round.serialize() == False: 
            print('\n*** Le tournoi référencé dans "round" n\'existe pas, vous devez d\'abord le créer. ***') 
            self.start(False) 
        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    def report_rounds(self, ask_for_tournament_id): 
        
        tournament_id = int(ask_for_tournament_id)-1 
        # tournament object : 
        tournament = self.select_one_tournament(tournament_id) 
        # print(f'tournament MC246 : {tournament}') 

        data = [] 
        for t_data in tournament: 
            print(f't_data MC253 : {t_data}') 
            data.append(t_data) 
        
        # Instantiate the tournament ( --> object) : 
        if 'rounds' not in data: 
            self.tournament = Tournament_model(**tournament, rounds=[]) 
        else: 
            self.tournament = Tournament_model(**tournament) 
        # print(f'self.tournament MC262 : {self.tournament}') 

        ### ajouter check keys (à factoriser) ### 
        # self.check_key('round', Tournament_model, tournament, 'rounds') 
        rounds = [] 
        # Extract the rounds from the tournament (list od dicts) : 
        for round_data in tournament['rounds']: 
            # print(f'round_data MC267 : {round_data}') 
            keys = [] 
            for k,v in round_data.items(): 
                keys.append(k) 
            if 'tournament_id' not in keys: 
                rounds.append(Round_model(**round_data, tournament_id=None)) 
            else: 
                rounds.append(Round_model(**round_data)) 
        
        # print(f'rounds MC280 : {rounds}') 
        self.tournament.rounds = rounds 
        # print(f'self.tournament MC281 : {self.tournament}') 
        
        self.report_view.display_rounds_one_tournament(self.tournament) 

        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    


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





