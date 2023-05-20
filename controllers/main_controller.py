
from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from utils.define_matches import Define_matches 

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
        report_view: Report_view, 
        define: Define_matches 
    ): 
        self.board = board 
        self.in_view = in_view 
        self.report_view = report_view 
        self.define = define 
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

            # Nom et dates d'un tournoi # TODO 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_name_date_tournament() 

            # Les joueurs du tournoi par ordre alphabétique # TODO 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.players_from_tournament_alphabetical_order() 

            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? (son id ou "last" pour le dernier) ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 

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
        new_player_data['match_score'] = float(0.0) 
        # print(f'\nnew_player_data MC226 : {new_player_data}')   
        self.player = Player_model(**new_player_data) 
        # print(f'self.player MC228 : {self.player}') 
        self.player.serialize_object(True) 

        self.report_players('firstname', True)  # finished 


    """ TODO """ 
    def enter_many_new_players(self): 
        pass 


    """ Display all the players """  # ok 230505 
    def report_all_players(self, sort, finished): 
        """ 
            Displays the players from players.json. 
            parameters: 
                sort (str): 'firstname' or 'global_score', the name of the field on wich to sort the players. 
                finished (boolean): if the method is called the last one (True -> display the start menu) or if there are other methods colled after this one (False -> not call the start menu). 
        """ 
        print('report_all_players MC239') 
        # players = Player_model.get_registered_all('players') 
        players = Player_model.get_registered_dict('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        # Choice of the order ('firstname' -> alphabetical or 'global_score' -> by score): 
        if sort == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'global_score') 
        self.report_view.display_players(players_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        if finished == True: 
            self.start(False) 
    
    """ comment """ 
    def report_players_from_tournament(self, sort, finished, tournament_id): 
        tournament_dict = self.select_one_tournament(tournament_id) 
        tournament_obj = Tournament_model(**tournament_dict) 
        players_obj = tournament_obj.players 

        # Choice of the order (alphabetical or by score): 
        if sort == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'global_score') 
        
        self.report_view.display_players(players_obj) 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        if finished == True: 
            self.start(False)  


         
    ### 230515 
    """ Update the global_scores of the players (json) """ 
    def update_players_scores(self): 
        # Select the scores of each player into the current match 
        last_tournament = self.select_one_tournament('last') 
        # Try to instantiate the last tournament 
        last_tournament_obj = Tournament_model(**last_tournament) 
        # last_round = last_tournament['rounds'].pop() 
        last_round = last_tournament_obj.rounds.pop() 
        print(f'\ntype(last_round) MC274 : {type(last_round)}') 
        # Select players global_scores 
        p_dicts = Player_model.get_registered_dict('players') 
        # Try to instantiate the players 
        players_obj = [Player_model(**data) for data in p_dicts] 
        for player in players_obj: 
            player_last_score = player.global_score 
            for match in last_round.matches: 
                if match[0] == player.id: 
                    player_input_score = player.global_score 
                    player_last_score += player_input_score  
            print(f'\nplayer MC285 : {player}') 
        # for p in p_dicts: 
        #     player_last_score = p['global_score'] 
        #     for match in last_round['matches']: 
        #         if match[0] == p['id']: 
        #             player_input_score = p['global_score'] 
        #             player_last_score += player_input_score 

        # Register the new scores into players.json 
        if Player_model.serialize_object(False): 
            print(f'\nLes nouveaux scores des joueurs ont bien été enregistrés. ')
            # self.report_players()  
            # self.report_players_from_tournament('firstname', False, 'last')  
        


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
        self.report_all_players('firstname', False)  ### finished: False 
        
        # Prompt if needed to regsiter a new player  ###TODO 
        player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
        # If yes : 
        if player_needed == 'y': 
            self.enter_new_player()  # ok 230507 

        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 
        
        self.tournament_data['players'] = [int(player) for player in re.findall(r'\d', self.tournament_data['players'])] 
        # tournament_data['players'] = [player for player in tournament_data['players'].split(',')]  # list of str 
        print(f'self.tournament_data MC355 : {self.tournament_data}') 

        # Set the next id to the last tournament: 
        self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 
        # all_tournaments = Tournament_model.get_registered_dict('tournaments') 
        # last_tournament = all_tournaments.pop() 
        # print(f'last_tournament MC297 : {last_tournament}') 
        # self.tournament_data['id'] = int(last_tournament['id']) + 1 
        print(f'self.tournament_data MC363 : {self.tournament_data}') 

        # Set 'rounds' = [] 
        if 'rounds' not in self.tournament_data.keys(): 
            self.tournament_data['rounds'] = [] 
        
        self.enter_new_round(True) 
        # Check self.round_object 
        print(f'self.round_object MC376 : {self.round_object}') 

        self.tournament_data['rounds'].append(self.round_object) 
        print(f'self.tournament_data MC379 : {self.tournament_data}') 
        print(f'self.tournament_data MC380 : {self.tournament_data["rounds"][0].__str__()}') 

        # Instantiate the current tournament: 
        self.tournament = Tournament_model(**self.tournament_data) 
        # print(f'self.tournament MC383 : {self.tournament}') 

        
        # all_tournaments = Tournament_model.get_registered_dict('tournaments') 
        # all_tournaments_obj = [Tournament_model(**tournament) for tournament in all_tournaments] 
        # self.report_view.display_all_tournaments(all_tournaments_obj) 

        # if self.tournament.serialize_object(True) == False: 
        #     print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
        # else: 
        #     print(f'\nLe tournoi {self.tournament} a bien été enregistré') 

        # self.report_tournaments() 

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
        # self.board.ask_for_report = None 

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
        self.start(False) 


    """ comment """ # TODO ### 
    def report_one_tournament(self, tournament_id): 
        tournament = self.select_one_tournament(tournament_id) 
        # tournaments = Tournament_model.get_registered_dict('tournaments') 
        # if tournament_id == 'last': 
        #     tournament = tournaments.pop() 
        # else: 
        #     tournament = tournament[int(tournament_id)-1] 

        self.report_view.display_today_s_tournament(tournament) 
    
        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    #### ============ R O U N D S ============ #### 

    ###TODO ajouter close_precedent_round() et close_current_tournament() 
    """ auto (when register_scores or register_new_tournament)""" 
    def enter_new_round(self, first):  # first = first round 
        """ Creates a new round, relative to the number of the round. 

        Args:
            first (boolean): the round is the first or not. 
        """ 
        print('\nEnter new round') 

        if first: 
            # Check the data 
            print(f'\nself.tournament_data MC484 : {self.tournament_data}') 
        else: 
            self.tournament_data = self.select_one_tournament("last") 
            print(f'\nself.tournament_data MC486 : {self.tournament_data}') 

        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 
        print(f'\nround_data MC475 : {round_data}') 
        
        round_data['start_datetime'] = str(datetime.now()) 
        round_data['end_datetime'] = "" 
        round_data['tournament_id'] = self.tournament_data['id'] 

        # Check the data 
        print(f'self.tournament_data["rounds"] MC498 : {self.tournament_data["rounds"]}') 
        
        # Get the last round's id and attribute the id to the current round: 
        if self.tournament_data['rounds'] == []: 
            round_data['id'] = 1 
            self.enter_new_matches(True) 
        else: ### à corriger ? ### 
            round_data['id'] = int(self.tournament_data['rounds'][-1]['id']) + 1 
            print(f'self.tournament_data["rounds"] MC489 : {self.tournament_data["rounds"]}') 
            # If the round isn't the first one of the tournament 
            #     -> register the end_datetime of the precedent round ###TODO 
            # self.add_ending_round() 
            self.enter_new_matches(False) 
            
        # check the data 
        # print(f'self.peers MC496 : {self.peers}') 
        print(f'self.matches MC502 : {self.matches}') 
        
        print(f'round_data MC504 : {round_data}') 

        round_data['matches'] = self.matches  ### 230519 
        print(f'round_data["matches"] MC507 : {round_data["matches"]}') 

        # Instantiate the courrent round 
        self.round_object = Round_model(**round_data) 
        print(f'self.round_object MC503 : {self.round_object}') 

        # return self.round_object 


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
                self.enter_new_round(False) 
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
            self.start(False) 




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
        print(f'\nlast_tournament MC594 : {last_tournament}') 
        
        # Try to instantiate it (obj) 
        self.last_tournament = Tournament_model(**last_tournament) 
        print(f'\ntype(self.last_tournament) MC598 : {type(self.last_tournament)}') # obj ok 

        # Get the last round (object) 
        self.last_round = self.last_tournament.rounds[-1] 
        print(f'\nself.last_round MC602 : {self.last_round}') # obj ok 
        print(f'\ntype(self.last_round) MC603 : {type(self.last_round)}') # obj ok 

        # get the matches 
        current_matches_dicts = self.last_round.matches 
        print(f'\ncurrent_matches_dicts MC607 : {current_matches_dicts}') 
        print(f'\ntype(current_matches_dicts) MC608 : {type(current_matches_dicts)}') # obj ok 

        # Get the matches only, without the "match" key  ### à voir ??? 
        current_matches_list = [] 
        for curr_match in current_matches_dicts: 
            # for curr_match_value in curr_match.values(): 
                # print(f'\ncurr_match_value MC567 : {curr_match_value}') 
            curr_match_tuple = tuple(curr_match) 
            curr_match_obj = Match_model(*curr_match_tuple) 
            print(f'\ncurr_match_obj MC617 : {curr_match_obj}') 
            current_matches_list.append(curr_match_obj) 
        print(f'\ncurrent_matches_list MC619 : {current_matches_list}')  # [<models.match_model.Match_model object at 0x00000220F74744C0>, <models.match_model.Match_model object at 0x00000220F7437670>, <models.match_model.Match_model object at 0x00000220F74355D0>, <models.match_model.Match_model object at 0x00000220F74358A0>] 
        print(f'\ntype(current_matches_list) MC620 : {type(current_matches_list)}')  # [([6, 0.0], [2, 0.0]), ([8, 0.0], [1, 0.0]), ([4, 0.0], [5, 0.0]), ([3, 0.0], [7, 0.0])] 
        
        # Call the input_scores with the matches as parameter 
        input_results = self.in_view.input_scores(current_matches_list) 
        # print(f'\ninput_results MC588 : {input_results}') 
        print('---------------------') 
        # Get the first player from the current_matches who is into the input_matches_scores[0] 
        null_matches = [] 
        won_matches = [] 
        winners = input_results[1] 
        for current_match in current_matches_list: 
            for null_match in input_results[0]: 
                # print(f'\nnull_match MC594 : {null_match}') 
                if null_match in current_match.player_1: 
                    # print(f'\ncurrent_match[0][0] MC596 : {current_match[0][0]}') 
                    # Null matches : set 0.5 as the score of all the players in null_matches 
                    current_match.player_1[1] = 0.5 
                    current_match.player_2[1] = 0.5 
                    null_matches.append(current_match) 
            for winner in winners: 
                # print(f'\nwinner MC604 : {winner}') 
                if (winner in current_match.player_1): 
                    # print(f'\ncurrent_match MC607 : {current_match}') 
                    current_match.player_1[1] = 1.0 
                    print(f'\ntype(current_match) MC644 : {type(current_match)}') 
                    won_matches.append(current_match) 
                if (winner in current_match.player_2): 
                    # print(f'\ncurrent_match MC610 : {current_match}') 
                    current_match.player_1[1] = 1.0 
                    won_matches.append(current_match) 
                
        print(f'\nnull_matches MC651 : {null_matches[0].player_1}')  # [6, 0.5] 
        print(f'\nnull_matches MC652 : {null_matches}') 
        print(f'\nwon_matches MC653 : {won_matches}') 

        new_matches = null_matches[0:] 
        new_matches += won_matches[0:]  # list of objects 
        print(f'\nnew_matches MC657 : {new_matches}')  # [<models.match_model.Match_model object at 0x0000024ACC243790>, <models.match_model.Match_model object at 0x0000024ACC241720>, <models.match_model.Match_model object at 0x0000024ACC242AD0>, <models.match_model.Match_model object at 0x0000024ACC243E20>] 
        print(f'\ntype(new_matches) MC658 : {type(new_matches)}') 

        # Put back the rounds and the matches into the round 
        self.last_tournament.rounds[-1].matches = new_matches 
        print(f'\nself.last_tournament MC662 : {self.last_tournament}') 
        print(f'\nself.last_tournament.rounds[-1] MC663 : {self.last_tournament.rounds[-1]}') 
        print(f'\nself.last_tournament.rounds[-1].matches MC664 : {self.last_tournament.rounds[-1].matches[0].player_1}') 

        # Serialize the tournaments (new=False)  
        self.last_tournament.serialize_object(False) 

        """ - Modifier les scores des joueurs dans players.json """ 
        self.update_players_scores()  ### 230515 

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
        self.close_round() 

        session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 

    
    """ comment """  # à corriger ### 
    # def define_first_round(self): 
    def enter_new_matches(self, first=False):  ### 0511-1931 
        """ Select the players' ids witch will play against each other during the first round. """ 
        # We have already self.tournament_data 
        print(f'\nself.tournament_data MC787 : {self.tournament_data}') 
        tournament_players = self.tournament_data['players'] 
        
        # Copy the players list to work with 
        players_copy = list(tournament_players) 
        print(f'\nplayers_copy MC792 : {players_copy}') 
        # Get the data of the players_copy from the players.json file 
        players_dicts = Player_model.get_registered_dict('players') 

        # Instantiate the players :  ### besoin des objets seulement pour classer les joueurs par score pour les rounds 2 à 4 
        players_obj = [] 
        for p in players_copy: 
            print(f"\np MC799 : {p}") 
            p_dict = players_dicts[p-1] 
            print(f"\np_dict MC801 : {p_dict}") 
            player_obj = Player_model( 
                **p_dict 
            ) 
            print(f"\nplayer_obj MC805 : {player_obj}") 
            players_obj.append(player_obj) 
        print(f"\nplayers_obj MC807 : {players_obj}") 

        # matches to store into the current round 
        # self.matches = [] 
        # self.peers = [] 

        # Randomly define the pairs of players for 4 matches 
        # if first != True: call the sort_objects_by_field() function 
        print(f"\nfirst MC691 : {first}") 
        if not first: # != True: 
            players = self.sort_objects_by_field(players_obj, 'global_score') 
        peers = self.define.random_matches(players_obj) 
        # self.random_matches(players_obj)  # returns matches 

        # Check the matches 
        # print(f'\nself.matches MC824 : {self.matches}')  # OK 230519 
        # print(f'\nself.peers MC827 : {self.peers}') # list of lists of objects 
        print(f'\npeers MC827 : {peers}') # list of lists of dicts 
        
        self.matches = [] 
        # Instantiate the matches 
        # for peer in peers: 
        #     peer_obj = Match_model(*peer) 
        #     self.matches.append(peer_obj) 
        self.matches = [Match_model(*data) for data in peers] 
        # self.matches = [Match_model(*data) for data in matches] 
        print(f'\nself.matches MC767 : {self.matches}') # dict 
        
        # # # Register the matches into the tournament dict 
        # print(f'\nself.tournament_data MC770 : {self.tournament_data}') # dict 
        # # self.tournament_data['rounds'][-1]['matches'] = self.peers ### 
        # # print(f'\nself.tournament_data MC832 : {self.tournament_data}') 

        # # # Register the matches into tournament.json 
        # rounds = self.tournament_data["rounds"] 
        # print(f'rounds MC775 : {rounds}') 
        # rounds['matches'] = [] 
        # self.tournament_data["rounds"].append(self.matches) 
        # print(f'rounds MC777 : {self.tournament_data["rounds"]}') 
        # # # if Match_model.serialize_object(new=True): 
        # # print(f'\nEnregistrement des matches ') 
        # # if Match_model.serialize_object(self.peers): 
        # # # Match_model.serialize_object(new=True) 

        # # #     print(f'\nnew MC835 : {new}') 
        # #     print(f'\nLes matches ont bien été enregistrés ') 
        # # else: 
        # #     print(f'\nIl y a eu un problème à l\'enregistrement, essayez de recommencer. ') 




    """ comment """  # à supprimer ### 
    def report_matches(self, ask_for_tournament_id): 

        # tournament dict : 
        tournament = self.select_one_tournament(ask_for_tournament_id) 
        print(f'tournament dict MC621 : {tournament}') 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds = [] 
        self.tournament = Tournament_model(**tournament) 
        print(f'self.tournament MC626 : {self.tournament}') 

        rounds = self.tournament.rounds 
        print(f'rounds MC629 : {rounds}') 

        self.report_view.display_matches_one_tournament(self.tournament) 

        # session.prompt('Appuyer sur Entrée  pour continuer ') 
        # self.start(False) 




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
            t_dict = t_dicts[t_id] 
        return t_dict 






