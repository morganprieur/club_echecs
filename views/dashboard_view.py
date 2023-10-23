
from prompt_toolkit import PromptSession 
session = PromptSession() 


class Dashboard_view(): 

    welcome = '\n* * * * * * * * * * * * * * * * * \
        \n\033[1mBonjour et bienvenue !\033[0m \
        \n\n\tCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs. \
        \nSi vous rencontrez des erreurs, le fichier README.md contient les informations pour envoyer des feedbacks. \
        \n\n\tDans le menu, vous pouvez à tout moment utiliser les Commandes de secours : \
        \n\033[1m* pour revenir au menu principal \n0 pour sortir\033[0m' 

    main_menu = [ 
        '========', 
        '\033[1mMenu principal :\033[0m ', 
        '1 : enregistrer', 
        '2 : afficher', 
        '--------', 
        'Commandes de secours : ', 
        '* pour revenir au menu principal', 
        '0 pour sortir' 
    ] 

    register_menu = [ 
        '\033[1mMenu "enregistrer" :\033[0m ', 
        '1 : Enregistrer un joueur', 
        '2 : Enregistrer plusieurs joueurs', 
        '3 : Enregistrer un nouveau tournoi', 
        '4 : Enregistrer des scores et clôturer le round', 
        '5 : Clôturer un round', 
        '6 : Clôturer un tournoi', 
        '--------', 
        '\033[1mCommandes de secours :\033[0m ', 
        '* Revenir au menu principal', 
        '0 Sortir' 
    ] 

    display_menu = [ 
        '\033[1mMenu "Afficher" :\033[0m ', 
        '1 : Tous les joueurs par ordre alphabétique (par prénom) ', 
        '2 : Tous les joueurs par classement INE ',  # pas demandé mais c'est fait 
        '3 : Tous les tournois ', 
        '4 : Un tournoi ', 
        '5 : Nom et dates d\'un tournoi ', 
        '6 : Les joueurs d\'un tournoi par ordre alphabétique ', 
        '7 : Les tours et matches d\'un tournoi ', 
        '----', 
        '10: définir un nouveau match ', 
        '--------', 
        '\033[1mCommandes de secours :\033[0m ', 
        '* pour revenir au menu principal ', 
        '0 pour sortir et fermer l\'application ' 
    ] 


    def __init__(self): 
        pass 


    def display_welcome(self): 
        print(self.welcome) 


    def display_first_menu(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for m in self.main_menu: 
            print(m) 
        self.ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        print('') 
        return self.ask_for_menu_action 


    def display_register(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for i in range(len(self.register_menu)): 
            print(self.register_menu[i]) 
        self.ask_for_register = session.prompt('\nChoisir quoi enregistrer : ') 
        print('') 
        return self.ask_for_register 


    def display_report(self): 
        print('\n* * * * * * * * * * * * * * * * *') 
        for i in range(len(self.display_menu)): 
            print(self.display_menu[i]) 
        self.ask_for_report = session.prompt('\nChoisir un rapport : ') 
        print('') 
        return self.ask_for_report 
