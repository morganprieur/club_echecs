
import random 

class Define_matches(): 

    """ Random define the pairs of players into each round """  # à corriger ### 
    def random_matches(self, registered_players): 
        """ Select the players' ids for one match. 
            Args:
                players (list): the list of the players' ids of the last tournament. 
                matches (list): the list of the selected players' ids for the round. 
            Returns:
                list: the list of the selected players' ids, added the new selected ones. 
        """ 
        # self.peers = [] 
        peers = [] 
        for i in range(int(4)): 
            # score = the score at the start of the round (for the first round : 0) 
            # score = float(0) 
            # match = the tuple containing 2 lists 'selected_player' 
            # match = ([], []) 
            # selected = the list of player's id and player's score 
            selected = [] 
            for i in range(int(2)): 
                print(f'\nregistered_players DM24 : {registered_players}') 
                # choice = the randomly chosen player's id 
                chosen = random.choice(registered_players) 
                selected.append(chosen) 
                registered_players.remove(chosen) 
                print(f'\nregistered_players DM29 : {registered_players}') 
                print(f'\nchosen DM30 : {chosen}') 
                print(f'\nselected DM31 : {selected}') 
        #     print(f'\nselected[0].__str__() MC872 : {selected[0].__str__()}') 
        #     # print(f'\ntype(selected[0]) MC873 : {type(selected[0])}') 
            player_1 = [selected[0].id, selected[0].global_score] 
            player_2 = [selected[1].id, selected[1].global_score] 
            # peer = tuple([selected[0].id, selected[0].global_score], [selected[1].id, selected[0].global_score]) 
            peer = [player_1, player_2] 
            print(f'\npeer DM38 : {peer}') 
            # peer_obj = Match_model(*peer) 
            #     match = ([peer[0].id, peer[0].global_score], [peer[1].id, peer[1].global_score]) 
            #     # match = ([selected[0], score], [selected[1], score]) 
            #     print(f'\nmatch MC876 : {match}') 
            #     self.matches.append(match) 
            # self.peers.append(peer) 
            # self.peers.append(peer_obj) 
            peers.append(peer) 
        # print(f'\nself.matches MC878 : {self.matches}') 
        # print(f'\nself.peers MC888 : {self.peers}')  # 4 matches objets ok 
        print(f'\npeers DM49 : {peers}') 
        return peers 





