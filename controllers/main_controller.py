
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
            new_session (boolean), default=False. 
                If True -> displays the menu and the welcome message, 
                else -> displays only the menu. 
        """ 
        # print("\nStart main controller") 

        if new_session: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        #### ======== "R E G I S T E R"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 


            # ==== Register one player ==== # à vérifier 
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 
                
                print('\nEnregistrer un joueur') 
                self.enter_new_player() 
                if not self.player.serialize_object(True): #  == False 
                    print('Il y a eu un problème, veuillez recommencer ou envoyer un feedback. merci de votre compréhension. ') 
                else: 
                    print(f'Le joueur a bien été enregistré. ') 
                    self.report_one_player('last') ### à vérifier 

                session.prompt('Appuyer sur une touche pour continuer MC71') 
                self.start() 


            # ==== Register many new players ==== # TODO: à vérifier 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                self.enter_many_new_players() 
                # not_registered = 0 
                for self.player in self.new_players: 
                    if not self.player.serialize_object(True): ### serialize_object() non reconnu ??? ### 
                        # not_registered += 1 
                        print('Il y a eu un problème, veuillez recommencer ou envoyer un feedback. merci de votre compréhension. ') 
                    else: 
                        print(f'Le joueur {self.player.firstname} {self.player.lastname} a bien été enregistré. ') 
                # if not_registered == 0: 
                # self.report_all_players('id') 

                session.prompt('Appuyer sur une touche pour continuer RMC91') 
                self.start() 


            # ==== Register new tournament ==== # TODO : à vérifier et nettoyer 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 

                print('\nEnregistrer un tournoi') 
                # Set the global_scores to the last local_scores, 
                # and the local_scores to zero
                self.set_players_scores_to_zero() 

                # Display registered players to select the current ones: 
                print('Voici les joueurs enregistrés : ') 
                self.report_all_players('id') 
                session.prompt('Appuyer sur une touche pour continuer MC107') 
                
                # Prompt if needed to regsiter a new player  ###TODO 
                player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                # If yes : 
                if player_needed == 'y': 
                    self.enter_new_player()  # ok 230507 
                
                self.enter_new_tournament() 
                self.enter_new_round() 
                # (returns self.round_object) 
                # Debug self.round_object : 
                # print(f'self.round_object MC375 : {self.round_object}') 

                self.tournament_data_obj.rounds.append(self.round_object) 
                # print(f'self.tournament_data_obj.rounds MC380 : {self.tournament_data_obj.rounds}') 
                # print(f'self.tournament_data_obj.rounds[0].__str__() MC381 : {self.tournament_data_obj.rounds[0].__str__()}') 
                
                # self.report_view.display_tournaments(all_tournaments_obj) 
                # print(f'self.tournament MC382 : {self.tournament}') 
                # print(f'self.tournament_data_obj MC383 : {self.tournament_data_obj}') 

                if self.tournament_data_obj.serialize_object(True) == False: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
                else: 
                    print(f'\nLe tournoi {self.tournament_data_obj} a bien été enregistré') 
                    # Display the last tournament  
                    self.report_one_tournament('last') 
                session.prompt('\nAppuyer sur une touche pour continuer MC135') 
                self.start() 


            # ==== Register new scores + close round ==== # TODO : à vérifier et nettoyer et nettoyer 
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 

                print('Enregistrer les scores') 

                # Get the last tournament (dict) 
                last_tournament = self.select_one_tournament('last') 
                
                # Instantiate it (obj) 
                self.last_tournament = Tournament_model(**last_tournament) 
                # print(f'\ntype(self.last_tournament) MC732 : {type(self.last_tournament)}') # obj ok 

                # Get the last round (object) 
                self.last_round = self.last_tournament.rounds.pop() 
                # print(f'\nself.last_round MC736 : {self.last_round}') # obj ok 
                # print(f'\ntype(self.last_round) MC737 : {type(self.last_round)}') # obj ok 

                self.enter_scores() 

                """ Update the players' scores into players.json """ 
                self.update_players_local_scores() 
                self.report_players_from_tournament('last') ### à vérifier 
                session.prompt('\nAppuyer sur une touche pour continuer MC163') 
                
                # close round : define the end_datetime # TODO ### 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                if self.last_round.id == self.last_tournament.rounds_left: 
                    self.close_tournament() ### 
                else: 
                    #TODO: Tester define_next_rounds : 
                    self.enter_new_round() ### 
                    self.enter_new_matches() ### 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_one_tournament('last') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', 'last') 

                # TODO: à vérifier, peut-être déjà visibles dans report_one_tournament('last) : 
                print(f'\nLes matches du round {round.id+1} ont été définis : ') 

                session.prompt('Appuyez sur une touche pour continuer MC189') 
                self.start() # default=False 
            

            # ==== Clôturer un round ==== # TODO : à vérifier et nettoyer 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                #TODO: Tester define_next_rounds : 
                print('\nClôturer un round') 

                # close round : define the end_datetime 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 
                
                if self.last_round.id == self.last_tournament.rounds_left: 
                    self.close_tournament() ### 
                else: 
                    #TODO: Tester define_next_rounds : 
                    self.enter_new_round() ### 
                    self.enter_new_matches() ### 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_one_tournament('last') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', 'last') 

                # TODO: à vérifier, peut-être déjà visibles dans report_one_tournament('last) : 
                print(f'\nLes matches du round {round.id+1} ont été définis : ') 

                session.prompt('Appuyez sur une touche pour continuer MC224') 
                self.start() # default=False 
            

            #### ======== T E S T  M E N U S ======== #### 

            # TEST # 
            ### 50 : Mettre à jour les scores des joueurs # TEST 
            if self.board.ask_for_register == '50': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.update_players_local_scores() 
                
                # close round : define the end_datetime # TODO ### 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                if self.last_round.id == self.last_tournament.rounds_left: 
                    self.close_tournament() ### 
                else: 
                    #TODO: Tester define_next_rounds : 
                    self.enter_new_round() ### 
                    self.enter_new_matches() ### 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_one_tournament('last') 
                session.prompt('Appuyez sur une touche pour continuer MC253') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', 'last') 
                session.prompt('Appuyez sur une touche pour continuer MC257') 

                # TODO: à vérifier, peut-être déjà visibles dans report_one_tournament('last) : 
                print(f'\nLes matches du round {round.id+1} ont été définis : ') 
                session.prompt('Appuyez sur une touche pour continuer MC261') 

                self.start() # default=False 


            # TEST # enter new matches # ok 230707 
            # # auto quand on rentre les scores des matches d'un round 
            if self.board.ask_for_register == '7':  # TODO 
                self.board.ask_for_register = None 

                print('Enregistrer les nouveaux matches') 
                self.enter_new_matches() # first_round=False 

                self.report_one_tournament('last') 
                session.prompt('Appuyez sur une touche pour continuer MC279') 

                self.report_players_from_tournament('firstname', 'last') 
                session.prompt('Appuyez sur une touche pour continuer MC285') 

                self.start() 


            # TEST # define first round # 
            if self.board.ask_for_register == '9': 
                self.board.ask_for_register = None 
                # Tester define_first_round : 
                self.define_first_round() 
                print(f'self.matches MC525 : {self.matches}') 
                session.prompt('Appuyez sur une touche pour continuer MC297') 
                self.start() # default=False 


            # TEST # define next rounds # # ok 230707 
            if self.board.ask_for_register == '10': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.define_next_rounds() 
                print(f'self.matches MC535 : {self.matches}') 
                session.prompt('Appuyez sur une touche pour continuer MC308') 
                self.start() # default=False 



            #### ============ COMMANDES DE SECOURS ============ #### 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                return True 

            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                Main_controller.close_the_app() 

        #### ======== "R E P O R T"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 


            # Report all players by firstname # TODO à vérifier 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par prénom MC349') 
                self.report_all_players('firstname') 
                
                session.prompt('Appuyez sur une touche pour continuer MC338') 
                self.start() # default=False 


            # Report all players by scores # TODO à vérifier  
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                
                print('Afficher les joueurs par score MC359') 
                self.report_all_players('score') 

                session.prompt('Appuyez sur une touche pour continuer MC349') 
                self.start() # default=False 


            # Report all tournaments # TODO : à vérifier  
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 
                
                print('Afficher les tournois MC372') 
                self.report_all_tournaments() 
                
                session.prompt('Appuyez sur une touche pour continuer MC360') 
                self.start() # default=False 
            

            # Report one tournament # TODO à vérifier 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 
                
                print('Afficher un tournoi MC383') 
                tournament_id = session.prompt('Quel tournoi voulez-vous ? (son id ou "last" pour le dernier) ') 
                self.report_one_tournament(tournament_id) 
                
                session.prompt('Appuyez sur une touche pour continuer MC372') 
                self.start() # default=False 


            # Report name and date of one tournament # TODO: à vérifier 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 
                
                print('Afficher un tournoi MC395') 
                tournament_id = session.prompt('\nDe quel tournoi voulez-vous les nom et date ? (pour le dernier, tapez "last") : ') 
                self.report_name_date_tournament(tournament_id) 
                
                session.prompt('Appuyez sur une touche pour continuer MC384') 
                self.start() # default=False 


            # Report all players of one tournament # TODO: à vérifier 
            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs d\'un tournoi MC407') 
                tournament_id = session.prompt('\nDe quel tournoi voulez-vous les joueurs ? (pour le dernier, tapez "last") : ') 
                self.report_players_from_tournament('firstname', tournament_id) # TODO: à vérifier 
                
                session.prompt('Appuyez sur une touche pour continuer MC396') 
                self.start() # default=False 


            # Report rounds and matches of one tournament # TODO: à vérifier 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 
                
                print('Afficher les rounds et matches d\'un tournoi MC419') 
                tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? (son id ou "last" pour le dernier) ') 
                self.report_rounds(tournament_id) # TODO: à vérifier 

                session.prompt('Appuyez sur une touche pour continuer MC408') 
                self.start() # default=False 


        #### ============ COMMANDES DE SECOURS ============ #### 

            """ Emergency command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                Main_controller.close_the_app() 



        # corriger la commande "*" partout 
        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            self.start(False) 
            return True # <-- ça fait quoi ça ? ### 

        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            Main_controller.close_the_app() 

            return False # <-- ça fait quoi ça ? ### 


    """ Command to quit the application """ 
    @staticmethod 
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
        

    """ TODO: à vérifier """ 
    def enter_many_new_players(self): 
        """ 
            Calls the `enter_new_player` more than one time. 
        """ 
        player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 

        self.new_players = [] 
        while True: 
            player = self.enter_new_player() 
            self.new_players.append(player) 
            # self.new_players.append(self.enter_new_player()) ### à vérifier ou corriger 
            if (player_needed == 'y') or (player_needed == 'Y'): 
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

        
    
    """ comment """ 
    def report_players_from_tournament(self, field, tournament_id): 
        
        ### à vérifier dans les appels : 
        # tournament_id = session.prompt('De quel tournoi voulez-vous les joueurs ? (son id ou "last" pour le dernier) ') 
        tournament_dict = self.select_one_tournament(tournament_id) 
        # sort = session.prompt('Ordre d\'enregistrement : "1", alphabetique : "2", ou par classement : "3" ? ') 
        
        tournament_obj = Tournament_model(**tournament_dict) 

        players_ids = tournament_obj.players 
        print(f'players_ids MC519 : {players_ids}') # ids 

        # ---- récupérer les joueurs et les instancier 

        players = [] 
        for player_id in players_ids: 
            player = self.select_one_player(player_id) 
            print(f'player_id MC525 : {player_id}') # player_dict ? 
            players.append(player) 
        players_objs = [Player_model(**player) for player in players] 

        # Choice of the order (id, alphabetical or by score): 
        # if sort == 'id': 
        if field == 'id': 
            print('\nJoueurs par ordre d\'id : ') 
        # if sort == 'firstname': 
        if field == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
        # if sort == 'score': 
        if field == 'score': 
            print('\nJoueurs par score : ') 
        self.sort_objects_by_field(players_objs, field) # sort 
        
        self.report_view.display_players(players_objs) 
        # session.prompt('Appuyer sur une touche pour continuer MC344') 
        

    # """ comment """ 
    def report_one_player(self, player_id): 
        self.select_one_player(player_id) 
        self.report_view.display_one_player() 
        # session.prompt('\nAppuyez sur une touche pour continuer  MC547') 

         
    ### 230609 
    """ Update the local_scores of the players (json) """ 
    def update_players_local_scores(self): 
        """ Update the scores into the players.json file. 
        """ 
        # Get registered players local_scores 
        p_dicts = Player_model.get_registered_dict('players') 
        # Instantiate the players 
        self.players_obj = [Player_model(**data) for data in p_dicts] 
        for self.player_obj in self.players_obj: 
            player_last_score = self.player_obj.local_score 
            # for match in last_round.matches: 
            for match in self.last_round.matches: 
                if match[0][0] == self.player_obj.id: # voir si on peut "fusionner" ces 2 "if" : 
                    player_input_score = match[0][1] 
                    ### à vérifier, sinon remettre : ### 
                    # player_last_score += player_input_score 
                    # player_obj.local_score = player_last_score
                    # print(f'\nplayer_input_score MC363 : {player_input_score}') # input score 
                    
                elif match[1][0] == self.player_obj.id: 
                    player_input_score = match[1][1] 
                    ### à vérifier, sinon remettre : ### 
                    # player_last_score += player_input_score 
                    # player_obj.local_score = player_last_score
                    # print(f'\nplayer_input_score MC368 : {player_input_score}') # input score 
                ### à vérifier, sinon enlever : ### 
                player_last_score += player_input_score 
                self.player_obj.local_score = player_last_score 
            # print(f'\nplayer_obj MC365 : {player_obj}') 

            # Register the new scores into players.json # ok 
            self.player_obj.serialize_object(True) ### à vérifier 
            # if self.player_obj.serialize_object(True): 
            #     # TODO: à changer : 
            #     print(f'\nLe nouveau score du joueur {self.player_obj.firstname} {self.player_obj.lastname} a bien été enregistré : {self.player_obj.global_score}. ') 
                

    """ comment """ # TODO: à vérifier 
    def set_players_scores_to_zero(self):  # à vérifier 
        players_dicts = Player_model.get_registered_dict('players') 
        self.players_objs = [Player_model(**player_dict) for player_dict in players_dicts] # à vérifier 

        for player_obj in self.players_objs: 
            player_obj.global_score += player_obj.local_score 
            player_obj.local_score = float(0) 
        self.players_objs = Player_model.serialize_object(False) ### à vérifier ### 
            # updated_player = Player_model.serialize_object(False) 


    #### ============ T O U R N A M E N T S ============ #### 
    
    """ Create one tournament """ 
    def enter_new_tournament(self): 

        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 

        self.tournament_data['players'] = [int(player) for player in re.findall(r'\d+', self.tournament_data['players'])] 
        # print(f'self.tournament_data MC355 : {self.tournament_data}')  # dict, ok 

        # Set the next id to the last tournament: 
        self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 
        # print(f'self.tournament_data MC363 : {self.tournament_data}')  # dict, ok 

        # Set 'rounds' = [] 
        if 'rounds' not in self.tournament_data.keys(): 
            self.tournament_data['rounds'] = [] 
        
        # Instantiate the current tournament: 
        self.tournament_data_obj = Tournament_model(**self.tournament_data) 
        

    """ auto """ 
    def close_tournament(self): 
        today = datetime.today() 
        # Select the last tournament 
        # last_tournament = self.select_one_tournament('last') 
        # Get the value of input_closing_tournament 
        closing_tournament = self.in_view.input_closing_tournament() 

        if closing_tournament == 'y': 
            # Set the end_date 
            self.last_tournament.end_date = str(today) 
            print(f'self.last_tournament MC470 : {self.last_tournament}') 
            self.last_tournament.serialize_object(False) 
            # self.start(False) 
            print(f'\nC\'était le dernier round, le tournoi {self.last_tournament["name"]} a été clôturé avec succès.') 
            print(f'\nVoici les résultats du tournoi : ') 
            self.report_one_tournament('last') 
            print(f'\nEt les nouveaux scores des joueurs : ') 
            self.report_players_from_tournament('firstname', 'last') 
        else: 
            print(f'\nLa clôture du tournoi a été annulée, vous pourrez la relancer depuis le menu. ') 
        # session.prompt('\nAppuyer sur une touche pour continuer MC507') 
        
        print(f'\nself.last_tournament MC509 : {self.last_tournament}') 


    """ comment """ # à vérifier 
    def report_all_tournaments(self): 

        tournaments = Tournament_model.get_registered_dict('tournaments') 
        tournaments_obj = [] 

        for tournament in tournaments: 
            if 'rounds' not in tournament.keys(): 
                tournament['rounds'] = [] 
            # print(f'tournament MC356 : {tournament}') 
            self.tournament = Tournament_model(**tournament) 
            # print(f'self.tournament MC358 : {self.tournament}') 
            tournaments_obj.append(self.tournament) 
        
        self.report_view.display_tournaments(tournaments_obj) 

        

    """ comment """ # TODO: à corriger ### 
    def report_one_tournament(self, tournament_id): 

        tournament = self.select_one_tournament(tournament_id) 
        last_tournament = Tournament_model(**tournament) 
        self.report_view.display_one_tournament(last_tournament) ### "last" comme id 
        # self.report_view.display_one_tournament(tournament) ### "last" comme id 
        
    
    """ comment """ # TODO: à vérifier ### 
    def report_name_date_tournament(self, tournament_id): 

        tournament = self.select_one_tournament(tournament_id) 
        self.report_view.display_name_date_tournament(tournament) ### "last" comme id 

        

    #### ============ R O U N D S ============ #### 

    """ T E S T   M E T H O D """ 
    def define_first_round(self): 
        registered_players = Player_model.get_registered_dict('players') 
        selected_players = define_matches.random_matches(registered_players) 
        print(f'selected_players MC523 : {selected_players}') 
        self.matches = define_matches.make_peers(selected_players) 
        # print(f'matches MC525 : {self.matches}') 

        # session.prompt('Appuyez sur une touche pour continuer  MC545') 
    
    """ T E S T   M E T H O D """ 
    def define_next_rounds(self): 
        last_tournament = self.select_one_tournament('last') 
        tournament_obj = Tournament_model(**last_tournament) 

        players_ids = tournament_obj.players 

        players = [] 
        for player_id in players_ids: 
            player = self.select_one_player(player_id) 
            print(f'player_id MC525 : {player_id}') # player_dict ? 
            players.append(player) 
        players_objs = [Player_model(**player) for player in players] 

        # registered_players = Player_model.get_registered_dict('players') 
        # sorted_players = self.sort_objects_by_field(registered_players, 'local_score', True) ### 230707 
        sorted_players = self.sort_objects_by_field(players_objs, 'local_score', True) ### 230707 
        print(f'sorted_players MC719 : {sorted_players}') 
        self.matches = define_matches.make_peers(sorted_players, False, tournament_obj) 
        # print(f'self.matches MC535 : {self.matches}') 


    ###TODO ajouter close_precedent_round() et close_current_tournament() 
    """ auto (when register_scores or register_new_tournament)""" 
    def enter_new_round(self): # , first=False  # first = first round # TODO: à retirer 
        """ Auto: when register_scores. 
            Creates a new round, relative to the number of the round. 
            Args:
                first (boolean): the round is the first or not. # TODO: à retirer 
        """ 
        print('\nEnter new round') 

        # self.tournament_data_obj = self.select_one_tournament("last") 
        self.tournament_data_dict = self.select_one_tournament("last") 
        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 

        # 'id': self.id, 
        # 'round_name': self.round_name, 
        # 'start_datetime': self.start_datetime, 
        # 'end_datetime': end_datetime, 
        # 'tournament_id': self.tournament_id, 
        # 'matches': self.matches 

        print(f'\nround_data MC576 : {round_data}') 
        
        round_data['start_datetime'] = str(datetime.now()) 
        round_data['end_datetime'] = "" 
        round_data['matches'] = [] 


        # on peut pas, il faut remplir les champs pour l'instancier : 
        # ### 230612 enregistrer le tournoi "vide" avant de créer les matches ? 
        # self.tournament = Tournament_model(**self.tournament_data_dict) 

        # Check the data 
        print(f'self.tournament_data_dict["rounds"] MC593 : {self.tournament_data_dict["rounds"]}') 
        
        # Get the last round's id and attribute the id to the current round: 
        if self.tournament_data_dict['rounds'] == []: 
            round_data['id'] = 1 
            round_data['tournament_id'] = self.tournament_data['id']+1 # à vérifier 
            self.enter_new_matches(True) # first_round 
        else: ### à corriger ? ### 
            round_data['id'] = int(self.tournament_data_dict['rounds'][-1]['id']) + 1 
            round_data['tournament_id'] = self.tournament_data_dict['id'] # à vérifier 
            print(f'self.tournament_data_dict["rounds"] MC608 : {self.tournament_data_dict["rounds"]}') 
            # If the round isn't the first one of the tournament 
            #     -> register the end_datetime of the precedent round ###TODO 
            # self.add_ending_round() 
            ### à vérifier 
            if self.tournament_data_dict['rounds'][-1]['end_datetime'] == '': 
                self.tournament_data_dict['rounds'][-1]['end_datetime'] = datetime.now() 
            # self.tournament_data_dict['rounds'][-1]['matches'] = [] 

            self.enter_new_matches() # first=False default 

            self.tournament_data_obj = Tournament_model(**self.tournament_data_dict) 
            print(f'self.tournament_data_obj MC628 : {self.tournament_data_obj["rounds"]}') 
            
        # check the data 
        # print(f'self.peers MC496 : {self.peers}') 
        print(f'self.matches MC624 : {self.matches}') # list of objs ok 
        for m in self.matches: 
            # for p in m: 
                print(f'm str MC616 : {m.__str__()}') 
        
        round_data['matches'].append(self.matches) 
        print(f'round_data MC619 : {round_data}') 

        self.round_object = self.tournament_data_obj.rounds[-1] 
        print(f'self.round_object MC652 : {self.round_object}') 

        # TODO: à vérifier 
        self.report_rounds('last') 
        session.prompt('\nAppuyez sur une touche pour continuer MC664') 

        return self.round_object 


    def report_rounds(self, tournament_id): 
        tournament = self.select_one_tournament(tournament_id) 
        Report_view.display_rounds_one_tournament(tournament) 
        
        

    #### ============ M A T C H E S ============ #### 

    """ Register scores """  # à corriger ### 
    def enter_scores(self): 
        """ 
        # TODO: 
        - Afficher les matches pour demander les scores 
        - Récupérer les scores 
        - Marquer les scores dans chaque match 
        """ 
        ### à vérifier 230630 

        # get the matches (list of lists) 
        current_matches_dicts = self.last_round.matches 
        # print(f'\ncurrent_matches_dicts MC741 : {current_matches_dicts}') # list 
        # print(f'\ntype(current_matches_dicts) MC742 : {type(current_matches_dicts)}') # list 

        # Get the matches (obj as tuples)  
        current_matches_list = [] 
        for curr_match in current_matches_dicts: 
            print(f'curr_match MC780 : {curr_match}') 
            curr_match_tuple = tuple(curr_match) 
            print(f'\ncurr_match_tuple MC749 : {curr_match_tuple}') 
            curr_match_obj = Match_model(curr_match_tuple) 
            # curr_match_obj = Match_model(*curr_match_tuple) 
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

        # Put back the rounds and the matches into the round 
        self.last_tournament.rounds[-1].matches = new_matches 
        # print(f'\nself.last_tournament MC867 : {self.last_tournament}') 
        # print(f'\nself.last_tournament.rounds[-1] MC868 : {self.last_tournament.rounds[-1]}') 
        # print(f'\nself.last_tournament.rounds[-1].matches[0] MC869 : {self.last_tournament.rounds[-1].matches[0]}') 
        # print(f'\nself.last_tournament.rounds[-1].matches[0][0].__str__() MC870 : {self.last_tournament.rounds[-1].matches[0].__str__()}') 
        # print(f'\ntype(self.last_tournament.rounds[-1].matches[0]) MC871 : {type(self.last_tournament.rounds[-1].matches[0])}') 
        
        # Serialize the tournament (new=False)  
        self.last_tournament.serialize_object(False) 

        # """ Update the players' scores into players.json """ 
        # self.update_players_local_scores() 
        # """ 
        # + Clôturer le round : 
        # -   Enregistrer la date-heure de fin 
        # -   Afficher les matches### pour montrer les scores 
        # -   Voir si round.id == 4 
        # + Si round.id==4 
        # +   -> cloturer le tournoi 
        # -       Afficher le tournoi 
        # + Sinon 
        # +   -> Enregistrer nouveau round 
        # -       créer liste de matches = []
        # -       Définir les matches de ce round 
        # - Afficher les matches 
        # """ 
        # ### 230515 : appeler close_round depuis l'appel du menu ??? 
        # # self.last_round -> objet 
        # if self.last_round.id == self.last_tournament.rounds_left: 
        #     self.close_round(True) # tournament_finished, default = False 
        # else:  
        #     self.close_round() # tournament_finished, default = False 
        # # self.define_matches.make_peers() 
        # # session.prompt('Appuyez sur une touche  pour continuer MC881') 
        # # self.start(False) 

    
    """ comment """  
    # TODO: différencier les matches à partir du round 2 ### 
    # first = first round 
    def enter_new_matches(self, first_round=False):  ### 0511-1931 
        """ Select the players' ids witch will play against each other during the round. 
            args (boolean): True if it is the first round, False otherwise.  
        """ 
        ### TODO: check self.last_tournament with a print() ### 
        last_tournament = self.select_one_tournament('last') 
        # We have already self.tournament_data as dict 
        print(f'\nlast_tournament MC881 : {last_tournament}') # obj ?  # dict, ok 
        tournament_players = last_tournament['players']  # list 
        print(f'\ntournament_players MC889 : {tournament_players}') # list, ok  
        
        # Copy the players list to work with 
        players_copy = list(tournament_players) 
        print(f'\nplayers_copy MC893 : {players_copy}') # list, ok 
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
        
        # debug : 
        for pl in players_obj:
            print(f'player MC771 : {pl.id}') 
        print(f"\nplayers_obj MC765 : {players_obj}") 

        # Get the registered tournament to check if the matches are uniques 
        # tournament = self.last_tournament 

        # Randomly define the pairs of players for the first match  
        # if first != True: call the sort_objects_by_field() method 
        print(f"\nfirst_round MC932 : {first_round}") 
        if first_round: ### True: 
            selected = define_matches.random_matches(players_obj) 
            # peers = define_matches.make_peers(selected, False, tournament)  # first_round 
        
        else: ### != True: 
            selected = self.sort_objects_by_field(players_obj, 'local_score', True) 
            # selected = define_matches.random_matches(sorted_players_obj) 
            # peers = random_matches(players_obj) 
        
        new_matches = define_matches.make_peers(selected, False, last_tournament)  # first_round 

        # Check the peers 
        # print(f'\nself.peers MC827 : {self.peers}') # list of lists of objects 
        print(f'\nnew_matches MC945 : {new_matches}') # list of lists 
        # print(f'player 1 str : {peers[0][0].__str__()}') 

        # debug: 
        for new_match in new_matches: 
            print(f'new_match MC970 : {new_match}') 
            for player in new_match: 
                print(f'player MC972 : {player}') 

        self.matches = [Match_model(data) for data in new_matches] # ok 230616 
        # print(f'\nself.matches MC982 : {self.matches}') # obj ? 

        # debug 
        for m in self.matches: 
            print(f'\nm MC884 : {m.__str__()}') 

        return self.matches 
        


    #### ============ U T I L S ============ #### 

    """ Sort objects by field arg """  # ok 
    # @staticmethod ### 230707 
    def sort_objects_by_field(self, objects, field, reversed=False):  
        print() 
        objects.sort(key=attrgetter(field), reverse=reversed) 
        # print(f'objects MC655 : ') 
        # for obj in objects: 
        #     print(obj.__str__()) 
        return objects 

    
    """ Select one tournament from JSON file """  ### peut-être à supprimer ??? 
    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournament.json file. 
            Args:
                t_id (int): the tournament's id 
            Returns:
                int: the tournament's id 
        """ 
        t_dicts = Tournament_model.get_registered_dict('tournaments') 
        # Get the tournament from its id (dict) 
        if t_id == 'last': 
            t_dict = t_dicts.pop() 
        else: 
            t_dict = t_dicts[t_id-1] ### vérifier 
        return t_dict 


    def select_one_player(self, player_id): 
        players_dicts = Player_model.get_registered_dict('players') 
        if player_id == 'last': 
            player = players_dicts.pop() 
        else: 
            player = players_dicts[player_id-1] ### vérifier 
        return player 

