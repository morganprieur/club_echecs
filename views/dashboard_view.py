

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
        # '2 : Enregistrer plusieurs joueurs',  # TODO 
        '3 : Enregistrer un nouveau tournoi',  # TODO: select the players 
        '4 : Enregistrer des scores',  # TODO 

        # auto quand on cloture un round et que c'est le 4è round : 
        # '4 : Clôturer un tournoi', 
        # auto quand on cloture un round et que c'est PAS le 4è round : 
        # '5 : Enregistrer un nouveau round', 
        # auto quand on rentre les scores des matches du 4è round 
        # '6 : Clôturer un round', 
        # auto quand on enregistre les scores des matches 
        # '7 : Enregistrer nouveau un match', 
        '', 
        'Commandes de secours : ', 
        '* Revenir au menu principal', 
        '0 Sortir' 
    ] 

    display_menu = [ 
        'Menu "Afficher" : ', 
        '1 : Tous les joueurs par ordre alphabétique',  # TODO 
        '2 : Tous les joueurs par classement',  # pas demandé mais c'est fait 
        '3 : Tous les tournois',  # TODO 
        '4 : Nom et dates d\'un tournoi',  # TODO 
        # '5 : Les joueurs du tournoi par ordre alphabétique',  # TODO 
        '6 : Les tours et matches d\'un tournoi',  # TODO 
        
        # '4 : Les joueurs du tournoi par classement',  # pas demandé 
        # '5 : les résultats du tournoi',  # pas demandé
        '--------', 
        # pas demandés, pour tests : 
        '7 : les matches',  # pas demandé 
        '9 : test define_first_round', 
        '10 : test define_next_rounds', 
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

