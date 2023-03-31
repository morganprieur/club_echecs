
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    def __init__(self) -> None:
        pass 

    """ 
    ==== Reports tournaments ==== 
    """ 

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
            print(f'date début : \t{tournament.start_date}') 
            print(f'date fin : \t{tournament.end_date}')  ### à vérifier ### 
            print(f'durée : {tournament.duration}') 
            print(f'description : \t{tournament.description}') 
            print('rounds : \t') 

            rounds = tournament.rounds 
            for round in rounds: 
                self.display_round(round) 
            # self.display_rounds_one_tournament(t) 
        print('\n====\n') 

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
        if rounds == []: 
            print(f'\nLe tournoi {tournament.id} n\'a pas encore de rounds') 
        else:  
            # Afficher les rounds : 
            for r in tournament.rounds: 

                print(f'\nID : \t{r.id}') 
                print(f'Nom : \t{r.round_name}') 
                print(f'Date et heure de début : \t{r.start_datetime}') 
        ### 
                print('matches : ') 
                for match in r.matches: 
                    self.display_match(match) 
                    # print(f'\n\t[{match[0][0]}, {match[0][1]}], [{match[1][0]}, {match[1][1]}]') 
                    # TODO Afficher le round  
        print('\n====\n') 

    """ 
    ==== Reports rounds ==== 
    """ 
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

    """ 
    ==== Display ==== 
    """ 
    def display_match(self, match): 
        match_tuple = tuple(match) 
        print(match_tuple) 

    def display_round(self, round): 
        print(f'\tID : \t{round.id}') 
        print(f'\tNom : \t{round.round_name}') 
        print(f'\tDate et heure de début : \t{round.start_datetime}') 
        print('\tmatches : ') 

        matches = round.matches 
        for match in matches: 
            self.display_match(match) 

    """ 
    ==== Reports players ==== 
    """ 

    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        for obj in objects: 
            print(f'{obj.firstname} \t{obj.lastname}, \tclassement : {obj.rank}') 


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
