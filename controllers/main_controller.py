
from utils import helpers 
from controllers.register_controller import Register_controller 
from controllers.report_controller import Report_controller 

from models.match_model import Match_model 
from models.player_model import Player_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from datetime import datetime, date 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Main_controller(): 

    def __init__( 
        self, 

        board: Dashboard_view, 
        in_view: Input_view, 
        report_view: Report_view, 

        report_controller: Report_controller, 
        register_controller: Register_controller, 
    ): 
        self.board = board 
        self.in_view = in_view 
        self.report_view = report_view 

        self.report_controller = report_controller 
        self.register_controller = register_controller 

        self.match = None 
        self.player = None 
        self.round = None 
        self.tournament = None 


    def start(self, new_session=False): 
        """ Displays the menus 
            Args:
                new_session (boolean), default=False. 
                    If True -> displays the menu and the welcome message, 
                    else -> displays only the menu. 
        """ 

        if new_session: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        # ======== "R E G I S T E R"  M E N U S ======== # 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            # ==== Registers one player ==== # 
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 

                print('\nEnregistrer un joueur') 
                self.register_controller.enter_new_player(self) 

                session.prompt('Appuyez sur entrée pour continuer MC71') 
                self.start() 

            # ==== Registers many new players ==== # 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                self.register_controller.enter_many_new_players(self) 

                self.start() 

            # ==== Registers one new tournament ==== # 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 

                print('\n\033[1mEnregistrer un tournoi\033[0m') 
                last_tournament = self.select_one_tournament('last') 
                tournament = Tournament_model(**last_tournament) 

                if last_tournament != {}: 
                    self.register_controller.set_players_scores_to_zero(tournament) 

                # Display registered players to select the current ones: 
                print('\033[1mVoici les joueurs enregistrés :\033[0m ') 
                self.report_controller.report_all_players('id', False) 

                # Prompt if needed to register a new player 
                player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                if player_needed == 'y': 
                    self.register_controller.enter_many_new_players(self) 

                self.register_controller.enter_new_tournament(self) 
                # returns self.tournament_obj (object) 

                print('\n\033[1mEnregistrer un nouveau round\033[0m') 
                self.register_controller.enter_new_round(True)  # first_round 
                # returns self.round_object (object) 

                self.tournament_obj.rounds.append(self.round_object)  # ### 

                # Get the tournament's players (dicts) 
                players_objs = self.select_tournament_players() 

                self.round_object = self.tournament_obj.rounds[-1] 
                if self.round_object.matches == []: 
                    self.selected = helpers.random_matches(players_objs) 
                    next_matches = self.register_controller.enter_new_matches(True)  # first_round 
                    # returns next_matches  (list of dicts) 

                    selected = self.selected 
                    self.starters = helpers.define_starters(selected, next_matches) 
                else: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 

                self.round_object.matches = next_matches  

                self.tournament_obj.serialize_object(True)  # True = new tournament 

                # Displays the last tournament  
                self.report_controller.report_one_tournament('last') 
                session.prompt('\nAppuyez sur entrée pour continuer MC124') 

                # Displays the starters 
                self.report_controller.report_starters(self) 
                session.prompt('\nAppuyez sur entrée pour continuer MC128') 

                self.start() 

            # ==== Registers new scores + close round ====
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 

                print('Enregistrer les scores') 

                # Get the last tournament (dict) 
                last_tournament = self.select_one_tournament('last') 

                # Instantiate it (obj) 
                self.tournament_obj = Tournament_model(**last_tournament) 

                # Get the last round (object) 
                self.last_round = self.tournament_obj.rounds.pop() 

                self.curr_players = self.select_tournament_players() 
                self.register_controller.enter_scores(self) 
                #  returns self.tournament_obj <-- à vérifier ### 

                # Register the players 
                self.registered_players_objs = self.register_controller.update_players_local_scores(self) 
                self.players_objs = self.select_tournament_players() 

                # Report the players 
                self.report_controller.report_players_from_tournament('score') 
                session.prompt('\nAppuyez sur entrée pour continuer ') 

                # close round : define the end_datetime 
                print('\nClôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                # if this is the last round: 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.register_controller.close_tournament(self) 

                    if not self.tournament_obj.serialize_object(False): 
                        print('''
                            Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                            Merci de votre compréhension. 
                        ''') 
                        session.prompt('Appuyez sur entrée pour continuer ') 
                    else: 
                        print(f'''
                            \nLe tournoi {self.tournament_obj.name} a été clôturé avec succès. 
                        ''') 

                    # Display the results 
                    print('\nVoici les résultats du tournoi : ') 
                    session.prompt('\nAppuyer sur entrée pour continuer ') 

                    self.report_controller.report_rounds('last') 

                    # Display the scores 
                    print('\nEt les nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyer sur entrée pour continuer ') 
                    self.report_controller.report_players_from_tournament('firstname') 
                    session.prompt('\nAppuyer sur entrée pour continuer ') 
                else: 
                    print('\nLe round a bien été clôturé, création d\'un nouveau round. ') 
                    self.register_controller.enter_new_round(False) 
                    # returns self.round_object 

                    self.players_objs = self.select_tournament_players() 
                    # returns List of objects 

                    self.selected = helpers.sort_objects_by_field(self.players_objs, 'local_score', True) 
                    next_matches = self.register_controller.enter_new_matches(False)  # first_round 
                    # returns next_matches  (dicts) 

                    self.starters = helpers.define_starters(self.selected, next_matches)  # ### 

                    # Displays the starters 
                    self.report_controller.report_starters(self) 
                    session.prompt('\nAppuyez sur entrée pour continuer ') 

                    self.matches = [Match_model(data) for data in next_matches] 

                    self.round_object.matches = self.matches 
                    self.tournament_obj.rounds.append(self.round_object) 

                    self.tournament_obj.serialize_object(False) 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC203') 
                    self.report_controller.report_rounds('last') 

                    print('\nLes nouveaux scores des joueurs : ') 
                    session.prompt('Appuyez sur entrée pour continuer ') 
                    self.report_controller.report_players_from_tournament('global_score') 
                    session.prompt('Appuyez sur entrée pour continuer ') 

                self.start() 

            # ==== Clôturer un round ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                # close round : define the end_datetime 
                print('\nClôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                tournament = self.select_one_tournament('last') 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.tournament_obj = Tournament_model(**tournament) 
                    self.last_round = self.tournament_obj.rounds[-1] 

                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC227') 

                # No need to check if this is the first round. 
                # If it is the last round: close the tournament 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.register_controller.close_tournament() 
                    print(f'''\nLe tournoi {self.tournament_obj.name} a été clôturé avec succès.''') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC281') 

                    # Display the results 
                    print('\nVoici les résultats du tournoi : ') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC285') 

                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC237') 

                    print('\nEt les nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC240') 
                    self.report_players_from_tournament('firstname') 
                    session.prompt('\nAppuyer sur entrée pour continuer MC242') 
                else: 
                    self.enter_new_round(False)  # first_round 
                    # returns self.round_object 

                    next_matches = self.enter_new_matches(True)  # first_round 
                    # returns next_matches  (dicts) 

                    self.starters = helpers.define_starters(players_objs, next_matches) 

                    # Displays the starters 
                    self.report_starters() 
                    session.prompt('\nAppuyez sur entrée pour continuer MC303') 

                    self.matches = [Match_model(data) for data in next_matches] 

                    self.round_object.matches = self.matches 
                    self.tournament_obj.rounds.append(self.round_object) 

                    if not self.tournament_obj.serialize_object(False): 
                        print('''\n
                            Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                            Merci de votre compréhension. 
                        ''') 
                        session.prompt('\nAppuyez sur entrée pour continuer MC254') 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    session.prompt('\nAppuyez sur entrée pour continuer MC257') 
                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyez sur entrée pour continuer MC259') 

                    print('\nLes nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyez sur entrée pour continuer MC262') 
                    self.report_players_from_tournament('firstname') 
                    session.prompt('Appuyez sur entrée pour continuer MC265') 

                self.start() 

            # ==== Clôturer un tournoi ==== # 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '6': 
                self.board.ask_for_register = None 

                # close tournament : define the end_date 
                print('Clôturer le tournoi') 
                closing_tournament = self.in_view.input_closing_tournament() 

                last_tournament = self.select_one_tournament('last') 
                self.last_tournament = Tournament_model(**last_tournament) 

                if (closing_tournament != 'y') or (closing_tournament != 'Y'): 
                    print('*** La clôture du tournoi a été annulée. ***') 
                    session.prompt('Appuyez sur entrée pour continuer MC265') 
                else: 
                    self.last_tournament.end_date = str(date.today()) 

                    if not self.last_tournament.serialize_object(False): 
                        print('Un problème est survenu, veuillez envoyer un feedback. Désolé pour les désagréments. ') 
                    else: 
                        print('Le tournoi a bien été clôturé. ') 
                        session.prompt('Appuyez sur entrée pour continuer MC292') 

                    print('Voici les résultats du tournoi : ') 
                    session.prompt('Appuyez sur entrée pour continuer MC295') 
                    self.report_one_tournament('last') 

                session.prompt('Appuyez sur entrée pour continuer MC298') 
                self.start() 

            # ============ COMMANDES DE SECOURS ============ # 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                self.start(False) 
                return True 

            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                Main_controller.close_the_app() 

        # ======== "R E P O R T"  M E N U S ======== # 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 

            # menu "afficher" : 
            self.board.display_report() 

            # Reports all players by firstname 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par prénom') 
                session.prompt('Appuyez sur entrée pour continuer MC432') 

                self.report_controller.report_all_players('firstname', False) 

                session.prompt('Appuyez sur entrée pour continuer ') 
                self.start()  # default=False 

            # Reports all players by scores 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par score dans le tournoi') 
                session.prompt('Appuyez sur entrée pour continuer MC444') 

                self.report_controller.report_all_players('score')  # rev=True default 

                session.prompt('Appuyez sur entrée pour continuer ') 
                self.start()  # default=False 

            # Reports all tournaments 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 

                print('Afficher les tournois') 
                self.report_controller.report_all_tournaments(self) 

                session.prompt('Appuyez sur entrée pour continuer MC352') 
                self.start()  # default=False 

            # Reports one tournament 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi') 
                tournament_id = session.prompt('Quel tournoi voulez-vous ? (son id ou "last" pour le dernier) ') 
                self.report_controller.report_one_tournament(tournament_id) 


                session.prompt('Appuyez sur entrée pour continuer MC365') 
                self.start()  # default=False 

            # Reports name and date of one tournament 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi') 
                tournament_id = session.prompt('''\nDe quel tournoi voulez-vous les nom et date ? 
                    (pour le dernier, tapez "last")''') 
                self.report_controller.report_name_date_tournament(tournament_id) 

                session.prompt('Appuyez sur entrée pour continuer MC388') 
                self.start()  # default=False 

            # Reports all players from one tournament 
            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs d\'un tournoi') 
                tournament_id = session.prompt('''\nDe quel tournoi voulez-vous les joueurs ? 
                    (pour le dernier, tapez "last")''') 

                # ---- 
                tournament_dict = self.select_one_tournament(tournament_id) 
                if tournament_dict == {}: 
                    print('Il n\'y a pas de tournoi à afficher.') 
                else: 
                    self.tournament_obj = Tournament_model(**tournament_dict) 
                # ---- 
                self.registered_players_objs = self.select_tournament_players() 
                self.report_controller.report_players_from_tournament('firstname') 

                session.prompt('Appuyez sur entrée pour continuer MC391') 
                self.start()  # default=False 

            # Reports rounds and matches of one tournament 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 

                print('Afficher les rounds et matches d\'un tournoi') 

                tournament_id = session.prompt('''De quel tournoi voulez-vous les tours ? (son id ou "last" 
                                               pour le dernier) ''') 
                self.report_controller.report_rounds(tournament_id) 
                session.prompt('Appuyez sur entrée pour continuer MC404') 

                self.start()  # default=False 


        # ============ COMMANDES DE SECOURS ============ # 

            """ Emergency command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                self.start(False) 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                Main_controller.close_the_app() 

        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            self.start(False) 


        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            Main_controller.close_the_app() 


    """ Command to quit the application """ 
    @staticmethod 
    def close_the_app(): 
        print('Fermeture de l\'application. Bonne fin de journée !') 


    # ============ U T I L S ============ # 


    def select_one_player(self, player_id): 
        """ Select one player from its id, from the players.json file. 
            Args:
                player_id (int): the player's id 
            Returns: 
                int: the player's id 
        """ 
        if Player_model.get_registered_dict('players') == []: 
            print('Il n\'y a pas de joueur à afficher. ') 
            return {} 
        else: 
            players_dicts = Player_model.get_registered_dict('players') 
            if player_id == 'last': 
                player = players_dicts.pop() 
            else: 
                player = players_dicts[player_id - 1] 
        return player 


    def select_tournament_players(self): 
        """ Selects the players of the `self.tournament_obj` 
            already selected into the precedent method. 

            Returns:
                list of Player_models: Returns a list of objects Player, stored in Main_controller. 
        """
        players_ids = self.tournament_obj.players 

        players = [] 
        for player_id in players_ids: 
            player = self.select_one_player(player_id) 
            players.append(player) 
        self.players_objs = [Player_model(**player) for player in players] 
        return self.players_objs  # list of objects 


    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournaments.json file. 
            Args:
                t_id (int): the tournament's id 
            Returns:
                int: the tournament's id 
        """ 
        if Tournament_model.get_registered_dict('tournaments') == []: 
            return {} 
        else: 
            t_dicts = Tournament_model.get_registered_dict('tournaments') 

            if t_id == 'last': 
                t_dict = t_dicts.pop() 
            else: 
                t_dict = t_dicts[int(t_id) - 1] 
            return t_dict 

