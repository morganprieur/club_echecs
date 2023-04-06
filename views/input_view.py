
from datetime import date 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    today = date.today() 

    def __init__(self, today): 
        self.today = today 

    # print("start input view") 

    def input_tournament(self): 
        # print(f'now IV19 : {self.now}') 
        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['start_date'] = str(self.today) 
        new_tournament['end_date'] = '' 
        # new_tournament['players'] = session.prompt('\nJoueurs (id, séparés par des virgules) : ') 
        new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 
        return new_tournament 

    def input_closing_tournament(self): 
        is_tournament_done = session.prompt('\nConfirmer la clôture du tournoi ? (y/N) : ') 
        return is_tournament_done 

    """ Players """ 
    def input_player(self): 
        new_player = {} 
        new_player['lastname'] = session.prompt('\nNom : ')  
        new_player['firstname'] = session.prompt('\nPrénom : ') 
        new_player['rank'] = int(session.prompt('\nClassement : ')) 
        # new_player['global_score'] = float(0) 
        return new_player 

    """ Rounds """ 
    def input_round(self): 
        new_round = {} 
        # round.id must be automatically defined (into Main_controller): 
        new_round['tournament_id'] = int(session.prompt('\nID du tournoi : ')) 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        # new_round['start_datetime'] = str(self.now) 
        # Date + heure de fin du round quand on démarre un nouveau round : 
        # new_round['end_datetime'] = str(self.now) 
        return new_round 
    
    """ Rounds """ 
    def input_closing_round(self): 
        is_round_done = session.prompt('\nConfirmer la clôture du round ? (y/N)') 
        return is_round_done  

    """ Matches """ 
    def input_match(self): 
        new_match = {} 
        # match.id must be automatically defined (into Main_controller): 
        new_match['round_id'] = int(session.prompt('\nID du round : '))  # to define automatically ### 
        new_match['id_joueur_1'] = int(session.prompt('\nID du joueur n°1 : ')) 
        new_match['score_joueur_1'] = float(session.prompt('\nScore du joueur n°1 : ')) 
        new_match['id_joueur_2'] = int(session.prompt('\nID du joueur n°2 : ')) 
        new_match['score_joueur_2'] = float(session.prompt('\nScore du joueur n°2 : ')) 

        # new_match['player_1'] = [new_match['id_joueur_1'], new_match['score_joueur_1']] 
        # new_match['player_2'] = [new_match['id_joueur_2'], new_match['score_joueur_2']] 
        # new_match['match'] = tuple() 
        print(f'match IV59 : {new_match}') 
        return new_match 

    """ Matches """ 
    def input_matches_scores(self): 
        scores = [] 
        # new_match = [] 
        # print(f'\nnew_match IV78 : {new_match}') 
         
        number_of_matches_scores = int(
            session.prompt('\nCombien de matches à enregistrer ? : ') 
        ) 

        for i in range(number_of_matches_scores): 
            scores.append(int(session.prompt('\nMatch numéro : '))) 
            print(f'\nscores IV86 : {scores}') 

            scores.append(float(session.prompt('\nScore du 1er joueur : ')))     
            print(f'\nscores IV90 : {scores}') 
            # scores.append(score_joueur_1) 
            
            # scores.append(float(session.prompt('\nScore du 2è joueur : '))) 
            # print(f'\nscores IV94 : {scores}') 
            # scores.append(scores) 
            # scores.append(score_joueur_2) 
            # new_match[0][0][1] = float(session.prompt('\nScore du 1er joueur : '))     
            # new_match[1][0][1] = float(session.prompt('\nScore du 2è joueur : '))     
        print(f'\nscores IV99 : {scores}') 
        return scores 

        

