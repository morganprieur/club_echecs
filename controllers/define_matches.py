
import random 


""" Random define the pairs of players into each round """  # à corriger ### 
def random_matches(registered_players): 
    """ Select the players' ids for one match. 
        Args: 
            players (list of objects): the list of the players' ids of the last tournament. 
        Returns: 
            selected (list of ints): the list of the selected players' ids. 
    """ 
    # for i in range(int(4)): 
        # score = the score at the start of the round (for the first round : 0) 
        # score = float(0) 
        # match = the tuple containing 2 lists 'selected_player' 
        # match = ([], []) 
        # selected = the list of player's id and player's score 
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


def make_peers(selected): 

    firsts = selected[::2] 
    seconds = selected[1::2] 
    
    peers = [] 
    for firsts, seconds in zip(firsts, seconds): 
        peers.append([firsts, seconds]) 
            
    return peers 

# ma_liste = [[premier, second] for premier, second in zip(a[::2], a[1::2])] 

