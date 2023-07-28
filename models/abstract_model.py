
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    def __init__(self, table) -> None: 
        self.table = table 
        pass 

    @staticmethod 
    def check_if_json_empty(table): 
        with open(f"data/{table}.json", 'rb') as f: 
            if len(f.read()) == 0: 
                return True 
            else: 
                return False 

    @staticmethod 
    def get_registered_dict(table): 
        with open(f'data/{table}.json', 'r') as file: 
            # list of dicts : 
            try:  
                registered = json.load(file) 
            # except: 
            except json.decoder.JSONDecodeError: 
                return [] 
        return registered 

    @staticmethod  # à corriger ### 
    def select_one_obj(table, obj_id): 
        objs = AbstractModel.get_registered_dict(table) 
        objet = objs[obj_id] 
        return objet  

    def serialize_object(self, new=True): 
        """ Abstract method for serialize the objects from the models 
            when adding a new one. 
            new (boolean): 
                if the object must be added -> True, 
                if it must be replaced -> False. 
        """ 
        if not self.check_if_json_empty(self.table): 
            objects = AbstractModel.get_registered_dict(self.table) 
        else: 
            objects = [] 
        objects.append(self.to_dict()) 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(objects, file, indent=4) 

    @abstractmethod 
    def to_dict(self): 
        """
            A common method for building each model. 
        """ 
        pass 
        # ... 





