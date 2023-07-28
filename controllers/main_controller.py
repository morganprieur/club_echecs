
from controllers import define_matches  

from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

# import random 
import re 

from datetime import datetime, date 
from operator import attrgetter 
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

        # ======== "R E G I S T E R"  M E N U S ======== # 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            # ==== Register one player ==== # 
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 

                print('\nEnregistrer un joueur') 
                self.enter_new_player() 

                session.prompt('Appuyez sur une touche pour continuer MC71') 
                self.start() 

            # ==== Register many new players ==== # 
            if self.board.ask_for_register == '2': 
                self.board.ask_for_register = None 

                print('\nEnregistrer plusieurs joueurs') 
                self.enter_many_new_players() 

                # session.prompt('Appuyez sur une touche pour continuer MC93') 
                self.start() 

            # ==== Register new tournament ==== # 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 

                print('\n\033[1mEnregistrer un tournoi\033[0m') 
                last_tournament = self.select_one_tournament('last') 
                tournament = Tournament_model(**last_tournament) 
                # if Tournament_model.get_registered_dict('tournament') != []: 
                # Set the global_scores to the last local_scores, 
                # and the local_scores to zero
                if last_tournament != {}: 
                    self.set_players_scores_to_zero(tournament) 

                # Display registered players to select the current ones: 
                print('\033[1mVoici les joueurs enregistrés :\033[0m ') 
                self.report_all_players('id', False) 
                session.prompt('Appuyez sur une touche pour continuer MC95') 

                # Prompt if needed to register a new player 
                player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) ') 
                if player_needed == 'y': 
                    self.enter_many_new_players()  # object 
                    # self.enter_new_player()  # object 

                self.enter_new_tournament() 
                # return self.tournament_obj (object) 

                print('\n\033[1mEnregistrer un nouveau round\033[0m') 
                self.enter_new_round(True)  # first_round # object 
                # returns self.round_object (object) 

                self.tournament_obj.rounds.append(self.round_object) 

                self.round_object = self.tournament_obj.rounds[-1] 
                if self.round_object.matches == []: 
                    self.enter_new_matches(True)  # first_round 
                    # return self.matches (objects) 
                else: 
                    print('\nUn problème est survenu, merci d\'envoyer un feedback.') 

                self.round_object.matches = self.matches 
                # print(f'self.round_object.matches MC126 : {self.round_object.matches}') 
                # print(f'self.tournament_obj MC127 : {self.tournament_obj}') 

                self.tournament_obj.serialize_object(True)  # True = new tournament 

                # Display the last tournament  
                self.report_one_tournament('last') 

                session.prompt('\nAppuyez sur une touche pour continuer MC132') 
                self.start() 

            # ==== Register new scores + close round ====
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 

                print('Enregistrer les scores') 

                # Get the last tournament (dict) 
                last_tournament = self.select_one_tournament('last') 
                print(f'\nlast_tournament MC150 : {last_tournament}')  # check if there is at least 1 round 

                # Instantiate it (obj) 
                self.tournament_obj = Tournament_model(**last_tournament) 
                # print(f'\nlast_tournament MC154 : {last_tournament}')  # check if there is at least 1 round 

                # Get the last round (object) 
                self.last_round = self.tournament_obj.rounds.pop() 
                # print(f'\nself.last_round MC158 : {self.last_round}') 

                self.enter_scores() 

                """ Update the players' scores into players.json """ 
                self.update_players_local_scores() 
                self.report_players_from_tournament('id', 'last') 
                session.prompt('\nAppuyez sur une touche pour continuer MC160') 

                # close round : define the end_datetime 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 

                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    end_of_phrase = 'a été clôturé avec succès.' 
                    print(f'\nC\'était le dernier round, le tournoi {self.tournament_obj["name"]} {end_of_phrase}') 
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
                    self.enter_new_round(False) 
                    # returns self.round_object 

                    self.enter_new_matches(False) 
                    # returns self.matches 

                    self.round_object.matches = self.matches 
                    self.tournament_obj.rounds.append(self.round_object) 

                    print('\nVoici les résultats provisoires du tournoi : ') 
                    self.report_rounds('last') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC203') 

                    print('\nLes nouveaux scores des joueurs : ') 
                    self.report_players_from_tournament('id', 'last') 
                    session.prompt('Appuyez sur une touche pour continuer MC217') 

                if not self.tournament_obj.serialize_object(False): 
                    end_of_phrase = 'Merci de votre compréhension.' 
                    print(f'Il y a eu un problème. Essayez de recommencer et envoyez un feedback. {end_of_phrase} ') 

                self.start() 

            # ==== Clôturer un round ==== 
            # en cas d'incident lors de la clôture automatique 
            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 

                # close round : define the end_datetime 
                print('Clôturer le round') 
                closing_round = self.in_view.input_closing_round() 
                if (closing_round == 'y') or (closing_round == 'Y'): 
                    self.last_round.end_datetime = str(datetime.now()) 
                else: 
                    print('*** La clôture du round a été annulée. Vous pourrez clôturer le round depuis le menu. ***') 
                    session.prompt('\nAppuyer sur une touche pour continuer MC227') 

                # Pas besoin de vérifier si 1er round 
                if self.last_round.id == self.tournament_obj.rounds_left: 
                    self.close_tournament() 
                    end_of_phrase = 'a été clôturé avec succès.' 
                    print(f'\nC\'était le dernier round, le tournoi {self.last_tournament["name"]} {end_of_phrase}') 
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
                    # ret self.round_object 

                    self.enter_new_matches(False) 

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

            # Report all players by firstname 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par prénom MC349') 
                session.prompt('Appuyez sur une touche pour continuer MC325') 
                self.report_all_players('firstname', False) 

                session.prompt('Appuyez sur une touche pour continuer MC328') 
                self.start()  # default=False 

            # Report all players by scores 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs par score MC359') 
                session.prompt('Appuyez sur une touche pour continuer MC337') 
                self.report_all_players('score', True) 

                session.prompt('Appuyez sur une touche pour continuer MC340') 
                self.start()  # default=False 

            # Report all tournaments 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 

                print('Afficher les tournois MC372') 
                session.prompt('Appuyez sur une touche pour continuer MC349') 
                self.report_all_tournaments() 

                session.prompt('Appuyez sur une touche pour continuer MC352') 
                self.start()  # default=False 

            # Report one tournament 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi MC383') 
                session.prompt('Appuyez sur une touche pour continuer MC361') 
                tournament_id = session.prompt('Quel tournoi voulez-vous ? (son id ou "last" pour le dernier) ') 
                self.report_one_tournament(tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC365') 
                self.start()  # default=False 

            # Report name and date of one tournament 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 

                print('Afficher un tournoi MC395') 
                session.prompt('Appuyez sur une touche pour continuer MC374') 
                end_of_phrase = '(pour le dernier, tapez "last") : ' 
                tournament_id = session.prompt(f'\nDe quel tournoi voulez-vous les nom et date ? {end_of_phrase}') 
                self.report_name_date_tournament(tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC388') 
                self.start()  # default=False 

            # Report all players of one tournament 
            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 

                print('Afficher les joueurs d\'un tournoi MC386') 
                session.prompt('Appuyez sur une touche pour continuer MC387') 
                end_of_phrase = '(pour le dernier, tapez "last") : ' 
                tournament_id = session.prompt(f'\nDe quel tournoi voulez-vous les joueurs ? {end_of_phrase}') 
                self.report_players_from_tournament('firstname', tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC391') 
                self.start()  # default=False 

            # Report rounds and matches of one tournament 
            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 

                print('Afficher les rounds et matches d\'un tournoi MC319') 
                session.prompt('Appuyez sur une touche pour continuer MC400') 
                end_of_phrase = '(son id ou "last" pour le dernier) ' 
                tournament_id = session.prompt(f'De quel tournoi voulez-vous les tours ? {end_of_phrase}') 
                self.report_rounds(tournament_id) 

                session.prompt('Appuyez sur une touche pour continuer MC404') 
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

        # corriger la commande "*" partout 
        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            self.start(False) 

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

    # ============ R E P O R T S ============ # 

    def report_all_players(self, sort, rev):  # rev : reverse 
        """ 
            Displays the players from players.json. 
            parameters: 
                sort (str): 'id', 'firstname' or 'local_score', the name of the field on wich to sort the players. 
                rev (bool): if we have to reverse the list of objects. 
        """ 
        if Player_model.get_registered_dict('players') == []: 
            print('Il n\'y a pas de joueur à afficher. ') 
        else: 
            players = Player_model.get_registered_dict('players') 
            players_obj = [] 
            for player in players: 
                self.player = Player_model(**player) 
                players_obj.append(self.player) 

            # Choice of the order ('id' -> chronological, 'firstname' -> alphabetical or 'local_score' -> by score): 
            if sort == 'id': 
                print('\n==== Tous les joueurs par ordre d\'enregistrement :  ==== ') 
                self.sort_objects_by_field(players_obj, 'id', rev) 
            if sort == 'firstname': 
                print('\n==== Tous les joueurs par ordre alphabétique :  ==== ') 
                self.sort_objects_by_field(players_obj, 'firstname', rev) 
            if sort == 'score': 
                print('\n==== Tous les joueurs par score :  ==== ') 
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
        if tournament_dict == {}: 
            print('Il n\y a pas de tournoi à afficher. MC595') 
        else: 
            tournament_obj = Tournament_model(**tournament_dict) 

            players_ids = tournament_obj.players 

            # ---- récupérer les joueurs et les instancier ---- # 
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
            self.sort_objects_by_field(players_objs, field)  # sort 

            self.report_view.display_players(players_objs) 

    def report_one_player(self, player_id): 
        """ Displays one player from its id. 
        Args:
            player_id (int or 'last'): the player's id, or for the last one, type 'last'. 
        """ 
        player = self.select_one_player(player_id) 
        if player == {}: 
            print('Il n\'y a pas de joueur à aficher. MC627') 
        else: 
            player_obj = Player_model(**player) 
            self.report_view.display_one_player(player_obj) 

    def report_all_tournaments(self): 
        """ Displays all the registered tournaments. 
        """ 
        if Tournament_model.get_registered_dict('tournaments') == []: 
            print('Il n\'y a pas de tournoi à afficher. MC630') 
        else: 
            tournaments = Tournament_model.get_registered_dict('tournaments') 
            tournaments_objs = [] 

            for tournament in tournaments: 
                if 'rounds' not in tournament.keys(): 
                    tournament['rounds'] = [] 
                self.tournament = Tournament_model(**tournament) 
                tournaments_objs.append(self.tournament) 

                self.report_view.display_tournaments(tournaments_objs) 

    def report_one_tournament(self, tournament_id): 
        """ Displays one tournament from its id. 
            Args: 
                tournament_id (int or 'last'): the tournament's id, or 'last' for the last one. 
        """ 
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afficher. MC651') 
        else: 
            last_tournament = Tournament_model(**tournament) 
            self.report_view.display_one_tournament(last_tournament) 

    def report_name_date_tournament(self, tournament_id): 
        """ Displays the name and the dates of the tournament. 
            Args:
                tournament_id (int or 'last'): the id of the tournament, or 'last' for the last one. 
        """
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afficher. MC664') 
        else: 
            self.report_view.display_name_date_tournament(tournament) 

    def report_rounds(self, tournament_id): 
        """ Displays the rounds of a tournament. 
            Args:
                tournament_id (int or 'last'): the tournament's id or 'last' for the last one. 
        """
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afifcher. MC679') 
        else: 
            tournament_obj = Tournament_model(**tournament) 
            self.report_view.display_rounds_one_tournament(tournament_obj) 

    # ============ P L A Y E R S ============ # 

    """ Register one player """  # ok 230507 
    def enter_new_player(self): 
        new_player_data = self.in_view.input_player() 
        if Player_model.get_registered_dict('players') == []: 
            new_player_data['id'] = 1 
        else: 
            last_player_id = Player_model.get_registered_dict('players')[-1]['id'] 
            new_player_data['id'] = last_player_id + 1  
        new_player_data['local_score'] = float(0.0) 
        new_player_data['global_score'] = float(0.0) 
        new_player_data['local_score'] = float(0.0) 

        self.player = Player_model(**new_player_data) 

        if not self.player.serialize_object(True): 
            print('Il y a eu un problème, veuillez recommencer ou envoyer un feedback. merci de votre compréhension. ') 
        else: 
            print('\nLe joueur a bien été enregistré. ') 
            self.report_one_player('last') 
        session.prompt('Appuyez sur une touche pour continuer  MC710')  

    def enter_many_new_players(self): 
        """ 
            Calls the `enter_new_player` more than one time. 
        """ 
        self.players = [] 
        while True: 
            player = self.enter_new_player() 
            self.players.append(player) 
            player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) : ') 
            if not (player_needed == "y" or player_needed == "Y"): 
                # print(f'player_needed : {player_needed}') 
                # print(f'type(player_needed) : {type(player_needed)}') 
                # return True 
                #     pass 
                # else: 
                return False 
        # ==== tuto real python do...while 
        # while True:
        #     number = int(input("Enter a positive number: "))
        #     print(number)
        #     if not number > 0:
        #         break
        # ==== 

    def update_players_local_scores(self): 
        """ Update the scores into the players.json file. 
        """ 
        # Get registered players local_scores 
        p_dicts = Player_model.get_registered_dict('players') 
        # Instantiate the players 
        self.players_objs = [Player_model(**data) for data in p_dicts] 
        for self.player_obj in self.players_objs: 
            for match in self.last_round.matches: 
                # print(f'\nmatch MC760 : {match}') 
                # print(f'\nself.player_obj.id MC764 : {self.player_obj.id}') 
                # print(f'\nmatch.player_1_id MC765 : {match.player_1_id}') 
                # print(f'\nmatch.player_2_id MC766 : {match.player_2_id}') 
                if self.player_obj.id == match.player_1_id: 
                    # print(f'\nself.player_obj.local_score MC770 : {self.player_obj.local_score}') 
                    # print(f'\nmatch.player_1_score MC771 : {match.player_1_score}') 
                    self.player_obj.local_score += match.player_1_score 

                elif self.player_obj.id == match.player_2_id: 
                    # print(f'\nself.player_obj.local_score MC784 : {self.player_obj.local_score}') 
                    # print(f'\nmatch.player_2_score MC785 : {match.player_2_score}') 
                    self.player_obj.local_score += match.player_2_score 

            # Register the new scores into players.json 
            self.player_obj.serialize_object(False) 

    def set_players_scores_to_zero(self, tournament):  # retirer tournament ### 
        """ At the begining of a tournament, add the players' local_scores ot their global_scores, 
            and set the local scores to 0. 
        """ 
        players_dicts = Player_model.get_registered_dict('players') 
        self.players_objs = [Player_model(**player_dict) for player_dict in players_dicts] 

        for player_obj in self.players_objs: 
            player_obj.global_score += player_obj.local_score 
            player_obj.local_score = float(0) 

            player_obj.serialize_object(False) 

    # ============ T O U R N A M E N T S ============ # 

    def enter_new_tournament(self): 
        """ Register a new tournament with the data entered by the user. 
            returns: self.tournament_obj 
        """ 
        # Get the data for the current tournament: 
        self.tournament_data = self.in_view.input_tournament() 

        players_ids = re.findall(r'\d+', self.tournament_data['players']) 
        self.tournament_data['players'] = [int(player) for player in players_ids] 
        # self.tournament_data['players'] = [int(player) for player in 
        # re.findall(r'\d+', self.tournament_data['players'])] 

        # Set the id relative to the last tournament: 
        if self.select_one_tournament('last') == {}: 
            self.tournament_data['id'] = 1 
        else: 
            self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 

        # Set 'rounds' = [] 
        self.tournament_data['rounds'] = [] 

        # Instantiate the current tournament: 
        self.tournament_obj = Tournament_model(**self.tournament_data) 
        return self.tournament_obj 

    def close_tournament(self): 
        """ If the auto closing of the tournament has been canceled, closes the tournament. 
        """ 
        today = date.today() 
        if not self.tournament_obj: 
            last_tournament = self.select_one_tournament('last') 
            self.tournament_obj = Tournament_model(**last_tournament)  

        closing_tournament = self.in_view.input_closing_tournament() 
        if closing_tournament == 'y': 
            # Set the end_date 
            self.tournament_obj.end_date = str(today) 
            self.tournament_obj.serialize_object(False) 
        else: 
            print('\nLa clôture du tournoi a été annulée, vous pourrez la relancer depuis le menu. ') 

    # ============ R O U N D S ============ # 

    def enter_new_round(self, first_round):  # first_round = bool 
        """ Register a new round with its data. 
            Args: 
                first_round (bool): if it is the first round. 
            Returns: self.round_object 
        """         

        # Get the prompt data for the current round: 
        round_data = self.in_view.input_round() 
        print(f'type(round_data) MC882 : {type(round_data)}') 
        if first_round: 
            round_data['id'] = 1 
        else: 
            round_data['id'] = int(self.tournament_obj.rounds[-1].id) + 1 
            if self.tournament_obj.rounds[-1].end_datetime == '': 
                self.tournament_obj.rounds[-1].end_datetime = datetime.now() 
        round_data['tournament_id'] = int(self.tournament_obj.id) 

        round_data['start_datetime'] = str(datetime.now()) 
        round_data['end_datetime'] = "" 
        round_data['matches'] = [] 

        self.round_object = Round_model(**round_data) 

        return self.round_object 

    # ============ M A T C H E S ============ # 

    def enter_scores(self): 
        """ Get the scores from the terminal and register them into the matches. 
        """ 

        # get the matches (list of lists) 
        current_matches_dicts = self.last_round.matches 

        # Get the matches (obj as tuples)  
        current_matches_list = [] 
        for curr_match in current_matches_dicts: 
            curr_match_tuple = tuple(curr_match) 
            curr_match_obj = Match_model(curr_match_tuple) 
            current_matches_list.append(curr_match_obj) 

        # Get the input_scores for the registered matches 
        input_results = self.in_view.input_scores(current_matches_list) 
        print('---------------------') 

        # Get the differentiated data from the input 
        null_matches = input_results[0] 
        winners = input_results[1] 

        # Set the new scores of the matches 
        new_scores = [] 

        # Loop on null_matches and winners lists to update the scores into the matches (current_matches_list) 
        for null_match in null_matches: 
            for current_match in current_matches_list: 
                print(f'\ncurrent_match MC948 : {current_match}') 
                if current_match.player_1_id == null_match.player_1_id: 
                    current_match.player_1_score += float(0.5) 
                    current_match.player_2_score += float(0.5) 
                    new_scores.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 

        for winner in winners: 
            for current_match in current_matches_list: 
                if current_match.player_1_id == winner[0]: 
                    current_match.player_1_score += float(1) 
                    new_scores.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 
                elif current_match.player_2_id == winner[0]: 
                    current_match.player_2_score += float(1) 
                    new_scores.append(current_match) 
                    cm_index = current_matches_list.index(current_match) 
                    current_matches_list.pop(cm_index) 

        # Put back the rounds and the matches into the round 
        self.last_round.matches = new_scores 
        # print(f'\nself.last_round MC952 : {self.last_round}') 
        # print(f'\nself.last_round.matches MC953 : {self.last_round.matches}') 
        self.tournament_obj.rounds.append(self.last_round) 

        # Serialize the tournament (new=False)  
        self.tournament_obj.serialize_object(False) 

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
        players_dicts = Player_model.get_registered_dict('players')  # dict 
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
            last_tournament = self.tournament_obj 
            next_matches = define_matches.make_peers(selected, True, last_tournament)  # True = first_round 
        else: 
            selected = self.sort_objects_by_field(players_obj, 'local_score', True) 
            last_tournament = self.tournament_obj 
            next_matches = define_matches.make_peers(selected, False, last_tournament)  # True = first_round 

        self.matches = [Match_model(data) for data in next_matches] 
        # print(f'\nnext_matches MC979 : {next_matches}')  # list of tuples 

        return self.matches 

    # ============ U T I L S ============ # 

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

    """ Select one tournament from JSON file """ 
    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournaments.json file. 
            Args:
                t_id (int): the tournament's id 
            Returns:
                int: the tournament's id 
        """ 
        if Tournament_model.get_registered_dict('tournaments') == []: 
            # print(f'Il n\'y a pas de tournoi à afficher. MC974') 
            return {} 
        else: 
            t_dicts = Tournament_model.get_registered_dict('tournaments') 

            if t_id == 'last': 
                t_dict = t_dicts.pop() 
            else: 
                t_dict = t_dicts[t_id - 1] 
            return t_dict 

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

