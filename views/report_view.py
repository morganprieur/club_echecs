
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    def __init__(self) -> None:
        pass 


    ###==== Reports tournaments ====### 

    """ Pas demandés :  
    def display_last_tournament(self, last_tournament): 
        print('\n---- Dernier tournoi ----') 
        print(last_tournament) 


    # def display_today_s_tournament(self, tournament): 
    #     print('\n---- Dernier tournoi ----') 
    #     print(tournament) 
    #     print('----') 
    """ 


    def display_all_tournaments(self, all_tournaments): 
        print('\n==== Tous les tournois ====') 
        # print(f'\ntournois RV57 : {all_tournaments} : ') 
    
        for tournament in all_tournaments: 
            print(f'\ntournoi {all_tournaments.index(tournament)+1} : ') 
            print(f'ID : \t{tournament.id}') 
            print(f'nom : \t{tournament.name}') 
            print(f'lieu : \t{tournament.site}') 
            print(f'date : \t{tournament.t_date}') 
            print(f'durée : {tournament.duration}') 
            print(f'description : \t{tournament.description}') 
            print(f'rounds : \t') 

            rounds = tournament.rounds 
            for round in rounds: 
                self.display_round(round) 
            # self.display_rounds_one_tournament(t) 

        print('\n====\n') 

    
    ###==== Reports rounds ====### 
    def display_rounds_one_tournament(self, tournament): 
        """ Display all the rounds from one tournament. 

        Args: 
            tournament (int): 
                the tournament object the rounds must be displayed from. 
        """ 
        print(f'\n---- Tous les tours du tournoi {int(tournament.id)} ----') 
        # print(f'tournament RV27 : {tournament}') 

        rounds = tournament.rounds 

        # If there isn't any rounds : 
        if rounds == []: 
            print(f'\nLe tournoi {tournament.id} n\'a pas encore de rounds') 
        else:  
            # Afficher les rounds : 
            for round in rounds: 
                self.display_round(round) 
                # print(f'\nID : \t{r.id}') 
                # print(f'Nom : \t{r.round_name}') 
                # print(f'Date et heure de début : \t{r.start_datetime}') 

                # if (round.matches == []) or (round.matches == None): 
                #     print(f'\nLe round {round.id} n\'a pas encore de matches') 
                # else: 
                #     for match in round.matches: 
                #         self.display_match(match) 


        print('\n====\n') 
    

    ###==== Reports tournaments ====### 

    def display_matches_one_tournament(self, tournament): 
        """ Display all the matches from one tournament. 

        Args: 
            tournament (int): 
                the ID of the tournament the matches will be getting from. 
        """ 
        print(f'\n---- Tous les matches du tournoi {int(tournament.id)} ----') 
        # print(f'tournament RV85 : {tournament}') 
        # print(f'tournament RV88 : {round}') 

        rounds = tournament.rounds 
### 
        # If there isn't any rounds : 
        if tournament.rounds == []: 
            print(f'\nLe tournoi {tournament.id} n\'a pas encore de rounds') 
        else:  
            # Afficher les rounds : 
            for r in tournament.rounds: 

                print(f'\nID : \t{r.id}') 
                print(f'Nom : \t{r.round_name}') 
                print(f'Date et heure de début : \t{r.start_datetime}') 
### 
                print(f'matches : ') 
                for match in r.matches: 
                    self.display_match(match) 
                    # print(f'\n\t[{match[0][0]}, {match[0][1]}], [{match[1][0]}, {match[1][1]}]') 
                    # TODO Afficher le round  
                    
                    
        print('\n====\n') 


    ###==== Display ====### 
    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(match_tuple) 

    def display_round(self, round): 
        print(f'\nID : \t{round.id}') 
        print(f'Nom : \t{round.round_name}') 
        print(f'Date et heure de début : \t{round.start_datetime}') 
        print(f'matches : ') 

        matches = round.matches 
        for match in matches: 
            self.display_match(match) 


    ###==== Reports players ====### 
    
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        for obj in objects: 
            print(f'{obj.firstname} \t{obj.lastname}, \tclassement : {obj.rank}') 




###==== Consigne ====### 
""" 
Nous aimerions pouvoir afficher les rapports suivants dans le programme :

    • Liste de tous les acteurs : V 
        ◦ par ordre alphabétique ; V 
        ◦ par classement. V 
    • Liste de tous les joueurs d'un tournoi :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les tournois. V 
    • Liste de tous les tours d'un tournoi. --> WIP 
    • Liste de tous les matches d'un tournoi.

Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire 
pour l'instant.
""" 




