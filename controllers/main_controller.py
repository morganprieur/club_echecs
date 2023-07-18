
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
                
                session.prompt('Appuyez sur une touche pour continuer MC71') 
                self.start() 


            # ==== Register many new players ==== # TODO: à vérifier 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                self.enter_many_new_players() 
                # check self.new_players : 
                # print(f'\nself.players MC81 : {self.players} ') 

                session.prompt('Appuyez sur une touche pour continuer RMC93') 
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
                session.prompt('Appuyez sur une touche pour continuer MC95') 
                
                # Prompt if needed to register a new player  ###TODO 
                player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                # If yes : 
                if player_needed == 'y': 
                    self.enter_new_player()  # object 
                    session.prompt('Appuyez sur une touche pour continuer MC102') 
                
                self.enter_new_tournament() 
                # return self.tournament_obj (object) 
                print('\nEnregistrer un nouveau round') 
                self.enter_new_round(True) # first_round # object 
                # returns self.round_object (objects) 
                # Debug self.round_object : 
                # print(f'self.round_object MC375 : {self.round_object}') 
                # self.tournament_obj.rounds.append(self.round_object) # plus bas 

                ### TODO : à vérifier 
                # self.new_matches = self.round_object.matches 
                # if self.new_matches == []: 
                if self.round_object.matches == []: 
                    self.enter_new_matches(True) # first_round 
                    # return self.matches (objects) 
                else: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 

                self.round_object.matches.append(self.matches) 
                self.tournament_obj.rounds.append(self.round_object) 
                # print(f'self.tournament_data_obj.rounds MC134 : {self.tournament_data_obj.rounds}') 

                # if self.tournament_obj.serialize_object(True) == False: 
                if not self.tournament_obj.serialize_object(True): 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
                else: 
                    print(f'\nLe tournoi {self.tournament_obj.id} a bien été enregistré') 
                    # Display the last tournament  
                    self.report_one_tournament('last') 
                
                session.prompt('\nAppuyez sur une touche pour continuer MC132') 
                self.start() 


            # TODO: à vérifier 
            # ==== Register new scores + close round ====
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 

                print('Enregistrer les scores') 

                # Get the last tournament (dict) 
                last_tournament = self.select_one_tournament('last') 
                
                # Instantiate it (obj) 
                self.tournament_obj = Tournament_model(**last_tournament) 
                # print(f'\ntype(self.last_tournament) MC732 : {type(self.last_tournament)}') # obj ok 

                # Get the last round (object) 
                self.last_round = self.tournament_obj.rounds.pop() 
                # print(f'\nself.last_round MC736 : {self.last_round}') # obj ok 
                
                self.enter_scores() 

                """ Update the players' scores into players.json """ 
                self.update_players_local_scores() 
                self.report_players_from_tournament('last') ### à vérifier 
                session.prompt('\nAppuyez sur une touche pour continuer MC160') 
                
                # close round : define the end_datetime # TODO ### 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    print(f'\nC\'était le dernier round, le tournoi {self.tournament_o["name"]} a été clôturé avec succès.') 
                    print(f'\nVoici les résultats du tournoi : ') 
                    self.report_rounds('last') ### TODO: à vérifier 
                    session.prompt('\nAppuyer sur une touche pour continuer MC175') 
                    
                    # self.report_one_tournament('last') 
                    print(f'\nEt les nouveaux scores des joueurs : ') 
                    self.report_players_from_tournament('firstname', 'last') 
                else: 
                    ### TODO: à vérifier : 
                    self.enter_new_round(False) 
                    # returns self.round_object 
                    
                    ### TODO : vérifier self.round_object 
                    print(f'self.round_object MC180 : {self.round_object}') 
                    # self.new_matches = self.round_object.matches 
                    # check the data 
                    # print(f'self.matches MC183 : {self.matches}') 
                    # for m in self.matches: 
                    #     print(f'm str MC616 : {m.__str__()}') 
                    
                    ### TODO: à vérifier : 
                    self.enter_new_matches(False) 
                    # returns self.matches 
                    
                    ### TODO : vérifier self.matches 
                    self.round_object.matches.append(self.matches) 
                    self.tournament_obj.rounds.append(self.round_object) 
                    print(f'self.round_object MC201 : {self.round_object}') 

                if not self.tournament_obj.serialize_object(False): 
                    print('Il y a eu un problème. Essayez de recommencer et envoyez un feedback. merci de votre compréhension.') 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_rounds('last') 
                # self.report_one_tournament('last') 
                session.prompt('\nAppuyer sur une touche pour continuer MC209') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', 'last') 
                session.prompt('Appuyez sur une touche pour continuer MC213') 

                self.start() 
            

            # TODO : à vérifier et nettoyer 
            # ==== Clôturer un round ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                # close round : define the end_datetime # TODO ### 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                # Pas besoin de vérifier si 1er round, 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    print(f'\nC\'était le dernier round, le tournoi {self.last_tournament["name"]} a été clôturé avec succès.') 
                    print(f'\nVoici les résultats du tournoi : ') 
                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC231') 

                    print(f'\nEt les nouveaux scores des joueurs : ') 
                    self.report_players_from_tournament('firstname', 'last') 
                else: 
                    ### TODO: Vérifier : 
                    self.enter_new_round(False) # first_round 
                    # ret self.round_object 
                    
                    ### TODO : vérifier self.round_object 
                    print(f'self.round_object MC240 : {self.round_object}') 
                    # self.new_matches = self.round_object.matches 
                    # check the data 
                    # print(f'self.matches MC243 : {self.matches}') 
                    # for m in self.matches: 
                    #     print(f'm str MC616 : {m.__str__()}') 
                    
                    ### TODO: à vérifier : 
                    self.enter_new_matches(False) 
                    
                    ### TODO : vérifier self.matches 
                    self.round_object.matches.append(self.matches) 
                    # print(f'self.round_object MC195 : {self.new_round}') 
                    self.tournament_obj.rounds.append(self.round_object) 

                    if not self.tournament_obj.serialize_object(False): 
                        print('Il y a eu un problème. Essayez de recommencer et envoyez un feedback. Merci de votre compréhension.') 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                self.report_one_tournament('last') 
                session.prompt('\nAppuyez sur une touche pour continuer MC256') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', 'last') 

                session.prompt('Appuyez sur une touche pour continuer MC207') 
                self.start() 
            

            
            # TODO : à vérifier et nettoyer 
            # ==== Clôturer un tournoi ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '6': 
                self.board.ask_for_register = None 

                # close tournament : define the end_date # TODO ### 
                print('Clôturer le tournoi') 
                closing_tournament = self.in_view.input_closing_tournament() 

                last_tournament = self.select_one_tournament('last') 
                self.last_tournament = Tournament_model(**last_tournament) 

                # if (not closing_tournament == 'y') or (not closing_tournament == 'Y'): 
                if (closing_tournament != 'y') or (closing_tournament != 'Y'): 
                    print('*** La clôture du tournoi a été annulée. ***') 
                else: 
                    self.last_tournament.end_date = str(date.today()) 


                    if not self.last_tournament.serialize_object(False): 
                        print('Un problème est survenu, veuillez envoyer un feedback. Désolé pour les désagréments. ') 
                    else: 
                        print('Le tournoi a bien été cl$oturé. ') 

                    self.report_one_tournament('last') 
 
                session.prompt('Appuyez sur une touche pour continuer MC298') 
                self.start() 

                

            #### ======== T E S T  M E N U S ======== #### 

            # TEST # 
            ### 50 : Mettre à jour les scores des joueurs # TEST 
            if self.board.ask_for_register == '50': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.update_players_local_scores() 
                
                # close round : define the end_datetime # TODO ### 
                print('Clôturer le round') 

                # last_tournament = self.select_one_tournament('last') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    print(f'\nC\'était le dernier round, le tournoi {self.last_tournament["name"]} a été clôturé avec succès.') 
                    print(f'\nVoici les résultats du tournoi : ') 
                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyez sur une touche pour continuer MC322') 

                    print(f'\nEt les nouveaux scores des joueurs : ') 
                    self.report_players_from_tournament('firstname', 'last') 
                    session.prompt('\nAppuyez sur une touche pour continuer MC326') 
                else: 
                    #TODO: Tester define_next_rounds : 
                    self.enter_new_round(False) # first_round 
                    # return self.round_object 
                    # self.new_matches = self.round_object.matches 
                    self.enter_new_matches(False) 
                    # returns self.matches 
                    self.round_object.matches.append(self.matches) 
                    self.tournament_obj.rounds.append(self.round_object) 

                    if not self.tournament_obj.serialize_object(False): 
                        print('Il y a eu un problème. Essayez de recommencer et envoyez un feedback. Merci de votre compréhension.') 

                print(f'\nVoici les résultats provisoires du tournoi : ') 
                tournament_id = self.tournament_obj.id 
                self.report_one_tournament() 
                # self.report_one_tournament('last') 
                session.prompt('Appuyez sur une touche pour continuer MC344') 

                print(f'\nLes nouveaux scores des joueurs : ') 
                self.report_players_from_tournament('firstname', tournament_id) 
                # self.report_players_from_tournament('firstname', 'last') 
                session.prompt('Appuyez sur une touche pour continuer MC349') 

                # TODO: à vérifier, peut-être déjà visibles dans report_one_tournament('last) : 
                # print(f'\nLes matches du round {round.id+1} ont été définis : ') 
                session.prompt('Appuyez sur une touche pour continuer MC261') 

                self.start() # default=False 


            # TEST # enter new matches # ok 230707 
            # # auto quand on rentre les scores des matches d'un round 
            if self.board.ask_for_register == '7':  # TODO 
                self.board.ask_for_register = None 

                last_tournament = self.select_one_tournament('last') 
                self.tournament_obj = Tournament_model(**last_tournament) 

                if self.tournament_obj.rounds == []: 
                    self.enter_new_matches(True) # first_round 
                    # returns self.matches 
                else: 
                    self.last_round = self.last_tournament.rounds[-1] 

                    if self.last_round.id == self.tournament.rounds_left: 
                        print('\nC\'est le dernier round, pas de nouveaux matches') 
                        session.prompt('Appuyez sur une touche pour continuer MC319') 
                    else: 
                        self.enter_new_matches(False) 
                
                self.last_round.matches.append(self.matches) 
                self.tournament_obj.rounds.append(self.last_round) 

                if not self.tournament_obj.serialize_object(False): 
                    print('Il y a eu un problème. Essayez de recommencer et envoyez un feedback. Merci de votre compréhension. ') 

                self.report_one_tournament('last') 
                session.prompt('Appuyez sur une touche pour continuer MC324') 

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
    

    #### ============ R E P O R T S ============ #### 


    def report_all_players(self, sort, rev): # rev : reverse 
        """ 
            Displays the players from players.json. 
            parameters: 
                sort (str): 'id', 'firstname' or 'local_score', the name of the field on wich to sort the players. 
                rev (bool): if we have to reverse the list of objects. 
        """ 
        players = Player_model.get_registered_dict('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        # Choice of the order ('id' -> chronological, 'firstname' -> alphabetical or 'local_score' -> by score): 
        if sort == 'id': 
            print('\nJoueurs par ordre d\'enregistrement : ') 
            self.sort_objects_by_field(players_obj, 'id', rev) 
        if sort == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
            self.sort_objects_by_field(players_obj, 'firstname', rev) 
        if sort == 'score': 
            print('\nJoueurs par score : ') 
            self.sort_objects_by_field(players_obj, 'local_score', rev) 
        
        self.report_view.display_players(players_obj) 


    def report_players_from_tournament(self, field, tournament_id): 
        """ Displays the players of one tournament. 
        Args: 
            field (string): the field we will sort the players on. 
            tournament_id (int or 'last'): the id of the tournament. 
                For the last one, type 'last' ; 
        """ 
        tournament_dict = self.select_one_tournament(tournament_id) 
        tournament_obj = Tournament_model(**tournament_dict) 

        players_ids = tournament_obj.players 

        # ---- récupérer les joueurs et les instancier 
        players = [] 
        for player_id in players_ids: 
            player = self.select_one_player(player_id) 
            players.append(player) 
        players_objs = [Player_model(**player) for player in players] 

        # Choice of the order (id, alphabetical or by score): 
        if field == 'id': 
            print('\nJoueurs par ordre d\'id : ') 
        if field == 'firstname': 
            print('\nJoueurs par ordre alphabétique : ') 
        if field == 'score': 
            print('\nJoueurs par score : ') 
        self.sort_objects_by_field(players_objs, field) # sort 
        
        self.report_view.display_players(players_objs) 


    def report_one_player(self, player_id): 
        """ Displays one player from its id. 
        Args:
            player_id (int or 'last'): the player's id, or for the last one, type 'last'. 
        """ 
        self.select_one_player(player_id) 
        self.report_view.display_one_player() 


    def report_all_tournaments(self): 
        """ Displays all the registered tournaments. 
        """ 
        tournaments = Tournament_model.get_registered_dict('tournaments') 
        tournaments_obj = [] 

        for tournament in tournaments: 
            if 'rounds' not in tournament.keys(): 
                tournament['rounds'] = [] 
            self.tournament = Tournament_model(**tournament) 
            tournaments_obj.append(self.tournament) 
        
        self.report_view.display_tournaments(tournaments_obj) 


    def report_one_tournament(self, tournament_id): 
        """ Display one tournament from its id. 
            Args: 
                tournament_id (int or 'last'): the tournament's id, or 'last' for the last one. 
        """ 
        tournament = self.select_one_tournament(tournament_id) 
        last_tournament = Tournament_model(**tournament) 
        self.report_view.display_one_tournament(last_tournament) 
        

    def report_name_date_tournament(self, tournament_id): 
        """ Displays the name and the dates of the tournament. 
            Args:
                tournament_id (int or 'last'): the id of the tournament, or 'last' for the last one. 
        """
        tournament = self.select_one_tournament(tournament_id) 
        self.report_view.display_name_date_tournament(tournament) 


    def report_rounds(self, tournament_id): 
        """ Displays the rounds of a tournament. 
            Args:
                tournament_id (int or 'last'): the tournament's id or 'last' for the last one. 
        """
        tournament = self.select_one_tournament(tournament_id) 
        self.report_view.display_rounds_one_tournament(tournament) 



    #### ============ P L A Y E R S ============ #### 

    """ Register one player """  # ok 230507 
    def enter_new_player(self): 
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

        if not self.player.serialize_object(True): 
            print(f'Il y a eu un problème, veuillez recommencer ou envoyer un feedback. merci de votre compréhension. ') 
        else: 
            print(f'Le joueur a bien été enregistré. ') 
            self.report_one_player('last') 
        

    """ TODO: à vérifier """ 
    def enter_many_new_players(self): 
        """ 
            Calls the `enter_new_player` more than one time. 
        """ 
        player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 

        self.players = [] 
        while True: 
            player = self.enter_new_player() 
            self.players.append(player) 
            if (player_needed == 'y') or (player_needed == 'Y'): 
                return True 
            else: 
                return False 
        

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
                if self.player_obj.id == match[0][0] : 
                    player_input_score = match[0][1] 
                    
                elif self.player_obj.id == match[1][0]: 
                    player_input_score = match[1][1] 

                player_last_score += player_input_score 
                self.player_obj.local_score = player_last_score 

            # Register the new scores into players.json # ok 
            self.player_obj.serialize_object(True) ### à vérifier 
                


    def set_players_scores_to_zero(self): 
        """ At the begining of a tournament, add the players' local_scores ot their global_scores, and set the local scores to 0. 
        """ 
        players_dicts = Player_model.get_registered_dict('players') 
        self.players_objs = [Player_model(**player_dict) for player_dict in players_dicts] # à vérifier 

        for player_obj in self.players_objs: 
            player_obj.global_score += player_obj.local_score 
            player_obj.local_score = float(0) 
        
            player_obj.serialize_object(False) 



    #### ============ T O U R N A M E N T S ============ #### 
    

    def enter_new_tournament(self): 
        """ Register a new tournament with the data entered by the user. 
            returns: self.tournament_obj 
        """ 
        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 
        self.tournament_data['players'] = [int(player) for player in re.findall(r'\d+', self.tournament_data['players'])] 

        # Set the id relative to the last tournament: 
        self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 

        # Set 'rounds' = [] 
        self.tournament_data['rounds'] = [] 
        
        # Instantiate the current tournament: 
        self.tournament_obj = Tournament_model(**self.tournament_data) 
        return self.tournament_obj 


    def close_tournament(self): 
        """ If the auto closing of the tournament has been canceled, closes the tournament. 
        """ 
        today = datetime.today() 
        if not self.tournament_obj: 
            last_tournament = self.select_one_tournament('last') 
            self.tournament_obj = Tournament_model(**last_tournament)  
        
        closing_tournament = self.in_view.input_closing_tournament() 
        if closing_tournament == 'y': 
            # Set the end_date 
            self.tournament_obj.end_date = str(today) 
            self.tournament_obj.serialize_object(False) 
        else: 
            print(f'\nLa clôture du tournoi a été annulée, vous pourrez la relancer depuis le menu. ') 


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


    def enter_new_round(self, first_round): # first_round = bool 
        """ Register a new round with its data. 
            Args: 
                first_round (bool): if it is the first round. 
            Returns: self.round_object 
        """         
        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 
        if first_round: 
            round_data['id'] = 1 
        else: 
            round_data['id'] = int(self.tournament_obj.rounds[-1]['id']) + 1 
            if self.tournament_obj.rounds[-1].end_datetime == '': 
                self.tournament_obj.rounds[-1].end_datetime = datetime.now() 
        round_data['tournament_id'] = int(self.tournament_obj.id)+1 # à vérifier 

        self.tournament_obj.rounds.append(round_data) 
        self.new_round = self.tournament_obj.rounds[-1] 

        self.new_round.start_datetime = str(datetime.now()) 
        self.new_round.end_datetime = "" 
        self.new_round.matches = [] 

        self.round_object = Round_model(**self.new_round) 
        
        return self.round_object 


    #### ============ M A T C H E S ============ #### 

    def enter_scores(self): 
        """ Get the scores from the terminal and register them into the matches. 
        """ 
        # get the matches (list of lists) 
        current_matches_dicts = self.last_round.matches 

        # Get the matches (obj as tuples)  
        current_matches_list = [] 
        for curr_match in current_matches_dicts: 
            # print(f'curr_match MC780 : {curr_match}') 
            curr_match_tuple = tuple(curr_match) 
            # print(f'\ncurr_match_tuple MC749 : {curr_match_tuple}') 
            curr_match_obj = Match_model(curr_match_tuple) 
            current_matches_list.append(curr_match_obj) 
        
        # Get the input_scores for the registered matches 
        input_results = self.in_view.input_scores(current_matches_list) 
        print('---------------------') 

        # Get the differentiated data from the input 
        null_matches = input_results[0] 
        winners = input_results[1] 

        # Set the new scores of the matches 
        new_matches = [] 
        
        # Loop on null_matches and winners lists to update the scores into the matches (current_matches_list) 
        for null_match in null_matches: 
            for current_match in current_matches_list: 
                if current_match.player_1_id == null_match.player_1_id: 
                    current_match.player_1_score += float(0.5) 
                    current_match.player_2_score += float(0.5) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
        
        for winner in winners: 
            for current_match in current_matches_list: 
                if current_match.player_1_id == winner[0]: 
                    current_match.player_1_score += float(1) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
                elif current_match.player_2_id == winner[0]: 
                    current_match.player_2_score += float(1) 
                    new_matches.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 

        # Put back the rounds and the matches into the round 
        self.last_tournament.rounds[-1].matches = new_matches 
        
        # Serialize the tournament (new=False)  
        self.last_tournament.serialize_object(False) 

    
    """ comment """  
    def enter_new_matches(self, first_round): 
        """ Define and register the new matches. 
            Args:
                first_round (bool): if there is the matches of the first round. 
            Returns:
                self.matches (objects): the list of matches to register into the new round. 
        """ 
        self.tournament_players = self.tournament_obj.players  # list of objects 
        
        # Copy the players list to work with 
        players_copy = list(self.tournament_players) 
        
        # Get the data of the players_copy from the players.json file 
        players_dicts = Player_model.get_registered_dict('players') # dict 
        current_players = [] 
        player_copy_data = {} 
        for player_copy in players_copy: 
            for registered_player in players_dicts: 
                if registered_player['id'] == player_copy: 
                    player_copy_data = dict(**registered_player) 
                    current_players.append(player_copy_data) 
        players_obj = [Player_model(**data) for data in current_players] 

        if first_round: 
            selected = define_matches.random_matches(players_obj) 
        else: 
            selected = self.sort_objects_by_field(players_obj, 'local_score', True) 
        
        last_tournament = self.tournament_obj 
        new_matches = define_matches.make_peers(selected, False, last_tournament)  # first_round 

        self.matches = [Match_model(data) for data in new_matches] 

        return self.matches 
        


    #### ============ U T I L S ============ #### 

    def sort_objects_by_field(self, objects, field, reversed=False): 
        """ Sort the given objects dict by the given field. 
            Args: 
                objects (dict): the list of objects to sort. 
                field (string): the field which sort. 
                reversed (bool): if we have to reverse the result. Default False. 
            Returns objects 
        """ 
        objects.sort(key=attrgetter(field), reverse=reversed) 
        return objects 

    
    """ Select one tournament from JSON file """  ### peut-être à supprimer ??? 
    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournaments.json file. 
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
        """ Select one player from its id, from the players.json file. 
            Args:
                player_id (int): the player's id 
            Returns: 
                int: the player's id 
        """ 
        players_dicts = Player_model.get_registered_dict('players') 
        if player_id == 'last': 
            player = players_dicts.pop() 
        else: 
            player = players_dicts[player_id-1] 
        return player 

