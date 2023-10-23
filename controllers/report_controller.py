
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

# from views.input_view import Input_view 
from views.report_view import Report_view 

# Voir si c'est possible : 
from utils import helpers 


class Report_controller(): 

    report_view = Report_view 

    def __init__( 
        self, 
        player_model: Player_model, 
        round_model: Round_model, 
        tournament_model: Tournament_model, 

        # in_view: Input_view, 
        # report_view: Report_view, 
    ): 
        self.player_model 
        self.round_model 
        self.tournament_model 

        # self.in_view = in_view 
        # self.report_view = report_view 


    def report_all_players(self, sort, rev=True):  # rev : reverse 
        """ 
            Displays the players from players.json. 
            parameters: 
                sort (str): 'id', 'firstname' or 'score', 
                    the name of the field on wich to sort the players. 
                rev (bool): if we have to reverse the list of objects. 
        """ 
        if Player_model.get_registered_dict('players') == []: 
            print('Il n\'y a pas de joueur à afficher. ') 
        else: 
            players = Player_model.get_registered_dict('players') 
            players_obj = [] 
            for player in players: 
                player_obj = Player_model(**player) 
                players_obj.append(player_obj) 

            # Choice of the order ( 
            #     'id' -> chronological, 
            #     'firstname' -> alphabetical or 
            #     'score' -> by INE 
            # ): 
            if sort == 'id': 
                print('\n==== Tous les joueurs par ordre d\'enregistrement :  ==== ') 
                sorted_players = helpers.sort_objects_by_field(players_obj, 'id', rev) 
            if sort == 'firstname': 
                print('\n==== Tous les joueurs par ordre alphabétique :  ==== ') 
                sorted_players = helpers.sort_objects_by_field(players_obj, 'firstname', rev) 
            if sort == 'score': 
                # print('\n==== Tous les joueurs par score INE :  ==== ') 
                sorted_players = helpers.sort_objects_by_field(players_obj, 'score', rev) 
                # sorted_players = helpers.sort_objects_by_field(players_obj, 'global_score', rev) 

        self.report_view.display_players(self, sorted_players) 
        # self.report_view.display_players(sorted_players) 


    def report_one_player(self, player_id): 
        """ Displays one player from its id. 
            Args:
                player_id (int or 'last'): the player's id, or for the last one, type 'last'. 
        """ 
        player = self.select_one_player(player_id) 
        if player == {}: 
            print('Il n\'y a pas de joueur à aficher.') 
        else: 
            player_obj = Player_model(**player) 
            self.report_view.display_one_player(self, player_obj) 


    def report_players_from_tournament(self, field): 
        """ Displays the players of one tournament. 
            Args: 
                field (string): the field we will sort the players on. 
                # tournament_id (int or 'last'): the id of the tournament. 
                    For the last one, type 'last' ;  ### 
        """ 
        # print(f'dir(self) RPC105 : {dir(self)}') 
        if not self.players_objs: 
            print('Il n\'y a pas de joueurs à afficher.') 
        else: 
            players_objs = self.players_objs 
            print('======== ') 
            # Choice of the order (id, alphabetical or by INE score): 
            if field == 'id': 
                print('\nJoueurs par ordre d\'enregistrement : ') 
                self.tournament_players_objs = helpers.sort_objects_by_field(players_objs, 'id') 
            if field == 'firstname': 
                print('\nJoueurs par ordre alphabétique : ') 
                self.tournament_players_objs = helpers.sort_objects_by_field(players_objs, 'firstname') 
            if field == 'score': 
                print('\nJoueurs par score : ') 
                self.tournament_players_objs = helpers.sort_objects_by_field( 
                    players_objs, 'global_score', reversed=True 
                ) 

            self.report_view.display_players(self, self.tournament_players_objs) 

            return self.tournament_players_objs 


    def report_all_tournaments(self): 
        """ Displays all the registered tournaments. 
        """ 
        if Tournament_model.get_registered_dict('tournaments') == []: 
            print('Il n\'y a pas de tournoi à afficher.') 
        else: 
            tournaments = Tournament_model.get_registered_dict('tournaments') 
            tournaments_objs = [] 

            for tournament in tournaments: 
                if 'rounds' not in tournament.keys(): 
                    tournament['rounds'] = [] 
                self.tournament = Tournament_model(**tournament) 
                tournaments_objs.append(self.tournament) 

                self.report_view.display_tournaments(self, tournaments_objs) 


    def report_one_tournament(self, tournament_id): 
        """ Displays one tournament from its id. 
            Args: 
                tournament_id (int or 'last'): the tournament's id, or 'last' for the last one. 
        """ 
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afficher.') 
        else: 
            tournament_obj = Tournament_model(**tournament) 
            self.report_view.display_one_tournament(self, tournament_obj) 


    def report_name_date_tournament(self, tournament_id): 
        """ Displays the name and the dates of the tournament. 
            Args: 
                tournament_id (int or 'last'): the id of the tournament, or 'last' for the last one. 
        """
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afficher.') 
        else: 
            tournament_obj = Tournament_model(**tournament) 
            self.report_view.display_name_date_tournament(self, tournament_obj) 


    def report_rounds(self, tournament_id): 
        """ Displays the rounds of a tournament. 
            Args: 
                tournament_id (int or 'last'): the tournament's id or 'last' for the last one. 
        """ 
        tournament = self.select_one_tournament(tournament_id) 
        if tournament == {}: 
            print('Il n\'y a pas de tournoi à afifcher.') 
        else: 
            tournament_obj = Tournament_model(**tournament) 
            self.report_view.display_rounds_one_tournament(self, tournament_obj) 

    def report_starters(self): 
        starters = self.starters 
        self.report_view.display_starters(self, starters) 

    # ---------------------------------------------- 
    """ comment """ 
    def report_one_round(self, tournament_id, round_id): 
        self.tournament = self.select_one_tournament(tournament_id) 
        if round_id == 'last': 
            round = self.tournament['rounds'].pop() 
        else: 
            round = self.tournament[round_id] - 1 
        one_round = Round_model(**round) 

        self.report_view.display_one_round(self, one_round) 


