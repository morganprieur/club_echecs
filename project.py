
from controllers.main_controller import Main_controller 
from views.dashboard_view import Dashboard_view 
from views.report_view import Report_view 
from views.input_view import Input_view 


welcome = '\n* * * * * * * * * * * * * * * * * \
    \n\nBonjour et bienvenue ! \
    \n\nCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs. \
    \nSi vous rencontrez des erreurs, le fichier README.md contient les informations pour envoyer des feedbacks. \
    \n\nDans le menu, vous pouvez à tout moment utiliser les Commandes de sortie : \
    \n* pour revenir au menu précédent, \n0 pour revenir au menu principal' 

main_menu = [ 
    'Menu principal : ', 
    '1 = saisir', 
    '2 = afficher' 
] 

register_menu = [ 
    'Menu "saisir" : ', 
    '1 = un joueur', 
    '2 = un tournoi' 
] 

display_menu = [ 
    'Menu "Afficher" : ', 
    # A faire + tard : 
    # '1 = Tous les joueurs par ordre alphabétique', 
    # '2 = Tous les joueurs par classement', 
    # '3 = Les joueurs du tournoi par ordre alphabétique', 
    # '4 = Les joueurs du tournoi par classement', 
    # '5 = les résultats du tournoi', 
    # '6 = les tours', 
    # '7 = les matches', 
    '8 = tous les tournois', 

    # pas demandés : 
    # '9 = le dernier tournoi', 
    # '9 = le tournoi du jour', 
    '', 
    'Commandes de secours : ', 
    '0 = Retour au menu précédent', 
    '* = Menu principal'
] 


if __name__ == "__main__": 
    new_board = Dashboard_view( 
        welcome=welcome, 
        main_menu=main_menu, 
        register_menu=register_menu, 
        display_menu=display_menu 
    ) 
    new_input_view = Input_view() 
    new_reporter = Report_view() 

    new_controller = Main_controller( 
        board=new_board, 
        in_view=new_input_view, 
        report_view=new_reporter 
    ) 
    new_controller.start() 


