
# from operator import attrgetter 
from prompt_toolkit import PromptSession 
session = PromptSession() 

class Report_view(): 

    def __init__(self) -> None:
        pass 


    #### ============ D I S P L A Y   P L A Y E R S ============ #### 

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
        # print('\n==== Tous les joueurs ====') 

        if not players_obj: 
            print('Il n\'y a aucun joueur à afficher.') 
        else: 
            for player in players_obj: 
                self.display_one_player(player) 

        print('\n====\n') 


    #### ============ D I S P L A Y   T O U R N A M E N T S ============ #### 

 
    def display_one_tournament(self, one_tournament): 
        if not one_tournament: 
            print('Il n\'y a aucun tournoi à afficher.') 
        else: 
            print(f'\n ==== \033[1mTournoi {one_tournament.id} :\033[0m ==== ') 
            print(f'nom : \t{one_tournament.name}') 
            print(f'lieu : \t{one_tournament.site}') 
            print(f'date début : \t{one_tournament.start_date}') 
            print(f'date fin : \t{one_tournament.end_date}')  ### à vérifier ### 
            # print(f'durée : {tournament.duration}') 
            print(f'description : \t{one_tournament.description}') 
            print('rounds : \t') 

            rounds = one_tournament.rounds 
            for round in rounds: 
                self.display_round(round) 
        

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


    #### ============ D I S P L A Y   R O U N D S ============ #### 

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
                self.display_round(round) 
        print('\n====\n') 
    

    def display_round(self, round): 
        print(f'\t\033[1mRound {round.id} :\033[0m ') 
        print(f'\tNom : \t{round.round_name}') 
        print(f'\tDate et heure de début : \t{round.start_datetime}') 
        print('\tmatches : ') 

        if round.matches == []: 
            print('Il n\'y a aucun match à afficher.') 
        else: 
            matches = round.matches 
            for match in matches: 
                self.display_match(match) 
        

    #### ============ D I S P L A Y   M A T C H E S ============ #### 

    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(f'\t\t{match_tuple}') 


""" 
==== Consigne ====  

## RAPPORTS
Nous aimerions pouvoir afficher les rapports suivants dans le programme : 

# joueurs : 
● liste de tous les joueurs par ordre alphabétique ;
● liste des joueurs du tournoi par ordre alphabétique ; 

# tournois : 
● liste de tous les tournois ;
● nom et dates d’un tournoi donné ; 

# rounds et matches : 
● liste de tous les tours du tournoi et de tous les matchs du tour.

Les rapports peuvent être en texte brut, à condition qu'ils soient bien formatés et faciles à lire. Vous pouvez même utiliser des modèles HTML !

Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
""" 
