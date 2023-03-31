
from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from models.player_model import Player_model 
from models.tournament_model import Tournament_model 
from models.round_model import Round_model 
from models.match_model import Match_model 

from datetime import datetime, date 
from prompt_toolkit import PromptSession 
session = PromptSession() 
import random 


class Main_controller(): 

    now = datetime.now() 
    today = date.today() 

    def __init__( 
        self, 
        board: Dashboard_view, 
        in_view: Input_view, 
        report_view: Report_view, 
        now, 
        today 
    ): 
        self.board = board 
        self.in_view = in_view 
        self.report_view = report_view 
        self.tournament = None 
        # self.last_tournament = None 
        self.player = None 
        self.round = None 
        self.now = now 
        self.today = today 

    """ comment """ 
    def start(self, tourn): 
        # print("\nStart main controller") 

        if tourn == True: 
            self.board.display_welcome() 
        self.board.display_first_menu() 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_player() 

            # if self.board.ask_for_register == '2':   # TODO 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_many_new_players() 

            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_tournament() 

            if self.board.ask_for_register == '4':  # TODO 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.close_tournament() 

            if self.board.ask_for_register == '5': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_round() 

            if self.board.ask_for_register == '6':  # TODO 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.close_round() 

            if self.board.ask_for_register == '7': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_match() 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                return True 

            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                # print(self.board.ask_for_menu_action) 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 

            # print('control menu 2 : ', self.board.ask_for_report)    
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('alphabétique') 

            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('classement') 

            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 

            if self.board.ask_for_report == '7': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les matches ? ') 
                # afficher les matches : 
                # self.board.ask_for_tournament_id 
                self.report_matches(ask_for_tournament_id) 

            if self.board.ask_for_report == '8': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_tournaments() 

            if self.board.ask_for_report == '9': 
                self.board.ask_for_report = None 
                # Tester define_first_round : 
                self.define_first_round() 

            """ comment """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 

            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
                # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        """ comment """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            return True 

        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
            # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
            print('Fermeture de l\'application. Bonne fin de journée !') 

        return False 

    """ comment """ 
    def enter_new_tournament(self): 
        print('\nEnter new tournament') 

        # Get the data for the current tournament: 
        tournament_data = self.in_view.input_tournament() 

        # Get all the registered tournaments: 
        tournaments = Tournament_model.get_registered_all('tournaments') 
        last_tournament = tournaments.pop() 
        # print(f'last_tournament MC128 : {last_tournament}') 

        # Attribute the id to the current tournament: 
        tournament_data['id'] = int(last_tournament['id']) + 1 
        # print(f'tournament_data MC130 : {tournament_data}') 

        # check key 'rounds' 
        if 'rounds' not in tournament_data.keys(): 
            tournament_data['rounds'] = [] 

        # Instantiate the current tournament: 
        self.tournament = Tournament_model(**tournament_data) 

        # print(f'self.tournament MC134 : {self.tournament}') 
        if self.tournament.serialize() == False: 
            print('\nUn problème est survenu, merci d\'envoyer un feedback.') 
        else: 
            print(f'\nLe tournoi {self.tournament} a bien été enregistré') 

        # continuer = 
        session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 

    """ comment ### à corriger """ 
    def close_tournament(self): 
        # Select the last tournament 
        last_tournament = self.select_the_last_tournament() 
        # Get the value of input_closing_tournament 
        closing_tournament = self.in_view.input_closing_tournament() 
        if closing_tournament == 'y': 
            # Set the end_date 
            last_tournament['end_date'] = str(self.today) 
            print(f'last_tournament MC199 : {last_tournament}') 
        else: 
            print(f'\nLa clôture du tournoi a été annulée. ') 
            self.start(False) 
        # Instantiate it 
        self.last_tournament = Tournament_model(**last_tournament) 
        print(f'\nself.last_tournament MC205 : {self.last_tournament}') 
        print(f'\ntype(last_tournament) MC206 : {type(last_tournament)}') 
        rounds = self.last_tournament.rounds 
        # serialize the rounds 
        # for round in rounds: 
        #     print(f'\ntype(round) MC210 : {type(round)}') 
        #     round.to_dict() 
        #     print(f'\nround MC212 : {round}') 
        #     print(f'\ntype(round) MC213 : {type(round)}') 
        # Delete the last tournament 
        # + Serialize the list 
        # + Append the modified tournament to the registered list 
        # + Write the list of dictionaries into the json file 
        tournaments_dict = self.last_tournament.serialize_modified_object() 
        print(f'dict of tournaments MC217 : {tournaments_dict}') 
        # Display the last modified tournament 
        print(f'the last tournament MC219 : {tournaments_dict[-1]}') 
        # pass 
        self.start(False) 

    """ comment """ 
    def report_tournaments(self): 
        self.board.ask_for_report = None 

        tournaments = Tournament_model.get_registered_all('tournaments') 
        tournaments_obj = [] 

        for tournament in tournaments: 
            if 'rounds' not in tournament.keys(): 
                tournament['rounds'] = [] 
            for round in tournament['rounds']: 
                self.report_one_round(round)

                # round_id = tournament['rounds'].index(round) 
                # if 'matches' not in tournament['rounds'][round_id].keys(): 
                #     tournament['rounds'][round_id] = [] 
            self.tournament = Tournament_model(**tournament) 
            print(f'self.tournament MC183 : {self.tournament}') 
            tournaments_obj.append(self.tournament) 
        self.report_view.display_all_tournaments(tournaments_obj) 

        # continuer = 
        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    """ comment ### à corriger """ 
    def enter_new_player(self): 
        print('\nEnter new player') 
        player_data = self.in_view.input_player() 
        last_player_id = int(Player_model.get_registered_all('players')[-1]['id']) 
        # print(f'\nlast_player_id MC255 : {last_player_id}')  
        player_data['id'] = int(last_player_id)+1 
        # print(f'\nplayer_data MC257 : {player_data}')   
        self.player = Player_model(**player_data) 
        # print(f'self.player MC259 : {self.player}') 
        self.player.serialize_new_object() 

        self.report_players('alphabet') 

    """ TODO """ 
    def enter_many_new_players(self): 
        pass 

    """ comment """ 
    def report_players(self, sort): 

        players = Player_model.get_registered_all('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        if sort == 'alphabet': 
            print('\nJoueurs par ordre alphabet : ') 
            self.report_view.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'rank': 
            print('\nJoueurs par rank : ') 
            self.report_view.sort_objects_by_field(players_obj, 'rank') 

        # continuer = 
        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    """ comment ### à corriger """ 
    def enter_new_round(self): 
        print('\nEnter new round') 

        # Get the data for the current round: 
        data = self.in_view.input_round() 
        round_data = data[0] 
        print(f'\nround_data MC245 : {round_data}') 

        # Get the tournament where to register the current round: 
        # tournament = self.select_one_tournament(round_data['tournament_id'] - 1) 
        tournament = self.select_the_last_tournament() 

        print(f'tournament["rounds"] MC258 : {tournament["rounds"]}') 
        # Get the last round's id and attribute the id to the current round: 
        if tournament['rounds'] == []: 
            round_data['id'] = 1 
        else: 
            # If the round isn't the first one of the tournament, register the precedent tournament with the end of the precedent round  
            # self.add_ending_round() 
            round_data['id'] = int(tournament['rounds'].pop()['id']) + 1 

        if 'matches' not in round_data.keys(): 
            round_data['matches'] = [] 
        # start_datetime : 
        round_data['start_datetime'] = str(self.now) 

        # end_datetime : 

        self.round = Round_model(**round_data) 
        print(f'\nself.round MC268 : {self.round}') 

        # Register the round:  ### à corriger 
        if self.round.serialize_new_round() == False: 
            print('\n*** Le tournoi référencé dans "round" n\'existe pas, vous devez d\'abord le créer. ***') 
            self.start(False) 
        else: 
            print(f'\nLe round {self.round} a bien été enregistré') 
            # Update the number of rounds into the tournament : 
            self.tournament.nb_rounds -= 1 
            ### à corriger 
            if self.tournament.serialize() == False: 
                print('\n*** Le tournoi n\'a pas pu être mis à jour. ***') 
                self.start(False) 
            else: 
                print(f'\nLe nombre de rounds du tournoi {self.tournament.id} a bien été mis à jour. Il reste {self.tournament.nb_rounds}  rounds à jouer.') 

            # self.report_rounds(self.tournament.id) 
            self.report_tournaments(self.tournament.id) 

        # continuer = 
        session.prompt('\nAppuyer sur Entrée pour continuer ') 
        self.start(False) 

    """ comment """ 
    def close_round(self): 
        print('Clôturer un round') 

        closing_round = self.in_view.input_closing_round() 

        if (closing_round == 'N') or (closing_round == 'n') or (closing_round == ''): 
            print('*** La clôture du round a été annulée. ***') 
            self.start(False) 
        elif (closing_round == 'y') or (closing_round == 'Y'): 
            # Get the last round 
            last_tournament = self.select_the_last_tournament() 
            last_round = last_tournament['rounds'].pop() 
            # Add the end_datetime 
            last_round['end_datetime'] = str(self.now) 
            ### Add matches  --> à retirer et vérifier 
            if 'matches' not in last_round.keys(): 
                last_round['matches'] = [] 
            ### 
            # Instantiate the round 
            self.round = Round_model(**last_round) 

            # Register the round again 
            if self.round.serialize_modified_object() == False: 
                print('\nIl y a eu un problème, essayez de recommencer.') 
                session.prompt('\nAppuyer sur Entrée pour continuer ') 
                self.start(False) 
            else: 
                # Tell that the round has been closed 
                print(f'Le round {self.round.round_name} a été clôturé avec succès.') 
                session.prompt('\nAppuyer sur Entrée pour continuer ') 
                self.start(False) 
        else: 
            print('Les seules options sont "y" ou "Y" pour oui, "n" ou "N" pour non.') 
            session.prompt('\nAppuyer sur Entrée pour continuer ') 
            self.start(False) 

    """ comment """ 
    def report_one_round(self, round): 
        # for round in tournament['rounds']: 
        # print(f'round MC266 : {round}') 
        if 'matches' not in round.keys(): 
            round['matches'] = [] 

        # print(f'round["matches"] MC270 : {round["matches"]}') 

        matches = round['matches'] 
        for match in matches: 
            # change match list in a tuple: 
            match_tuple = tuple(match) 

            # Get the attributes from the data 
            match_dict = {} 
            match_dict['round_id'] = round['id'] 
            match_dict['id_joueur_1'] = match_tuple[0][0] 
            match_dict['score_joueur_1'] = match_tuple[0][1] 
            match_dict['id_joueur_2'] = match_tuple[1][0] 
            match_dict['score_joueur_2'] = match_tuple[1][1] 

            self.match = Match_model(**match_dict) 
        self.round = Round_model(**round) 

    """ comment """ 
    def report_rounds(self, ask_for_tournament_id): 

        tournament_id = int(ask_for_tournament_id) - 1 
        # tournament object : 
        tournament = self.select_one_tournament(tournament_id) 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds = [] 
        # print(f'tournament MC262 : {tournament}')  # matches ok 
        # print(f'tournament["rounds"] MC263 : {tournament["rounds"]}')  # matches ok 

        # for round in tournament['rounds']: 
        #     # print(f'round MC266 : {round}') 
        #     if 'matches' not in round.keys(): 
        #         round['matches'] = [] 

        #     # print(f'round["matches"] MC270 : {round["matches"]}') 

        #     matches = round['matches'] 
        #     for match in matches: 
        #         # change match list in a tuple: 
        #         match_tuple = tuple(match) 

        #         # Get the attributes from the data 
        #         match_dict = {} 
        #         match_dict['round_id'] = round['id'] 
        #         match_dict['id_joueur_1'] = match_tuple[0][0] 
        #         match_dict['score_joueur_1'] = match_tuple[0][1] 
        #         match_dict['id_joueur_2'] = match_tuple[1][0] 
        #         match_dict['score_joueur_2'] = match_tuple[1][1] 

        #         self.match = Match_model(**match_dict) 
        #     self.round = Round_model(**round) 

        # Instantiate the tournament : 
        self.tournament = Tournament_model(**tournament) 
        # print(f'self.tournament MC286 : {self.tournament}') 

        # Extract the rounds from the tournament (list of objects) : 
        # rounds = self.tournament.rounds 
        # matches = self.round.matches 

        self.report_view.display_rounds_one_tournament(self.tournament) 

        # continuer = 
        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 

    """ comment """ 
    def enter_new_match(self): 
        print('\nEnter new match') 

        ### Appeler la méthode define_first_round() ### 
        ### Appeler la méthode define_next_matches() ### 

        # Get the data for the current match: 
        match_data = self.in_view.input_match() 
        print(f'\nmatch_data MC306 : {match_data}') 
        round_id = match_data['round_id'] 
        # new_match = (match_data['player_1'], match_data['player_2']) 

        # print(f'\nround_id MC310 : {round_id}') 
        # print(f'\nround_id-1 MC311 : {round_id-1}') 
        # print(f'\nrounds[round_id-1] MC312 : rounds[{round_id-1}]') 

        # Get the (last) tournament where to register the current round: 
        tournaments = Tournament_model.get_registered_all('tournaments') 
        # current_tournament = len(tournaments)-1 
        current_tournament = tournaments.pop() 
        print(f'current_tournament MC316 : {current_tournament}') 
        print(f'type(current_tournament) MC317 : {type(current_tournament)}')  # dict 

        rounds = current_tournament['rounds'] 
        # print(f'\nrounds[0] MC322 : {rounds[0]}') 

        # Check if the given round exists 
        print(f'rounds MC325 : {rounds}') 
        print(f'len(rounds) MC326 : {len(rounds)}') 
        # print(f'type(round_id) PC323 : {type(round_id)}') 
        if not rounds or (rounds == []):  # or (rounds[round_id]-1==None): 
            print('Il faut d\'abord enregistrer le round.') 
        # elif not int(rounds[match_data['round_id']-1]):  # >len(rounds): 
        elif not rounds[round_id - 1]:  # >len(rounds): 
            print(f"Le round {match_data['round_id']} n\'est pas encore créé.") 
        # Get the given round, where to register the match 
        else: 
            # print(f"rounds['round_id']-1 MC334 : {rounds[match_data['round_id']-1]}") 
            current_round = rounds[match_data['round_id'] - 1] 
            # current_round = current_tournament['rounds'].pop() 
            if 'matches' not in current_round.keys(): 
                current_round['matches'] = [] 
            # self.round = Round_model(**current_round) 
            # print(f'current_round MC340 : {current_round}') 
            # print(f'type(current_round) MC331 : {type(current_round)}') 

            # Get the match's id and attribute the id to the current match: 
            # print(f'\nnew_match MC345 : {match_data}') 
            self.match = Match_model(**match_data) 
            # print(f'\nself.match MC347 : {self.match}') 
            # print(f'\ntype(self.match) MC348 : {type(self.match)}') 

            # Instantiate the round : 
            current_round = rounds[round_id - 1] 
            self.round = Round_model(**current_round) 
            # print(f'\self.round MC353 : {self.round}') 
            # Instantiate the tournament : 
            self.tournament = Tournament_model(**current_tournament) 
            # print(f'\self.tournament MC356 : {self.tournament}') 

            # Register the match: 
            if self.match.serialize() == False: 
                print(f"\n*** Le round désigné (id {round_id}) n\'existe pas, il faut d\'abord le créer. ***") 
                self.start(False) 
            else: 
                print(f'\nLe match {self.match} a bien été enregistré') 
                # self.report_matches(current_tournament.id) 
        # ==== 
        # continuer = 
        session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 

    """ comment """ 
    def report_matches(self, ask_for_tournament_id): 
        tournament_id = int(ask_for_tournament_id) - 1 
        # tournament object : 
        tournament = self.select_one_tournament(tournament_id) 

        if 'rounds' not in tournament.keys(): 
            tournament.rounds = [] 
        self.tournament = Tournament_model(**tournament) 
        print(f'self.tournament MC290 : {self.tournament}') 

        rounds = self.tournament.rounds 
        print(f'rounds MC293 : {rounds}') 

        self.report_view.display_matches_one_tournament(self.tournament) 

        # continuer = 
        session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 

    """ =================== UTILS =================== """ 

    """ comment """ 
    def define_first_round(self): 
        # Select the players bound with the last tournament 
        last_tournament = self.select_the_last_tournament() 
        # print(f'\nlast_tournament.keys() MC558 : {last_tournament.keys()}') 
        players = last_tournament['players'] 
        print(f'\nlast_tournament players MC560 : {players}')  # v 

        matches = [] 
        # Randomly define the pears of players for 4 matches 
        for i in range(int(4)): 
            self.define_match(players, matches) 
        
        print(f'\nMatches MC572 : {matches}') 
        # print(f'\nMatches MC567 : {matches}') 


    def define_match(self, players, matches): 
        match = [] 
        for i in range(int(2)): 
            selected = random.choice(players) 
            # match_select = self.define_match(players, match) 
            match.append(selected) 
            print(f'\nmatch MC576 : {match}') 
        matches.append(match) 
        # match_select = self.define_match(players, match) 
        # print(f'\nmatches MC579 : {matches}') 
        # matches.append(match_select) 
        return matches 



    # def define_match(self, players, match): 
        
    #     print(f'\nSelected MC573 : {selected}') 
    #     # print(f'\ntype(selected) MC564 : {type(selected)}') 
    #     match.append(selected) 
    #     players.remove(selected) 
    #     print(f'\nPlayers MC576 : {players}') 
    #     return match 


        
         

    """ comment """ 
    def check_key(self, key, model, objs): 
        # print(f'objs MC142 : {objs}')
        list_objs = []
        for data in objs: 
            # print(f'data MC145 : {data}') 
            if key not in data.keys():  
                data[key] = []  
            list_objs.append(model(**data)) 

        return list_objs 

    """ comment """ 
    def select_one_tournament(self, t_id): 
        # Récupérer tous les <obj> dans la liste <objs> (liste de dicts) : 
        t_objs = Tournament_model.get_registered_all('tournaments') 
        # Sélectionner le <objet> indiqué dans id (dict)  # -1 : pas eu ce problème auparavant 
        t_obj = t_objs[t_id]  # -1  ### 
        return t_obj 

    def select_the_last_tournament(self): 
        t_objs = Tournament_model.get_registered_all('tournaments') 
        t_obj = t_objs[-1] 
        print(f'last tournament MC593 : {t_obj}') 
        return t_obj 

    """ 
    ## SAUVEGARDE / CHARGEMENT DES DONNÉES
    Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.
    Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
    charger toutes ses données à partir des fichiers JSON et **pouvoir restaurer son état entre les exécutions**. 
    
    ====  
    **Si vous avez le choix entre la manipulation de dictionnaires ou d'instances de classe, 
    choisissez toujours des instances de classe pour assurer la conformité avec le modèle de conception MVC.**  

    """ 
