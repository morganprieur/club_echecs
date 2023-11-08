
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 
    """ Abstract class to extend by the model classes. """ 
    def __init__(self, table) -> None: 
        self.table = table 


    def serialize_object(self, new=True): 
        """ Abstract method for serializing the objects from the models 
            when adding or changing a new one. 
            new (boolean): new object or not. 
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


    @staticmethod 
    def check_if_json_empty(table): 
        """ Method to prevent throwing exception if the json file is empty. 
            Args:
                table (string): the json file name (without the '.json' extension) where the data is registered. 
            Returns:
                bool: True if the file is empty, False if it isn't empty. 
        """
        with open(f"data/{table}.json", 'rb') as f: 
            if len(f.read()) == 0: 
                return True 
            else: 
                return False 


    @staticmethod 
    def get_registered_dict(table): 
        """ Gets the data from a json file. 
            Args: 
                table (str): the json file name (without the '.json' extension) where the data is registered. 
            returns: 
                registered (list of dicts): the data registered. 
                or empty list if the file doen't contain anything. 
        """ 
        with open(f'data/{table}.json', 'r') as file: 
            # list of dicts : 
            try:  
                registered = json.load(file) 
            # except: 
            except json.decoder.JSONDecodeError: 
                return [] 
        return registered 

