
import random 
# from datetime import datetime 
from operator import attrgetter 


""" Random define the pairs of players into each round 
""" 


def random_matches(registered_players): 
    """ Select the players' ids for one match. 
        Args: 
            players (list of objects): the list of the players' ids of the last tournament. 
        Returns: 
            selected (list of ints): the list of the selected players' ids. 
    """ 
    print('Define matches first round') 
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
    # print(f'now DM69 : {datetime.now()}') 
    # print(f'selected DM53 : {selected}') 
    # print(f'type(selected[0]) DM54 : {type(selected[0])}') 

    firsts = selected[::2] 
    # print(f'firsts DM62 : {firsts}') 
    seconds = selected[1::2] 
    # print(f'seconds DM64 : {seconds}') 
    # firsts = rev[::2] 
    # # print(f'firsts DM62 : {firsts}') 
    # seconds = rev[1::2] 
    # # print(f'seconds DM64 : {seconds}') 

    next_matches = [] 
    if first_round: 
        for firsts, seconds in zip(firsts, seconds): 
            current_peer = ([firsts.id, firsts.local_score], [seconds.id, seconds.local_score])
            next_matches.append(current_peer) 
    else: 
        # sort the players by score 
        selected.sort(key=attrgetter('local_score')) 
        print(f'sort DM57 : {selected}') 
        rev = list(reversed(selected)) 
        print(f'rev DM59 : {rev}') 

        old_matches = [] 
        for round in tournament.rounds: 
            for match in round.matches: 
                print('match DM78 : ', match) 
                old_matches.append(match) 
        print('old_matches DM80 : ', old_matches) 

        while firsts: 
            first = firsts.pop(0) 
            print("first", first, firsts) 
            while seconds: 
                second = seconds.pop(0) 
                print("second", second, seconds) 

                new_match = ([first.id, first.local_score], [second.id, second.local_score]) 
                if new_match in old_matches: 
                    seconds.append(second) 
                else: 
                    next_matches.append(new_match) 
                    print(f'new_matches DM95 : {next_matches}') 
                    break 
    print(f'next_matches DM81 : {next_matches}') 

    return next_matches 


def define_starters(players, matches): 
    """ Defines who plays the whites for each match. 
        Args: 
            players_obj (Player_model): all the players 
            next_matches (list of Math_models): all the matches 
        Returns: 
            list of Player_models: only the players who begin the matches. 
    """ 
    # Determines the ids of the players who play the whites 
    whites = [] 
    for match in matches: 
        white = random.choice(match) 
        whites.append(white) 
    print(whites) 

    starters = [] 
    # Displays who begins  
    for starter in whites: 
        for player in players: 
            if starter[0] == player['id']: 
                starters.append(player) 
    print(starters) 

    return starters 





