
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 
from datetime import datetime 



class Input_view(): 

    now = datetime.now() 

    def __init__(self, now): 
        self.now = now  

    # print("start input view") 
    
    def input_tournament(self): 
        # print(f'now IV19 : {self.now}') 
        new_tournament = {} 
        # new_tournament['id'] must be defined automatically in MC 
        # new_tournament['id'] = int(session.prompt('\nID du tournoi : ')) 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        # new_tournament['t_date'] = session.prompt('\nDate (YYYY/MM/DD) : ') 
        new_tournament['t_date'] = str(self.now) 
        # new_tournament['players'] = session.prompt('\nJoueurs (id, séparés par des virgules) : ') 
        new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 
        return new_tournament 
    

    def input_player(self): 
        new_player = {} 
        new_player['lastname'] = session.prompt('\nlastname : ')  
        new_player['firstname'] = session.prompt('\nfirstname : ') 
        new_player['rank'] = int(session.prompt('\nrank : ')) 
        return new_player 

    
    def input_round(self): 
        new_round = {} 
        # round.id must be automatically defined (into Main_controller): 
        # new_round['id'] = int(session.prompt('\nID du round : ')) 
        new_round['tournament_id'] = int(session.prompt('\nID du tournoi : ')) 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        new_round['start_datetime'] = str(self.now) 
        return new_round 





