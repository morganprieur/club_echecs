
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    def __init__(self) -> None:
        pass 

    # print("start input view") 
    
    def input_tournament(self): 
        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['t_date'] = session.prompt('\nDate (YYYY/MM/DD) : ') 
        new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 
        return new_tournament 
    

    def input_player(self): 
        new_player = {} 
        new_player['lastname'] = session.prompt('\nlastname : ')  
        new_player['firstname'] = session.prompt('\nfirstname : ') 
        new_player['rank'] = session.prompt('\nrank : ') 
        return new_player 






