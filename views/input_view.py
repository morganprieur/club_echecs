
from datetime import date 
from prompt_toolkit import PromptSession 
# to use prompt as an instance 
session = PromptSession() 


class Input_view(): 

    def __init__(self): 
        pass 


    # ============ P L A Y E R S ============ # 


    def input_player(self): 
        new_player = {} 
        new_player['firstname'] = session.prompt('\nPrénom : ') 
        new_player['lastname'] = session.prompt('\nNom : ')  
        new_player['ine'] = session.prompt('\nI. N. E. : ')  
        new_player['birthdate'] = str(session.prompt('\nDate de naissance (yyyy-mm-dd) : ')) 
        return new_player 


    # ============ T O U R N A M E N T S ============ # 


    def input_tournament(self): 
        today = date.today() 

        new_tournament = {} 
        new_tournament['name'] = session.prompt('\nNom du tournoi : ') 
        new_tournament['site'] = session.prompt('\nLieu : ') 
        new_tournament['start_date'] = str(today) 
        new_tournament['end_date'] = '' 

        rounds_number = session.prompt('\nNombre de rounds ("Entrée" = 4) ') 
        new_tournament['rounds_left'] = 4 if rounds_number == '' else int(rounds_number) 

        # Get the players' ids for registering them into the tournaments.json file 
        # We'll get the players later. 
        new_tournament['players'] = session.prompt('\nJoueurs (id séparées par des virgules) : ') 

        new_tournament['description'] = session.prompt('\nDescription : ') 

        return new_tournament 


    def input_closing_tournament(self): 
        is_tournament_done = session.prompt('\nC\'est le dernier round. Confirmer la clôture du tournoi ? (y/n) : ') 
        return is_tournament_done 


    # ============ R O U N D S ============ # 


    def input_round(self): 
        new_round = {} 
        new_round['round_name'] = session.prompt('\nNom du round : ') 
        return new_round 


    def input_closing_round(self): 
        is_round_done = session.prompt('Confirmer la clôture du round ? (y/n) ') 
        return is_round_done  


    # ============ M A T C H E S ============ # 


    def input_scores(self, matches, players_objs): 
        """ Get the scores of the last matches. 
            Args:
                matches (array):  the match_model instances 
                players_objs (array): the player_model instances. 
            Returns:
                tuple: (array of the null matches (match_model instances), 
                        array of the winners (Player_model instances)). 
        """ 
        null_matches = [] 
        winners = [] 
        for match in matches: 
            for player in players_objs: 
                if match.player_1_id == player.id: 
                    player1 = f'{player.firstname} {player.lastname}' 
                elif match.player_2_id == player.id: 
                    player2 = f'{player.firstname} {player.lastname}'
            print(f'\nMatch : joueur \033[1m{match.player_1_id} {player1}\033[0m \
                contre joueur \033[1m{match.player_2_id} {player2}\033[0m ') 

            # Check if the user's answer is correct, else repeat the question.  
            null_match = session.prompt('\nY a-t-il eu match nul ? (y/n) ') 
            while (null_match not in ['y', 'Y', 'n', 'N']): 
                print('Vous devez taper "y" ou "n" pour indiquer si le match a un résultat nul ou pas. ') 
                null_match = session.prompt('\nY a-t-il eu match nul ? (y/n) ') 
            if (null_match == 'y') | (null_match == 'Y'): 
                null_matches.append(match) 
            elif (null_match == 'n') | (null_match == 'N'): 
                winner_position = session.prompt(f'\nQuel joueur a gagné {match.player_1} ou {match.player_2} ? \
                    (Entrer sa place dans la liste : 1 ou 2) ') 

                # Check if the user's answer is correct, else repeat the question. 
                while (winner_position not in [1, 2]): 
                    print('Vous devez indiquer si c\'est le joueur en position 1 ou celui en position 2 qui a gagné \
                le match . ') 
                    winner_position = int(session.prompt(f'\nQuel joueur a gagné {match.player_1} ou \
                {match.player_2} ? \
                        (Entrer sa place dans la liste : 1 ou 2) ')) 

                if winner_position == 1: 
                    winner = match.player_1 
                else: 
                    winner = match.player_2 
                winners.append(winner) 

        return (null_matches, winners) 


    # ============ U T I L S ============ # 


    def input_object_id(self, object): 
        id = session.prompt(f'\nQuelle ID du {object} ? (pour le dernier, tapez "last") : ') 
        return id 


    def input_yes_or_no(self, question): 
        choice = session.prompt(f'\n{question} (y/n) : ') 
        return choice 

