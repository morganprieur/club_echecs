
# from controllers.main_controller import Main_controller 
from operator import attrgetter 


class Report_view(): 

    """ 
    report_tournament = [ 
        { 
            'name': 'tournoi 1', 
            'site': 'lieu 1', 
            't_date': '15/12/2022', 
            'duration': 'blitz', 
            'description': 'Observations du directeur du tournoi.' 
        }, 
        { 
            'name': 'tournoi 2', 
            'site': 'lieu 2', 
            't_date': '05/01/2023', 
            'duration': 'bullet', 
            'description': 'Observations.' 
        }, 
        { 
            'name': 'tournoi 3', 
            'site': 'lieu 1', 
            't_date': '06/01/2023', 
            'duration': 'coup rapide', 
            'description': 'Observations du directeur.' 
        } 
    ] 
    """ 
    # today_s_tournament = Main_controller.tournament 
    # all_tournaments = Main_controller.registered_tournaments 

    # def __init__(self, today_s_tournament):  # , report_tournament 
    #     self.today_s_tournament = today_s_tournament 
    
    # def get_tournament_data(self): 
    #     report_tournament =  [ 
    #         { 
    #             'name': 'tournoi 1', 
    #             'site': 'lieu 1', 
    #             't_date': '15/12/2022', 
    #             'duration': 'blitz', 
    #             'description': 'Observations du directeur du tournoi.' 
    #         }, 
    #         { 
    #             'name': 'tournoi 2', 
    #             'site': 'lieu 2', 
    #             't_date': '05/01/2023', 
    #             'duration': 'bullet', 
    #             'description': 'Observations.' 
    #         }, 
    #         { 
    #             'name': 'tournoi 3', 
    #             'site': 'lieu 1', 
    #             't_date': '06/01/2023', 
    #             'duration': 'coup rapide', 
    #             'description': 'Observations du directeur.' 
    #         } 
    #     ] 
    #     return report_tournament 

    def __init__(self) -> None:
        pass 
    # on pourrait tout mettre en statique 
    
    ###==== Tournaments ====### 

    def display_last_tournament(self, last_tournament): 
        print('\n---- last tournament ----') 
        print(last_tournament) 


    # def display_today_s_tournament(self, today_s_tournament): 
    def display_today_s_tournament(self, tournament): 
        print('\n---- today\'s tournament ----') 
        print(tournament) 
        print('----') 


    def display_all_tournaments(self, all_tournaments): 
        print('\n==== Tous les tournois ====') 
        print('') 
        for t in all_tournaments: 
            print(f'tournoi {all_tournaments.index(t)+1} : ') 
            print(f'Nom : {t.name}, lieu : {t.site}, date : {t.t_date}, durée : {t.duration}, description : {t.description}') 
            print('')  
        print('====\n') 
    
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




