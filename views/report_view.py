
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Report_view(): 

    def __init__(self) -> None:
        pass 


    # ============ D I S P L A Y   P L A Y E R S ============ # 


    """ ANSI \033[1m \033[0m --> gras """ 
    def display_one_player(self, player): 
        if not player: 
            print('Il n\'y a aucun joueur à afficher.') 
        else: 
            print(f'''
                \n\033[1mJoueur {player.id}\033[0m :   

                nom complet : \t\t{player.firstname} {player.lastname} 
                date de naissance : \t{player.birthdate} 
                I. N. E. : \t\t{player.ine} 
                score du dernier round : \t{player.round_score} 
                score du tournoi : \t{player.tournament_score} 
            ''')  
        print('\n====\n') 


    def display_players(self, players_obj): 

        for player in players_obj: 
            self.display_one_player(player) 


    def display_starters(self, starters): 
        print('\n\033[1m==== Les joueurs qui ont les blancs : ====\033[0m') 

        for starter in starters: 
            if not starter: 
                print('Il n\'y a aucun joueur à afficher.') 
            else: 
                print(f"\n\033[1mJoueur {starter.id}, {starter.firstname} {starter.lastname}\033[0m ") 

        print('\n====\n') 


    """def display_round_results(self, last_round, matches_objs, players_objs): """ 
    def display_matches_results(self, matches_objs, players_objs): 

        print('\033[1mRésultats des matches :\033[0m ') 

        if matches_objs == []: 
            print('\t\t\tIl n\'y a aucun match à afficher.') 
        else: 
            for match in matches_objs: 
                print(f'''\nMatch : {match.player_1_id} contre {match.player_2_id} :''') 
                for player in players_objs:
                    if match.player_1_id == player.id: 
                        print(f'''joueur {player.id} : {player.firstname} {player.lastname}, score : {player.round_score}''') 
                    elif match.player_2_id == player.id: 
                        print(f'''joueur {player.id} : {player.firstname} {player.lastname}, score : {player.round_score}''') 



    # ============ D I S P L A Y   T O U R N A M E N T S ============ # 


    def display_one_tournament(self, one_tournament): 

        print(f'''\n ==== \033[1mTournoi {one_tournament.id} :\033[0m ====  
            nom : \t{one_tournament.name} 
            lieu : \t{one_tournament.site} 
            date début : \t{one_tournament.start_date} 
            date fin : \t{one_tournament.end_date} 
            description : \t{one_tournament.description} 
            rounds : \t 
        ''') 

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
        print(f'''
            \n---- \033[1mNom et dates du tournoi {tournament.id} :\033[0m ---- 
            nom : \t{tournament.name} 
            date début : \t{tournament.start_date} 
            date fin : \t{tournament.end_date} 
            ---- 
        ''') 


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
        print(f''' 
            \t\033[1mRound {one_round.id} :\033[0m  
            \tNom : \t{one_round.round_name} 
            \tDate et heure de début : {one_round.start_datetime} 
        ''') 
        if one_round.end_datetime: 
            print(f'\t\tDate et heure de fin : {one_round.start_datetime}') 
        else: 
            print('\t\tDate et heure de fin : ') 
        print('\t\t\t\033[1mmatches :\033[0m ') 

        if one_round.matches == []: 
            print('\t\t\tIl n\'y a aucun match à afficher.') 
        else: 
            matches = one_round.matches 
            for match in matches: 
                self.display_match(match) 


    # ============ D I S P L A Y   M A T C H E S ============ # 


    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(f'\t\t\t{match_tuple}') 

