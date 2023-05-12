
from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from datetime import datetime, date 
from operator import attrgetter 
from prompt_toolkit import PromptSession 
session = PromptSession() 
import random 
import re 




class Main_controller(): 

    def __init__( 
        self, 
        board: Dashboard_view, 
        in_view: Input_view, 
        report_view: Report_view, 
    ): 
        self.board = board 
        self.in_view = in_view 
        self.report_view = report_view 
        self.tournament = None 
        self.player = None 
        self.round = None 


    def start(self, tourn): 
        """ Displays the menus 

        Args:
            tourn (boolean): if True -> display the menu and the welcome message, 
                            else -> displays only the menu. 
        """ 
        # print("\nStart main controller") 

        if tourn == True: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        #### ======== "R E G I S T E R"  M E N U S ======== #### 


        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            # Enregistrer un joueur  # à corriger  
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_player() 

            # # Enregistrer plusieurs joueurs  # TODO 
            # if self.board.ask_for_register == '2': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_many_new_players() 

            # Enregistrer un nouveau tournoi #TODO 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_tournament() 

            # Enregistrer les scores  # TODO 
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.enter_scores() 

            # # auto quand on cloture un round et que c'est le 4è round 
            # if self.board.ask_for_register == '4':  # TODO 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.close_tournament() 

            # # auto + génération des matches quand on cloture un round 
            # et que c'est PAS le 4è round 
            # if self.board.ask_for_register == '5': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_new_round() 

            # # auto quand on rentre les scores des matches d'un round 
            # if self.board.ask_for_register == '6':  # TODO 
            #     self.board.ask_for_register = None 
            #     self.close_round() 
            #     # set end_datetime 
            #     # if round.id == 1: 
            #     #    define_matches(first=True) 
            #     # elif round.id = 4: 
            #     #    call close_tournament() 
            #     # else: 
            #     # define_matches(first=False) 
            #     # self.enter_new_matches() 

            # # auto quand on enregistre les scores des matches 
            # if self.board.ask_for_register == '7': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_new_matches() 


            #### ============ COMMANDES DE SECOURS ============ #### 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                return True 

            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                # print(self.board.ask_for_menu_action) 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        #### ======== "R E P O R T"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 

            # Tous les joueurs par ordre alphabétique 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('firstname', True)  # finished 

            # Tous les joueurs par nombre de points 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('score', True)  # finished 

            # Tous les tournois 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_tournaments() 

            # Nom et dates d'un tournoi 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_name_date_tournament() 

            # Les joueurs du tournoi par ordre alphabétique 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.players_from_tournament_alphabetical_order() 

            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 

            # # pas demandé 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les matches ? ') 
                self.report_matches(ask_for_tournament_id) 


            #### ======== T E S T  M E N U S ======== #### 

            if self.board.ask_for_report == '9': 
                self.board.ask_for_report = None 
                # Tester define_first_round : 
                self.define_first_round() 

            if self.board.ask_for_report == '10': 
                self.board.ask_for_report = None 
                # Tester define_next_round : 
                self.define_next_rounds() 

            """ Command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        #### ============ COMMANDES DE SECOURS ============ #### 

        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            return True 

        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
            # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
            print('Fermeture de l\'application. Bonne fin de journée !') 

        return False 


    #### ============ P L A Y E R S ============ #### 

    """ Register one player """  # ok 230507 
    def enter_new_player(self): 
        print('\nEnter new player') 
        new_player_data = self.in_view.input_player() 
        last_player_dict = Player_model.get_registered_dict('players')[-1] 
        # print(f'\nlast_player_dict MC221 : {last_player_dict}') 
        last_player_id = int(last_player_dict['id']) 
        # print(f'\nlast_player_id MC223 : {last_player_id}') 
        new_player_data['id'] = int(last_player_id) + 1 
        new_player_data['global_score'] = float(0.0) 
        # print(f'\nnew_player_data MC226 : {new_player_data}')   
        self.player = Player_model(**new_player_data) 
        # print(f'self.player MC228 : {self.player}') 
        self.player.serialize_object(True) 

        self.report_players('firstname', True)  # finished 


    """ TODO """ 
    def enter_many_new_players(self): 
        pass 


    """ Display all the players """  # ok 230505 
    def report_players(self, sort, finished): 
        print('report_players MC239') 
        # players = Player_model.get_registered_all('players') 
        players = Player_model.get_registered_dict('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        # Choice of the order (alphabetical or by score): 
        if sort == 'alphabet': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'global_score') 
        self.report_view.display_all_players(players_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        if finished == 'yes': 
            self.start(False) 
        

    #### ============ T O U R N A M E N T S ============ #### 
    
    """ Create one tournament """ 
    ### TODO: 
    # - set the 1st empty round 
    # - define the first matches 
    # - register the first matches with scores = 0 
    def enter_new_tournament(self): 
        print('\nEnter new tournament') 

        # Display registered players to select the current ones: 
        print('Voici les joueurs enregistrés : ') 
        self.report_players('alphabet', False)  ### finished 

        # # Prompt if needed to regsiter a new player  ###TODO 
        # player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
        # # If yes : 
        # if player_needed == 'y': 
        #     self.enter_new_player()  # ok 230507 

        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 
        
        self.tournament_data['players'] = [int(player) for player in re.findall(r'\d', self.tournament_data['players'])] 
        # tournament_data['players'] = [player for player in tournament_data['players'].split(',')]  # list of str 
        print(f'self.tournament_data MC292 : {self.tournament_data}') 

        # Set the next id to the current tournament: 
        all_tournaments = Tournament_model.get_registered_dict('tournaments') 
        last_tournament = all_tournaments.pop() 
        print(f'last_tournament MC297 : {last_tournament}') 
        self.tournament_data['id'] = int(last_tournament['id']) + 1 
        print(f'self.tournament_data MC299 : {self.tournament_data}')  # id ok 

        # Set 'rounds' = [] 
        if 'rounds' not in self.tournament_data.keys(): 
            self.tournament_data['rounds'] = [] 
        
        self.enter_new_round() 
        # Check self.round_object 
        print(f'self.round_object MC308 : {self.round_object}') 

        self.tournament_data['rounds'].append(self.round_object) 
        print(f'self.tournament_data MC310 : {self.tournament_data}') 

        # Instantiate the current tournament: 
        self.tournament = Tournament_model(**self.tournament_data) 

        if self.tournament.serialize_object(True) == False: 
            print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
        else: 
            print(f'\nLe tournoi {self.tournament} a bien été enregistré') 

        self.report_tournaments() 

        session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 



    """ comment """ 
    def report_tournaments(self): 
        # self.board.ask_for_report = None 

        tournaments = Tournament_model.get_registered_dict(('tournaments')) 
        tournaments_obj = [] 

        for tournament in tournaments: 
            if 'rounds' not in tournament.keys(): 
                tournament['rounds'] = [] 
            # for round in tournament['rounds']: 
                # self.report_one_round(round)  # 230425 
                # pass 
                # print(f'round MC351 : {round}') 

                # round_id = tournament['rounds'].index(round) 
                # if 'matches' not in tournament['rounds'][round_id].keys(): 
                #     tournament['rounds'][round_id] = [] 
            # print(f'tournament MC356 : {tournament}') 
            self.tournament = Tournament_model(**tournament) 
            # print(f'self.tournament MC358 : {self.tournament}') 
            tournaments_obj.append(self.tournament) 
        
        self.report_view.display_all_tournaments(tournaments_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    #### ============ R O U N D S ============ #### 

    ###TODO ajouter close_precedent_round() et close_current_tournament() 
    """ auto (when register_scores or register_new_tournament)""" 
    def enter_new_round(self): 
        print('\nEnter new round') 

        # Check the data 
        print(f'\nself.tournament_data MC317 : {self.tournament_data}') 

        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 
        print(f'\nround_data MC321 : {round_data}') 
        
        round_data['start_datetime'] = str(datetime.now()) 
        round_data['tournament_id'] = self.tournament_data['id'] 

        # Check the data 
        print(f'self.tournament_data["rounds"] MC327 : {self.tournament_data["rounds"]}') 
        
        # Get the last round's id and attribute the id to the current round: 
        if self.tournament_data['rounds'] == []: 
            round_data['id'] = 1 
            self.define_matches(True) 
        else: ### à corriger ? ### 
            round_data['id'] = int(self.tournament_data['rounds'][-1]['id']) + 1 
            print(f'self.tournament_data["rounds"] MC323 : {self.tournament_data["rounds"]}') 
            # If the round isn't the first one of the tournament 
            #     -> register the end_datetime of the precedent round ###TODO 
            # self.add_ending_round() 
            self.define_matches(False) 
            
        # check the data 
        print(f'self.matches_objects MC342 : {self.matches_objects}') 

        round_data['matches'] = self.matches_objects 
        print(f'round_data["matches"] MC349 : {round_data["matches"]}') 

        # Instantiate the courrent round 
        self.round_object = Round_model(**round_data) 
        print(f'self.round_object MC353 : {self.round_object}') 

        return self.round_object 



    #### ============ U T I L S ============ #### 

    """ Sort objects by field arg """  # ok 
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        print(f'objects MC655 : ') 
        for obj in objects: 
            print(obj.__str__()) 
        return objects 

    """ comment """  # à corriger ### 
    # def define_first_round(self): 
    def define_matches(self, first):  ### 0511-1931 
        """ Select the players' ids witch will play against each other during the first round. """ 
        # We have already self.tournament_data 
        print(f'\nself.tournament_data MC6358 : {self.tournament_data}') 
        players = self.tournament_data['players'] 
        
        # Copy the players list to work with 
        players_copy = list(players) 
        # Instantiate the players : 
        self.players = [] 
        for p in players_copy: 
            player = Player_model(**p) 
            self.players.append(player) 
        print(f"\nself.players objects MC371 : {self.players}") 

        # matches to store into the current round 
        self.matches = [] 

        # Randomly define the pairs of players for 4 matches 
        # if first != True: call the sort_objects_by_field() function 
        print(f"\nfirst MC374 : {first}") 
        if first != True: 
            sorted_players_by_scores = self.sort_objects_by_field(players_copy, 'global_score') 
            self.random_matches(sorted_players_by_scores)  # returns matches 
        else: 
            self.random_matches(sorted_players_by_scores)  # returns matches 
        # Check the matches 
        print(f'\nself.matches MC385 : {self.matches}') 
        
        # Instantiate the matches 
        self.matches_objects = [] 
        for m in self.matches: 
            match = Match_model(**m) 
            self.matches_objects.append(match) 
        print(f'\nself.matches_objectss MC393 : {self.matches_objects}') 
        
        return self.matches_objects 


    """ Random define the pairs of players into each round """  # à corriger ### 
    def random_matches(self, players_copy): 
        """ Select the players' ids for one match. 
            Args:
                players (list): the list of the players' ids of the last tournament. 
                matches (list): the list of the selected players' ids for the round. 
            Returns:
                list: the list of the selected players' ids, added the new selected ones. 
        """ 
        for i in range(int(4)): 
            # score = the score at the start of the round (for the first round : 0) 
            score = float(0)  
            # match = the tuple containing 2 lists 'selected_player' 
            match = ([], []) 
            # selected = the list of player's id and player's score 
            selected = [] 
            for i in range(int(2)): 
                print(f'\nplayers_copy MC729 : {players_copy}') 
                # choice = the randomly chosen player's id 
                chosen = random.choice(players_copy) 
                selected.append(chosen) 
                players_copy.remove(chosen[-1]) 
                print(f'\nplayers_copy MC411 : {players_copy}') 
                print(f'\nchosen MC412 : {chosen}') 
                print(f'\nchosen MC413 : {selected}') 
            match = ([selected[0], score], [selected[1], score]) 
            print(f'\nmatch MC415 : {match}') 
            self.matches.append(match) 
        print(f'\nself.matches MC417 : {self.matches}') 
        return self.matches 




