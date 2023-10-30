
from utils import helpers 

from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.input_view import Input_view 
from views.report_view import Report_view 
from controllers.report_controller import Report_controller 

import re 
from datetime import datetime, date 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Register_controller(): 


    def __init__( 
        self, 
        # player_model: Player_model, 
        # round_model: Round_model, 
        # tournament_model: Tournament_model, 

        in_view: Input_view(), 
        new_reporter: Report_view() 
        # report_view: Report_view, 
    ): 
        # self.player_model 
        # self.round_model 
        # self.tournament_model 
        self.in_view = in_view 
        self.report_view = new_reporter 
        self.report_controller = Report_controller(new_reporter) 

        # self.report_view = report_view 


    # ============ P L A Y E R S ============ # 


    """ Register one player """ 
    def enter_new_player(self): 
        new_player_data = self.in_view.input_player() 
        # new_player = Player_model(**new_player_data) 
        print(f'self RGC49 : {self}') 
        print(f'dir(self) RGC50 : {dir(self)}') 
        print(f'new_player_data RGC51 : {new_player_data}') 
        registered_player = helpers.select_one_player('last') 
        # if Player_model.get_registered_dict('players') == []: 
        if registered_player and not isinstance(registered_player, Player_model): 
            # new_player.id = 1 
            new_player_data['id'] = 1 
        else: 
            # last_player_id = Player_model.get_registered_dict('players')[-1]['id'] 
            new_player_data['id'] = int(registered_player.id) + 1  
        # new_player_data['round_score'] = float(0) 
        # new_player_data['tournament_score'] = float(0) 

        player = Player_model(**new_player_data, round_score=float(0), tournament_score=float(0)) 

        if not player.serialize_object(True): 
            print('Il y a eu un problème, veuillez recommencer ou envoyer un feedback. Merci de votre compréhension. ') 
        else: 
            print('\nLe joueur a bien été enregistré. ') 
            self.report_controller.report_one_player('last')  


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
                return False 


    def update_players_tournament_scores(self, tournament_obj): 
        """ Updates the current tournament's scores into the players.json file. 
        """ 
        curr_players = helpers.select_tournament_players(tournament_obj.id) 
        # matches = tournament_obj.rounds[-1].matches 

        for player_obj in curr_players: 
            player_obj.tournament_score == player_obj.round_score 

        for player_obj in curr_players: 
            player_obj.serialize_object(False) 
        return curr_players  # list of objects  


    def update_players_round_scores(self, tournament_obj): 
        """ Updates the current round's scores into the players.json file. 
        """ 
        # Get registered players round_score 
        # p_dicts = Player_model.get_registered_dict('players') 
        curr_players = helpers.select_tournament_players(tournament_obj.id) 
        matches = tournament_obj.rounds[-1].matches 

        for player_obj in curr_players: 
            player_obj.round_score == 0.0 
            for match in matches: 
                if player_obj.id == match.player_1_id: 
                    player_obj.round_score += match.player_1_score 

                elif player_obj.id == match.player_2_id: 
                    player_obj.round_score += match.player_2_score 
                # player_obj.round_score = 0.0 

        for player_obj in curr_players: 
            player_obj.serialize_object(False) 
        return curr_players  # list of objects  


    def set_players_scores_to_zero(self, tournament_obj):  # retirer tournament ### 
        """ At the begining of a tournament, set the tournament_scores to 0. 
            param: 
                list of objects: the players of the tournament. 
            returns: 
                self.updated_players_objs: a list of the updated players. 
        """ 
        print(f'dir(self) RGC105 : {dir(self)}') 
        players_objs = helpers.select_tournament_players(tournament_obj.id) 
        updated_players_objs = [] 
        for player_obj in players_objs: 
            player_obj.tournament_score = float(0) 
            player_obj.round_score = float(0) 
            updated_players_objs.append(player_obj) 

            player_obj.serialize_object(False) 

        return updated_players_objs 


    # ============ T O U R N A M E N T S ============ # 


    def enter_new_tournament(self, last_tournament_obj): 
        """ Register a new tournament with the data entered by the user. 
            returns: self.tournament_obj 
        """ 
        # Get the data for the current tournament: 
        tournament_data = self.in_view.input_tournament() 

        players_ids = re.findall(r'\d+', tournament_data['players']) 
        tournament_data['players'] = [int(id) for id in players_ids] 

        # Set the id relative to the last tournament: 
        # last_tournament_obj = helpers.select_one_tournament('last') 
        if not last_tournament_obj or not isinstance(last_tournament_obj, Tournament_model): 
            tournament_data['id'] = 1 
        else: 
            tournament_data['id'] = int(last_tournament_obj.id) + 1 

        tournament_data['rounds'] = [] 

        # Instantiate the current tournament: 
        tournament_obj = Tournament_model(**tournament_data) 
        # self.tournament_obj = Tournament_model(**tournament_data) 

        # return True 
        return tournament_obj 
        # return self.tournament_obj 


    def close_tournament(self): 
        """ If the auto closing of the tournament has been canceled, closes the tournament. 
        """ 
        today = date.today() 
        if not self.tournament_obj: 
            self.tournament_obj = self.select_one_tournament('last') 

        closing_tournament = self.in_view.input_closing_tournament() 
        if closing_tournament == 'y': 
            # Set the end_date 
            self.tournament_obj.end_date = str(today) 
            self.tournament_obj.serialize_object(False) 
        else: 
            print('\nLa clôture du tournoi a été annulée, vous pourrez la relancer depuis le menu. ') 
        return True 


    # ============ R O U N D S ============ # 


    def enter_new_round(self, first_round, tournament_obj):  # first_round = bool 
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
            round_data['id'] = int(tournament_obj.rounds[-1].id) + 1 
            if tournament_obj.rounds[-1].end_datetime == '': 
                tournament_obj.rounds[-1].end_datetime = datetime.now() 
        round_data['tournament_id'] = int(tournament_obj.id) 

        round_data['start_datetime'] = str(datetime.now()) 
        round_data['end_datetime'] = "" 
        round_data['matches'] = [] 

        # round_object = Round_model(**round_data) 
        round_object = Round_model(**round_data) 

        # return round_object 
        return round_object 


    # ============ M A T C H E S ============ # 


    def enter_scores(self, tournament_obj): 
        """ Get the scores from the terminal and register them into the matches. 
        """ 
        last_round = tournament_obj.rounds[-1] 
        current_matches = last_round.matches 

        # Get the matches (obj as tuples)  
        current_matches_list = [] 
        for curr_match in current_matches: 
            curr_match_tuple = tuple(curr_match) 
            curr_match_obj = Match_model(curr_match_tuple) 
            current_matches_list.append(curr_match_obj) 

        players_objs = helpers.select_tournament_players(tournament_obj.id) 

        input_results = self.in_view.input_scores(current_matches_list, players_objs) 
        print('---------------------') 

        # Get the differentiated data from the input 
        null_matches = input_results[0] 
        winners = input_results[1] 

        # Set the new scores of the matches 
        new_scores = [] 
        # Loop on null_matches and winners lists to update the scores 
        # into the matches (current_matches_list) 
        for null_match in null_matches: 
            for current_match in current_matches_list: 
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
        last_round.matches = new_scores 

        tournament_obj.rounds.pop() 
        tournament_obj.rounds.append(last_round) 

        # Serialize the tournament (new=False)  
        tournament_obj.serialize_object(False)  # à vérifier ? ### 

        return tournament_obj 


    def enter_new_matches(self, first_round, last_tournament):  # , last_tournament ### 
        """ Defines and registers the new matches. 
            Args:
                first_round (bool): if there is the matches of the first round. 
            Returns:
                next_matches (objects): the list of matches to register into the new round. 
        """ 
        players_objs = helpers.select_tournament_players('last') 

        if first_round: 
            selected = helpers.random_matches(players_objs) 
            next_matches = helpers.make_peers(selected, True, last_tournament)  # True = first_round 
        else: 
            selected = players_objs 
            next_matches = helpers.make_peers(selected, False, last_tournament)  # True = first_round 

        return next_matches 


