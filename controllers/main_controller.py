
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

        # check key 'rounds' 
        keys = [] 
        for t in tournament_data: 
            # print(f't MC128 : {t}') 
            keys.append(t) 
        if 'rounds' not in keys: 
            self.tournament.rounds = rounds=[] 
        self.tournament = Tournament_model(**tournament_data) 
        # print(f'self.tournament MC134 : {self.tournament}') 
        print(f'\nLe round {self.round} a bien été enregistré') 
        self.tournament.serialize() 

        continuer = session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 
    

    def report_tournaments(self): 
        self.board.ask_for_report = None 

        # print('\nTous les tournois : ') 
        tournaments = Tournament_model.get_registered_all('t_table') 
        tournaments_obj = [] 
        
        list_tournements = self.check_key('rounds', Tournament_model, tournaments) 
        for tournament in list_tournements: 
            # print(f'tournament MC176 : {tournament}') 
            # print(f'type(tournament) MC177 : {type(tournament)}') 
            self.tournament = tournament
            # print(f'self.tournament MC179 : {self.tournament}') 
            tournaments_obj.append(self.tournament) 
        self.report_view.display_all_tournaments(tournaments_obj) 

        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


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
        # Get the previous round's id, to define the current round's id: 
        # Get the data for the current round: 
        round_data = self.in_view.input_round() 
        print(f'\nround_data MC193 : {round_data}') 
        # Get the tournament where to register the current round: 
        tournament = self.select_one_tournament(round_data['tournament_id']-1) 
        print(f'tournament["rounds"] MC196 : {tournament["rounds"]}') 
        
        if tournament['rounds'] == []: 
            round_data['id'] = 1 
            # print(f'round_data["id"] MC204 : {round_data["id"]}') 
        else: 
            round_data['id'] = int(tournament['rounds'].pop()['id'])+1 
            # print(f'round_data["id"] MC201 : {round_data["id"]}') 
        # print(f'round_data["id"] MC205 : {round_data["id"]}') 
        self.round = Round_model(**round_data) 
        print(f'\nself.round MC201 : {self.round}') 
        if self.round.serialize() == False: 
            print('\n*** Le tournoi référencé dans "round" n\'existe pas, vous devez d\'abord le créer. ***') 
            self.start(False) 
        else: 
            print(f'\nLe round {self.round} a bien été enregistré') 
            self.report_rounds(tournament['id']) 
    
        continuer = session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 


    def report_rounds(self, ask_for_tournament_id): 
        
        tournament_id = int(ask_for_tournament_id)-1 
        # tournament object : 
        tournament = self.select_one_tournament(tournament_id) 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds=[] 
        # Instantiate the tournament ( --> object) : 
        self.tournament = Tournament_model(**tournament) 
        # print(f'type(self.tournament) MC215 : {type(self.tournament)}') 
        
        # Extract the rounds from the tournament (list of objects) : 
        # print(f'self.tournament.rounds MC229 : {self.tournament.rounds}') 
        rounds = self.tournament.rounds 
        # print(f'rounds MC232 : {rounds}') 

        self.report_view.display_rounds_one_tournament(self.tournament) 

        # continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        # self.start(False) 

    
    # =================== UTILS =================== # 
    
    def check_key(self, key, model, objs): 
        # print(f'objs MC142 : {objs}')
        list_objs = []
        for data in objs: 
            # print(f'data MC145 : {data}') 
            if key not in data.keys():  
                data[key] = []  
            list_objs.append(model(**data)) 

        return list_objs 


    def select_one_tournament(self, t_id): 
        # Récupérer tous les <obj> dans la liste <objs> (liste de dicts) : 
        t_objs = Tournament_model.get_registered_all('t_table') 
        # Sélectionner le <objet> indiqué dans id (dict)  # -1 : pas eu ce problème auparavant 
        t_obj = t_objs[t_id]  # -1  ### 
        return t_obj 


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





