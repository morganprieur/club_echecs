

from prompt_toolkit import PromptSession 
session = PromptSession() 


class Dashboard_view(): 

    welcome = '\n* * * * * * * * * * * * * * * * * \
        \nBonjour et bienvenue ! \
        \n\nCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs. \
        \nSi vous rencontrez des erreurs, le fichier README.md contient les informations pour envoyer des feedbacks. \
        \n\nDans le menu, vous pouvez à tout moment utiliser les Commandes de secours : \
        \n  * pour revenir au menu principal \n  0 pour sortir'  # 0 Menu précédent,  

    main_menu = [ 
        'Menu principal : ', 
        '1 : saisir', 
        '2 : afficher', 
        '', 
        'Commandes de secours : ', 
        '* pour revenir au menu principal', 
        '0 pour sortir' 
    ] 

    register_menu = [ 
        'Menu "saisir" : ', 
        '1 : Enregistrer un joueur', 
        # '2 : Enregistrer plusieurs joueurs', 
        '3 : Enregistrer un nouveau tournoi', 
        '4 : Clôturer un tournoi', 
        '5 : Enregistrer un nouveau round', 
        '6 : Clôturer un round', 
        '7 : Enregistrer un match', 
        '', 
        'Commandes de secours : ', 
        '* Revenir au menu principal', 
        '0 Sortir' 
    ] 

    display_menu = [ 
        'Menu "Afficher" : ', 
        # A faire + tard : 
        # '1 : tous les joueurs par ordre chrono', 
        '1 : Tous les joueurs par ordre alphabétique', 
        '2 : Tous les joueurs par classement', 
        # '3 : Les joueurs du tournoi par ordre alphabétique', 
        # '4 : Les joueurs du tournoi par classement', 
        # '5 : les résultats du tournoi', 
        '6 : les tours d\'un tournoi', 
        '7 : les matches', 
        '8 : tous les tournois', 
        '--------', 
        # pas demandés : 
        '9 : test define_first_round', 
        # '9 : le dernier tournoi', 
        # '9 : le tournoi du jour', 
        '', 
        'Commandes de secours : ', 
        '* pour revenir au menu principal', 
        '0 pour sortir' 
    ] 

    def __init__(self): 
        pass 

    """ comment """ 
    def display_welcome(self): 
        print(self.welcome) 

    """ comment """ 
    def display_first_menu(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for m in self.main_menu: 
            print(m) 
        self.ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        print('') 
        return self.ask_for_menu_action 

    """ comment """ 
    def display_register(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for i in range(len(self.register_menu)): 
            print(self.register_menu[i]) 
        self.ask_for_register = session.prompt('\nChoisir quoi enregistrer : ') 
        print('') 
        return self.ask_for_register 

    """ comment """ 
    def display_report(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for i in range(len(self.display_menu)): 
            print(self.display_menu[i]) 
        self.ask_for_report = session.prompt('\nChoisir un rapport : ') 
        # print(f'DV90 self.ask_for_report : {self.ask_for_report}') 
        print('') 
        return self.ask_for_report 

""" comment """ 
if __name__ == "__main__": 
    Dashboard_view.display_welcome() 

