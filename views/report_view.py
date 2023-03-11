
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    def __init__(self) -> None:
        pass 

    
    ###==== Reports ====### 
    def display_rounds_one_tournament(self, tournament): 
        """ Display all the rounds in one tournament. 

        Args: 
            tournament (int): 
                the tournament object the rounds must be displayed from. 
        """ 
        t_id = int(tournament.id)+1 
        print(f'\n---- Tous les tours du tournoi {t_id} ----') 
        # print(f'tournament RV27 : {tournament}') 

        # Afficher les rounds : 
        for r in tournament.rounds: 
            print(f'\nID : \t{r.id}') 
            print(f'Nom : \t{r.round_name}') 
            print(f'Nom : \t{r.start_datetime}')

        print('\n====\n') 
    

    ###==== Tournaments ====### 

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
    
        for t in all_tournaments: 
            print(f'\ntournoi {all_tournaments.index(t)+1} : ') 
            print(f'ID : \t{t.id}') 
            print(f'nom : \t{t.name}') 
            print(f'lieu : \t{t.site}') 
            print(f'date : \t{t.t_date}') 
            print(f'durée : {t.duration}') 
            print(f'description : \t{t.description}') 
            print(f'rounds : \t') 
            
            for r in t.rounds: 
                # for p,v in r.items(): 
                #     print(f'\t{p} : \t{v}') 
                print(f'\tID : \t{r.id}') 
                print(f'\tnom : \t{r.round_name}') 
                print(f'\tdébut : \t{r.start_datetime}') 

        print('\n====\n') 

    
    ###==== Players ====### 
    
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




