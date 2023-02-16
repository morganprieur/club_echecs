
from abc import ABC, abstractmethod 
import json 


class AbstractModel(ABC): 

    def __init__(self, table) -> None:
        self.table = table 


    def check_if_json_empty(self, table): 
        print(f'self in AM13 : {self}') 
        # with open(f"tables/{self.table}.json",'rb') as f: 
        with open(f"tables/{table}.json",'rb') as f: 
            if len(f.read()) == 0: 
                print("The file is empty.") 
                return True 
            else: 
                print("The file is not empty.") 
                return False 
    

    # Si le fichier JSON n'est pas vide : 
    # @staticmethod 
    def get_registered(self): 
        # print(f'self AM35 : {self}')  # if project.py ==> 'p_table' elif player_model.py ==> object player 
        # with open(f'tables/{self.table}.json', 'r') as file:  # ==> self.table inconnu 
        with open(f'tables/{self}.json', 'r') as file: 
            registered = json.load(file) 
        # print(f'registered AC16 : {registered}') 
        # print(f'type(registered) AC17 : {type(registered)}') 
        return registered 
    ### erreurs 
    ### project.py 
    #     File "C:\Users\mprieur\Dropbox\Formation_OCR\P4\work\models\abstract_model.py", line 36, in get_registered
    #         with open(f'tables/{self.table}.json', 'r') as file:  # ==> self.table inconnu
    #     AttributeError: 'str' object has no attribute 'table'. Did you mean: 'title'? 

    ### player_model.py 
    # File "C:\Users\mprieur\Dropbox\Formation_OCR\P4\work\models\abstract_model.py", line 37, in get_registered
    #     with open(f'tables/{self}.json', 'r') as file:
    # OSError: [Errno 22] Invalid argument: 'tables/<__main__.Player_model object at 0x000002EB64A4FC70>.json' 


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


