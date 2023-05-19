
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    def __init__(self, table) -> None: 
        self.table = table 
        pass 

    @staticmethod 
    def check_if_json_empty(table): 
    # def check_if_json_empty(self): 
        # print(f'self.table in AM14 : {self.table}') 
        with open(f"data/{table}.json",'rb') as f: 
        # with open(f"data/{self.table}.json",'rb') as f: 
            if len(f.read()) == 0: 
                # print("The file is empty.") 
                return True 
            else: 
                # print("The file is not empty.") 
                return False 

    # TODO: merge the 2 following methods: 
    def get_registered(self): 
        # print(f'self AM26 : {self}') 
        with open(f'data/{self.table}.json', 'r') as file: 
            registered = json.load(file) 
        return registered 

    @staticmethod 
    def get_registered_dict(table): 
        with open(f'data/{table}.json', 'r') as file: 
            # list of dicts : 
            registered = json.load(file) 
        return registered 
    
    @staticmethod  # à corriger ### 
    def select_one_obj(table, obj_id): 
        objs = AbstractModel.get_registered_dict(table) 
        # objs = AbstractModel.get_registered_all(table) 
        objet = objs[obj_id] 
        return objet  

    def serialize_object(self, new=True): 
        """ Abstract method for serialize the objects from the models 
            when adding a new one. 
            new (boolean): 
                if the object must be added -> True, 
                if it must be replaced -> False. 
        """ 
        # print(f'self.table AM41 :{self}') 
        # print(f'self.table AM48 :{self.table}') 
        if not self.check_if_json_empty(self.table):  ### ??? 
            objects = self.get_registered() 
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





