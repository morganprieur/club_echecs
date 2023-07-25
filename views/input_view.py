
from datetime import date 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 
from datetime import datetime, date 


class Input_view(): 

    # today = date.today() 

    def __init__(self):  # , today 
        # self.today = today 
        pass 

    # print("start input view") 
    
    #### ============ P L A Y E R S ============ #### 

    def input_player(self):  # ok 230507 
        new_player = {} 
        new_player['firstname'] = session.prompt('\nPrénom : ') 
        new_player['lastname'] = session.prompt('\nNom : ')  
        new_player['ine'] = session.prompt('\nI. N. E. : ')  
        new_player['birthdate'] = str(session.prompt('\nDate de naissance (yyyy-mm-dd) : ')) 
        # new_player['global_score'] = float(0)  # auto 
        # new_player['local_score'] = float(0)  # auto 
        return new_player 
    
    #### ============ T O U R N A M E N T S ============ #### 

    def input_tournament(self):  # ajouter sélection des joueurs ### 
        today = date.today() 

        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['start_date'] = str(today) 
        new_tournament['end_date'] = '' 

        rounds_number = session.prompt('\nNombre de rounds ("Entrée = 4") ') 
        # if rounds_number == '': 
        #     rounds_number = 4 
        new_tournament['rounds_left'] = 4 if rounds_number == '' else int(rounds_number) 
        
        # récupérer les joueurs pour les enregistrer dans le fichier tournaments.json 
        new_tournament['players'] = session.prompt('\nJoueurs (id séparées par des virgules) : ') 
        # new_tournament['duration'] = session.prompt('\nDurée : ') 
        new_tournament['description'] = session.prompt('\nDescription : ') 
        
        return new_tournament 

    def input_closing_tournament(self): 
        is_tournament_done = session.prompt('\nConfirmer la clôture du tournoi ? (y/N) : ') 
        return is_tournament_done 

    #### ============ R O U N D S ============ #### 

    """ Rounds """ 
    def input_round(self): 
        new_round = {} 
        # round.id must be automatically defined (into Main_controller): 
        ### à corriger ### 
        # new_round['tournament_id'] = int(session.prompt('\nID du tournoi : ')) 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        # new_round['start_datetime'] = str(self.now) 
        # Date + heure de fin du round quand on démarre un nouveau round : 
        # new_round['end_datetime'] = str(self.now) 
        return new_round 
    
    """ Rounds """ 
    def input_closing_round(self): 
        is_round_done = session.prompt('\nConfirmer la clôture du round ? (y/N) ') 
        return is_round_done  

    #### ============ M A T C H E S ============ #### 

    """ Matches (automatique) """ ### TODO: supprimer 
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
    def input_scores(self, matches): 
        # print(f'\nmatches IV76 : {matches}') 
        # scores = [] 
        null_matches = [] 
        winners = [] 
        # input_matches = [] 
        # for i in range(len(matches)): 
        for match in matches: 
            # print(f'\nMatch IV105 : {matches[i]}') 
            print(f'\nmatch IV105 : {match}') 
            print(f'\ndir(match) IV106 : {dir(match)}') 
            print(f'\nmatch.player_1 IV107 : {match.player_1}') 
            # print(f'\nIV83 : {matches[i][0][0]} ou {matches[i][1][0]}') 
            null_match = session.prompt(f'\nY a-t-il match nul ? (y/n) ') 
            if null_match == 'y': 
                print(f'\nmatch IV110 : {match}') 
                null_matches.append(match) 
                print(f'\nnull_matches IV112 : {null_matches}') 
                # continue  ### ? 
            else: 
                winner_position = int(session.prompt(f'\nQuel joueur a gagné {match.player_1} ou {match.player_2} ? (Entrer sa place : 1 ou 2) ')) 
                if winner_position == 1: 
                    winner = match.player_1  # AttributeError: 'Match_model' object has no attribute 'items' 
                    # winner = match[winner_id-1]  # AttributeError: 'Match_model' object has no attribute 'items' 
                else: 
                    winner = match.player_2 
                print(f'\nwinner IV122 : {winner}') 
                winners.append(winner) 
                # winners.append(matches[i].player_1[0]) 
                print(f'\nwinners IV125 : {winners}') 
        print(f'\nnull_matches IV126 : {null_matches}') 
        print(f'\nwinners IV127 : {winners}') 

        return (null_matches, winners) 
        

            # scores.append(match_result) 

        #     id_pl_1 = int(session.prompt(f'\nID du 1er joueur parmi {players} : '))
        #     players.remove(int(id_pl_1)-1)  # trouver l'index pour le del 
        #     score_pl_1 = float(session.prompt('\nScore du 1er joueur : '))
            
        #     input_match = [] 
        #     input_match.append(id_pl_1) 
        #     print(f'\ninput_match IV88 : {input_match}') 

        #     input_match.append(score_pl_1) 
        #     print(f'\ninput_match IV91 : {input_match}') 
            
        #     print(f'\ni IV93 : {i}') 
        #     scores.append(input_match)  
        # print(f'\nscores IV95 : {scores}') 
        
        # return scores 

        

