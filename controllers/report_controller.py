
from models.match_model import Match_model 
# from models.round_model import Round_model 
# from models.tournament_model import Tournament_model 

# from views.input_view import Input_view 
from views.report_view import Report_view 

# Voir si c'est possible : 
from utils import helpers 


class Report_controller(): 

    def __init__( 
        self, 
        new_reporter: Report_view(), 
    ): 
        self.report_view = new_reporter 


    def report_all_players(self, players_objs, field, rev=False):  # rev : reverse 
        """ Displays the players from players.json. 
            parameters: 
                sort (str): 'id', 'firstname' or 'score', 
                    the name of the field on wich to sort the players. 
                rev (bool): if we have to reverse the list of objects. 
        """ 
        if not players_objs: 
            players_objs = helpers.select_all_players() 

        # Choice of the order : 
        if field == 'id': 
            print('\n==== Tous les joueurs par ordre d\'enregistrement :  ==== ') 
        if field == 'firstname': 
            print('\n==== Tous les joueurs par ordre alphabétique :  ==== ') 
        if field == 'score': 
            rev = True 
            print('\n==== Tous les joueurs par score INE :  ==== ') 
        sorted_players = helpers.sort_objects_by_field(players_objs, field, rev) 

        self.report_view.display_players(sorted_players) 


    def report_one_player(self, player_id): 
        """ Displays one player from its id. 
            Args:
                player_id (int or 'last'): the player's id, or for the last one, type 'last'. 
        """ 
        player_obj = helpers.select_one_player(player_id) 
        if player_obj is None: 
            print('Il n\'y a pas (ou plus) de joueur à aficher.') 
        else: 
            self.report_view.display_one_player(player_obj) 


    def report_players_from_tournament(self, field, tournament_id): 
        """ Displays the players of one tournament. 
            Args: 
                field (string): the field we will sort the players on. 
                tournament_id (int or 'last'): the id of the tournament. 
                    For the last one, type 'last' 
        """ 
        reversed = False 
        players_objs = helpers.select_tournament_players(tournament_id) 
        if not players_objs: 
            print('Il n\'y a pas de joueurs à afficher.') 
        else: 
            print('======== ') 
            # Choice of the order (id, alphabetical, tournament_score or by INE score): 
            if field == 'id': 
                print('\nJoueurs par ordre d\'enregistrement : ') 
            if field == 'firstname': 
                print('\nJoueurs par ordre alphabétique : ') 
            if field == 'score': 
                print('\nJoueurs par score : ') 
                field = 'ine' 
                reversed = True 
            if field == 'tournament_score': 
                print('\nJoueurs par score dans le tournoi : ') 
                reversed = True 
            # à tester ### 
            tournament_players_objs = helpers.sort_objects_by_field( 
                players_objs, field, reversed 
            ) 

            self.report_view.display_players(tournament_players_objs) 

            return tournament_players_objs 


    def report_round_results(self, tournament_id): 
        last_round = helpers.select_one_tournament(tournament_id).rounds[-1] 
        matches = last_round.matches 
        [tuple(match) for match in matches] 
        matches_objs = [Match_model(data) for data in last_round.matches] 
        players_objs = helpers.select_tournament_players(tournament_id) 

        self.report_view.display_matches_results(matches_objs, players_objs) 


    def report_all_tournaments(self, tournaments_objs): 
        """ Displays all the registered tournaments. 
        """ 
        if not tournaments_objs: 
            tournaments_objs = helpers.select_all_tournaments() 

        self.report_view.display_tournaments(tournaments_objs) 

        return tournaments_objs 


    def report_one_tournament(self, tournament_id): 
        """ Displays one tournament from its id. 
            Args: 
                tournament_id (int or 'last'): the tournament's id, or 'last' for the last one. 
        """ 
        tournament_obj = helpers.select_one_tournament(tournament_id) 

        if not tournament_obj: 
            print('Il n\'y a pas de tournoi à afficher.') 
        else: 
            self.report_view.display_one_tournament(tournament_obj) 

        return tournament_obj 


    def report_name_date_tournament(self, tournament_id): 
        """ Displays the name and the dates of the tournament. 
            Args: 
                tournament_id (int or 'last'): the id of the tournament, or 'last' for the last one. 
        """
        tournament_obj = helpers.select_one_tournament(tournament_id) 
        # if tournament_obj == {}: 
        if not tournament_obj: 
            print('Il n\'y a pas de tournoi à afficher.') 
        else: 
            self.report_view.display_name_date_tournament(tournament_obj) 

        return tournament_obj 


    def report_rounds(self, tournament_id): 
        """ Select the tournament to display the rounds from. 
            Args: 
                tournament_id (int or 'last'): the tournament's id or 'last' for the last one. 
        """ 
        tournament_obj = helpers.select_one_tournament(tournament_id) 
        if not tournament_obj: 
            print('Il n\'y a pas de tournoi à afifcher.') 
        else: 
            self.report_view.display_rounds_one_tournament(tournament_obj) 

        return tournament_obj 


    def report_starters(self, starters): 
        self.report_view.display_starters(starters) 

    # ---------------------------------------------- 
    # """ comment """ 
    # def report_one_round(self, tournament_id, round_id): 
    #     tournament_obj = helpers.select_one_tournament(tournament_id) 
    #     if tournament_obj.rounds and not isinstance(tournament_obj.rounds[0], Round_model): 
    #         rounds = [Round_model(**data) for data in tournament_obj.rounds] 
    #     else: 
    #         rounds = tournament_obj.rounds 

    #     if round_id == 'last': 
    #         round_obj = rounds[-1] 
    #     else: 
    #         round_obj = int(rounds.round_id) 

    #     self.report_view.display_one_round(round_obj) 


