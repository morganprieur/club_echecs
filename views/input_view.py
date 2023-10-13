
from datetime import date 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    def __init__(self): 
        pass 

    # ============ P L A Y E R S ============ # 

    def input_player(self):  # ok 230507 
        new_player = {} 
        new_player['firstname'] = session.prompt('\nPrénom : ') 
        new_player['lastname'] = session.prompt('\nNom : ')  
        new_player['ine'] = session.prompt('\nI. N. E. : ')  
        new_player['birthdate'] = str(session.prompt('\nDate de naissance (yyyy-mm-dd) : ')) 
        return new_player 

    # ============ T O U R N A M E N T S ============ # 

    def input_tournament(self):  # ajouter sélection des joueurs ### 
        today = date.today() 

        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['start_date'] = str(today) 
        new_tournament['end_date'] = '' 

        rounds_number = session.prompt('\nNombre de rounds ("Entrée" = 4) ') 
        new_tournament['rounds_left'] = 4 if rounds_number == '' else int(rounds_number) 

        # récupérer les joueurs pour les enregistrer dans le fichier tournaments.json 
        new_tournament['players'] = session.prompt('\nJoueurs (id séparées par des virgules) : ') 

        # new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 

        return new_tournament 

    def input_closing_tournament(self): 
        is_tournament_done = session.prompt('\nC\'est le dernier round. Confirmer la clôture du tournoi ? (y/N) : ') 
        return is_tournament_done 

    # ============ R O U N D S ============ # 

    """ Rounds """ 
    def input_round(self): 
        new_round = {} 
        # round.id is automatically defined (into Main_controller): 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        return new_round 

    """ Rounds """ 
    def input_closing_round(self): 
        is_round_done = session.prompt('Confirmer la clôture du round ? (y/N) ') 
        return is_round_done  

    # ============ M A T C H E S ============ # 

    """ Matches (automatique) """  # TODO: supprimer ??? ### 
    def input_match(self): 
        new_match = {} 
        # match.id is automatically defined (into Main_controller): 
        new_match['round_id'] = int(session.prompt('\nID du round : '))  # to define automatically ### 
        new_match['id_joueur_1'] = int(session.prompt('\nID du joueur n°1 : ')) 
        new_match['score_joueur_1'] = float(session.prompt('\nScore du joueur n°1 : ')) 
        new_match['id_joueur_2'] = int(session.prompt('\nID du joueur n°2 : ')) 
        new_match['score_joueur_2'] = float(session.prompt('\nScore du joueur n°2 : ')) 
        return new_match 

    """ Matches """ 
    def input_scores(self, matches): 
        null_matches = [] 
        winners = [] 
        for match in matches: 
            print(f'\n\033[1mMatch : joueur {match.player_1_id} contre joueur {match.player_2_id}\033[0m ') 
            null_match = session.prompt('\nY a-t-il match nul ? (y/n) ') 
            if null_match == 'y': 
                null_matches.append(match) 
            else: 
                winner_position = int(session.prompt(f'''
                                                     \nQuel joueur a gagné {match.player_1} ou {match.player_2} ? 
                                                     (Entrer sa place dans la liste : 1 ou 2) ''')) 
                if winner_position == 1: 
                    winner = match.player_1 
                else: 
                    winner = match.player_2 
                winners.append(winner) 

        return (null_matches, winners) 
