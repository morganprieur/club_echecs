
from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from models.player_model import Player_model 
from models.tournament_model import Tournament_model 
from models.round_model import Round_model 
from models.match_model import Match_model 

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
            
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_match() 

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
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 

            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les matches ? ') 
                # afficher les matches : 
                # self.board.ask_for_tournament_id 
                self.report_matches(ask_for_tournament_id) 
            
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
        
        # Get the data for the current tournament: 
        tournament_data = self.in_view.input_tournament() 

        # Get all the registered tournaments: 
        tournaments = Tournament_model.get_registered_all('t_table') 
        last_tournament = tournaments.pop() 
        # print(f'last_tournament MC128 : {last_tournament}') 

        # Attribute the id to the current tournament: 
        tournament_data['id'] = int(last_tournament['id'])+1 
        # print(f'tournament_data MC130 : {tournament_data}') 
        
        # check key 'rounds' 
        if 'rounds' not in tournament_data.keys(): 
            tournament_data['rounds'] = [] 

        # Instantiate the current tournament: 
        self.tournament = Tournament_model(**tournament_data) 

        # print(f'self.tournament MC134 : {self.tournament}') 
        if self.tournament.serialize() == False: 
            print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
        else: 
            print(f'\nLe tournoi {self.tournament} a bien été enregistré') 

        continuer = session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 
    

    def report_tournaments(self): 
        self.board.ask_for_report = None 

        # print('\nTous les tournois : ') 
        tournaments = Tournament_model.get_registered_all('t_table') 
        tournaments_obj = [] 
        
        # list_tournements = self.check_key('rounds', Tournament_model, tournaments) 

        for tournament in tournaments: 
            if 'rounds' not in tournaments.keys(): 
                tournament['rounds'] = [] 
            for round in tournament['rounds']: 
                if 'matches' not in tournament['rounds'].keys(): 
                    tournament['rounds']['matches'] = [] 
            self.tournament = Tournament_model(**tournament) 
            # print(f'tournament MC176 : {tournament}') 
            # print(f'type(tournament) MC177 : {type(tournament)}') 
            print(f'self.tournament MC183 : {self.tournament}') 
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

        # Get the data for the current round: 
        round_data = self.in_view.input_round() 
        # print(f'\nround_data MC193 : {round_data}') 

        # Get the tournament where to register the current round: 
        tournament = self.select_one_tournament(round_data['tournament_id']-1) 
        # print(f'tournament["rounds"] MC196 : {tournament["rounds"]}') 
        
        # Get the round's id and attribute the id to the current round: 
        if tournament['rounds'] == []: 
            round_data['id'] = 1 
        else: 
            round_data['id'] = int(tournament['rounds'].pop()['id'])+1 
        
        if 'matches' not in round_data.keys(): 
            round_data['matches'] = [] 
        self.round = Round_model(**round_data) 
        # print(f'\nself.round MC201 : {self.round}') 

        # Register the round: 
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
            tournament.rounds = [] 
        print(f'tournament MC262 : {tournament}')  # matches ok 
        print(f'tournament["rounds"] MC263 : {tournament["rounds"]}')  # matches ok 

        for round in tournament['rounds']: 
            print(f'round MC266 : {round}') 
            if 'matches' not in round.keys(): 
                round['matches'] = [] 

            print(f'round["matches"] MC270 : {round["matches"]}') 

            matches = round['matches'] 
            for match in matches: 
                match_tuple = tuple(match) 
                print(f'match_tuple MC274 : {match_tuple}')  # ok 
                print(f'type(match_tuple) MC275 : {type(match_tuple)}')  # ok 
                print(f'matches[0] MC276 : {matches[0]}')  # matches[0] ok  
                # https://stackoverflow.com/questions/15721363/preserve-python-tuples-with-json 
                self.match = Match_model(**match_tuple)  # TypeError: models.match_model.Match_model() argument after ** must be a mapping, not list ### 
                print(f'self.match MC280 : {self.match}') 
                # matches.append(self.match) 
            self.round = Round_model(**round) 
            print(f'self.round MC283 : {self.round}') 
            # rounds.append(self.round) 

        # Instantiate the tournament ( --> object) : 
        self.tournament = Tournament_model(**tournament) 
        # print(f'type(self.tournament) MC273 : {type(self.tournament)}') 
        print(f'self.tournament MC286 : {self.tournament}') 
        # print(f'self.tournament.rounds.matches MC276 : {self.tournament.rounds.matches}') 

        # Extract the rounds from the tournament (list of objects) : 
        # print(f'self.tournament.rounds MC229 : {self.tournament.rounds}') 
        rounds = self.tournament.rounds 
        # print(f'rounds MC232 : {rounds}') 
        matches = self.round.matches 

        self.report_view.display_rounds_one_tournament(self.tournament) 

        continuer = session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    def enter_new_match(self): 
        print('\nEnter new match') 

        # Get the data for the current match: 
        match_data = self.in_view.input_match() 
        print(f'\nmatch_data MC284 : {match_data}')  # ok 

        # Get the (last) tournament where to register the current round: 
        tournaments = Tournament_model.get_registered_all('t_table') 
        # current_tournament = len(tournaments)-1 
        current_tournament = tournaments.pop() 
        print(f'current_tournament MC290 : {current_tournament}')  # ok 
        print(f'type(current_tournament) MC291 : {type(current_tournament)}')  # dict 
        
        # Get the last round, where to register the match 
        if not (current_tournament['rounds']): 
            # print(f'current_tournament["rounds"] MC295 : {current_tournament["rounds"]}') 
            # current_round = {} 
            # current_round['matches'] = [] 
            print(f'Il faut d\'abord enregistrer un round.') 
        else: 
            print('MC300') 
            current_round = current_tournament['rounds'].pop() 
            if 'matches' not in current_round.keys(): 
                current_round['matches'] = [] 
            # self.round = Round_model(**current_round) 
            print(f'current_round MC300 : {current_round}') 
            print(f'type(current_round) MC301 : {type(current_round)}') 
        
        # Get the match's id and attribute the id to the current match: 
        # if current_round['matches'] == []: 
        #     match_data['id'] = 1 
        # else: 
            # round_data['id'] = int(tournament['rounds'].pop()['id'])+1 
            # print(f"current_round['matches'].pop() MC333 : {current_round['matches'].pop()}")
            # match_data['id'] = int(current_round['matches'].pop()['id'])+1 
        self.match = Match_model(**match_data) 
        print(f'\nself.match MC336 : {self.match}') 
        print(f'\type(self.match) MC337 : {type(self.match)}') 

        # Instantiate the round : 
        self.round = Round_model(**current_round) 
        print(f'\self.round MC341 : {self.round}') 
        # Instantiate the tournament : 
        self.tournament = Tournament_model(**current_tournament) 
        print(f'\self.tournament MC344 : {self.tournament}') 

        # Register the match: 
        if self.match.serialize() == False: 
            print('\n*** Le round référencé dans "match" n\'existe pas, vous devez d\'abord le créer. ***') 
            self.start(False) 
        else: 
            print(f'\nLe match {self.match} a bien été enregistré') 
            # self.report_matches(current_tournament.id) 
        # ==== 
        continuer = session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 


    def report_matches(self, ask_for_tournament_id): 
        tournament_id = int(ask_for_tournament_id)-1 
        # tournament object : 
        tournament = self.select_one_tournament(tournament_id) 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds = [] 
        self.tournament = Tournament_model(**tournament) 
        print(f'self.tournament MC290 : {self.tournament}') 

        rounds = self.tournament.rounds 
        print(f'rounds MC293 : {rounds}') 

        self.report_view.display_matches_one_tournament(self.tournament) 

        continuer = session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 




    
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

        •X Liste de tous les joueurs:
            ◦X par ordre alphabétique ;
            ◦X par classement.
        • Liste de tous les joueurs d'un tournoi :
            ◦ par ordre alphabétique ;
            ◦ par classement.
        •X Liste de tous les tournois.
        •X Liste de tous les tours d'un tournoi.
        • Liste de tous les matchs d'un tournoi.

    Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
    """ 





