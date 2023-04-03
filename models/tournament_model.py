
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
            self.players = [Player_model(*data) for data in players] 
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

    def __str__(self):  # , roundDicts        
        tournament_string_start = (f'{self.id}, {self.name}, {self.site}, {self.start_date}, {self.end_date}, players : {self.players}') 
        tournament_string_end = (f' rounds : \n{self.rounds}, {self.duration}, {self.description}') 
        return tournament_string_start + tournament_string_end 

    """ comment """ 
    def to_dict(self): 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            'start_date': self.start_date, 
            'end_date': self.end_date, 
            'players': self.players, 
            'rounds': self.rounds, 
            'duration': self.duration, 
            'description': self.description 
        } 
    
    """ comment """ 
    def serialize_modified_object(self):
        """ Abstract method for serialize the objects from the models. """ 
        if not self.check_if_json_empty(): 
            t_dicts = self.get_registered() 
            print(f'\nt_dicts TM69 : {t_dicts}') 
            print(f'\ndir(self) TM70 : {dir(self)}') 
            # suppress the last tournament : 
            t_dicts.pop() 
            # serialize the rounds 
            t_dicts.append(self.to_dict()) 
            print(f'\nt_dicts TM76 : {t_dicts}') 
            t = t_dicts[-1] 
            print(f'\nt TM78 : {t}') 
            rounds_obj = t['rounds'] 
            print(f'\nrounds TM80 : {rounds_obj}') 
            rounds = [] 
            for round in rounds_obj: 
                print(f'\nround TM83 : {round}') 
                print(f'\ntype(round) TM84 : {type(round)}') 
                round_dict = round.to_dict() 
                # rounds.append(round.to_dict()) 
                print(f'\ntype(round_dict) TM88 : {type(round_dict)}') 
                rounds.append(round_dict) 
                matches_obj = round_dict['matches'] 
                matches = [] 
                for match in matches_obj: 
                    match = match.to_dict() 
                    # matches.append(match.to_dict()) 
                    matches.append(match) 
                    print(f'\nmatch TM95 : {match}') 
                    print(f'\ntype(match) TM95 : {type(match)}') 
                print(f'\nmatches TM96 : {matches}') 
                round_dict['matches'] = matches 
                # rounds.append(round) 
            print(f'\nrounds TM100 : {rounds}') 
            t_dicts[-1]['rounds'] = rounds 
            print(f'\nt_dicts TM102 : {t_dicts}') 
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(t_dicts, file, indent=4) 
            # json.dump(objects, file, default=my_callback)  # voir howto callback, dump ne veut pas "my_callback" en defaut 
        
    # def my_callback(obj): 
    #     # objs = [] 
    #     # Effectue une opération sur l'objet avant la sérialisation 
    #     # objs.append(obj.to_dict) 
    #     obj.to_dict 
    #     return obj 

    #     my_object = {'foo': 'bar', 'baz': [1, 2, 3]}
    #     with open('myfile.json', 'w') as f:
    #         json.dump(my_object, f, default=my_callback) 


    ### 
    # def serialize_modified_object(self): 
    #     """ Abstract method for serialize the objects from the models. """ 
    #     if not self.check_if_json_empty(): 
    #         objects = self.get_registered() 
    #         # select the last tournament : 
    #         t_dict = objects[-1] 
    #         t_dict['rounds'].pop() 
    #         # print(f't_dict RM90 : {t_dict}') 
    #         t_dict['rounds'].append(self.to_dict()) 
    #         # print(f't_dict["rounds"] RM83 : {t_dict["rounds"]}') 
    #     else: 
    #         print('Erreur : le fichier tournaments ne peut pas être vide.') 
    #     with open(f"data/{self.table}.json", "w") as file: 
    #         json.dump(objects, file) 
    ### 


