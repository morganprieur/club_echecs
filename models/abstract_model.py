
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    def __init__(self, table) -> None:
        self.table = table 


    def check_if_json_empty(self): 
        with open(f"tables/{self.table}.json",'rb') as f: 
            if len(f.read()) == 0: 
                print("The file is empty.") 
                return True 
            else: 
                print("The file is not empty.") 
                return False 
    
    # @staticmethod 
    # def check_if_json_empty(table): 
    #     with open(f"tables/{table}.json",'rb') as f: 
    #         if len(f.read()) == 0: 
    #             print("The file is empty.") 
    #             return True 
    #         else: 
    #             print("The file is not empty.") 
    #             return False 
    

    # Si le fichier JSON n'est pas vide : 
    # @staticmethod 
    def get_registered(self): 
        # print(f'self AM35 : {self}') 
        # with open(f'tables/{self.table}.json', 'r') as file:  # ==> self.table inconnu 
        with open(f'tables/{self}.json', 'r') as file: 
            registered = json.load(file) 
        # print(f'registered AC16 : {registered}') 
        # print(f'type(registered) AC17 : {type(registered)}') 
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


    # @abstractmethod 
    # def serialize(self): 
    #     """ méthode abstraite blablabla 
    #     """
    #     pass 

    def serialize(self): 
        """
            Abstract method for serialize the objects from the models. 
        """
        # print(f'one_tournament TM172 : {self}') 
        if not self.check_if_json_empty(): 
            objects = self.get_registered() 
        else: 
            objects = [] 
        objects.append(self.to_dict()) 
        with open(f"tables/{self.table}.json", "w") as file: 
            json.dump(objects, file) 
    

    @abstractmethod 
    def to_dict(self): 
        """
            A common method for building each model. 
        """ 
        pass 
        # ... 


