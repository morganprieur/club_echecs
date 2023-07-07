
from .abstract_model import AbstractModel 
from .player_model import Player_model 
from .round_model import Round_model 
from .match_model import Match_model 

import json 
import re 

class Tournament_model(AbstractModel): 

    def __init__( 
        self, id: int, 
        name: str, 
        site: str, 
        start_date: str, 
        end_date: str, 
        rounds_left: int, ### ? 
        players: list, 
        rounds: list, 
        description: str 
    ): 
        super().__init__('tournaments') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.start_date = start_date 
        self.end_date = end_date 
        self.rounds_left = rounds_left ### ? nouveau 
        # self.rounds_left = 4 ### ? nouveau 
        if players and isinstance(players[0], dict): 
            self.players = [Player_model(**data) for data in players] 
        else: 
            self.players = players 
        # self.nb_rounds = nb_rounds 
        if rounds and isinstance(rounds[0], dict): 
            # print(f'\nrounds TM39 : {rounds}')  # (list of dicts)
            self.rounds = [Round_model(**data) for data in rounds] 
        else: 
            self.rounds = rounds 
        self.description = description 

    def __str__(self): 
        return ( 
            f'{self.id}, {self.name}, {self.site}, {self.start_date}, {self.end_date},, nombre de rounds : {self.rounds_left}, joueurs : {self.players}  rounds : \n{self.rounds}, {self.description}' 
        ) 


    """ comment """ 
    def to_dict(self): 
        # player_ids = [player.id for player in self.players] 
        player_ids = [player for player in self.players] 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            'start_date': self.start_date, 
            'end_date': self.end_date, 
            'rounds_left': self.rounds_left, 
            'players': player_ids, 
            'rounds': self.rounds, 
            'description': self.description 
        } 
    
    """ comment """ 
    def serialize_object(self, new):
        """ Abstract method to serialize the object 
        Args:
            new (boolean): if the object is new: True, 
                if the data must modify the last entity into the hson: False. 
        """ 
        if not self.check_if_json_empty('tournaments'): 
            # print(f'\ntype(t_dicts) TM76 : {type(t_dicts)}') 
            # Get the tournaments from the JSON file 
            t_dicts = self.get_registered_dict('tournaments') ### à vérifier ### 
            # print(f'\nt_dicts TM86 : {t_dicts}') # list 
            if not new: 
                ### à supprimer : Replaces the last tournament with the modified one : 
                # Removes the last tournament from le list of dicts from json file : 
                last_t_dict = t_dicts.pop() 
                print(f'\nlast_t_dict TM82 : {last_t_dict}')  ### 
            
            last_tournament_dict = self.to_dict() 
            ### à vérifier ### 
            print(f"\nlast_tournament_dict['rounds'][0].matches[0].__str__() TM85 : {last_tournament_dict['rounds'][0].matches[0].__str__()}")  ### 

            last_rounds_list = [] 
            for last_round_obj in last_tournament_dict['rounds']: 
                last_round_dict = Round_model.to_dict(last_round_obj) 
                print(f"\nlast_round_dict['rounds'][0]['matches'][0] TM98 : {last_round_dict['matches'][0]}") # [2, 0.5], [3, 0.5] ok 

                last_matches_list = [] 
                for last_match_obj in last_round_dict['matches']: 
                    print(f'\nlast_match_obj.__str__() TM102 : {last_match_obj.__str__()}')  ### 
                    last_match_dict = Match_model.to_dict(last_match_obj) ### 
                    print(f'\nlast_match_dict TM104 : {last_match_dict}')  ### 

                    last_matches_list.append(last_match_dict) 
                last_round_dict['matches'] = last_matches_list 

                last_rounds_list.append(last_round_dict) 
            last_tournament_dict['rounds'] = last_rounds_list 

            t_dicts.append(last_tournament_dict) 
            print(f't_dicts TM109 : {t_dicts}') 
                
        else: 
            ### 230707 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(t_dicts, file, indent=4) 
    #         json.dump(t_dicts, file, default=self.my_callback)  # voir howto callback, dump ne veut pas "my_callback" en defaut 
        
    def my_callback(obj): 
        # objs = [] 
        # Effectue une opération sur l'objet avant la sérialisation 
        # objs.append(obj.to_dict) 
        obj.to_dict 
        return obj 


