

from models.player_model import Player_model 
from models.tournament_model import Tournament_model 

from operator import attrgetter 
import random 


def random_matches(registered_players): 
    """ Random define the pairs of players for each round. 
        Args: 
            players (list of objects): the list of the players' ids of the last tournament. 
        Returns: 
            selected (list of ints): the list of the selected players' ids. 
    """ 
    print('Define matches first round ') 
    selected = [] 
    for i in range(len(registered_players)): 
        chosen = random.choice(registered_players) 
        selected.append(chosen) 
        registered_players.remove(chosen) 
    return selected 


def make_peers(selected, first_round, tournament): 
    """ groups players by peers, and differenciate the matches regarding the precedent ones, if this is not the first. 
        Args:
            selected (list): the players for the matches. 
            first (boolean): is this the first round ? If False: check the precedent matches and blend the players. 
        Returns:
            list: the peers of players that make the matches. 
    """ 
    firsts = selected[::2] 
    seconds = selected[1::2] 

    next_matches = [] 
    if first_round: 
        for firsts, seconds in zip(firsts, seconds): 
            current_peer = ([firsts.id, firsts.local_score], [seconds.id, seconds.local_score])
            next_matches.append(current_peer) 
    else: 
        # sort the players by score 
        selected.sort(key=attrgetter('local_score')) 
        list(reversed(selected)) 

        # For comparing the peers: 
        old_matches = [] 
        for round in tournament.rounds: 
            for match in round.matches: 
                old_matches.append(match) 

        # Define peers: 
        while firsts: 
            first = firsts.pop(0) 
            while seconds: 
                second = seconds.pop(0) 

                new_match = ([first.id, float(0.0)], [second.id, float(0.0)]) 
                if new_match in old_matches: 
                    seconds.append(second) 
                else: 
                    next_matches.append(new_match) 
                    break 
    # List of dicts 
    return next_matches 


def define_starters(players, matches): 
    """ Defines who plays the whites for each match. 
        Args: 
            players (List of Player_models): all the players of the tournament. 
            next_matches (list of Match_models): all the new matches. 
        Returns: 
            starters (list of Player_models): only the players who begin the matches. 
    """ 
    # Determines the ids of the players who play the whites 
    whites = [] 
    for match in matches: 
        white = random.choice(match) 
        whites.append(white) 

    starters = [] 
    # Displays who begins  
    for starter in whites: 
        for player in players: 
            if player and isinstance(player, Player_model): 
                if starter[0] == player.id: 
                    starters.append(player) 
            elif player and isinstance(player, dict): 
                if starter[0] == player['id']: 
                    starters.append(player) 
    # List of Player_models 
    return starters 


# ============ U T I L S ============ # 


def select_one_player(player_id): 
    """ Select one player object from its id, from the players.json file. 
        Args:
            player_id (int): the player's id 
        Returns: 
            player (object): player object 
    """ 
    if not Player_model.check_if_json_empty: 
        print('Il n\'y a pas de joueur à afficher. ') 
        return False 
    else: 
        players_dicts = Player_model.get_registered_dict('players') 
        players_objs = [Player_model(**data) for data in players_dicts] 

        if player_id == 'last': 
            ids = [] 
            for player in players_objs: 
                ids.append(player.id) 
            last_player_id = max(ids) 
            # print(f'last_player_id H122 : {last_player_id}') 
            for player in players_objs: 
                if player.id == last_player_id: 
                    return player 
        else: 
            for player in players_objs: 
                if player.id == player_id: 
                    return player 


def select_tournament_players(tournament_id): 
    # """ Selects the players of the `self.tournament_obj` 
    """ Selects the players of the `tournament_id` tournament 
        already selected into the precedent method. 

        Returns:
            list of Player_models: Returns a list of objects Player, stored in Main_controller. 
    """ 
    tournament_obj = select_one_tournament(tournament_id) 
    # tournament_obj = Tournament_model(**tournament) 
    players_ids = tournament_obj.players 

    players_objs = [] 
    for player_id in players_ids: 
        player = select_one_player(player_id) 
        players_objs.append(player) 
    return players_objs  # list of objects 


def select_one_tournament(tournament_id): 
    """ Select one tournament from its id, from the tournaments.json file. 
        Args:
            tournament_id (int): the tournament's id 
        Returns:
            t_obj (Object): the tournament object 
    """ 
    # Vérifier check_if_json_empty(table) : ### 
    if not Tournament_model.check_if_json_empty('tournaments'): 

        if Tournament_model.get_registered_dict('tournaments') == []: 
            t_obj = None  
        else: 
            t_dicts = Tournament_model.get_registered_dict('tournaments') 
            t_objs = [Tournament_model(**data) for data in t_dicts] 

            if tournament_id == 'last': 
                id = 0 
                for tourn in t_objs: 
                    if tourn.id > id: 
                        id = tourn.id 
                    if tourn.id == id: 
                        t_obj = tourn 
            else: 
                for tourn in t_objs: 
                    if tourn.id == int(tournament_id): 
                        t_obj = tourn 
            return t_obj 


def sort_objects_by_field(objects, field, reversed=False): 
    """ Sort the given objects dict by the given field. 
        Args: 
            objects (dict): the list of objects to sort. 
            field (string): the field which sort. 
            reversed (bool): if we have to reverse the result. Default False. 
        Returns objects 
    """ 
    if field == 'score': 
        objects.sort(key=attrgetter('ine'), reverse=reversed) 
    else: 
        objects.sort(key=attrgetter(field), reverse=reversed) 
    return objects 

