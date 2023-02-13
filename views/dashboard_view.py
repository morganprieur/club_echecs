

from prompt_toolkit import PromptSession 
session = PromptSession() 


class Dashboard_view(): 

    welcome = '\n* * * * * * * * * * * * * * * * * \
        \n\nBonjour et bienvenue ! \
        \n\nCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs. \
        \nSi vous rencontrez des erreurs, le fichier README.md contient les informations pour envoyer des feedbacks. \
        \n\nDans le menu, vous pouvez à tout moment utiliser les Commandes de sortie : \
        \n* pour revenir au menu précédent, \n0 pour revenir au menu principal' 

    main_menu = [ 
        'Menu principal : ', 
        '1 : saisir', 
        '2 : afficher' 
    ] 

    register_menu = [ 
        'Menu "saisir" : ', 
        '1 : un joueur', 
        '2 : un tournoi' 
    ] 

    display_menu = [ 
        'Menu "Afficher" : ', 
        # A faire + tard : 
        # '1 : tous les joueurs par ordre chrono', 
        '1 : Tous les joueurs par ordre alphabétique', 
        # '2 : Tous les joueurs par classement', 
        # '3 : Les joueurs du tournoi par ordre alphabétique', 
        # '4 : Les joueurs du tournoi par classement', 
        # '5 : les résultats du tournoi', 
        # '6 : les tours', 
        # '7 : les matches', 
        '8 : tous les tournois', 

        # pas demandés : 
        # '9 : le dernier tournoi', 
        # '9 : le tournoi du jour', 
        '', 
        'Commandes de secours : ', 
        '0 : Retour au menu précédent', 
        '* : Menu principal' 
    ] 


    def __init__(self): 
        pass 


    def display_welcome(self): 
        print(self.welcome) 


    def display_first_menu(self): 
        print('') 
        for m in self.main_menu: 
            print(m) 
        self.ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        print('') 
        return self.ask_for_menu_action 


    def report(self): 
        for i in range(len(self.display_menu)): 
            print(self.display_menu[i]) 
        self.ask_for_report = session.prompt('\nChoisir un rapport ou revenir à un menu précédent: ') 
        print('') 
        return self.ask_for_report 


if __name__ == "__main__": 
    Dashboard_view.display_welcome()  # manque 'self'  









