
from utils import helpers 
from controllers.register_controller import Register_controller 
from controllers.report_controller import Report_controller 

from models.match_model import Match_model 
from models.player_model import Player_model 
# from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from datetime import datetime, date 
# from operator import attrgetter 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Main_controller(): 

    def __init__( 
        self, 
        board: Dashboard_view, 

        # match_model: Match_model, 
        # # player_model: Player_model, 
        # # round_model: Round_model, 
        # tournament_model: Tournament_model, 

        in_view: Input_view, 
        report_view: Report_view, 
        register_controller: Register_controller, 
        report_controller: Report_controller, 
    ): 
        self.board = board 

        # self.match_model 
        # self.tournament_model 

        self.in_view = in_view 
        self.report_view = report_view 
        self.register_controller = register_controller 
        self.report_controller = report_controller 

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
                # input_player = self.in_view.input_player() 
                self.register_controller.enter_new_player(self) 
                # self.register_controller.enter_new_player(self, input_player) 

                session.prompt('Appuyez sur une touche pour continuer MC71') 
                self.start() 

            # ==== Registers many new players ==== # 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                # input_player = self.in_view.input_player() 
                self.register_controller.enter_many_new_players(self) 

                self.start() 

            # ==== Registers one new tournament ==== # 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 

                print('\n\033[1mEnregistrer un tournoi\033[0m') 
                last_tournament = self.select_one_tournament('last') 
                tournament = Tournament_model(**last_tournament) 

                # à changer : ### 
                if last_tournament != {}: 
                    self.register_controller.set_players_scores_to_zero(self, tournament) 

                # Display registered players to select the current ones: 
                print('\033[1mVoici les joueurs enregistrés :\033[0m ') 
                self.report_controller.report_all_players(self, 'id', False) 

                # Prompt if needed to register a new player 
                player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                if player_needed == 'y': 
                    self.register_controller.enter_many_new_players(self) 

                self.register_controller.enter_new_tournament(self) 
                # returns self.tournament_obj (object) 

                print('\n\033[1mEnregistrer un nouveau round\033[0m') 
                self.register_controller.enter_new_round(self, True)  # first_round 
                # returns self.round_object (object) 

                self.tournament_obj.rounds.append(self.round_object) 

                # Get the tournament's players (dicts) 
                players_objs = self.select_tournament_players() 
                # current_players = self.select_tournament_players() 

                self.round_object = self.tournament_obj.rounds[-1] 
                if self.round_object.matches == []: 
                    self.selected = helpers.random_matches(players_objs) 
                    next_matches = self.register_controller.enter_new_matches(self, True)  # first_round 
                    # returns next_matches  (list of dicts) 

                    selected = self.selected 
                    self.starters = helpers.define_starters(selected, next_matches) 
                else: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 

                self.round_object.matches = next_matches  

                self.tournament_obj.serialize_object(True)  # True = new tournament 

                # Displays the last tournament  
                self.report_controller.report_one_tournament(self, 'last') 
                session.prompt('\nAppuyez sur une touche pour continuer MC124') 

                # Displays the starters 
                self.report_controller.report_starters(self) 
                session.prompt('\nAppuyez sur une touche pour continuer MC128') 

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

                self.register_controller.enter_scores(self) 
                #  returns self.tournament_obj <-- à vérifier ### 

                # ---- 
                # """ Update the players' scores into players.json """ 
                # # Get registered players local_scores 
                # p_dicts = Player_model.get_registered_dict('players') 
                # # Instantiate the players 
                # players_objs = [Player_model(**data) for data in p_dicts] 
                # for player_obj in players_objs: 
                #     for match in self.last_round.matches: 
                #         if player_obj.id == match.player_1_id: 
                #             player_obj.local_score += match.player_1_score 

                #         elif player_obj.id == match.player_2_id: 
                #             player_obj.local_score += match.player_2_score 

                # # players_objs = self.players_objs 
                # self.helpers.sort_objects_by_field(players_objs, 'id') 

                # # Register the new scores into players.json 
                # for self.player in players_objs: 
                #     self.player_obj.serialize_object(False) 
                # ---- 
                # self.select_tournament_players() 

                # ---- 
                # # tournament_dict = self.select_one_tournament(tournament_id) 
                # # tournament_dict = self.select_one_tournament('last') 
                # self.players_objs = self.tournament_obj.players 

                # Register the players 
                self.registered_players_objs = self.register_controller.update_players_local_scores(self) 
                self.players_objs = self.select_tournament_players() 
                # Report the players 
                self.report_controller.report_players_from_tournament(self, 'score') 
                session.prompt('\nAppuyez sur une touche pour continuer MC160') 

                # close round : define the end_datetime 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                # if this is the last round: 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 

                    if not self.tournament_obj.serialize_object(False): 
                        print('''
                        Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                        Merci de votre compréhension. ''') 
                        session.prompt('Appuyez sur une touche pour continuer MC237') 
                    else: 
                        print(f'''
                        \nLe tournoi {self.tournament_obj["name"]} a été clôturé avec succès. 
                        ''') 
                        session.prompt('\nAppuyer sur une touche pour continuer MC178') 

                    # Display the results 
                    print('\nVoici les résultats du tournoi : ') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC180') 

                    self.report_rounds('last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC182') 

                    # Display the scores 
                    print('\nEt les nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC185') 
                    self.report_players_from_tournament('firstname', 'last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC187') 
                else: 
                    print('Le round a bien été clôturé, création d\'un nouveau round. ') 
                    self.register_controller.enter_new_round(self, False) 
                    # returns self.round_object 

                    # ---- 
                    # tournament_players = self.tournament_obj.players  # list of ints 

                    # # Copy the players list to work with 
                    # players_copy = list(tournament_players) 

                    # # Get the data of the players_copy from the players.json file 
                    # players_dicts = Player_model.get_registered_dict('players')  # dict 
                    # current_players = [] 
                    # player_copy_data = {} 
                    # for player_copy in players_copy: 
                    #     for registered_player in players_dicts: 
                    #         if registered_player['id'] == player_copy: 
                    #             player_copy_data = dict(**registered_player) 
                    #             current_players.append(player_copy_data) 
                    # self.players_obj = [Player_model(**data) for data in current_players] 

                    self.players_objs = self.select_tournament_players() 
                    # returns List of objects 

                    # players_obj = self.players_objs 
                    # self.selected = helpers.sort_objects_by_field(players_obj, 'local_score', True) 
                    self.selected = helpers.sort_objects_by_field(self.players_objs, 'local_score', True) 
                    # # self.selected = helpers.sort_objects_by_field(self.players_obj, 'local_score', True) 
                    # ---- 
                    next_matches = self.register_controller.enter_new_matches(self, False)  # first_round 
                    # returns next_matches  (dicts) 

                    # players = [] 
                    # for player in self.tournament_obj.players: 
                    #     player = self.select_one_player(player) 
                    #     players.append(player) 

                    self.starters = helpers.define_starters(self.selected, next_matches) 
                    # self.starters = helpers.define_starters(players_objs, next_matches) 
                    # self.starters = helpers.define_starters(players, next_matches) 
                    print(f'self.starters : {self.starters}') 
                    # Displays the starters 
                    self.report_controller.report_starters(self) 
                    session.prompt('\nAppuyez sur une touche pour continuer MC128') 

                    self.matches = [Match_model(data) for data in next_matches] 

                    self.round_object.matches = self.matches 
                    self.tournament_obj.rounds.append(self.round_object) 

                    self.tournament_obj.serialize_object(False) 
                    # session.prompt('Appuyez sur une touche pour continuer MC237') 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    self.report_rounds('last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC203') 

                    print('\nLes nouveaux scores des joueurs : ') 
                    self.report_controller.report_players_from_tournament(self, 'id', 'last') 
                    session.prompt('Appuyez sur une touche pour continuer MC217') 

                self.start() 

            # ==== Clôturer un round ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                # close round : define the end_datetime 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    tournament = self.select_one_tournament('last') 
                    self.tournament_obj = Tournament_model(**tournament) 
                    self.last_round = self.tournament_obj.rounds[-1] 
                    # print(f'self.tournament_obj MC249 : {self.tournament_obj}') 

                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC227') 

                # No need to check if this is the first round. 
                # If it is the last round: close the tournament 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    last_tournament = self.select_one_tournament('last') 
                    print(f'''\nLe tournoi {last_tournament["name"]} a été clôturé avec succès.''') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC233') 

                    # Display the results 
                    print('\nVoici les résultats du tournoi : ') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC235') 

                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC237') 

                    print('\nEt les nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC240') 
                    self.report_players_from_tournament('firstname', 'last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC242') 
                else: 
                    self.enter_new_round(False)  # first_round 
                    # returns self.round_object 

                    next_matches = self.enter_new_matches(True)  # first_round 
                    # returns next_matches  (dicts) 

                    self.starters = helpers.define_starters(players_objs, next_matches) 

                    # Displays the starters 
                    self.report_starters() 
                    session.prompt('\nAppuyez sur une touche pour continuer MC303') 

                    self.matches = [Match_model(data) for data in next_matches] 

                    self.round_object.matches = self.matches 
                    self.tournament_obj.rounds.append(self.round_object) 

                    if not self.tournament_obj.serialize_object(False): 
                        end_of_phrase = 'Merci de votre compréhension.' 
                        print(f'Il y a eu un problème. Essayez de recommencer et envoyez un feedback. {end_of_phrase}') 
                        session.prompt('\nAppuyez sur une touche pour continuer MC254') 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    session.prompt('\nAppuyez sur une touche pour continuer MC257') 
                    self.report_one_tournament('last') 
                    session.prompt('\nAppuyez sur une touche pour continuer MC259') 

                    print('\nLes nouveaux scores des joueurs : ') 
                    session.prompt('\nAppuyez sur une touche pour continuer MC262') 
                    self.report_players_from_tournament('firstname', 'last') 
                    session.prompt('Appuyez sur une touche pour continuer MC265') 

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
                    session.prompt('Appuyez sur une touche pour continuer MC265') 
                else: 
                    self.last_tournament.end_date = str(date.today()) 

                    if not self.last_tournament.serialize_object(False): 
                        print('Un problème est survenu, veuillez envoyer un feedback. Désolé pour les désagréments. ') 
                    else: 
                        print('Le tournoi a bien été clôturé. ') 
                        session.prompt('Appuyez sur une touche pour continuer MC292') 

                    print('Voici les résultats du tournoi : ') 
                    session.prompt('Appuyez sur une touche pour continuer MC295') 
                    self.report_one_tournament('last') 

                session.prompt('Appuyez sur une touche pour continuer MC298') 
                self.start() 

            # ============ COMMANDES DE SECOURS ============ # 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                self.start() 
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
                session.prompt('Appuyez sur une touche pour continuer MC432') 

                self.report_controller.report_all_players(self, 'firstname', False) 

                session.prompt('Appuyez sur une touche pour continuer ') 
                self.start()  # default=False 

            # Reports all players by scores 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par score dans le tournoi') 
                session.prompt('Appuyez sur une touche pour continuer MC444') 
                # print('Afficher les joueurs par score') 
                self.report_controller.report_all_players(self, 'score')  # rev=True default 
                # self.report_controller.report_all_players(self, 'score', True) 

                session.prompt('Appuyez sur une touche pour continuer ') 
                self.start()  # default=False 

            # Reports all tournaments 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 

                print('Afficher les tournois') 
                self.report_controller.report_all_tournaments(self) 

                session.prompt('Appuyez sur une touche pour continuer MC352') 
                self.start()  # default=False 

            # Reports one tournament 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi') 
                tournament_id = session.prompt('Quel tournoi voulez-vous ? (son id ou "last" pour le dernier) ') 
                self.report_controller.report_one_tournament(self, tournament_id) 

                # print('Classement des joueurs pour ce tournoi : ')
                # self.report_players_from_tournament('score', tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC365') 
                self.start()  # default=False 

            # Reports name and date of one tournament 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi') 
                tournament_id = session.prompt('''\nDe quel tournoi voulez-vous les nom et date ? 
                    (pour le dernier, tapez "last")''') 
                self.report_controller.report_name_date_tournament(self, tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC388') 
                self.start()  # default=False 

            # Reports all players from one tournament  # ok 231010 
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
                # self.report_players_from_tournament('firstname', tournament_id) 
                self.report_controller.report_players_from_tournament(self, 'firstname') 

                session.prompt('Appuyez sur une touche pour continuer MC391') 
                self.start()  # default=False 

            # Reports rounds and matches of one tournament 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 

                print('Afficher les rounds et matches d\'un tournoi') 

                tournament_id = session.prompt('''De quel tournoi voulez-vous les tours ? (son id ou "last" 
                                               pour le dernier) ''') 
                self.report_controller.report_rounds(self, tournament_id) 
                session.prompt('Appuyez sur une touche pour continuer MC404') 

                self.start()  # default=False 


        # ============ COMMANDES DE SECOURS ============ # 

            """ Emergency command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                self.start() 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                Main_controller.close_the_app() 

        # corriger la commande "*" partout 
        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            self.start() 

            # return True # <-- ça fait quoi ça ? ### 

        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            Main_controller.close_the_app() 

            # return False # <-- ça fait quoi ça ? ### 

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
        # if self.player.get_registered_dict('players') == []: 
        if Player_model.get_registered_dict('players') == []: 
            print('Il n\'y a pas de joueur à afficher. ') 
            return {} 
        else: 
            players_dicts = Player_model.get_registered_dict('players') 
            # players_dicts = self.player.get_registered_dict('players') 
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
        # ---- 
        print(f'self.tournament_obj MC504 : {self.tournament_obj}') 
        players_ids = self.tournament_obj.players 
        # ---- récupérer les joueurs et les instancier ---- # 
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
                # t_dict = t_dicts[t_id - 1] 
            return t_dict 

