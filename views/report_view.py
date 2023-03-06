
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    def __init__(self) -> None:
        pass 

    
    ###==== Reports ====### 
    def display_rounds_one_tournament(self, tournament_id, all_rounds): 
        """ Display all the rounds in one tournament. 

        Args: 
            tournament (int): 
                the id of the tournament the rounds must be displayed from.  
            all_rounds (list of objects): 
                Main_container.round instanciated and stored into a list. 
        """ 
        t_id = int(tournament_id)+1 
        print(f'\n---- Tous les tours du tournoi {t_id} ----') 
        
        # tournament = self.select_one_obj('tournament', tournament_id) 
        # main_controller.report_rounds(self, ask_for_tournament_id) 
        
        # Afficher les rounds : 
        for r in all_rounds: 
            print(f'\nID : \t{r.id}') 
            print(f'Nom : \t{r.round_name}')  

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
    
        for t in all_tournaments: 
            print(f'\ntournoi {all_tournaments.index(t)+1} : ') 
            print(f'ID : \t{t.id}') 
            print(f'nom : \t{t.name}') 
            print(f'lieu : \t{t.site}') 
            print(f'date : \t{t.t_date}') 
            print(f'durée : {t.duration}') 
            print(f'rounds : \t') 
            
            for r in t.rounds: 
                # for p,v in r.items(): 
                #     print(f'\t{p} : \t{v}') 
                print(f'ID : \t{r.id}') 

            print(f'description : \t{t.description}') 
        print('\n====\n') 

    
    ###==== Players ====### 
    
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        for obj in objects: 
            print(f'{obj.firstname}    {obj.lastname},    classement : {obj.rank}') 




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




