
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    new_tournament = { 
        'name': 'Nom 013', 
        'site': 'Lieu 013', 
        't_date': '2023/01/12', 
        'duration': 'blitz', 
        'description': 'Description 013' 
    } 

    def __init__(self, new_tournament):
        self.new_tournament = new_tournament 
    
    print("start input view") 

    def get_new_tourns(self): 
        # print(f'dir(self) : {dir(self)}') 
        # self.new_tournaments = [] 
        # self.new_tournaments.append(self.new_tournament)  
        print(f'self.new_tournament IV25 : {self.new_tournament}') 
    
    # def get_fct(self): 
    #     print(f'dir(self.get_new_tourns(self)) : {dir(self.get_new_tourns(self))}') 
        

    def get_input_tournament(self): 
        self.new_tournaments = [] 
        self.new_tournament = {} 
        self.new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        self.new_tournament['site'] = session.prompt('\nLieu : ') 
        self.new_tournament['t_date'] = session.prompt('\nDate (YYYY/MM/DD) : ') 
        self.new_tournament['duration'] = session.prompt('\nDurée : ') 
        self.new_tournament['description'] = session.prompt('\nDescription : ') 
        self.new_tournaments.append(self.new_tournament)  
        
    

    def print_input(self): 
        self.get_input_tournament(self) 
        print(f'self.new_tournament : {self.new_tournament}') 





