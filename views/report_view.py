
# from operator import attrgetter 
from prompt_toolkit import PromptSession 
session = PromptSession() 

class Report_view(): 

    def __init__(self) -> None:
        pass 


    #### ============ D I S P L A Y   P L A Y E R S ============ #### 

    def display_one_player(self, player): 

        print(f"\n\033[1mJoueur {player.id}\033[0m : ")  # ANSI \033[1m \033[0m --> gras 

        print(f'nom complet : \t\t{player.firstname} {player.lastname}') 
        print(f'I. N. E. : \t\t{player.ine}') 
        print(f'score dans le tournoi : \t{player.local_score}') 
        print(f'score global : \t\t{player.global_score}') 


    def display_players(self, players_obj): 
        print('\n==== Tous les joueurs ====') 

        for player in players_obj: 
            self.display_one_player(player) 

        print('\n====\n') 


    #### ============ D I S P L A Y   T O U R N A M E N T S ============ #### 


    # def display_today_s_tournament(self, tournament): 
    def display_one_tournament(self, one_tournament): 
        print('\n ==== Un tournoi ==== ') 
        # print('\n---- Dernier tournoi ----') 
        # print(tournament) 
        print(f'ID : \t{one_tournament.id}') 
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
        # session.prompt('Appuyez sur une touche pour continuer RV55') 
    

    def display_tournaments(self, all_tournaments): 
        print('\n==== Tous les tournois ====') 
        # print(f'\ntournois RV57 : {all_tournaments} : ') 

        for tournament in all_tournaments: 
            print(f'\ntournoi {all_tournaments.index(tournament)+1} : ') 
            Report_view.display_one_tournament(tournament) 
            # print(f'ID : \t{tournament.id}') 
            # print(f'nom : \t{tournament.name}') 
            # print(f'lieu : \t{tournament.site}') 
            # print(f'date début : \t{tournament.start_date}') 
            # print(f'date fin : \t{tournament.end_date}')  ### à vérifier ### 
            # # print(f'durée : {tournament.duration}') 
            # print(f'description : \t{tournament.description}') 
            # print('rounds : \t') 

            # rounds = tournament.rounds 
            # for round in rounds: 
            #     self.display_round(round) 
            # # self.display_rounds_one_tournament(t) 
        print('\n====\n') 
        # session.prompt('Appuyer sur une touche pour continuer RV82') 


    def display_name_date_tournament(self, tournament): 
        """ Displays the name and dates of the tournament. 

        Args:
            tournament (object): the tournament from wich will be displayed the name and dates. 
        """ 
        print('\n---- Nom et dates d\'un ournoi ----') 
        print(f'nom : \t{tournament.name}') 
        print(f'date début : \t{tournament.start_date}') 
        print(f'date fin : \t{tournament.end_date}')  ### à vérifier ### 

        print('----') 
        # session.prompt('Appuyer sur une touche pour continuer RV97') 


    #### ============ D I S P L A Y   R O U N D S ============ #### 

    def display_rounds_one_tournament(self, tournament): 
        """ Display all the rounds from one tournament. 
        Args: 
            tournament (object): 
                the tournament object the rounds must be displayed from. 
        """ 
        print(f'\n---- Tous les rounds du tournoi {tournament.id} ----') 
        # print(f'tournament RV27 : {tournament}') 

        rounds = tournament.rounds 

        # If there isn't any rounds : 
        if rounds == []: 
            print(f'\nLe tournoi {tournament.id} n\'a pas encore de rounds') 
        else:  
            # Display the rounds : 
            for round in rounds: 
                self.display_round(round) 
        print('\n====\n') 
        # session.prompt('Appuyer sur une touche pour continuer RV122') 
    

    def display_round(self, round): 
        print(f'\tID : \t{round.id}') 
        print(f'\tNom : \t{round.round_name}')  ### 230515 
        print(f'\tDate et heure de début : \t{round.start_datetime}') 
        print('\tmatches : ') 

        matches = round.matches  ### 230515 
        for match in matches: 
            self.display_match(match) 
        # session.prompt('Appuyer sur une touche pour continuer RV134') 


    #### ============ D I S P L A Y   M A T C H E S ============ #### 

    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(f'\t\t{match_tuple}')  ### 230515 # TODO: à vérifier 
        # session.prompt('Appuyer sur une touche pour continuer RV142') 



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
