
# from operator import attrgetter 
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Report_view(): 

    def __init__(self) -> None:
        pass 

    # ============ D I S P L A Y   P L A Y E R S ============ # 

    def display_one_player(self, player): 
        if not player: 
            print('Il n\'y a aucun joueur à afficher.') 
        else: 
            print(f"\n\033[1mJoueur {player.id}\033[0m : ")  # ANSI \033[1m \033[0m --> gras 

            print(f'nom complet : \t\t{player.firstname} {player.lastname}') 
            print(f'I. N. E. : \t\t{player.ine}') 
            print(f'score dans le tournoi : {player.local_score}') 
            print(f'score global : \t\t{player.global_score}') 
        print('\n====\n') 

    def display_players(self, players_obj): 
        print('\n\033[1m==== Tous les joueurs ====\033[0m') 

        for player in players_obj: 
            self.display_one_player(player) 


    """ def display_starters(self, starters): """ 
    # def display_starters(self): 
    def display_starters(self, starters): 
        print('\n\033[1m==== Les joueurs qui commencent les matches : ====\033[0m') 
        print(f'dir(self) RB37 : {dir(self)}') 
        for starter in self.starters: 
            if not starter: 
                print('Il n\'y a aucun joueur à afficher.') 
            else: 
                # ANSI \033[1m Texte en gras \033[0m 
                print(f"\n\033[1mJoueur {starter.id}, {starter.firstname} {starter.lastname}\033[0m : ") 

                print(f'nom complet : \t\t{starter.firstname} {starter.lastname}') 

        print('\n====\n') 

    # ============ D I S P L A Y   T O U R N A M E N T S ============ # 

    def display_one_tournament(self, one_tournament): 

        print(f'\n ==== \033[1mTournoi {one_tournament.id} :\033[0m ==== ') 
        print(f'nom : \t{one_tournament.name}') 
        print(f'lieu : \t{one_tournament.site}') 
        print(f'date début : \t{one_tournament.start_date}') 
        print(f'date fin : \t{one_tournament.end_date}') 
        print(f'description : \t{one_tournament.description}') 
        print('rounds : \t') 

        rounds = one_tournament.rounds 
        for round in rounds: 
            self.display_one_round(round) 

    def display_tournaments(self, all_tournaments): 
        print('\n==== Tous les tournois ====') 

        for tournament in all_tournaments: 
            print(f'\ntournoi {all_tournaments.index(tournament)+1} : ') 
            self.display_one_tournament(tournament) 

        print('\n====\n') 

    def display_name_date_tournament(self, tournament): 
        """ Displays the name and dates of the tournament. 
            Args:
                tournament (object): the tournament from wich will be displayed the name and dates. 
        """ 
        print(f'\n---- \033[1mNom et dates du tournoi {tournament.id} :\033[0m ----') 
        print(f'nom : \t{tournament.name}') 
        print(f'date début : \t{tournament.start_date}') 
        print(f'date fin : \t{tournament.end_date}') 

        print('----') 

    # ============ D I S P L A Y   R O U N D S ============ # 

    def display_rounds_one_tournament(self, tournament): 
        """ Display all the rounds from one tournament. 
            Args: 
                tournament (object): 
                    the tournament object the rounds must be displayed from. 
        """ 
        print(f'\n---- \033[1mTous les rounds du tournoi {tournament.id} : \033[0m ----') 

        rounds = tournament.rounds 

        # If there isn't any rounds : 
        if rounds == []: 
            print(f'\nLe tournoi {tournament.id} n\'a pas encore de rounds') 
        else:  
            for round in rounds: 
                self.display_one_round(round) 
        print('\n====\n') 

    def display_one_round(self, one_round): 
        """ Displays the properties of the round. 
            Args:
                one_round (Round_model): a Round object to display. 
        """ 
        print(f'\t\033[1mRound {one_round.id} :\033[0m ') 
        print(f'\tNom : \t{one_round.round_name}') 
        print(f'\tDate et heure de début : {one_round.start_datetime}') 
        if one_round.end_datetime: 
            print(f'\tDate et heure de début : {one_round.start_datetime}') 
        else: 
            print('\tDate et heure de début : ') 
        print('\t\033[1mmatches :\033[0m ') 

        if one_round.matches == []: 
            print('Il n\'y a aucun match à afficher.') 
        else: 
            matches = one_round.matches 
            for match in matches: 
                self.display_match(match) 

    # ============ D I S P L A Y   M A T C H E S ============ # 

    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(f'\t\t{match_tuple}') 
