
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    def __init__(self, table) -> None: 
        self.table = table 
        pass 

    
    # Test with the object in argument
    # @staticmethod 
    # def check_if_json_empty(table): 
    #     print(f'table in AM14 : {table}') 
    #     with open(f"tables/{table}.json",'rb') as f: 
    #         if len(f.read()) == 0: 
    #             print("The file is empty.") 
    #             return True 
    #         else: 
    #             print("The file is not empty.") 
    #             return False 
    def check_if_json_empty(self): 
        print(f'self.table in AM14 : {self.table}') 
        with open(f"tables/{self.table}.json",'rb') as f: 
            if len(f.read()) == 0: 
                print("The file is empty.") 
                return True 
            else: 
                print("The file is not empty.") 
                return False 
    

    # Si le fichier JSON n'est pas vide : 
    # @staticmethod 
    # def get_registered(table): 
    #     # print(f'self AM26 : {self}') 
    #     with open(f'tables/{table}.json', 'r') as file: 
    #         registered = json.load(file) 
    #     return registered 
    def get_registered(self): 
        print(f'self AM26 : {self}') 
        with open(f'tables/{self.table}.json', 'r') as file: 
            registered = json.load(file) 
        return registered 
    

    @staticmethod 
    def get_registered_all(table): 
        with open(f'tables/{table}.json', 'r') as file: 
            registered = json.load(file) 
        return registered 
    

    def serialize(self): 
        """ Abstract method for serialize the objects from the models. """ 
        # print(f'self.table AM41 :{self}') 
        # print(f'self.table AM48 :{self.table}') 
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


