
from utils import helpers 

from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.input_view import Input_view 

from controllers.report_controller import Report_controller 

import re 
from datetime import datetime, date 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Register_controller(): 
    """ This class has to get the data from the Input_view class, 
        validate and formate them, 
        and send them to the Model classes to register them. 
    """ 

    def __init__( 
        self, 

        in_view: Input_view, 
        report_controller: Report_controller 
    ): 
        self.in_view = in_view 
        self.report_controller = report_controller 


    # ============ P L A Y E R S ============ # 


    def enter_new_player(self): 
        """ Registers one player """ 
        new_player_data = self.in_view.input_player() 
        registered_player = helpers.select_one_player('last') 
        if not registered_player: 
            new_player_data['id'] = 1 
        else: 
            new_player_data['id'] = int(registered_player.id) + 1  

        player_obj = Player_model(**new_player_data, round_score=float(0), tournament_score=float(0)) 

        if not player_obj.serialize_object(True): 
            print('Il y a eu un problème, veuillez recommencer ou envoyer un feedback. Merci de votre compréhension. ') 
        else: 
            print('\nLe joueur a bien été enregistré. ') 
            self.report_controller.report_one_player('last') 


    def enter_many_new_players(self): 
        """ Calls the `enter_new_player` for each new player. """ 
        self.players = [] 
        while True: 
            player = self.enter_new_player() 
            self.players.append(player) 
            player_needed = self.in_view.input_yes_or_no('Enregistrer un nouveau joueur ?') 
            if not (player_needed == "y" or player_needed == "Y"): 
                return False 


    def update_players_tournament_scores(self, tournament_obj): 
        """ Updates the current tournament's scores 
            into the players.json file. 

            Args: 
                tournament_obj (Tournament_model instance): the tournament which to select the players from. 

            Returns: 
                curr_players (list of Player_model instances): the players of the tournament. 
        """ 
        curr_players = helpers.select_tournament_players(tournament_obj.id) 

        for player_obj in curr_players: 
            player_obj.tournament_score += player_obj.round_score 
            player_obj.round_score = float(0) 

        for player_obj in curr_players: 
            player_obj.serialize_object(False) 
        return curr_players  # list of objects  


    def update_players_round_scores(self, tournament_obj): 
        """ Updates the current round's scores 
            into the players.json file. 

            Args: 
                tournament_obj (Tournament_model instance): the tournament which to update the players' scores from. 

            Returns: 
                curr_players (list of Player_model instances): the players of the tournament. 
        """ 
        # Get registered players round_score 
        curr_players = helpers.select_tournament_players(tournament_obj.id) 
        matches = tournament_obj.rounds[-1].matches 

        for player_obj in curr_players: 
            player_obj.round_score = 0.0 
            for match in matches: 
                if player_obj.id == match.player_1_id: 
                    player_obj.round_score += match.player_1_score 

                elif player_obj.id == match.player_2_id: 
                    player_obj.round_score += match.player_2_score 

        for player_obj in curr_players: 
            player_obj.serialize_object(False) 
        return curr_players  # list of objects  


    def set_players_scores_to_zero(self, tournament_obj): 
        """ At the begining of a tournament, 
            sets the players round_scores and tournament_scores to 0. 
            param: 
                tournament (Tournament_model instances): the tournament from which to set the players scores to zero. 
            returns: 
                updated_players_objs: a list of the updated players (Player_model instances). 
        """ 
        players_objs = helpers.select_tournament_players(tournament_obj.id) 
        updated_players_objs = [] 
        for player_obj in players_objs: 
            player_obj.round_score = float(0) 
            player_obj.tournament_score = float(0) 
            updated_players_objs.append(player_obj) 

            player_obj.serialize_object(False) 

        return updated_players_objs 


    # ============ T O U R N A M E N T S ============ # 


    def enter_new_tournament(self, last_tournament_obj): 
        """ Register a new tournament with the data entered by the user. 
            Args: 
                last_tournament_obj (Tournament_model instance): the tournament to register. 
            returns: 
                tournament_obj(Tournament_model instance) 
        """ 
        # Get the data for the current tournament: 
        tournament_data = self.in_view.input_tournament() 

        players_ids = re.findall(r'\d+', tournament_data['players']) 
        tournament_data['players'] = [int(id) for id in players_ids] 

        # Set the id relative to the last tournament: 
        last_tournament_obj = helpers.select_one_tournament('last') 
        if not last_tournament_obj: 
            tournament_data['id'] = 1 
        else: 
            tournament_data['id'] = int(last_tournament_obj.id) + 1 

        tournament_data['rounds'] = [] 

        tournament_obj = Tournament_model(**tournament_data) 
        # à tester ### 
        tournament_obj.serialize_object(True)  # new object 

        return tournament_obj 


    def close_tournament(self, tournament_obj): 
        """ Assigns the date value to the end_date of the tournament. Serializes the tournament. 
            Args: 
                tournament_obj (Tournament_model instance): the tournament to close. 
            returns: 
                tournament_obj (Tournament_model instance): the closed tournament. 
        """ 
        today = date.today() 
        if not tournament_obj: 
            tournament_obj = helpers.select_one_tournament('last') 

        if tournament_obj.end_date != '': 
            print(f'Le tournoi {tournament_obj.name} est déjà clôturé. ') 

        closing_tournament = self.in_view.input_closing_tournament() 
        if not (closing_tournament == 'y') or (closing_tournament == 'Y'): 
            print('\nLa clôture du tournoi a été annulée, vous pourrez la relancer depuis le menu. ') 
        else: 
            # Set the end_date 
            tournament_obj.end_date = str(today) 
            if not tournament_obj.serialize_object(False): 
                print('\nIl y a eu un problème. Essayez de recommencer et envoyez un feedback. \
                    Merci de votre compréhension. ') 
            else: 
                print(f'''
                    \nLe tournoi {tournament_obj.name} a été clôturé avec succès. 
                ''') 

        return tournament_obj 


    # ============ R O U N D S ============ # 


    def enter_new_round(self, first_round, tournament_obj):  # first_round = bool 
        """ Registers a new round with its data. Serializes the tournament. 
            Args: 
                first_round (bool): if it is the first round. 
                tournament_obj (Tournament_model instance): the tournament which to get the round from. 
            Returns: 
                round_object (Round_model instance): the new round, registered. 
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

        round_object = Round_model(**round_data) 
        tournament_obj.rounds.append(round_object) 
        tournament_obj.serialize_object(False)  # not new object 

        return round_object 


    # ============ M A T C H E S ============ # 


    def enter_new_matches(self, first_round, last_tournament): 
        """ Defines the new matches. They will be registered into the main_container. 
            Args:
                first_round (bool): if this is the first round. 
                last_tournament (Tournament_model instance): the tournament which contains the round. 
            Returns: 
                next_matches (list of Match_model instances): the matches to register. 
        """ 
        players_objs = helpers.select_tournament_players(last_tournament.id) 

        if first_round: 
            selected = helpers.random_matches(players_objs) 
        else: 
            selected = players_objs 
        next_matches = helpers.make_peers(selected, first_round, last_tournament)  # True = first_round 

        return next_matches 


    def enter_scores(self, tournament_obj): 
        """ Get the scores from the terminal and register them into the tournaments.json. 
            Args: 
                tournament_obj (Tournament_model instance): the tournament to update the scores. 
            Returns: 
                tournament_obj (Tournament_model instance): the updated tournament. 
        """ 
        last_round = tournament_obj.rounds.pop() 
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

        tournament_obj.rounds.append(last_round) 

        # Serialize the tournament (new=False)  
        tournament_obj.serialize_object(False) 

        return tournament_obj 




