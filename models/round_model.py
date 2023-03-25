
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 
from .match_model import Match_model 

import json 


class Round_model(AbstractModel): 

    def __init__(self, id: int, round_name: str, tournament_id: int, start_datetime: str, matches: list, end_datetime:str): 
        super().__init__('tournaments') 
        self.id = id 
        self.round_name = round_name 
        self.start_datetime = start_datetime 
        self.end_datetime = end_datetime 
        self.tournament_id = tournament_id 
        # if matches and isinstance(matches[0], dict): 
        if matches and isinstance(matches[0], tuple): 
            # print(f'matches RM19 : {matches}') 
            self.matches = [Match_model(*data) for data in matches] 
        else: 
            self.matches = matches 
        
    def __str__(self): 
        if self.end_datetime : 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        round_string_start = (f'ID du round : {self.id}, nom : {self.round_name}, début : {self.start_datetime}, tournament_id : ') 
        round_string_end = (f', fin : {end_datetime}, {self.tournament_id}, matches : {self.matches}') 
        return round_string_start + round_string_end 

    """ comment """ 
    def to_dict(self): 
        if self.end_datetime: 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        round = { 
            'id': self.id, 
            'round_name': self.round_name, 
            'tournament_id': self.tournament_id, 
            'start_datetime': self.start_datetime, 
            'end_datetime': end_datetime 
        } 
        return round 

    """ comment """ 
    def serialize(self): 
        """ Rewrite method for serialize the round objects into the tournament file. """ 
        if not self.check_if_json_empty(): 
            objects = self.get_registered() 
            # print(f'type(objects[0]) RM46 : {type(objects[0])}') 
            # # with open(f'tables/t_table.json', 'r') as file: 
            # with open(f'data/tournaments.json', 'r') as file: 
            with open(f'data/{self.table}.json', 'r') as file: 
                t_id = int(self.tournament_id) - 1 
                if t_id > len(objects): 
                    return False 
                else: 
                    t_dict = objects[t_id] 

                    # keys = [] 
                    # for k,v in t_obj.items(): 
                    #     keys.append(k) 

                    if "rounds" not in t_dict.keys(): 
                        # print(f't_obj["rounds"]) n\'existe pas RM57') 
                        t_dict['rounds'] = [] 
                    else: 
                        t_dict['rounds'].append(self.to_dict()) 
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(objects, file) 


""" 
if __name__ == "__main__": 
    new_round = { 
        'id': 1, 
        'round_name': 'round_220', 
        'start_datetime': "2023-03-10 10:54:20.299443", 
        'tournament_id': 7 
    } 
    one_round = Round_model(**new_round) 
    print(f'new_round RM85 : {new_round}') 
    one_round.serialize() 
""" 

""" 
Round = liste des matches 
V un champ de nom. 
    --> Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 
V un champ Date et heure de début 
un champ Date et heure de fin, 
    V--> automatiquement remplis lorsque l'utilisateur crée un tour 
        et le marque comme terminé. 
V Les instances de round doivent être stockées dans une liste sur 
l'instance de tournoi à laquelle elles appartiennent.
""" 
