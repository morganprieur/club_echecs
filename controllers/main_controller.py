
from models.match_model import Match_model 
from models.player_model import Player_model 
from models.round_model import Round_model 
from models.tournament_model import Tournament_model 

from views.dashboard_view import Dashboard_view 
from views.input_view import Input_view 
from views.report_view import Report_view 

from datetime import datetime, date 
from operator import attrgetter 
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

        #### ======== "R E G I S T E R"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '1': 
            self.board.ask_for_menu_action = None 
            # menu "saisir" :
            self.board.display_register() 

            # Enregistrer un joueur  # à corriger  
            if self.board.ask_for_register == '1': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_player() 

            # # Enregistrer plusieurs joueurs  # TODO 
            # if self.board.ask_for_register == '2': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_many_new_players() 

            # Enregistrer un nouveau tournoi #TODO 
            if self.board.ask_for_register == '3': 
                self.board.ask_for_register = None 
                # saisir un joueur : 
                self.enter_new_tournament() 

            # Enregistrer les scores  # TODO 
            if self.board.ask_for_register == '4': 
                self.board.ask_for_register = None 
                # Tester define_next_round : 
                self.enter_scores() 

            # # auto quand on cloture un round et que c'est le 4è round 
            # if self.board.ask_for_register == '4':  # TODO 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.close_tournament() 

            # # auto + génération des matches quand on cloture un round et que c'est PAS le 4è round 
            # if self.board.ask_for_register == '5': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_new_round() 

            # # auto quand on rentre les scores des matches du 4è round 
            # if self.board.ask_for_register == '6':  # TODO 
            #     self.board.ask_for_register = None 
            #     self.close_round() 
            #     # set end_datetime 
            #     # if round.id == 1: 
            #     #    define_matches(first=True) 
            #     # elif round.id = 4: 
            #     #    call close_tournament() 
            #     # else: 
            #     # define_matches(first=False) 

            # # auto quand on enregistre les scores des matches 
            # if self.board.ask_for_register == '7': 
            #     self.board.ask_for_register = None 
            #     # saisir un joueur : 
            #     self.enter_new_matches() 

            

            #### ============ COMMANDES DE SECOURS ============ #### 

            if self.board.ask_for_register == '*': 
                self.board.ask_for_register = None 
                return True 

            if self.board.ask_for_register == '0': 
                self.board.ask_for_register = None 
                # print(self.board.ask_for_menu_action) 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        #### ======== "R E P O R T"  M E N U S ======== #### 

        if self.board.ask_for_menu_action == '2': 
            self.board.ask_for_menu_action = None 
            # menu "afficher" : 
            self.board.display_report() 

            # Tous les joueurs par ordre alphabétique 
            if self.board.ask_for_report == '1': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('alphabétique') 

            # Tous les joueurs par classement 
            if self.board.ask_for_report == '2': 
                self.board.ask_for_report = None 
                # afficher les joueurs : 
                self.report_players('classement') 

            # Tous les tournois 
            if self.board.ask_for_report == '3': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_tournaments() 

            # Nom et dates d'un tournoi 
            if self.board.ask_for_report == '4': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.report_name_date_tournament() 

            # Les joueurs du tournoi par ordre alphabétique 
            if self.board.ask_for_report == '5': 
                self.board.ask_for_report = None 
                # afficher les tournois : 
                self.players_from_tournament_alphabetical_order() 

            if self.board.ask_for_report == '6': 
                self.board.ask_for_report = None 
                # Choisir un tournoi : 
                ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les tours ? ') 
                # afficher les tours : 
                # self.board.ask_for_tournament_id 
                self.report_rounds(ask_for_tournament_id) 

            # # pas demandé 
            # if self.board.ask_for_report == '7': 
            #     self.board.ask_for_report = None 
            #     # Choisir un tournoi : 
            #     ask_for_tournament_id = session.prompt('De quel tournoi voulez-vous les matches ? ') 
            #     self.report_matches(ask_for_tournament_id) 

            #### ======== T E S T  M E N U S ======== #### 

            if self.board.ask_for_report == '9': 
                self.board.ask_for_report = None 
                # Tester define_first_round : 
                self.define_first_round() 

            if self.board.ask_for_report == '10': 
                self.board.ask_for_report = None 
                # Tester define_next_round : 
                self.define_next_rounds() 

            """ Command to return to the main menu """ 
            if self.board.ask_for_report == '*': 
                self.board.ask_for_report = None 
                return True 

            """ Command to quit the application """ 
            if self.board.ask_for_report == '0': 
                self.board.ask_for_report = None 
                print('Fermeture de l\'application. Bonne fin de journée !') 

        #### ============ COMMANDES DE SECOURS ============ #### 

        """ Command to return to the main menu """ 
        if self.board.ask_for_menu_action == '*': 
            self.board.ask_for_menu_action = None 
            return True 

        """ Command to quit the application """ 
        if self.board.ask_for_menu_action == '0': 
            self.board.ask_for_menu_action = None 
            # print(f'self.board.ask_for_menu_action : {self.board.ask_for_menu_action}') 
            # print(f'self.board.ask_for_report : {self.board.ask_for_report}') 
            print('Fermeture de l\'application. Bonne fin de journée !') 

        return False 


    #### ============ P L A Y E R S ============ #### 

    """ Register one player """  # à corriger ### 
    def enter_new_player(self): 
        print('\nEnter new player') 
        player_data = self.in_view.input_player() 
        last_player_id = int(Player_model.get_registered_all('players')[-1]['id']) 
        # print(f'\nlast_player_id MC255 : {last_player_id}')  
        player_data['id'] = int(last_player_id)+1 
        # print(f'\nplayer_data MC257 : {player_data}')   
        self.player = Player_model(**player_data) 
        # print(f'self.player MC259 : {self.player}') 
        self.player.serialize_object(True) 

        self.report_players('alphabet') 

    """ TODO """ 
    def enter_many_new_players(self): 
        pass 

    """ Display all the players """  # à corriger ### 
    def report_players(self, sort): 
        players = Player_model.get_registered_all('players') 
        players_obj = [] 
        for player in players: 
            self.player = Player_model(**player) 
            players_obj.append(self.player) 

        # Choice of the order (alphabetical or by rank): 
        if sort == 'alphabet': 
            print('\nJoueurs par ordre alphabet : ') 
            ### à vérifier : ### 
            self.sort_objects_by_field(players_obj, 'firstname') 
            # self.report_view.sort_objects_by_field(players_obj, 'firstname') 
        if sort == 'rank': 
            print('\nJoueurs par rank : ') 
            self.sort_objects_by_field(players_obj, 'rank') 
            # self.report_view.sort_objects_by_field(players_obj, 'rank') 

        session.prompt('Appuyer sur Entrée pour continuer ') 
        self.start(False) 


    #### ============ T O U R N A M E N T S ============ #### 
    
    """ Create one tournament """ 
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
        tournaments_dict = self.last_tournament.serialize_object(False) 
        print(f'\ndict of tournaments MC217 : {tournaments_dict}') 
        # Display the last modified tournament 
        # print(f'the last tournament MC219 : {tournaments_dict[-1]}') 
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

    

    """ Rounds ### à corriger """ 
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
        if self.round.serialize_object(True) == False: 
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
        """ 
        set end_datetime 
        if round.id == 1: 
            define_matches(first=True) 
        elif round.id = 4: 
            call close_tournament() 
        else: 
            define_matches(first=False) 
        """ 
        print('\nClôturer un round') 

        closing_round = self.in_view.input_closing_round() 

        if (closing_round == 'N') or (closing_round == 'n') or (closing_round == ''): 
            print('*** La clôture du round a été annulée. ***') 
            self.start(False) 
        elif (closing_round == 'y') or (closing_round == 'Y'): 
            # Get the last round 
            last_tournament = self.select_the_last_tournament() 
            last_round = last_tournament['rounds'].pop() 
            # Set the end_datetime 
            last_round['end_datetime'] = str(self.now) 
            
            # Instantiate the round 
            self.round = Round_model(**last_round) 

            # Define what to do according to the round's id 
            if round.id == 1: 
                self.define_matches(True) 
            elif round.id == 4: 
                self.close_tournament() 
            else: 
                self.define_matches(False) 

            # Register the round again 
            if self.round.serialize_object(False) == False: 
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

    """ Matches ### à supprimer """ 
    def enter_new_matches(self): 
        print('\nEnter new match') 

        # Get the data for the current match: 
        match_data = self.in_view.input_match() 
        print(f'\nmatch_data MC306 : {match_data}') 
        new_round_id = match_data['new_round_id'] 
        # new_match = (match_data['player_1'], match_data['player_2']) 

        # Get the last tournament, where to register the current round: 
        tournaments = Tournament_model.get_registered_all('tournaments') 
        current_tournament = tournaments.pop() 
        print(f'current_tournament MC485 : {current_tournament}') 
        print(f'type(current_tournament) MC486 : {type(current_tournament)}')  # dict 

        # Instantiate current_tournament 
        self.current_tournament = Tournament_model(**current_tournament) 
        print(f'\nself.current_tournament MC490 : {self.current_tournament}') 
        print(f'\ntype(self.current_tournament) MC491 : {type(self.current_tournament)}')  # dict 

        # rounds = current_tournament['rounds'] 
        rounds = self.current_tournament.rounds 
        current_round = rounds.pop() 
        print(f'\ncurrent_round MC495 : {current_round}') 
        
        ### Appeler la méthode define_matches() avec first=True ou first=False selon l'id du dernier round ### 
        if current_round.id == 1: 
            self.define_matches(True) 
        else:  
            self.define_matches(False) 

        # Check if the given round exists 
        print(f'rounds MC325 : {rounds}') 
        print(f'len(rounds) MC326 : {len(rounds)}') 
        # print(f'type(new_round_id) PC323 : {type(new_round_id)}') 
        if not rounds or (rounds == []):  # or (rounds[new_round_id]-1==None): 
            print('Il faut d\'abord enregistrer le round.') 
        # elif not int(rounds[match_data['new_round_id']-1]):  # >len(rounds): 
        elif not rounds[new_round_id - 1]:  # >len(rounds): 
            print(f"Le round {match_data['new_round_id']} n\'est pas encore créé.") 
        # Get the given round, where to register the match 
        else: 
            # print(f"rounds['new_round_id']-1 MC334 : {rounds[match_data['new_round_id']-1]}") 
            current_round = rounds[match_data['new_round_id'] - 1] 
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
            current_round = rounds[new_round_id - 1] 
            self.round = Round_model(**current_round) 
            # print(f'\self.round MC353 : {self.round}') 
            # Instantiate the tournament : 
            self.tournament = Tournament_model(**current_tournament) 
            # print(f'\self.tournament MC356 : {self.tournament}') 

            # Register the match: 
            if self.match.serialize() == False: 
                print(f"\n*** Le round désigné (id {new_round_id}) n\'existe pas, il faut d\'abord le créer. ***") 
                self.start(False) 
            else: 
                print(f'\nLe match {self.match} a bien été enregistré') 
                # self.report_matches(current_tournament.id) 
        # ==== 
        # continuer = 
        session.prompt('Appuyer sur Entrée  pour continuer ') 
        self.start(False) 

    def enter_scores(self): 
        # Get the last tournament (dict) 
        last_tournament = self.select_the_last_tournament() 
        print(f'\nlast_tournament MC547 : {last_tournament}') 

        # Try to instantiate it (obj) 
        self.last_tournament = Tournament_model(**last_tournament) 
        print(f'\ntype(self.last_tournament) MC559 : {type(self.last_tournament)}') # obj ok 
        
        # Get the last round (object) 
        self.last_round = self.last_tournament.rounds[-1] 
        print(f'\nself.last_tournament.rounds MC563 : {self.last_tournament.rounds}') # obj ok 
        print(f'\ntype(self.last_round) MC564 : {type(self.last_round)}') # obj ok 

        # get the matches 
        current_matches_dict = self.last_round.matches 
        print(f'\ncurrent_matches_dict MC568 : {current_matches_dict}') 
        print(f'\ntype(current_matches_dict) MC569 : {type(current_matches_dict)}') # obj ok 

        # Get the matches only, without the "match" key 
        current_matches_list = [] 
        for curr_match in current_matches_dict: 
            # for curr_match_value in curr_match.values(): 
                # print(f'\ncurr_match_value MC567 : {curr_match_value}') 
            curr_match_tuple = tuple(curr_match) 
            print(f'\ncurr_match_tuple MC569 : {curr_match_tuple}') 
            self.curr_match_tuple = Match_model(*curr_match_tuple) 
            current_matches_list.append(self.curr_match_tuple) 
        print(f'\ncurrent_matches_list MC572 : {current_matches_list}')  # [<models.match_model.Match_model object at 0x00000220F74744C0>, <models.match_model.Match_model object at 0x00000220F7437670>, <models.match_model.Match_model object at 0x00000220F74355D0>, <models.match_model.Match_model object at 0x00000220F74358A0>] 
        print(f'\ntype(current_matches_list) MC573 : {type(current_matches_list)}')  # [([6, 0.0], [2, 0.0]), ([8, 0.0], [1, 0.0]), ([4, 0.0], [5, 0.0]), ([3, 0.0], [7, 0.0])] 
        
        # Get the pairs of players 
        # matches_to_ask_scores = current_matches_list 
        # for match in current_matches_list: 
        #     matches_to_ask_scores.append(match) 
        print(f'\ncurrent_matches_list MC579 : {current_matches_list}') 

        # Call the input_scores with the matches as parameter 
        input_results = self.in_view.input_scores(current_matches_list) 
        # print(f'\ninput_results MC588 : {input_results}') 
        print('---------------------') 
        # Get the first player from the current_matches who is into the input_matches_scores[0] 
        null_matches = [] 
        won_matches = [] 
        winners = input_results[1] 
        for current_match in current_matches_list: 
            for null_match in input_results[0]: 
                # print(f'\nnull_match MC594 : {null_match}') 
                if null_match in current_match.player_1: 
                    # print(f'\ncurrent_match[0][0] MC596 : {current_match[0][0]}') 
                    # Null matches : set 0.5 as the score of all the players in null_matches 
                    current_match.player_1[1] = 0.5 
                    current_match.player_2[1] = 0.5 
                    null_matches.append(current_match) 
            for winner in winners: 
                # print(f'\nwinner MC604 : {winner}') 
                if (winner in current_match.player_1): 
                    # print(f'\ncurrent_match MC607 : {current_match}') 
                    current_match.player_1[1] = 1.0 
                    print(f'\ntype(current_match) MC603 : {type(current_match)}') 
                    won_matches.append(current_match) 
                if (winner in current_match.player_2): 
                    # print(f'\ncurrent_match MC610 : {current_match}') 
                    current_match.player_1[1] = 1.0 
                    won_matches.append(current_match) 
                
        print(f'\nnull_matches MC610 : {null_matches[0].player_1}')  # [6, 0.5] 
        print(f'\nnull_matches MC611 : {null_matches}') 
        print(f'\nwon_matches MC612 : {won_matches}') 

        new_matches = null_matches[0:] 
        new_matches += won_matches[0:]  # list of objects 
        print(f'\nnew_matches MC616 : {new_matches}')  # [<models.match_model.Match_model object at 0x0000024ACC243790>, <models.match_model.Match_model object at 0x0000024ACC241720>, <models.match_model.Match_model object at 0x0000024ACC242AD0>, <models.match_model.Match_model object at 0x0000024ACC243E20>] 
        print(f'\ntype(new_matches) MC617 : {type(new_matches)}') 

        # Put again the rounds and the matches into the round 
        self.last_tournament.rounds[-1].matches = new_matches 
        print(f'\nself.last_tournament MC641 : {self.last_tournament}') 
        print(f'\nself.last_tournament.rounds[-1] MC622 : {self.last_tournament.rounds[-1]}') 
        print(f'\nself.last_tournament.rounds[-1].matches MC623 : {self.last_tournament.rounds[-1].matches[0].player_1}') 

        # Serialize the tournaments (serialize_modified_object)  
        self.last_tournament.serialize_object(False) 

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

    """ sort objects by arg """ 
    @staticmethod 
    def sort_objects_by_field(objects, field): 
        print() 
        objects.sort(key=attrgetter(field)) 
        # for obj in objects: 
        #     print(f'{obj.firstname} \t{obj.lastname}, \tclassement : {obj.rank}') 
        print(f'objects MC655 : {objects}') 
        return objects 

    """ comment """ 
    # def sort_matches_b

    # def define_first_round(self): 
    def define_matches(self, first): 
        """ Select the players' ids witch will play against each other during the first round. """ 
        # We have already self.current_tournament 
        print(f'\nself.current_tournament MC672 : {self.current_tournament}') 
        players = self.current_tournament.players 
        # Copy the players list 
        players_copy = list(players) 
        # Instantiate the players : 
        self.players = [] 
        for p in players_copy: 
            player = Player_model(**p) 
            self.players.append(player) 
        print(f"\nself.players MC681 : {self.players}") 
        # if first != True: call the sort_objects_by_field() function 
        print(f"\nfirst MC683 : {first}") 
        if first != True: 
            self.sort_objects_by_field(players_copy, 'global_score') 
        
        matches = [] 
        # Randomly define the pairs of players for 4 matches 
        
        # self.define_matches_first_round(pl, matches, last_tournament) 
        self.random_matches(matches, players_copy)  # returns matches 
        print(f'\nMatches MC692 : {matches}') 

        


    # def define_matches_first_round(self, pl, matches, last_tournament): 
    def random_matches(self, matches, players_copy): 
    # def define_matches(self, pl, matches, last_tournament): 
        """ Select the players' ids for one match. 
            Args:
                players (list): the list of the players' ids of the last tournament. 
                matches (list): the list of the selected players' ids for the round. 
            Returns:
                list: the list of the selected players' ids, added the new selected ones. 
        """ 
        for i in range(int(4)): 
            # score = the score at the start of the round (for the first round : 0) 
            score = float(0)  
            # match = the tuple containing 2 lists 'selected_player' 
            match = ([], []) 
            # selected = the list of player's id and player's score 
            selected = [] 
            for i in range(int(2)): 
                print(f'\nplayers_copy MC729 : {players_copy}') 
                # choice = the randomly chosen player's id 
                choice = random.choice(players_copy) 
                selected.append(choice) 
                players_copy.remove(choice) 
                print(f'\nplayers_copy MC734 : {players_copy}') 
                print(f'\nchoice MC735 : {choice}') 
            match = ([selected[0], score], [selected[1], score]) 
            print(f'\nmatch MC737 : {match}') 
            matches.append(match) 
        print(f'\nmatches MC739 : {matches}') 
        return matches 
    
    # at the end of the round 
    def calculate_scores(self, players, matches, round): 
        # players_scores = list last_tournament['players']['global_score'] 
        # matches_scores = list matches[0]['score'] 
        # players_scores += matches_scores 
        # "matches": [[[1, 0.5], [3, 0.5]], [[5, 0], [7, 1]], [[9, 0.5], [11, 0.5]], [[4, 1], [8, 0]]] 
        # Matches MC572 : [[8, 7], [9, 5], [5, 7], [3, 5]] 
        matches.append
        round['matches'] = matches  

    def select_one_tournament(self, t_id): 
        """ Select one tournament from its id, from the tournament.json file. 
            Args:
                t_id (int): the tournament's id 
            Returns:
                int: the tournament's id 
        """
        # Get all the tournaments from the tournaments data file (list of dicts) : 
        t_dicts = Tournament_model.get_registered_all('tournaments') 
        # Get the tournament from its id (dict) 
        t_dict = t_dicts[t_id] 
        return t_dict 

    def select_the_last_tournament(self): 
        """ Select the last tournament from the tournament.json file. 
            Returns:
                int: the tournament's id 
        """ 
        # Get all the tournaments from the tournaments data file (list of dicts) : 
        t_dicts = Tournament_model.get_registered_all('tournaments') 
        # Get the last tournament from t_dicts (dict) 
        t_dict = t_dicts[-1] 
        return t_dict 

    """ 
    ## SAUVEGARDE / CHARGEMENT DES DONNÉES
    Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.
    Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
    charger toutes ses données à partir des fichiers JSON et **pouvoir restaurer son état entre les exécutions**. 
    
    ====  
    **Si vous avez le choix entre la manipulation de dictionnaires ou d'instances de classe, 
    choisissez toujours des instances de classe pour assurer la conformité avec le modèle de conception MVC.**  

    """ 
