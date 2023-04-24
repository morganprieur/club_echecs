
from .abstract_model import AbstractModel 
from .player_model import Player_model 
from .round_model import Round_model 

import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 


class Tournament_model(AbstractModel): 

    def __init__( 
        self, id: int, 
        name: str, 
        site: str, 
        start_date: str, 
        end_date: str, 
        players: list, 
        rounds: list, 
        duration: str, 
        description: str 
    ):  # ,  nb_rounds:int,  
        super().__init__('tournaments') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.start_date = start_date 
        self.end_date = end_date 
        if players and isinstance(players[0], dict): 
            print(f'\nplayers TM33 : {players}')  # (list of dicts)
            self.players = [Player_model(**data) for data in players] 
        else: 
            self.players = players 
        # self.nb_rounds = nb_rounds 
        if rounds and isinstance(rounds[0], dict): 
            print(f'\nrounds TM26 : {rounds}')  # (list of dicts)
            self.rounds = [Round_model(**data) for data in rounds] 
        else: 
            self.rounds = rounds 
        self.duration = duration 
        self.description = description 

    def __str__(self): 
        return ( 
            f'{self.id}, {self.name}, {self.site}, {self.start_date}, {self.end_date}, players : {self.players}  rounds : \n{self.rounds}, {self.duration}, {self.description}' 
        ) 


    """ comment """ 
    def to_dict(self): 
        player_ids = [player.id for player in self.players]
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            'start_date': self.start_date, 
            'end_date': self.end_date, 
            # 'players': self.players.id, 
            'players': player_ids, 
            'rounds': self.rounds, 
            'duration': self.duration, 
            'description': self.description 
        } 
    
    """ comment """ 
    def serialize_object(self, new):
        """ Abstract method for serialize the objects from the models. """ 
        print(f'\ntype(self) TM68 : {type(self)}')
        print(f'\ndir(self) TM69 : {dir(self)}') 
        # [6, 0.5] ok : 
        print(f'\nself.rounds[0].matches[0].player_1 TM70 : {self.rounds[0].matches[0].player_1}')
        if not self.check_if_json_empty(): 
            # Get the tournaments from the JSON file 
            t_dicts = self.get_registered() 
            print(f'\nt_dicts TM75 : {t_dicts}') 
            print(f'\ntype(t_dicts) TM76 : {type(t_dicts)}') 
            if new == False: 
                # Replace the last tournament with the modified one : 
                t_dicts.pop() 
                t_dicts.append(self.to_dict()) 
                print(f'\nt TM78 : {t}')  #### 
            print(f'\nt_dicts TM79 : {t_dicts}') 
            # t_dicts.pop().append(self.to_dict()) 
            # t_dicts.pop() 
            # serialize the tournaments with the last modified 
            # t_dicts.append(self.to_dict()) 
            # Get the last modified tournament 
            
            t = t_dicts.pop()  # à vérifier ### 

            # Select the rounds 
            rounds_dict = t['rounds'] 
            if len(rounds_dict) > 1: 
                rounds_dict.pop() 
            unchanged_rounds = rounds_dict 
            print(f'\nunchanged_rounds TM92 : {unchanged_rounds} \n') 
            rounds = [] 
            # Append the round from self  
            # for round in unchanged_rounds: 
            # print(f'\ntype(round) TM94 : {type(rounds[-1])} \n') 
            # round_dict = round.to_dict() 
            # rounds.append(round_dict) 
            # rounds.append(round) 
            rounds.append(self.rounds[-1].to_dict()) 
            # rounds.append(round.to_dict()) 
            # matches_obj = round_dict['matches'] 
            # round_dict = rounds[-1] 
            print(f'\nrounds[-1] TM104 : {rounds[-1]} \n') 
            # print(f'\ntype(round_dict) TM102 : {type(round_dict)} \n') 
            print(f'\ntype(rounds[0]) TM106 : {type(rounds[0])} \n') 
            matches_obj = rounds[-1]['matches'] 
            print(f"\nmatches_obj[-1].player_1 TM108 : {matches_obj[-1].player_1} \n") 
            print(f'\ntype(matches[-1]) TM109 : {type(rounds[-1])} \n') 
            matches = [] 
            for one_match in matches_obj: 
                # matches.append(one_match.to_dict()) 
                matches.append(one_match.match) 

            print(f'\nmatches TM112 : {matches} \n') 
            # matches_obj.pop() 
            # unchanged_matches = matches_obj 
            # matches = [] 
            # Serialize the matches 
            # for match in matches_obj: 
            #     print(f'\nmatch TM111 : {match} \n') 
            #     print(f'\ntype(match) TM112 : {type(match)} \n') 
            #     # match_dict = match.to_dict() 
            #     matches.pop().append(match) 
            #     # matches.append(match.to_dict()) 
            # round_dict['matches'] = matches 
            rounds[-1]['matches'] = matches 
            # rounds[-1]['matches'] = matches_obj 
            print(f"\nrounds[-1]['matches'] TM125 : {rounds[-1]['matches']} \n") 
            
            t_dicts[-1]['rounds'] = rounds 
            print(f'\nrounds TM119 : {rounds} \n') 
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(t_dicts, file, indent=4) 
    #         json.dump(t_dicts, file, default=self.my_callback)  # voir howto callback, dump ne veut pas "my_callback" en defaut 
        
    # def my_callback(obj): 
    #     # objs = [] 
    #     # Effectue une opération sur l'objet avant la sérialisation 
    #     # objs.append(obj.to_dict) 
    #     obj.to_dict 
    #     return obj 




