
from .abstract_model import AbstractModel 


import json 



class Match_model(AbstractModel): 

    def __init__(self, match_id_joueur_1:int, match_score_joueur_1:float, match_id_joueur_2:int, match_score_joueur_2:float, round_id:int): 
        super().__init__('t_table') 
        # self.id = id 
        self.match_id_joueur_1 = match_id_joueur_1 
        self.match_score_joueur_1 = match_score_joueur_1 
        self.match_id_joueur_2 = match_id_joueur_2 
        self.match_score_joueur_2 = match_score_joueur_2 
        # self.match = match 
        self.round_id = round_id 

    def __str__(self): 
        match = ([self.match_id_joueur_1, self.match_score_joueur_1], [self.match_id_joueur_2, self.match_score_joueur_2]) 
        print(f'type(match) MM23 : {type(match)}') 
        return f'{match}' 


    def to_dict(self): 
        return ( [self.match_id_joueur_1, self.match_score_joueur_1], [self.match_id_joueur_2, self.match_score_joueur_2] ) 
    

    def serialize(self): 
        """ Rewrite method for serialize the match objects into the round table""" 
        if not self.check_if_json_empty(): 
            # Get all the data from the t_table: 
            tournaments = self.get_registered() 
            # Get the current_tournament 
            # current_tournament = objects.pop() 
            current_tournament = tournaments[-1] 
            print(f'current_tournament MM44 : {current_tournament}') 
            # Get the rounds from the current_tournament 
            rounds = current_tournament['rounds'] 
            r_id = int(self.round_id)-1 
            if r_id > len(rounds): 
                return False 
            else: 
                # Get the round with the match.round_id 
                current_round = rounds[r_id] 
                print(f'current_round MM53 : {current_round}') 

                if 'matches' not in current_round.keys(): 
                    current_round['matches'] = [] 
                else: 
                    current_round['matches'].append(self.to_dict()) 
                print(f'current_round MM59 : {current_round}') 
                print(f'current_tournament MM60 : {current_tournament}') 
        else: 
            print('Erreur : la table t_table ne peut pas être vide.') 
        with open(f'tables/{self.table}.json', 'w') as file: 
            json.dump(tournaments, file) 



""" 
    Un match unique doit être stocké sous la forme d'un tuple 
    contenant deux listes, 
    chacune contenant deux éléments : 
        une référence à une instance de joueur et un score. 
    Les matchs multiples doivent être stockés sous forme de liste 
    sur l'instance du tour.
""" 

