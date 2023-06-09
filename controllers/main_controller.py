
from controllers import define_matches 
# import define_matches 

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
# import random 
import re 


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
        self.player = None 
        self.round = None 


    def start(self, new_session=False): 
        """ Displays the menus 
        Args:
            new_session (boolean): if True -> displays the menu and the welcome message, 
                            else -> displays only the menu. 
        """ 
        # print("\nStart main controller") 

        if new_session == True: 
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

            # # Enregistrer plusieurs joueurs  # TODO: à vérifier 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_many_new_players() 

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
            
            ### 50 : Mettre à jour les scores des joueurs # TEST  
            if self.board.ask_for_register == '50': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.update_players_local_scores()  

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
            #     #    enter_new_matches(first=True) 
            #     # elif round.id = 4: 
            #     #    call close_tournament() 
            #     # else: 
            #     # enter_new_matches(first=False) 
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
                self.close_the_app() 

        #### ======== "R E P O R T"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 

            # Tous les joueurs par ordre alphabétique 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_all_players('firstname') 
                self.start(False) 

            # Tous les joueurs par nombre de points 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_all_players('score') 
                self.start(False) 

            # Tous les tournois 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_tournaments() 
                self.start(False) 

            # Nom et dates d'un tournoi # TODO: à vérifier 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 
                # afficher le tournoi : 
                tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? (son id ou "last" pour le dernier) ') 
                tournament = self.select_one_tournament(tournament_id) 
                Report_view.report_name_date_tournament(tournament) # TODO: à vérifier 

                self.start(False) 

            # Les joueurs d'un tournoi par ordre alphabétique # TODO: à vérifier  
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 

                # afficher les tournois : 
                tournament_id = session.prompt('De quel tournoi voulez-vous les joueurs ? (son id ou "last" pour le dernier) ') 
                tournament = self.select_one_tournament(tournament_id) 
                
                sort = session.prompt('Ordre d\'enregistrement : "1", alphabetique : "2", ou par classement : "3" ? ') 
                self.report_players_from_tournament(sort, tournament_id) # TODO: à vérifier 

                self.start(False) 


            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? (son id ou "last" pour le dernier) ') 
                # afficher les tours : 
                self.report_rounds(ask_for_tournament_id) # TODO: à vérifier 

                self.start(False) 

            # # pas demandé 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les matches ?  (son id ou "last" pour le dernier)') 
                self.report_matches(ask_for_tournament_id) 


            #### ======== T E S T  M E N U S ======== #### 

            if self.board.ask_for_report == '9': 
                self.board.ask_for_report = None 
                # Tester define_first_round : 
                self.define_first_round() 
                self.start(False) 

            if self.board.ask_for_report == '10': 
                self.board.ask_for_report = None 
                # Tester define_next_round : 
                self.define_next_rounds() 
                self.start(False) 

            """ Emergency command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                self.close_the_app() 

        #### ============ COMMANDES DE SECOURS ============ #### 

        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            return True 

        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            self.close_the_app() 

        return False 


    """ Command to quit the application """ 
    def close_the_app(): 
        print('Fermeture de l\'application. Bonne fin de journée !') 
    

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
        new_player_data['local_score'] = float(0.0) 
        new_player_data['global_score'] = float(0.0) 
        new_player_data['match_score'] = float(0.0) 
        # print(f'\nnew_player_data MC226 : {new_player_data}')   
        self.player = Player_model(**new_player_data) 
        # print(f'self.player MC228 : {self.player}') 
        self.player.serialize_object(True) 

        self.report_all_players('firstname', True)  # finished 

    """ TODO: à vérifier """ 
    def enter_many_new_players(self): 
        """ 
            Calls the `enter_new_player` more than one time. 
        """ 
        while(True): 
            self.enter_new_player() 
            # Prompt if needed to regsiter another new player 
            player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
            if player_needed == 'y': 
                return True 
            else: 
                return False 

    """ Display all the players """  # ok 230505 # 
    def report_all_players(self, sort): # , finished retiré 
        """ 
            Displays the players from players.json. 
            parameters: 
                sort (str): 'id', 'firstname' or 'local_score', the name of the field on wich to sort the players. 
        """ 
        print('report_all_players MC239') 
        # players = Player_model.get_registered_all('players') 
        players = Player_model.get_registered_dict('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        # Choice of the order ('firstname' -> alphabetical or 'local_score' -> by score): 
        if sort == 'id': 
            print('\nJoueurs par ordre d\'enregistrement : ') 
            self.sort_objects_by_field(players_obj, 'id') 
        if sort == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'local_score') 
        self.report_view.display_players(players_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        # if finished == True: 
        #     self.start(False) 
    
    """ comment """ 
    def report_players_from_tournament(self, sort, tournament_id): # , finished 
        tournament_dict = self.select_one_tournament(tournament_id) 
        tournament_obj = Tournament_model(**tournament_dict) 
        players_obj = tournament_obj.players 

        # Choice of the order (alphabetical or by score): 
        if sort == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'local_score') 
        
        self.report_view.display_players(players_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        # if finished == True: 
        #     self.start(False)  

    """ comment """ 
    def report_one_player(self, player_id): # , finished 
        self.select_one_player(player_id) 
        session.prompt('\nAppuyer sur Entrée pour continuer ') 
        # if finished: 
        #     self.start(False) 


         
    ### 230515 
    """ Update the local_scores of the players (json) """ 
    def update_players_local_scores(self): 
        """ Update the scores into the players.json file. 
        """ 
        # Select the scores of each player into the current match 
        last_tournament = self.select_one_tournament('last') 
        # Try to instantiate the last tournament 
        last_tournament_obj = Tournament_model(**last_tournament) 
        # last_round = last_tournament['rounds'].pop() 
        last_round = last_tournament_obj.rounds.pop() 
        print(f'\nlast_round MC350 : {last_round}') # input_data 
        # print(f'\ntype(last_round) MC351 : {type(last_round)}') 
        # Select players local_scores 
        p_dicts = Player_model.get_registered_dict('players') 
        # Try to instantiate the players 
        players_obj = [Player_model(**data) for data in p_dicts] 
        for player_obj in players_obj: 
            ### à vérifier (ternaire) 
            # player_last_score = player_obj.global_score if score=='global' else player_obj.local_score 
            player_last_score = player_obj.local_score 
            for match in last_round.matches: 
                if match[0][0] == player_obj.id: 
                    player_input_score = match[0][1] 
                    print(f'\nplayer_input_score MC363 : {player_input_score}') # input score 
                    player_last_score += player_input_score 
                    player_obj.local_score = player_last_score 
                elif match[1][0] == player_obj.id: 
                    player_input_score = match[1][1] 
                    print(f'\nplayer_input_score MC368 : {player_input_score}') # input score 
                    player_last_score += player_input_score 
                    player_obj.local_score = player_last_score 
            print(f'\nplayer_obj MC365 : {player_obj}') 

            # Register the new scores into players.json ### à vérifier 
            if player_obj.serialize_object(False): 
            # if Player_model.serialize_object(False): 
                print(f'\nLe nouveau score du joueur {player_obj.firstname} {player_obj.lastname} a bien été enregistré. ') 
                # print(f'\nLe nouveau score ({self.score}) du joueur {player_obj.firstname} {player_obj.lastname} a bien été enregistré. ') 
                # self.report_players()  
                # self.report_players_from_tournament('firstname', False, 'last')  
    

    def set_players_scores_to_zero(self):  # à vérifier 
        players_dicts = Player_model.get_registered_dict('players') 
        players_objs = [Player_model(**player_dict) for player_dict in players_dicts] # à vérifier 

        for player_obj in players_objs: 
            player_obj.global_score += player_obj.local_score 
            player_obj.local_score = float(0) 
    
            player_updated = Player_model.serialize_object(False) 
            # self.report_one_player(player_obj.id, False) 
        self.report_all_players('id') 


    #### ============ T O U R N A M E N T S ============ #### 
    
    """ Create one tournament """ 
    ### TODO: 
    # - set the 1st empty round 
    # - define the first matches 
    # - register the first matches with scores = 0 
    def enter_new_tournament(self): 
        print('\nEnter new tournament') 

        self.set_players_scores_to_zero() 
        session.prompt('Appuyer sur Entrée pour continuer ') 

        # Display registered players to select the current ones: 
        print('Voici les joueurs enregistrés : ') 
        self.report_all_players('id', False)  ### finished: False 
        session.prompt('Appuyer sur Entrée pour continuer ') 
        
        # Prompt if needed to regsiter a new player  ###TODO 
        player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
        # If yes : 
        if player_needed == 'y': 
            self.enter_new_player()  # ok 230507 

        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 
        
        self.tournament_data['players'] = [int(player) for player in re.findall(r'\d+', self.tournament_data['players'])] 
        print(f'self.tournament_data MC355 : {self.tournament_data}')  # dict, ok 

        # Set the next id to the last tournament: 
        self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 
        print(f'self.tournament_data MC363 : {self.tournament_data}')  # dict, ok 

        # Set 'rounds' = [] 
        if 'rounds' not in self.tournament_data.keys(): 
            self.tournament_data['rounds'] = [] 
        
        # Instantiate the current tournament: 
        self.tournament_data_obj = Tournament_model(**self.tournament_data) 
        print(f'self.tournament_data_obj MC371 : {self.tournament_data_obj}') 

        self.enter_new_round(True) 
        # Check self.round_object 
        print(f'self.round_object MC375 : {self.round_object}') 

        self.tournament_data_obj.rounds.append(self.round_object) 
        print(f'self.tournament_data_obj.rounds MC380 : {self.tournament_data_obj.rounds}') 
        print(f'self.tournament_data_obj.rounds[0].__str__() MC381 : {self.tournament_data_obj.rounds[0].__str__()}') 
        
        # self.report_view.display_all_tournaments(all_tournaments_obj) 
        print(f'self.tournament MC382 : {self.tournament}') 
        print(f'self.tournament_data_obj MC383 : {self.tournament_data_obj}') 

        if self.tournament_data_obj.serialize_object(True) == False: 
            print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
        else: 
            print(f'\nLe tournoi {self.tournament_data_obj} a bien été enregistré') 

        # Display the last tournament  
        # self.report_tournaments() 
        self.report_one_tournament('last') 

        # session.prompt('\nAppuyer sur Entrée pour continuer ') 
        # self.start(False) 


    """ auto """ 
    def close_tournament(self): 
        today = datetime.today() 
        # Select the last tournament 
        last_tournament = self.select_one_tournament('last') 
        # Get the value of input_closing_tournament 
        closing_tournament = self.in_view.input_closing_tournament() 
        if closing_tournament == 'y': 
            # Set the end_date 
            last_tournament['end_date'] = str(today) 
            print(f'last_tournament MC199 : {last_tournament}') 
        else: 
            print(f'\nLa clôture du tournoi a été annulée. ') 
            self.start(False) 
        # Instantiate it 
        self.last_tournament = Tournament_model(**last_tournament) 
        print(f'\nself.last_tournament MC205 : {self.last_tournament}') 
        print(f'\ntype(last_tournament) MC206 : {type(last_tournament)}') 
        rounds = self.last_tournament.rounds 
        # serialize the rounds 
        # for round in rounds: 
        #     print(f'\ntype(round) MC210 : {type(round)}') 
        #     round.to_dict() 
        #     print(f'\nround MC212 : {round}') 
        #     print(f'\ntype(round) MC213 : {type(round)}') 
        # Delete the last tournament 
        # + Serialize the list 
        # + Append the modified tournament to the registered list 
        # + Write the list of dictionaries into the json file 
        tournaments_dict = self.last_tournament.serialize_object(False) 
        print(f'\ndict of tournaments MC217 : {tournaments_dict}') 
        # Display the last modified tournament 
        # print(f'the last tournament MC219 : {tournaments_dict[-1]}') 
        # pass 
        self.start(False) 



    """ comment """ 
    def report_tournaments(self): 

        tournaments = Tournament_model.get_registered_dict('tournaments') 
        tournaments_obj = [] 

        for tournament in tournaments: 
            if 'rounds' not in tournament.keys(): 
                tournament['rounds'] = [] 
            # print(f'tournament MC356 : {tournament}') 
            self.tournament = Tournament_model(**tournament) 
            # print(f'self.tournament MC358 : {self.tournament}') 
            tournaments_obj.append(self.tournament) 
        
        self.report_view.display_all_tournaments(tournaments_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 


    """ comment """ # TODO ### 
    def report_one_tournament(self, tournament_id): 
        tournament = self.select_one_tournament(tournament_id) 
        # tournaments = Tournament_model.get_registered_dict('tournaments') 
        # if tournament_id == 'last': 
        #     tournament = tournaments.pop() 
        # else: 
        #     tournament = tournament[int(tournament_id)-1] 

        self.report_view.display_today_s_tournament(tournament) 
        # --> AttributeError: 'Report_view' object has no attribute 'display_today_s_tournament'. Did you mean: 'display_one_tournament'? 
    
        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    #### ============ R O U N D S ============ #### 

    """ T E S T   M E T H O D """ 
    def define_first_round(self): 
        registered_players = Player_model.get_registered_dict('players') 
        selected_players = define_matches.random_matches(registered_players) 
        print(f'selected_players MC523 : {selected_players}') 
        matches = define_matches.make_peers(selected_players) 
        print(f'matches MC525 : {matches}') 

        session.prompt('Appuyez sur une touche pour continuer') 
    
    """ T E S T   M E T H O D """ 
    def define_next_rounds(self): 
        registered_players = Player_model.get_registered_dict('players') 
        sorted_players = self.sort_objects_by_field(registered_players, 'local_score')  
        print(f'sorted_players MC533 : {sorted_players}') 
        matches = define_matches.make_peers(sorted_players) 
        print(f'matches MC535 : {matches}') 

        session.prompt('Appuyez sur une touche pour continuer') 
    



    ###TODO ajouter close_precedent_round() et close_current_tournament() 
    ###TODO retirer argument first  
    """ auto (when register_scores or register_new_tournament)""" 
    def enter_new_round(self, first=False):  # first = first round # TODO: à retirer 
        """ Auto: when register_scores. 
            Creates a new round, relative to the number of the round. 
            Args:
                first (boolean): the round is the first or not. # TODO: à retirer 
        """ 
        print('\nEnter new round') 

        if first: 
            # Check the data 
            print(f'\nself.tournament_data_obj MC482 : {self.tournament_data_obj}') 
        else: 
            self.tournament_data_obj = self.select_one_tournament("last") 
            print(f'\nself.tournament_data_obj MC485 : {self.tournament_data_obj}') 

        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 

        # 'id': self.id, 
        # 'round_name': self.round_name, 
        # 'start_datetime': self.start_datetime, 
        # 'end_datetime': end_datetime, 
        # 'tournament_id': self.tournament_id, 
        # 'matches': self.matches 

        print(f'\nround_data MC497 : {round_data}') 
        
        round_data['start_datetime'] = str(datetime.now()) 
        round_data['end_datetime'] = "" 
        round_data['tournament_id'] = self.tournament_data['id'] 
        round_data['matches'] = [] 

        # Check the data 
        print(f'self.tournament_data["rounds"] MC498 : {self.tournament_data_obj.rounds}') 
        
        # Get the last round's id and attribute the id to the current round: 
        if self.tournament_data_obj.rounds == []: 
            round_data['id'] = 1 
            self.enter_new_matches(True) 
        else: ### à corriger ? ### 
            round_data['id'] = int(self.tournament_data['rounds'][-1]['id']) + 1 
            print(f'self.tournament_data_obj.rounds MC512 : {self.tournament_data_obj.rounds}') 
            # If the round isn't the first one of the tournament 
            #     -> register the end_datetime of the precedent round ###TODO 
            # self.add_ending_round() 
            self.enter_new_matches(False) 
            
        # check the data 
        # print(f'self.peers MC496 : {self.peers}') 
        print(f'self.matches MC520 : {self.matches}') # list of objs ok 
        for m in self.matches: 
            # for p in m: 
                print(f'm str MC523 : {m.__str__()}') 
        
        round_data['matches'].append(self.matches) 
        print(f'round_data MC527 : {round_data}') 

        # Instantiate the courrent round 
        self.round_object = Round_model(**round_data)  
        ### 230530 TypeError: Round_model.__init__() missing 1 required positional argument: 'matches' ### 
        print(f'self.round_object MC531 : {self.round_object}') 
        
        self.round_object.matches = self.matches 
        print(f'self.round_object.matches MC534 : {self.round_object.matches}') 

        # TODO: ajouter report_round() 
        self.report_rounds('last') 

        return self.round_object 

    ### 230515 
    """ auto (register_scores) """ # TODO ### 
    def close_round(self, last_round): 
        """ 
        -   Enregistrer la date-heure de fin 
        -   Afficher les matches### pour montrer les scores 
        -   Voir si round.id == 4 
        +   Si round.id==4 
        +       -> cloturer le tournoi 
        -           Afficher le tournoi 
        +   Sinon 
        +       -> Enregistrer nouveau round 
        -           créer liste de matches = []
        -           Définir les matches de ce round 
        -   Afficher les matches 

        -   set end_datetime. 
        -   Display matches### to show the results 
        -   Check if round.id == 4 
        +   if round.id == 4 
        +       -> Close tournament 
        -           Display the tournament 
        +   Else 
        +       -> Register new round 
        -           Create empty list of matches 
        -           Define the matches 
        -   Display the new matches 
        """ 
        print('\nClôturer un round') 

        closing_round = self.in_view.input_closing_round() 

        if (closing_round == 'N') or (closing_round == 'n') or (closing_round == ''): 
            print('*** La clôture du round a été annulée. ***') 
            self.start(False) 
        elif (closing_round == 'y') or (closing_round == 'Y'): 
            # Get the last round 
            last_tournament = self.select_one_tournament('last') 
            last_round = last_tournament['rounds'].pop() 
            # Try to instantiate the round 
            round = Round_model(**last_round)  ### self ??? 
            # Set the end_datetime 
            round.end_datetime = str(datetime.now()) 
            
            # Define what to do according to the round's id 
            # if round.id == 4: 
            #     self.close_tournament() 
            # elif  round.id == 1: 
            #     self.enter_new_matches(True) 
            # else: 
            #     self.enter_new_matches() # False ou pas besoin ? 
            
            # # Instantiate the round 
            # self.round = Round_model(**last_round) 

            # Register the round back 
            if not round.serialize_object(False): # == False: 
                print('\nIl y a eu un problème, essayez de recommencer.') 
                session.prompt('\nAppuyer sur Entrée pour continuer ') 
                self.start(False) 
            else: 
                # Tell that the round has been closed 
                print(f'\nLe round {round.round_name} a été clôturé avec succès.') 
            if round.id == 4:  ### corriger 
                self.close_tournament() 
                print(f'\nC\'était le dernier round, le tournoi {last_tournament["name"]} a été clôturé avec succès.') 
                print(f'\nVoici les résultats du tournoi : ') 
                self.report_one_tournament('last') 
                print(f'\nEt les nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', False, 'last') 
            else:  ### corriger 
                # print(f'\nPour débuter le round {round.id+1}, entrez son nom : ') 
                # self.enter_new_matches() # False ou pas besoin ? 
                # self.in_view.input_round() 
                self.enter_new_round()  # False 
                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_one_tournament('last') 
                print(f'\nEt les nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', False, 'last') 
                # self.enter_new_matches(False)  # appelé par enter_new_round() 
                print(f'\nLes matches du round {round.id+1} ont été définis : ') 
                self.report_matches('last')  ### à implémenter dans report_view 
                
                ### mettre dans une méthode : 230515 
                session.prompt('\nAppuyer sur Entrée pour continuer ') 
                self.start(False) 
        else: 
            print('Les seules options sont "y" ou "Y" pour oui, "n" ou "N" pour non.') 
            
            session.prompt('\nAppuyer sur Entrée pour continuer ') 

    def report_rounds(self, tournament_id): 
        tournament = self.select_one_tournament(tournament_id) 
        Report_view.display_rounds_one_tournament(tournament) 
        session.prompt('\nAppuyer sur Entrée pour continuer ') 


    #### ============ M A T C H E S ============ #### 

    """ Register scores """  # à corriger ### 
    def enter_scores(self): 
        """ 
        # TODO: 
        - Afficher les matches pour demander les scores 
        - Récupérer les scores 
        - Marquer les scores dans chaque match 
        """ 
        # Get the last tournament (dict) 
        last_tournament = self.select_one_tournament('last') 
        # print(f'\nlast_tournament MC727 : {last_tournament}') 
        
        # Instantiate it (obj) 
        self.last_tournament = Tournament_model(**last_tournament) 
        # print(f'\ntype(self.last_tournament) MC732 : {type(self.last_tournament)}') # obj ok 

        # Get the last round (object) 
        self.last_round = self.last_tournament.rounds[-1] 
        # print(f'\nself.last_round MC736 : {self.last_round}') # obj ok 
        # print(f'\ntype(self.last_round) MC737 : {type(self.last_round)}') # obj ok 

        # get the matches (list of lists) 
        current_matches_dicts = self.last_round.matches 
        # print(f'\ncurrent_matches_dicts MC741 : {current_matches_dicts}') # list 
        # print(f'\ntype(current_matches_dicts) MC742 : {type(current_matches_dicts)}') # list 

        # Get the matches (obj as tuples)  
        current_matches_list = [] 
        for curr_match in current_matches_dicts: 
            curr_match_tuple = tuple(curr_match) 
            # print(f'\ncurr_match_tuple MC749 : {curr_match_tuple}') 
            curr_match_obj = Match_model(*curr_match_tuple) 
            # print(f'\ncurr_match_obj MC751 : {curr_match_obj}') 
            current_matches_list.append(curr_match_obj) 
        # print(f'\ncurrent_matches_list MC753 : {current_matches_list}')  
        # print(f'\ntype(current_matches_list) MC755 : {type(current_matches_list)}')  # [([6, 0.0], [2, 0.0]), ([8, 0.0], [1, 0.0]), ([4, 0.0], [5, 0.0]), ([3, 0.0], [7, 0.0])] 
        
        # Get the input_scores for the registered matches 
        input_results = self.in_view.input_scores(current_matches_list) 
        # print(f'\ninput_results MC759 : {input_results}') 
        # print(f'\ninput_results[0] MC760 : {input_results[0]}') # [<models.match_model.Match_model object at 0x000002AE50975A80>, <models.match_model.Match_model object at 0x000002AE50975E10>] ok 230608 
        # print(f'\ninput_results[1] MC761 : {input_results[1]}') # [[4, 0.0], [5, 0.0]] ok 230608 
        print('---------------------') 

        # Get the differentiated data from the input 
        null_matches = input_results[0] 
        winners = input_results[1] 

        # Set the new scores of the matches 
        new_matches = [] 
        # print(f'\ncurrent_matches_list MC768 : {current_matches_list}')  

        # Loop on null_matches and winners lists to update the scores into the matches (current_matches_list) 
        for null_match in null_matches: 
            # print(f'\nnull_match MC771 : {null_match}') 
            # print(f'\ntype(null_match) MC772 : {type(null_match)}') 
            for current_match in current_matches_list: 
                # print(f'\ncurrent_match MC774 : {current_match}') 
                # print(f'\ntype(current_match) MC775 : {type(current_match)}') 
                if current_match.player_1_id == null_match.player_1_id: 
                    current_match.player_1_score += float(0.5) 
                    current_match.player_2_score += float(0.5) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
                    # print(f'\ncurrent_matches_list MC782 : {current_matches_list}') 
                # for new in new_matches: 
                #     print(f'\nnew.player_1_id, new.player_1_score, new.player_2_id, new.player_2_score MC785 : {new.player_1_id}, {new.player_1_score}, {new.player_2_id}, {new.player_2_score}') 
        for winner in winners: 
            # print(f'\nwinner MC788 : {winner}') 
            # print(f'\ntype(winner) MC789 : {type(winner)}') 
            for current_match in current_matches_list: 
                # print(f'\ncurrent_match MC791 : {current_match}') 
                # print(f'\ntype(current_match) MC792 : {type(current_match)}') 
                if current_match.player_1_id == winner[0]: 
                    current_match.player_1_score += float(1) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
                    # print(f'\ncurrent_matches_list MC798 : {current_matches_list}') 
                    # for new in new_matches: 
                    #     print(f'\nnew.player_1_id, new.player_1_score, new.player_2_id, new.player_2_score MC800 : {new.player_1_id}, {new.player_1_score}, {new.player_2_id}, {new.player_2_score}') 
                elif current_match.player_2_id == winner[0]: 
                    current_match.player_2_score += float(1) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
                    # print(f'\ncurrent_matches_list MC806 : {current_matches_list}') 
                    # for new in new_matches: 
                    #     print(f'\nnew.player_1_id, new.player_1_score, new.player_2_id, new.player_2_score MC808 : {new.player_1_id}, {new.player_1_score}, {new.player_2_id}, {new.player_2_score}') 

        # print(f'new_matches length : {len(new_matches)}') 
        # for new in new_matches: 
        #     print(f'\nnew.player_1_id, new.player_1_score, new.player_2_id, new.player_2_score MC812 : {new.player_1_id}, {new.player_1_score}, {new.player_2_id}, {new.player_2_score}') 
        #     print(f'new MC813 : {new}') 

        # Put back the rounds and the matches into the round 
        self.last_tournament.rounds[-1].matches = new_matches 
        # print(f'\nself.last_tournament MC867 : {self.last_tournament}') 
        # print(f'\nself.last_tournament.rounds[-1] MC868 : {self.last_tournament.rounds[-1]}') 
        # print(f'\nself.last_tournament.rounds[-1].matches[0] MC869 : {self.last_tournament.rounds[-1].matches[0]}') 
        # print(f'\nself.last_tournament.rounds[-1].matches[0][0].__str__() MC870 : {self.last_tournament.rounds[-1].matches[0].__str__()}') 
        # print(f'\ntype(self.last_tournament.rounds[-1].matches[0]) MC871 : {type(self.last_tournament.rounds[-1].matches[0])}') 
        
        # Serialize the tournament (new=False)  
        self.last_tournament.serialize_object(False) 

        """ Update the players' scores into players.json """ 
        # self.update_players_scores() 
        self.update_players_local_scores() # TypeError: Main_controller.update_players_local_scores() missing 1 required positional argument: 'score' 230608 

        """ 
        + Clôturer le round : 
        -   Enregistrer la date-heure de fin 
        -   Afficher les matches### pour montrer les scores 
        -   Voir si round.id == 4 
        + Si round.id==4 
        +   -> cloturer le tournoi 
        -       Afficher le tournoi 
        + Sinon 
        +   -> Enregistrer nouveau round 
        -       créer liste de matches = []
        -       Définir les matches de ce round 
        - Afficher les matches 
        """ 
        ### 230515 : appeler close_round depuis l'appel du menu ??? 
        # self.close_round() 

        # session.prompt('Appuyer sur Entrée  pour continuer ') 
        # self.start(False) 

    
    """ comment """  # TODO: à corriger ### 
    # first = first round 
    def enter_new_matches(self, first=False):  ### 0511-1931 
        """ Select the players' ids witch will play against each other during the round. 
            args (boolean): True if it is the first round, False otherwise.  
        """ 
        # We have already self.tournament_data as dict or obj ??? ### 
        print(f'\nself.tournament_data_obj MC744 : {self.tournament_data_obj}') # obj ?  # dict, ok 
        # self.tournament_data_obj = Tournament_model(self.tournament_data) # obj 
        tournament_players = self.tournament_data_obj.players  # list 
        print(f'\ntournament_players MC747 : {tournament_players}') # list, ok  
        
        # Copy the players list to work with 
        players_copy = list(tournament_players) 
        print(f'\nplayers_copy MC751 : {players_copy}') # list, ok 
        # Get the data of the players_copy from the players.json file 
        players_dicts = Player_model.get_registered_dict('players') # dict 
        current_players = [] 
        player_copy_data = {} 
        for player_copy in players_copy:  ### 0527 
            # player_copy_data['id'] = player_copy 
            for registered_player in players_dicts: 
                if registered_player['id'] == player_copy: 
                    player_copy_data = dict(**registered_player) 
                    print(f"\nplayer_copy_data MC761 : {player_copy_data}") 
                    current_players.append(player_copy_data) 
                # print(f"\ncurrent_players MC764 : {current_players}") 
        # Instantiate the players :  ### besoin des objets seulement pour classer les joueurs par score pour les rounds 2 à 4 
        # players_obj = [] 
        players_obj = [Player_model(**data) for data in current_players] 
        for pl in players_obj:
            print(f'player MC771 : {pl.id}') 
        print(f"\nplayers_obj MC765 : {players_obj}") 

        # Randomly define the pairs of players for the first match  
        # if first != True: call the sort_objects_by_field() method 
        print(f"\nfirst MC769 : {first}") 
        if first: # != True: 
            selected = define_matches.random_matches(players_obj) 
            peers = define_matches.make_peers(selected) 
        
        else: # != True: 
            selected = self.sort_objects_by_field(players_obj, 'local_score') 
            # selected = define_matches.random_matches(sorted_players_obj) 
            # peers = random_matches(players_obj) 
            peers = define_matches.make_peers(selected) 

        # Check the peers 
        # print(f'\nself.peers MC827 : {self.peers}') # list of lists of objects 
        print(f'\npeers MC788 : {peers}') # list of lists 
        # print(f'player 1 str : {peers[0][0].__str__()}') 

        """ 
        peers MC851 : 
        [
            [
                <models.player_model.Player_model object at 0x0000015C0DB23EE0>, 
                <models.player_model.Player_model object at 0x0000015C0DB47190>
            ], [
                <models.player_model.Player_model object at 0x0000015C0DB44E80>, 
                <models.player_model.Player_model object at 0x0000015C0DB23580>
            ], [
                <models.player_model.Player_model object at 0x0000015C0DB217E0>, 
                <models.player_model.Player_model object at 0x0000015C0DB47CA0>
            ], [
                <models.player_model.Player_model object at 0x0000015C0DB23220>, 
                <models.player_model.Player_model object at 0x0000015C0DB23A60>
            ]
        ] 
        """ 
        
        # self.matches = [] 
        # for peer in peers: 
        #     match = Match_model(**peer) 
        #     self.matches.append(match) 
        self.matches = [Match_model(data) for data in peers] 
        print(f'\nself.matches MC815 : {self.matches}') # obj ? 
        for m in self.matches: 
            print(f'\nm MC817 : {m.__str__()}') 

        return self.matches 
        
        # # Register the matches into the tournament dict 
        # print(f'\nself.tournament_data_obj MC779 : {self.tournament_data_obj}') # obj ? 
        # rounds = self.tournament_data_obj.rounds 
        # print(f'rounds MC781 : {rounds}') 
        # rounds[-1].matches = self.matches ### 
        # print(f'\nself.tournament_data_obj MC783 : {self.tournament_data_obj}') 

        # # Register the tournament into tournaments.json 
        # print(f'rounds MC791 : {rounds}') 
        
        # print(f'\nEnregistrement du tournoi ') 
        # if Tournament_model.serialize_object(new=True): 
        # #     print(f'\nnew MC790 : {new}') 
        #     print(f'\nLe tournoi a bien été enregistré ') 
        # else: 
        #     print(f'\nIl y a eu un problème à l\'enregistrement, essayez de recommencer. ') 
    

    """ comment """  # TODO: à vérifier ### 
    def report_matches(self, tournament_id): 

        # tournament dict : 
        tournament = self.select_one_tournament(tournament_id) 
        print(f'tournament dict MC904 : {tournament}') 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds = [] 
        self.tournament = Tournament_model(**tournament) 
        print(f'self.tournament MC626 : {self.tournament}') 

        rounds = self.tournament.rounds 
        print(f'rounds MC629 : {rounds}') 

        self.report_view.display_matches_one_tournament(self.tournament) 

        session.prompt('Appuyer sur une touche  pour continuer ') 



    #### ============ U T I L S ============ #### 

    """ Sort objects by field arg """  # ok 
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        print(f'objects MC655 : ') 
        # for obj in objects: 
        #     print(obj.__str__()) 
        return objects 
    
    
    # TODO 
    # # """ Select the last tournament from JSON file """ 
    # def select_the_last_tournament(self): 
    #     """ Select the last tournament from the tournament.json file. 
    #         Returns:
    #             int: the tournament's id 
    #     """ 
    #     # Get all the tournaments from the tournaments data file (list of dicts) : 
    #     # t_dicts = Tournament_model.get_registered_all('tournaments') 
    #     t_dicts = Tournament_model.get_registered_dict('tournaments') 
    #     # Get the last tournament from t_dicts (dict) 
    #     t_dict = t_dicts[-1] 
    #     return t_dict 
    
    
    """ Select one tournament from JSON file """  ### peut-être à supprimer ??? 
    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournament.json file. 
            Args:
                t_id (int): the tournament's id 
            Returns:
                int: the tournament's id 
        """ 
        # Get all the tournaments from the tournaments data file (list of dicts) : 
        # t_dicts = Tournament_model.get_registered_all('tournaments') 
        t_dicts = Tournament_model.get_registered_dict('tournaments') 
        # Get the tournament from its id (dict) 
        if t_id == 'last': 
            t_dict = t_dicts.pop() 
        else: 
            t_dict = t_dicts[t_id-1] ### vérifier 
        return t_dict 


    def select_one_player(self, player_id): 
        players_dicts = Player_model.get_registered_dict('players') 
        player = players_dicts[player_id-1] ### vérifier 
        return player 






