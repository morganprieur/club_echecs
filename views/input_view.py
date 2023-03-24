
from datetime import datetime 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    now = datetime.now() 

    def __init__(self, now): 
        self.now = now 

    # print("start input view") 

    def input_tournament(self): 
        # print(f'now IV19 : {self.now}') 
        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['t_date'] = str(self.now) 
        # new_tournament['players'] = session.prompt('\nJoueurs (id, séparés par des virgules) : ') 
        new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 
        return new_tournament 

    """ comment """ 
    def input_player(self): 
        new_player = {} 
        new_player['lastname'] = session.prompt('\nlastname : ')  
        new_player['firstname'] = session.prompt('\nfirstname : ') 
        new_player['rank'] = int(session.prompt('\nrank : ')) 
        return new_player 

    """ comment """ 
    def input_round(self): 
        new_round = {} 
        # round.id must be automatically defined (into Main_controller): 
        new_round['tournament_id'] = int(session.prompt('\nID du tournoi : ')) 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        # new_round['start_datetime'] = str(self.now) 
        # Date + heure de fin du round quand on démarre un nouveau round : 
        # new_round['end_datetime'] = str(self.now) 
        return new_round 

    """ comment """ 
    def input_match(self): 
        new_match = {} 
        # match.id must be automatically defined (into Main_controller): 
        new_match['round_id'] = int(session.prompt('\nID du round : ')) 
        new_match['id_joueur_1'] = int(session.prompt('\nID du joueur n°1 : ')) 
        new_match['score_joueur_1'] = float(session.prompt('\nScore du joueur n°1 : ')) 
        new_match['id_joueur_2'] = int(session.prompt('\nID du joueur n°2 : ')) 
        new_match['score_joueur_2'] = float(session.prompt('\nScore du joueur n°2 : ')) 

        # new_match['player_1'] = [new_match['id_joueur_1'], new_match['score_joueur_1']] 
        # new_match['player_2'] = [new_match['id_joueur_2'], new_match['score_joueur_2']] 
        # new_match['match'] = tuple() 
        print(f'match IV59 : {new_match}') 
        return new_match 

