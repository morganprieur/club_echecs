
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    def __init__(self) -> None:
        pass 
    

    ###==== Tournaments ====### 

    def display_last_tournament(self, last_tournament): 
        print('\n---- last tournament ----') 
        print(last_tournament) 


    """ Pas demandé 
    # def display_today_s_tournament(self, tournament): 
    #     print('\n---- today\'s tournament ----') 
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
                for p,v in r.items(): 
                    print(f'\t{p} : \t{v}') 

            print(f'description : \t{t.description}') 
        print('\n====\n') 

    
    ###==== Players ====### 
    
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        for obj in objects: 
            print(f'{obj.firstname}    {obj.lastname},    classement : {obj.rank}') 




###==== Rapports ====### 
""" 
Nous aimerions pouvoir afficher les rapports suivants dans le programme :

    • Liste de tous les acteurs :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les joueurs d'un tournoi :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les tournois.
    • Liste de tous les tours d'un tournoi.
    • Liste de tous les matchs d'un tournoi.

Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
""" 




