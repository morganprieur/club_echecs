

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

    """ 
    liste_menu_principal = [ 
        "\nMenu principal : ", 
        "1 : Saisir", 
        "2 : Afficher" 
    ] 

    liste_menu_saisir = [
        "Saisir", 
        "1 : un ou des joueurs", 
        "2 : un ou des matches", 
        "3 : un ou des tours", 
        "4 : un ou (?) des tournois", 
        "* : retour au menu précédent", 
        "0 : retour au menu principal" 
    ] 

    liste_menu_afficher = [ 
        "Afficher", 
        "1 : tous les joueurs par ordre alphabétique", 
        "2 : tous les joueurs par classement", 
        "3 : les joueurs du tournoi par ordre alphabétique", 
        "4 : les joueurs du tournoi par classement", 
        "5 : les résultats du tournoi", 
        "6 : les tours", 
        "7 : les matches", 
        "* : retour au menu précédent", 
        "0 retour au menu principal" 
    ] 
    """

    @staticmethod 
    def welcome_view(): 

        welcome = ' * * * * * * * * * * * * * * * * \nBonjour et bienvenue ! \
            \nCe programme va vous permettre de créer, gérer et afficher vos tournois d\'échecs. \
            \nSi vous rencontrez des erreurs, le fichier README.md contient les informations de feedback. \
            \nDans le menu, vous pouvez à tout moment utiliser les Commandes de sortie : \
            \n * pour revenir au menu précédent, \n 0 pour revenir au menu principal' 

        menu_principal = [ 
            '1 = saisir', 
            '2 = afficher' 
        ] 
        menu_saisie = [ 
            '1 = un joueur', 
            '2 = un tournoi' 
        ] 
        menu_affichage = [ 
            # A faire + tard : 
            # '1 = Tous les joueurs par ordre alphabétique', 
            # '2 = Tous les joueurs par classement', 
            # '3 = Les joueurs du tournoi par ordre alphabétique', 
            # '4 = Les joueurs du tournoi par classement', 
            # '5 = les résultats du tournoi', 
            # '6 = les tours', 
            # '7 = les matches', 

            '8 = le tournoi du jour', 
            '9 = tous les tournois', 

            '0 = retour au menu précédent' 
        ] 

        print(welcome) 

        print(menu_principal[0]) 
        print(menu_principal[1]) 


        # Prompt to ask the action to do 
        ask_for_menu_action = session.prompt('\nChoisir une action : ') 
        # return ask_for_menu_action 

        if ask_for_menu_action == '1': 
            # print('ok') 
            for i in range(len(menu_saisie)): 
                print(menu_saisie[i]) 
        elif ask_for_menu_action == '2': 
            # print('not ok') 
            for i in range(len(menu_affichage)): 
                print(menu_affichage[i]) 
        elif ask_for_menu_action == '0': 
            print(menu_principal[0]) 
            print(menu_principal[1]) 
        elif ask_for_menu_action == '*': 
            Dashboard_view.welcome_view() 
        else: 
            print('Cette réponse n\'est pas définie, veuillez choisir une autre action') 
            Dashboard_view.welcome_view() 

        # print(messages['menus'][0][int(ask_for_menu_action)]) 
        # print(messages['menus'][0][int(ask_for_menu_action)][1]) 
        # print(messages['menus'][0][int(ask_for_menu_action)][2]) 

if __name__ == "__main__": 
    Dashboard_view.welcome_view() 

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








