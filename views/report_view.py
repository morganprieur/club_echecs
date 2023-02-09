
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
    

    def display_last_tournament(self, last_tournament): 
        # print('---- last tournament RV70 ----') 
        print(last_tournament) 


    # def display_today_s_tournament(self, today_s_tournament): 
    def display_today_s_tournament(self, tournament): 
        # print('---- today\'s tournament RV76 ----') 
        print(tournament) 
        print('----') 


    def display_all_tournaments(self, all_tournaments): 
        # print('==== all tournaments RV82 ====') 
        for t in all_tournaments: 
            print(t)   
        print('====') 





