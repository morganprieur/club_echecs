

import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 
# # TinyDB 
# from tinydb import TinyDB 
# db = TinyDB('db.json') 
# tournament_table = db.table('tournament') 


class Tournament_model(): 

    # players = list 

    def __init__(self, name, site, t_date, duration, description):  # rounds, #  name, site, t_date, nb_rounds, players, duration, description  
        self.name = name 
        self.site = site 
        self.t_date = t_date 
        # self.nb_rounds = nb_rounds 
        # self.rounds = rounds 
        # self.rounds = None 
        # self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):  # , roundDicts        
        # begin_phrase = f'\nNom du tournoi : {self.name} \nlieu : {self.site} \ndate(s) : {self.t_date} \n{self.nb_rounds} tours \nliste des tours : \n' # (instances de tours à mettre ici ###)  
        # # roundsList = '' 
        # round_name = '' 
        # round_matches = '' 
        # start_datetime = '' 
        # end_datetime = '' 
        # middle_phrase = f'\njoueurs de ce tournoi : (instances de joueurs à mettre ici ###) \n' 
        # playersList = [] 
        # end_phrase = f'temps de jeu : {self.duration}. \nDescription : {self.description}' 
        # for r in self.rounds: 
        #     # print(f'i TM34 : {i}') 
        #     round_name += f'{r}\n' 
        #     # round_name += f'{r["round_name"]}\n' 
        #     # round_matches += f'{r["round_matches"]}\n' 
        #     # start_datetime += f'{r["start_datetime"]}\n' 
        #     # end_datetime += f'{r["end_datetime"]}\n' 
        # # print(f'len(self.players) TM49 : {len(self.players)}') 
        # print(f'len(players) TM49 : {len(self.players)}') 
        # if self.players:  # TypeError: 'Tournament_model' object is not iterable ### 
        #     for p in self.players: 
        #         playersList.append(p) 
        # return f'{begin_phrase}\n {round_name} {round_matches}players : {playersList}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}' 
        return f'{self.name}, {self.site}, {self.t_date}, {self.duration}, {self.description}' 
        

    # 'rounds': { 
    #     1: roundDicts[0][1], 
    #     2: roundDicts[0][2],  
    # }, ### comment intégrer l'objet Round ici ? 


    def instantiate_tournament(self, tourn): 
        # print(f'tourn TM58 : {tourn}') 
        # self.tournaments = [] 
        # for i in range(len(tourn)): 
        for t_obj in tourn: 
            self.tournament = Tournament_model( 
                name=tourn['name'], 
                site=tourn['site'], 
                t_date=tourn['t_date'], 
                duration=tourn['duration'], 
                description=tourn['description'] 
                # name=tourn[i]['name'], 
                # site=tourn[i]['site'], 
                # t_date=tourn[i]['t_date'], 
                # duration=tourn[i]['duration'], 
                # description=tourn[i]['description'] 
            ) 
            # self.tournaments.append(self.tournament) 
        print(f'self.tournament TM68 : {self.tournament}') 
        return self.tournament 
    
    def print_t(self): 
        print(f'dir(self) TM79 : {dir(self)}') 
        print(f'test TM78 : {self.tournament}') 

    # def instantiate_tournament(self, tournaments, roundDicts): 
    #     print(f'type(tournaments) TM63 : {type(tournaments)}') 
    #     print(f'tournaments TM64 : {tournaments}')  # tournament == déjà un objet 
    #     # for t in tournaments: 
    #     #     self.tournament_x = Tournament_model( 
    #     #         lastname=p, 
    #     #         firstname=p, 
    #     #         age=p, 
    #     #         genre=p, 
    #     #         rank=p 
    #     #     ) 

    #     # for p in players: 
    #     #     self.player_x = Player_model( 
    #     #         lastname=p, 

    #     for t in tournaments: 
    #         print(f't TM63 : {t}') 
    #         # print(f'type(tournaments[t]) TM61 : {type(tournaments[t])}') 
    #         self.tournament_x = Tournament_model( 
    #             name=t,  
    #             site=t,  
    #             t_date=t,  
    #             nb_rounds=t, 
    #             # rounds = tournaments['rounds'], 
    #             rounds= # [ 
    #                 roundDicts, 
    #                 # {      # key=1/2...: value='round_name'... 
    #                 # 'round_name' = roundDicts[0]["1"]['round_name'],  ### TypeError: tuple indices must be integers or slices, not str 
    #                 # 'round_matches' = roundDicts[0]["1"]['round_matches'], 
    #                 # 'start_datetime' = roundDicts[0]["1"]['start_datetime'], 
    #                 # 'end_datetime' = roundDicts[0]["1"]['end_datetime'] 
    #                 # }, 
    #             # ], 
    #             players=t, 
    #             duration=t, 
    #             description=t 
    #         ) 
    #         print(f'tournament_x.name TM95 : {self.tournament_x.name}') 
    #         print(f'type(self.tournament_x.name) TM96 : {type(self.tournament_x.name)}') 

    #     return self.tournament_x 
    
    ### Voir pour sérialiser : 
    def to_dict(self, exclude=None): 
        exclude = exclude or []
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and key not in exclude
            and not callable(getattr(self, key))
            and isinstance(getattr(self, key), (str, int, float))
        } 

    # def serialize_tournament(self): 
    def serialize_one_tournament(self):  # , tournament  # avec (self) ###  , players):  # players = serialized_players 
        print('serialize_one_tournament() TM143') 
        # print(f'type(tournament) TM109 : {type(self.tournament)}') 

        # serialized_tournaments = [] 

        # for t_obj in tournaments: 
            # print(f't_obj TM136 : {t_obj}') 
            # print(f'type(t_obj) TM136 : {type(t_obj)}') 
        self.one_serialized_tournament = { 
            'name': self.tournament.name, 
            'site': self.tournament.site, 
            't_date': self.tournament.t_date, 
            # 'nb_rounds': self.tournament.nb_rounds, 
            # 'rounds': self.tournament.rounds, 
            # 'players': self.tournament.players,
            'duration': self.tournament.duration, 
            'description': self.tournament.description 
        } 
        # print(f'serialized_tournament["name"] TM148 : {serialized_tournament["name"]}') 

        # serialized_tournaments.append(serialized_tournament) 
        # print(f'serialized_tournaments TM150 : {serialized_tournaments}') 
        # print(f'serialized_tournament TM157 : {self.one_serialized_tournament}') 

        # tournament_table.truncate() 
        # # Register the serialized tournaments into the DB: 
        # # tournament_table.insert_multiple(serialized_tournaments) 
        # tournament_table.insert(serialized_tournament) 

        return self.one_serialized_tournament 
    
   
    def serialize_tournaments(self): 
        # print(f'dir(self) TM176 : {dir(self)}') 
        # print(f'self.serialized_tournament TM177 : {self.serialized_tournament}') 
        Tournament_model.serialize_one_tournament(Tournament_model) 
        # ouvrir fichier en lecture : 
        self.serialized_tournaments = [] 
        if Tournament_model.check_if_json_empty(Tournament_model): 
            # si il est vide -> ajouter seulement le nouveau tournoi dans self.serialized_tournaments 
            self.serialized_tournaments.append(self.one_serialized_tournament) 
            # self.serialized_tournaments.append('truc') 
            # l'enregistrer : 
            # Tournament_model.register_tournaments(Tournament_model) 
        else: 
            # self.registered = json.load(file) 
            Tournament_model.get_registered_tournaments(Tournament_model) 
            print(f'self.registered TM190 : {self.registered}') # 
            Tournament_model.add_new_tournament(Tournament_model) 
            # print(f'self.serialized_tournaments TM192 : {self.serialized_tournaments}') ## 
        Tournament_model.register_tournaments(Tournament_model) 
        # print(f'self.serialized_tournaments TM194 : {self.serialized_tournaments}') ## 
        return self.serialized_tournaments 

    
    def check_if_json_empty(self): 
        with open("tables/t_table.json",'rb') as f: 
            if len(f.read()) == 0: 
                print("The file is empty.") 
                return True 
            else: 
                print("The file is not empty.") 
                return False 


    # Si le fichier JSON n'est pas vide : 
    def get_registered_tournaments(self): 
        with open('tables/t_table.json', 'r') as file: 
            self.registered = json.load(file) 
        # print(f'type(self.registered) TM192 : {type(self.registered)}') 
        print(f'self.registered TM213 : {self.registered}') 
        return self.registered 
    

    def add_new_tournament(self): 
        #   append le dernier tournoi à la liste, 
        print(f'self.one_serialized_tournament TM219 : {self.one_serialized_tournament}') 
        print(f'self.registered TM220 : \n{self.registered}') # 
        self.registered.append("tric") 
        # self.registered.append(self.one_serialized_tournament) 
        print(f'self.registered TM222 : \n{self.registered}') ## 
        for t in self.registered: 
            self.serialized_tournaments.append(t) 
        # print(f'self.serialized_tournaments TM225 : {self.serialized_tournaments}') ## 
        return self.serialized_tournaments 


    def register_tournaments(self): 
        # print(f'self.serialized_tournaments TM229 : {self.serialized_tournaments}') ## 
        # ouvrir le fichier en écriture totale : 
        with open('tables/t_table.json', 'w') as file: 
            json.dump(self.serialized_tournaments, file) 
            return self.serialized_tournaments 


 

""" 
    Chaque tournoi doit contenir au moins les informations suivantes :
    • Nom
    • Lieu :
    • Date
        ◦ Jusqu'à présent, tous nos tournois sont des événements d'un jour, mais nous pourrions en organiser de plusieurs jours à l'avenir, ce qui devrait donc permettre de varier les dates.
    • Nombre de tours
        ◦ Réglez la valeur par défaut sur 4.
    • Tournées
        ◦ La liste des instances rondes.
    • Joueurs
        ◦ Liste des indices correspondant aux instances du joueur stockées en mémoire.
    • Contrôle du temps
        ◦ C'est toujours un bullet, un blitz ou un coup rapide.
    • Description
        ◦ Les remarques générales du directeur du tournoi vont ici.
""" 

