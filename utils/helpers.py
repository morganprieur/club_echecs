

from models.player_model import Player_model 

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
        # print(f'\nchosen DM26 : {chosen}') 
        selected.append(chosen) 
        # print(f'\nselected DM35 : {selected}') 
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

        # For compare the peers: 
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
    print(f'next_matches h69 : {next_matches}') 

    # List of dicts 
    return next_matches 


def define_starters(players, matches): 
    """ Defines who plays the whites for each match. 
        Args: 
            players (List of Player_models): all the players of the tournament. 
            next_matches (list of Match_models): all the new matches. 
        Returns: 
            list of Player_models: only the players who begin the matches. 
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
            # ifnew_match and isinstance(new_match, Match_model): 
            # if player and isinstance(player, Player_model) or player and isinstance(player, dict): 
            if player and isinstance(player, Player_model): 
                if starter[0] == player.id: 
                    starters.append(player) 
            elif player and isinstance(player, dict): 
                if starter[0] == player['id']: 
                    starters.append(player) 
    # List of Player_models 
    return starters 


def sort_objects_by_field(objects, field, reversed=False): 
    """ Sort the given objects dict by the given field. 
        Args: 
            objects (dict): the list of objects to sort. 
            field (string): the field which sort. 
            reversed (bool): if we have to reverse the result. Default False. 
        Returns objects 
    """ 
    objects.sort(key=attrgetter(field), reverse=reversed) 
    return objects 



