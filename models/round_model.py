
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
            print(f'\nmatches RM21 : {matches}') 
            # self.matches = [Match_model(*data) for data in matches] 
            self.matches = [Match_model(*data) for data in matches] 
            # self.matches = [Match_model([1, 1.5], [2, 2.0]) for data in matches] data = ([1, 1.5], [2, 2.0]) 

        else: 
            self.matches = matches 
        
    def __str__(self): 
        if self.end_datetime : 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        return f'ID du round : {self.id}, nom : {self.round_name}, début : {self.start_datetime}, fin : {end_datetime}, tournament_id : {self.tournament_id}, matches : {self.matches}' 

    """ comment """ 
    def to_dict(self): 
        # To avoid Python throws an error for missing a property: 
        if self.end_datetime: 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        round = { 
            'id': self.id, 
            'round_name': self.round_name, 
            'start_datetime': self.start_datetime, 
            'end_datetime': end_datetime, 
            'tournament_id': self.tournament_id, 
            'matches': self.matches 
        } 
        return round 

    # """ comment """ 
    # def serialize_new_object(self): 
    #     """ Rewrite method for serialize the round objects into the tournament file. """ 
    #     if not self.check_if_json_empty(): 
    #         objects = self.get_registered() 
    #         with open(f'data/{self.table}.json', 'r') as file: 
    #             t_id = int(self.tournament_id) - 1 
    #             if t_id > len(objects): 
    #                 return False 
    #             else: 
    #                 t_dict = objects[t_id] 

    #                 if "rounds" not in t_dict.keys(): 
    #                     # print(f't_obj["rounds"]) n\'existe pas RM57') 
    #                     t_dict['rounds'] = [] 
    #                 else: 
    #                     t_dict['rounds'].append(self.to_dict()) 
    #     else: 
    #         print('Erreur : le fichier tournaments ne peut pas être vide.') 
    #     with open(f"data/{self.table}.json", "w") as file: 
    #         json.dump(objects, file) 

    def serialize_object(self, new): 
        """ Abstract method for serialize the objects from the models. """ 
        if not self.check_if_json_empty('tournaments'): 
            objects = self.get_registered() 
            # select the last tournament : 
            t_dict = objects[-1] 
            if new == False: 
                t_dict['rounds'].pop() 
                # print(f't_dict RM90 : {t_dict}') 
            t_dict['rounds'].append(self.to_dict()) 
            # print(f't_dict["rounds"] RM83 : {t_dict["rounds"]}') 
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(objects, file, indent=4) 

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
