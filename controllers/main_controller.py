
# import pdb
# import logging

from utils import helpers 
from controllers.register_controller import Register_controller 
from controllers.report_controller import Report_controller 

from models.match_model import Match_model 

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

        register_controller: Register_controller, 
        report_controller: Report_controller, 
    ): 
        self.board = board 
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

        # Check if a tournament isn't already closed, 
        # then set the new_session to False, 
        # else set it to True. 
        last_tournament = helpers.select_one_tournament('last') 
        if last_tournament.end_date == '': 
            new_session = False 
        else: 
            new_session = True 
            last_tournament = None 

        if new_session: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        # ======== "R E G I S T E R"  M E N U S ======== # 

        # ==== menu "enregistrer" ==== # 
        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 

            # Display only the useful menus 
            if new_session: 
                self.board.display_register([0, 1, 2, 3]) 
            else: 
                items = [] 
                items.append(0) 
                for i in range(4, 7): 
                    items.append(i) 
                self.board.display_register(items) 

            # ==== Registers one player ==== # 
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 

                print('\nEnregistrer un joueur') 
                self.register_controller.enter_new_player() 
                # serializes player 

                self.press_enter_to_continue() 
                self.start() 

            # ==== Registers many new players ==== # 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                self.register_controller.enter_many_new_players() 

                self.start() 

            # ==== Registers one new tournament ==== # 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 

                print('\n\033[1mEnregistrer un nouveau tournoi\033[0m') 

                # Sets the players' scores of the last tournament to zero. 
                last_tournament_obj = helpers.select_one_tournament('last') 
                if last_tournament_obj is not None: 
                    self.register_controller.set_players_scores_to_zero(last_tournament_obj) 
                    # serializes each player 
                last_tournament_obj = None 

                all_players = helpers.select_all_players() 

                # Displays registered players to select the current ones: 
                print('\033[1mVoici les joueurs enregistrés :\033[0m ') 
                self.report_controller.report_all_players(all_players, 'id')  # rev=False 

                # Prompt if needed to register a new player 
                player_needed = self.in_view.input_yes_or_no('Enregistrer un nouveau joueur ?') 
                # player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                if player_needed == 'y' or player_needed == 'Y': 
                    self.register_controller.enter_many_new_players() 

                tournament_obj = self.register_controller.enter_new_tournament(last_tournament_obj) 
                # returns object 

                print('\n\033[1mEnregistrer un nouveau round\033[0m') 
                round_object = self.register_controller.enter_new_round(True, tournament_obj)  # first_round 
                # returns object 

                matches = [] 
                round_object.matches = matches 

                tournament_obj.rounds.append(round_object) 

                if not tournament_obj.serialize_object(False): 
                    print(''' 
                        Il y a eu un problème, veuillez recommencer ou envoyer un feedback. 
                        Merci de votre compréhension. 
                    ''') 

                # Get the tournament's players (objects) 
                players_objs = helpers.select_tournament_players('last') 

                # Adds the matches to the tournament 
                if round_object.matches == []: 
                    print('Define matches first round ') 
                    selected = helpers.random_matches(players_objs) 
                    next_matches = self.register_controller.enter_new_matches(True, tournament_obj)  # first_round 
                    # returns next_matches  (list of objects) 

                    starters = helpers.define_starters(selected, next_matches) 
                else: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 

                round_object.matches = next_matches  

                # self.tournament_obj.serialize_object(True)  # True = new object 
                if not tournament_obj.serialize_object(False):  # False = not new object 
                    print(''' 
                        Il y a eu un problème, veuillez recommencer ou envoyer un feedback. 
                        Merci de votre compréhension. 
                    ''') 
                else: 
                    print('\nLe tournoi a bien été enregistré. ') 

                    # Displays the last tournament  
                    new_tournament_obj = self.report_controller.report_one_tournament('last') 
                    self.press_enter_to_continue() 

                    self.report_controller.report_players_from_tournament('tournament_score', new_tournament_obj.id) 

                    # Displays the starters 
                    self.report_controller.report_starters(starters) 
                    self.press_enter_to_continue() 

                self.start() 

            # ==== Enregistrer les scores ====
            if self.board.ask_for_register == '4': 
                """ Registers new scores, 
                    closes round, 
                    opens new round 
                    & defines new matches. 
                    Closes tournament if needed. 
                """ 
                self.board.ask_for_register = None 

                print('Enregistrer les scores') 

                # Get the last tournament (obj) 
                tournament_obj = helpers.select_one_tournament('last') 

                # if last_tournament_obj is not None: 
                if not tournament_obj: 
                    print('''
                        Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                        Merci de votre compréhension. 
                    ''') 
                else: 
                    self.register_controller.enter_scores(tournament_obj) 
                    # serializes tournament  

                    # Register the players round scores 
                    players_objs = self.register_controller.update_players_round_scores(tournament_obj) 
                    # serializes players 

                    # Report the players scores for the last round 
                    self.report_controller.report_round_results('last') 
                    self.press_enter_to_continue() 

                    # Register the players tournament scores  
                    self.register_controller.update_players_tournament_scores(tournament_obj) 
                    # serializes players 

                    # close round : define the end_datetime 
                    print('\nClôturer le round') 
                    last_round = tournament_obj.rounds.pop() 
                    closing_round = self.in_view.input_closing_round() 
                    if (closing_round == 'y') or (closing_round == 'Y'): 
                        last_round.end_datetime = str(datetime.now()) 
                    else: 
                        print('''*** 
                            La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. *** 
                            ''') 
                    tournament_obj.rounds.append(last_round) 
                    if not tournament_obj.serialize_object(False): 
                        print(''' 
                            Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                            Merci de votre compréhension. 
                        ''') 
                    else: 
                        print(f'''
                            \nLe round {tournament_obj.rounds[-1].round_name} a été clôturé avec succès. 
                        ''') 

                    # if this is the last round: 
                    if last_round.id == tournament_obj.rounds_left: 
                        self.register_controller.close_tournament(tournament_obj) 
                        # serializes tournament 

                        # Display the results 
                        print('\nVoici les résultats du tournoi : ') 
                        self.report_controller.report_one_tournament('last') 
                        self.press_enter_to_continue() 

                    else: 
                        tournament_obj.serialize_object(False) 
                        print('\nLe round a bien été clôturé, création d\'un nouveau round : ') 
                        round_obj = self.register_controller.enter_new_round(False, tournament_obj) 

                        """ Sort the players by tournament_score to define the next matches """ 
                        selected = helpers.sort_objects_by_field(players_objs, 'tournament_score', True) 
                        next_matches = self.register_controller.enter_new_matches(False, tournament_obj) 
                        # False : first_round 

                        # Displays the new matches 
                        print('\n\033[1mLes prochains matches : \033[0m ') 
                        for next in next_matches: 
                            print(f'{next[1][0]} contre {next[0][0]}') 

                        if next_matches and not isinstance(next_matches[0], Match_model): 
                            matches = [Match_model(data) for data in next_matches] 
                        else: 
                            matches = next_matches 

                        round_obj.matches = matches 

                        tournament_obj.serialize_object(False) 

                        last_tournament = helpers.select_one_tournament('last') 
                        new_matches = last_tournament.rounds[-1].matches 
                        starters = helpers.define_starters(selected, new_matches) 

                        # Displays the starters 
                        self.report_controller.report_starters(starters) 
                        self.press_enter_to_continue() 

                self.start() 

            # ==== Clôturer un round ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                # close round : define the end_datetime 
                print('\nClôturer le round en cours') 
                closing_round = self.in_view.input_closing_round() 
                tournament_obj = helpers.select_one_tournament('last') 
                if not (closing_round == 'y') or (closing_round == 'Y'): 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 
                    self.press_enter_to_continue() 
                else: 
                    self.last_round = tournament_obj.rounds[-1] 
                    self.last_round.end_datetime = str(datetime.now()) 

                # No need to check if this is the first round. 

                # If it is the last round: close the tournament 
                if self.last_round.id == tournament_obj.rounds_left: 
                    self.register_controller.close_tournament(tournament_obj) 
                    # serializes tournament_obj 
                    # print(f'''\nLe tournoi {tournament_obj.name} a été clôturé avec succès.''') 
                    self.press_enter_to_continue() 

                    # Displays the results 
                    print('\nVoici les résultats du tournoi : ') 
                    self.press_enter_to_continue() 
                    last_tournament_obj = self.report_controller.report_one_tournament('last') 
                    self.press_enter_to_continue() 

                    print('\nEt les nouveaux scores des joueurs : ') 
                    self.press_enter_to_continue() 
                    self.report_controller.report_players_from_tournament('tournament_score', last_tournament_obj.id) 
                    self.press_enter_to_continue() 
                else: 
                    round_object = self.enter_new_round(False)  # first_round 
                    # serializes tournament 

                    next_matches = self.enter_new_matches(True, tournament_obj)  # first_round 
                    # does not serialize tournament 

                    round_object.matches = matches 
                    tournament_obj.rounds.append(round_object) 

                    if not tournament_obj.serialize_object(False): 
                        print('''\n
                            Il y a eu un problème. Essayez de recommencer et envoyez un feedback. 
                            Merci de votre compréhension. 
                        ''') 
                        self.press_enter_to_continue() 

                    # à tester ### 
                    starters = helpers.define_starters(players_objs, tournament_obj.rounds[-1].matches) 

                    # Displays the starters 
                    self.report_controller.report_starters(starters) 
                    self.press_enter_to_continue() 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    self.press_enter_to_continue() 
                    self.report_controller.report_one_tournament('last') 
                    self.press_enter_to_continue() 

                    print('\nLes nouveaux scores des joueurs : ') 
                    self.press_enter_to_continue() 
                    self.report_controller.report_players_from_tournament('tournament_score', 'last') 
                    self.press_enter_to_continue() 

                self.start() 


            # ==== Clôturer un tournoi ==== # 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '6': 
                self.board.ask_for_register = None 

                # close tournament : define the end_date 
                print('Clôturer le tournoi') 
                closing_tournament = self.in_view.input_closing_tournament() 

                tournament_obj = helpers.select_one_tournament('last') 
                # self.tournament_obj = helpers.select_one_tournament('last') 

                if not (closing_tournament == 'y') or (closing_tournament == 'Y'): 
                    print(closing_tournament) 
                    print(type(closing_tournament)) 
                    print('''*** La clôture du tournoi a été annulée. \
                        Vous pourrez clôturer le tournoi depuis le menu. *** \
                    ''') 
                    self.press_enter_to_continue() 
                else: 
                    tournament_obj.end_date = str(date.today()) 
                    # self.tournament_obj.end_date = str(date.today()) 

                    # if not self.tournament_obj.serialize_object(False): 
                    if not tournament_obj.serialize_object(False): 
                        print('Un problème est survenu, veuillez envoyer un feedback. Désolé pour les désagréments. ') 
                        self.press_enter_to_continue() 
                    else: 
                        print('Le tournoi a bien été clôturé. ') 
                        self.press_enter_to_continue() 

                    print('Voici les résultats du tournoi : ') 
                    self.press_enter_to_continue() 
                    self.report_controller.report_one_tournament('last') 

                self.press_enter_to_continue() 
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
                self.press_enter_to_continue() 

                self.report_controller.report_all_players(None, 'firstname') 

                self.press_enter_to_continue() 
                self.start()  # default=False 


            # Reports all players by INE scores 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par score INE') 
                self.press_enter_to_continue() 

                self.report_controller.report_all_players(None, 'score') 

                self.press_enter_to_continue() 
                self.start()  # default=False 


            # Reports all tournaments 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 

                print('Afficher les tournois') 
                self.report_controller.report_all_tournaments(None) 

                self.press_enter_to_continue() 
                self.start()  # default=False 

            # Reports one tournament 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi') 
                tournament_id = self.in_view.input_object_id('tournoi') 
                # tournament_id = session.prompt('Quel tournoi voulez-vous ? (son id ou "last" pour le dernier) ') 
                self.report_controller.report_one_tournament(tournament_id) 


                self.press_enter_to_continue() 
                self.start()  # default=False 

            # Reports name and date of one tournament 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 

                print('Afficher le nom et la date d\'un tournoi') 
                tournament_id = self.in_view.input_object_id('tournoi') 
                # tournament_id = session.prompt('''\nDe quel tournoi voulez-vous les nom et date ? 
                #     (pour le dernier, tapez "last")''') 
                self.report_controller.report_name_date_tournament(tournament_id) 

                self.press_enter_to_continue() 
                self.start()  # default=False 

            # Reports all players from one tournament 
            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs d\'un tournoi') 
                tournament_id = self.in_view.input_object_id('tournoi') 
                # tournament_id = session.prompt('''\nDe quel tournoi voulez-vous les joueurs ? 
                #     (pour le dernier, tapez "last")''') 

                self.report_controller.report_players_from_tournament('id', tournament_id) 

                self.press_enter_to_continue() 
                self.start()  # default=False 

            # Reports rounds and matches of one tournament 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 

                print('Afficher les rounds et matches d\'un tournoi') 

                tournament_id = self.in_view.input_object_id('tournoi') 
                # tournament_id = session.prompt('''De quel tournoi voulez-vous les tours ? (son id ou "last" 
                #                                pour le dernier) ''') 
                self.report_controller.report_rounds(tournament_id) 
                self.press_enter_to_continue() 

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

        """ Emergency command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            self.start() 


        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            Main_controller.close_the_app() 

        # ============ COMMANDES DE TESTS - REGISTER ============ # 

        # ==== TEST : mettre tous les scores à 0 - TEST ==== # 
        if self.board.ask_for_menu_action == '10': 
            self.board.ask_for_menu_action = None 

            tournament_obj = helpers.select_one_tournament('last') 

            self.register_controller.set_players_scores_to_zero(tournament_obj) 

            self.report_controller.report_players_from_tournament('id', tournament_obj.id) 

            self.start() 

        # ==== TEST : enter_new_matches  TEST ==== # 
        if self.board.ask_for_menu_action == '11': 
            self.board.ask_for_menu_action = None 

            # print(f'dir(self) MC378 : {dir(self)}') 
            first = session.prompt('1er round ? Y/n ') 

            self.tournament_obj = helpers.select_one_tournament('last') 

            if (first == 'y') | (first == 'Y') | (first == ''): 
                self.register_controller.enter_new_matches(True, self.tournament_obj) 
            if (first == 'n') | (first == 'N'): 
                self.register_controller.enter_new_matches(False, self.tournament_obj) 

            self.start() 


        # ==== TEST : enter_new_round  TEST ==== # 
        if self.board.ask_for_menu_action == '12': 
            self.board.ask_for_menu_action = None 

            # print(f'dir(self) MC562 : {dir(self)}') 
            first = session.prompt('1er round ? Y/n ') 
            tournament_obj = helpers.select_one_tournament('last') 
            if (first == 'y') | (first == 'Y') | (first == ''): 
                tournament_obj = self.register_controller.enter_new_round(True, tournament_obj) 
            else: 
                tournament_obj = self.register_controller.enter_new_round(False, tournament_obj) 
            print(f'last_tournament MC566 : {last_tournament}') 
            last_tournament = helpers.select_one_tournament('last') 
            print(f'tournament_obj MC568 : {tournament_obj}') 

            if (first == 'y') | (first == 'Y') | (first == ''): 
                self.register_controller.enter_new_matches(True, tournament_obj) 
            if (first == 'n') | (first == 'N'): 
                self.register_controller.enter_new_matches(False, tournament_obj) 

            self.start() 

        # ============ COMMANDES DE TESTS - REPORTS ============ # 

        # TEST : Reports one player  TEST #  
        if self.board.ask_for_menu_action == '20': 
            self.board.ask_for_menu_action = None 

            print('Le dernier joueur enregistré : ') 
            self.report_controller.report_one_player('last') 

            self.press_enter_to_continue() 
            self.start()  # default=False 


        # ==== TEST : report_all_players  TEST ==== # 
        if self.board.ask_for_menu_action == '21': 
            self.board.ask_for_menu_action = None 

            self.report_controller.report_all_players(None, 'id', False) 
            self.press_enter_to_continue() 

            self.start() 


        # ==== TEST : report_tournament_players  TEST ==== # 
        if self.board.ask_for_menu_action == '22': 
            self.board.ask_for_menu_action = None 

            self.report_controller.report_players_from_tournament('id', 'last') 
            self.press_enter_to_continue() 

            self.start() 

    """ Command to action for continuing """ 
    @staticmethod 
    def press_enter_to_continue(): 
        session.prompt('Appuyez sur entrée pour continuer ') 

    """ Command to quit the application """ 
    @staticmethod 
    def close_the_app(): 
        print('Fermeture de l\'application. Bonne fin de journée !') 

