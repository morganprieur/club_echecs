
import random 
from datetime import datetime 
from models.player_model import Player_model 
from operator import attrgetter 

""" Random define the pairs of players into each round """  # à corriger ### 
def random_matches(registered_players): 
    """ Select the players' ids for one match. 
        Args: 
            players (list of objects): the list of the players' ids of the last tournament. 
        Returns: 
            selected (list of ints): the list of the selected players' ids. 
    """ 
    print('Define matches first round') 
    selected = [] 
    # for i in range(int(8)): 
    for i in range(len(registered_players)): 
        # print(f'\nregistered_players DM24 : {registered_players}') 
        # choice = the randomly chosen player's id 
        chosen = random.choice(registered_players) 
        print(f'\nchosen DM26 : {chosen}') 
        selected.append(chosen) 
        print(f'\nselected DM35 : {selected}') 
        # print(f'\nchosen DM27 : {chosen}') 
        # chosen_index = registered_players.index(chosen) 
        # print(f'\nchosen DM29 : {chosen_index}') 
        # print(f'\nregistered_players DM31 : {registered_players}') 
        registered_players.remove(chosen) 
        # print(f'\nregistered_players DM33 : {registered_players}') 
        # print(f'\nregistered_players DM29 : {registered_players}') 
        # print(f'\nchosen DM32 : {chosen}') 
    #     print(f'\nselected[0].__str__() MC872 : {selected[0].__str__()}') 
    #     # print(f'\ntype(selected[0]) MC873 : {type(selected[0])}') 
    return selected 


# TODO: différencier les matches à partir du round 2 
def make_peers(selected, first_round, tournament): 
    """ groups players by peers, and differenciate the matches regarding the precedent ones, if this is not the first. 
    Args:
        selected (list): the players for the matches. 
        first (boolean): is this the first round ? If False: check the precedent matches and blend the players. 
    Returns:
        list: the peers of players that make the matches. 
    """ 
    print(f'now DM69 : {datetime.now()}') 
    print(f'selected DM53 : {selected}') 
    print(f'type(selected[0]) DM54 : {type(selected[0])}') 

    # print(f'current_peer DM60 : {current_peer}') 
    firsts = rev[::2] 
    # print(f'firsts DM62 : {firsts}') 
    seconds = rev[1::2] 
    # print(f'seconds DM64 : {seconds}') 

    new_matches = [] 
    if first_round: 
        for firsts, seconds in zip(firsts, seconds): 
            current_peer = ([firsts.id, firsts.local_score], [seconds.id, seconds.local_score])
            new_matches.append(current_peer) 
    else: 
        # sort the players by score 
        selected.sort(key=attrgetter('local_score')) 
        print(f'sort DM57 : {selected}') 
        rev = list(reversed(selected)) 
        print(f'rev DM59 : {rev}') 

        old_matches = [] 
        for round in tournament['rounds']: 
            for match in round['matches']: 
                print('match DM78 : ', match) 
                old_matches.append(match) 
        print('old_matches DM80 : ', old_matches) # [[[1, 0.0], [3, 0.0]], [[9, 0.0], [2, 0.0]], [[5, 0.0], [7, 0.0]], [[4, 0.0], [8, 0.0]]]

        # new_matches = [] 
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
                    new_matches.append(new_match) 
                    print(f'new_matches DM95 : {new_matches}') 
                    break 
    print(f'new_matches DM97 : {new_matches}') 
    
    return new_matches 

""" 

matches = []
while firsts:
    first = firsts.pop(0)
    print("first", first, firsts)
    while seconds:
        second = seconds.pop(0)

        print("second", second, seconds)
        match = (first, second)
        if match in old_matches:
            seconds.append(second)
        else:
            matches.append(match)
            print(matches)
            break
matches

        # differentiate_matches(firsts, seconds, tournament, current_peer) 
        # peers = [] 
        # peer = [] 
        # print(f'i DM83 : {i}') 
        # peer.append(([firsts[i].id, firsts[i].local_score], [seconds[i].id, seconds[i].local_score])) 
        # print(f'peer DM85 : {peer}') 
        
        # if peer in tournament['rounds'] round['match']: 
        
        # for round in tournament['rounds']: 
        #     print(f'round DM77 : {round}') 
        #     for i in range(int(4)): 
        #     # for first in range(len(firsts)): 



        #         if not peer == match: 
        #             peers.append(peer) 
        #             print(f'peers DM88 : {peers}') 
        #             # peer = [] 
        #             print(f'peer DM90 : {peer}') 



        #             for match in round['matches']: 
        #                 print(f'match DM79 : {match}') 

        #             else: 
        #                 # idx1 = l.index('e') 
        #                 # idx2 = l.index('b') 
        #                 # l[idx1], l[idx2] = l[idx2], l[idx1] 
        #                 idx1 = seconds.index[i] 
        #                 idx2 = seconds.index[i+1] 
        #                 seconds[idx1], seconds[idx2] = seconds[idx2], seconds[idx1]

        #                 peer.append(([firsts[i].id, firsts[i].local_score], [seconds[i].id, seconds[i].local_score])) 
        #                 print(f'peer DM102 : {peer}') 
                    
        #             peer = [] 

    return peers 

# ma_liste = [[premier, second] for premier, second in zip(a[::2], a[1::2])] 


""" 
