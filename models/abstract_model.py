
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    # Si le fichier JSON n'est pas vide : 
    @staticmethod 
    # def get_tournaments(): 
    def get_registered(table): 
        # with open('tables/t_table.json', 'r') as file: 
        with open(f'tables/{table}', 'r') as file: 
            registered = json.load(file) 
        # print(f'type(self.registered) TM192 : {type(self.registered)}') 
        print(f'registered AC16 : {registered}') 
        print(f'type(registered) AC17 : {type(registered)}') 
        return registered 
    

    # def to_dict(self, exclude=None):
    #     exclude = exclude or []
    #     return {
    #         key: getattr(self, key)
    #         for key in dir(self)
    #         if not key.startswith("_")
    #         and key not in exclude
    #         and not callable(getattr(self, key))
    #         and isinstance(getattr(self, key), (str, int, float))
    #     } 


