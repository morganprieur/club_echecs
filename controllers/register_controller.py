
from utils import helpers 

from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.input_view import Input_view 
from views.report_view import Report_view 

import re 
from datetime import datetime, date 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Register_controller(): 

    def __init__( 
        self, 
        player_model: Player_model, 
        round_model: Round_model, 
        tournament_model: Tournament_model, 

        in_view: Input_view, 
        report_view: Report_view, 
    ): 
        self.player_model 
        self.round_model 
        self.tournament_model 

        self.in_view = in_view 
        self.report_view = report_view 


    # ============ P L A Y E R S ============ # 


    """ Register one player """ 
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
            self.report_controller.report_one_player('last')  


    def enter_many_new_players(self): 
        """ 
            Calls the `enter_new_player` more than one time. 
        """ 
        self.players = [] 
        while True: 
            player = self.register_controller.enter_new_player(self) 
            self.players.append(player) 
            player_needed = session.prompt('\nEnregistrer un nouveau joueur ? (y/n) : ') 
            if not (player_needed == "y" or player_needed == "Y"): 
                return False 


    def update_players_local_scores(self): 
        """ Update the scores into the players.json file. 
        """ 
        # Get registered players local_scores 
        p_dicts = Player_model.get_registered_dict('players') 

        # Instantiate the players 
        self.registered_players_objs = [Player_model(**data) for data in p_dicts] 

        for self.registered_player_obj in self.registered_players_objs: 
            for match in self.last_round.matches: 
                if self.registered_player_obj.id == match.player_1_id: 
                    self.registered_player_obj.global_score += match.player_1_score 

                elif self.registered_player_obj.id == match.player_2_id: 
                    self.registered_player_obj.global_score += match.player_2_score 
                self.registered_player_obj.local_score = 0.0 

        # Register the new scores into players.json 
        for self.registered_player_obj in self.registered_players_objs: 
            self.registered_player_obj.serialize_object(False) 
        return self.registered_players_objs 

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

        # Set the id relative to the last tournament: 
        if self.select_one_tournament('last') == {}: 
            self.tournament_data['id'] = 1 
        else: 
            self.tournament_data['id'] = int(self.select_one_tournament('last')['id']) + 1 

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
        return True 


    # ============ R O U N D S ============ # 


    def enter_new_round(self, first_round):  # first_round = bool 
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

        self.tournament_obj.rounds.append(self.last_round) 

        # Serialize the tournament (new=False)  
        self.tournament_obj.serialize_object(False) 
        # A vérifier : ### 
        return self.tournament_obj 


    """ comment """  
    def enter_new_matches(self, first_round): 
        """ Define and register the new matches. 
            Args:
                first_round (bool): if there is the matches of the first round. 
            Returns:
                self.matches (objects): the list of matches to register into the new round. 
        """ 
        if first_round: 
            # selected = helpers.random_matches(self.players_obj) 
            last_tournament = self.tournament_obj 
            next_matches = helpers.make_peers(self.selected, True, last_tournament)  # True = first_round 
        else: 
            last_tournament = self.tournament_obj 
            next_matches = helpers.make_peers(self.selected, False, last_tournament)  # True = first_round 

        return next_matches 


