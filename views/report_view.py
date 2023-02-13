
# from controllers.main_controller import Main_controller 



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
            for k,v in t.items(): 
                print(v) 
            print('')  
        print('====\n') 
    
    ###==== Players ====### 
    # sort players in alphabetical order : 
    @staticmethod 
    def sort_objects_by_field(objects, field):   # , serialized_players  
        # print(f'Match_controller dir MC67 : {dir(Match_controller)}') 
        # print(f'self.players MC64 : {self.players}') 
        sort_on = field 
        decorated = [(dict_[sort_on], dict_) for dict_ in objects] 
        decorated.sort() 
        sorted_table = [dict_ for (key, dict_) in decorated] 
        # print(f'result MC53 : {result}') 
        # print(f'sorted_table RV103 : {sorted_table}') 
        # for k,v in sorted_table.item(): 
        for p in sorted_table: 
            player = [] 
            for k,v in p.items(): 
                player.append(v) 
            print(f'{player[1]} {player[0]}') 


    """ Liste de tous les joueurs ordre alphabétique """ 
    def display_alphabetical_players(self, all_players): 
        # print('\n==== Tous les joueurs par ordre alphabétique ====') 
        print('') 
        print('\n==== Tous les joueurs par ordre chronologique ====') 
        print('') 
        # alphabetical_players = [] 
        for p in all_players: 
            # alphabetical_players.append(p) 
            print(f'Joueur {all_players.index(p)} : ') 
            # print(alphabetical_players) 
            for k,v in p.items(): 
                print(v) 
            print('')  
        print('====\n') 



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




