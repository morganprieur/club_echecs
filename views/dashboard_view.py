

from prompt_toolkit import PromptSession 
session = PromptSession() 



# Affichage Bienvenue + menu + touches de sortie : 
# 0 : menu principal 
# * : menu précédent 

# Afficher le menu 
#   1 : saisies 
#   2 : affichages
# 

# Menu saisir : 
#   1 : un ou des joueurs 
#   2 : un ou des matches 
#   3 : un ou des tours 
#   4 : un ou (?) des tournois 
#   0 : retour au menu précédent


# Menu afficher : 
#   1 : tous les joueurs par ordre alphabétique 
#   2 : tous les joueurs par classement 

#   3 : les joueurs du tournoi par ordre alphabétique 
#   4 : les joueurs du tournoi par classement 

#   5 : les résultats du tournoi 
#   6 : les tours 
#   7 : les matches

#   0 : retour au menu précédent


# # A chaque niveau : 
# # Retour au niveau supérieur 
# # Retour au menu principal 



class Dashboard_view(): 

    def __init__(self, 
        welcome: list, 
        main_menu: list, 
        register_menu: list, 
        display_menu: list 
    ): 
        self.welcome = welcome 
        self.main_menu = main_menu 
        self.register_menu = register_menu 
        self.display_menu = display_menu 



    # @staticmethod 
    def display_welcome(self): 

        print(self.welcome) 


    # @staticmethod 
    def display_first_menu(self): 
        print('') 
        for m in self.main_menu: 
            print(m) 
        self.ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        print('') 
        return self.ask_for_menu_action 

        # if self.ask_for_menu_action == '1': 
        #     # print('ok') 
        #     for i in range(len(self.register_menu)): 
        #         print(register_menu[i]) 
        # elif self.ask_for_menu_action == '2': 
        #     # print('not ok') 
        #     # Dashboard_view.report(self) 
        #     # for i in range(len(display_menu)): 
        #     #     print(display_menu[i]) 
            
        # elif self.ask_for_menu_action == '0': 
        #     print(self.main_menu[0]) 
        #     print(self.main_menu[1]) 
        # elif self.ask_for_menu_action == '*': 
        #     Dashboard_view.display_welcome() 
        # else: 
            # print('Cette réponse n\'est pas définie, veuillez choisir une autre action') 
            # Dashboard_view.display_welcome() 


    # @staticmethod 
    def report(self): 
        for i in range(len(self.display_menu)): 
            print(self.display_menu[i]) 
        self.ask_for_report = session.prompt('\nChoisir un rapport ou revenir à un menu précédent: ') 
        print('') 
        return self.ask_for_report 



if __name__ == "__main__": 
    Dashboard_view.display_welcome()  # manque 'self'  

    # new_tournament = {
    #     "name": "Nom 060", 
    #     "site": "Lieu 60", 
    #     "t_date": "2023/02/05", 
    #     "duration": "coup rapide", 
    #     "description": "description 060", 
    # } 
    # one_tournament = Tournament_model(**new_tournament) 
    # # print(f'new_tournament TP192 : {new_tournament}') 
    # # print(f'type(new_tournament) TP193 : {type(new_tournament)}') 
    # one_tournament.serialize() 
    # print(f'get tournaments TM193 : {Tournament_model.get_tournaments()}') 








