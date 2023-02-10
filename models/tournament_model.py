
from .abstract_model import AbstractModel 

import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 


class Tournament_model(AbstractModel): 

    # players = list 

    def __init__(self, name:str, site:str, t_date:str, players:list, duration:str, description:str):  # rounds, #  name, site, t_date, nb_rounds, duration, description  
        self.name = name 
        self.site = site 
        self.t_date = t_date 
        # self.nb_rounds = nb_rounds 
        # self.rounds = rounds 
        # self.rounds = None 
        self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):  # , roundDicts        
        # return f'{begin_phrase}\n {round_name} {round_matches}players : {playersList}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}' 
        return f'{self.name}, {self.site}, {self.t_date}, {self.duration}, {self.description}, players : {self.players}' 
        
    # print('start tournament model') 

    # 'rounds': { 
    #     1: roundDicts[0][1], 
    #     2: roundDicts[0][2],  
    # }, ### comment intégrer l'objet Round ici ? 


    # tourn = { 
    #     'name':'name1', 
    #     'site':'site1', 
    #     't_date':'t_date1', 
    #     'duration':'duration', 
    #     'description':'description'
    # } 

    # def instantiate_tournament(self, new_tournament): 
    #     # print(f'tourn TM58 : {tourn}') 
    #     # self.tournaments = [] 
    #     # for i in range(len(tourn)): 
    #     for t_obj in new_tournament: 
    #         self.tournament = Tournament_model( 
    #             name=new_tournament['name'], 
    #             site=new_tournament['site'], 
    #             t_date=new_tournament['t_date'], 
    #             duration=new_tournament['duration'], 
    #             description=new_tournament['description'] 
    #             # name=tourn[i]['name'], 
    #             # site=tourn[i]['site'], 
    #             # t_date=tourn[i]['t_date'], 
    #             # duration=tourn[i]['duration'], 
    #             # description=tourn[i]['description'] 
    #         ) 
    #         # self.tournaments.append(self.tournament) 
    #     print(f'type(self.tournament) TM87 : {type(self.tournament)}') 
    #     print(f'self.tournament TM88 : {self.tournament}') 
    #     return self.tournament 
    
    # def print_t(self): 
    #     print(f'dir(self) TM79 : {dir(self)}') 
    #     print(f'test TM78 : {self.tournament}') 

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
    

    @staticmethod 
    def check_if_json_empty(): 
        # with open("tables/t_table.json",'rb') as f: 
        with open("tables/t_table.json",'rb') as f: 
            if len(f.read()) == 0: 
                print("The file is empty.") 
                return True 
            else: 
                print("The file is not empty.") 
                return False 


    # # Si le fichier JSON n'est pas vide : 
    # @staticmethod 
    # def get_tournaments(): 
    #     with open('tables/t_table.json', 'r') as file: 
    #         tournaments = json.load(file) 
    #     # print(f'type(self.registered) TM192 : {type(self.registered)}') 
    #     print(f'tournaments TM166 : {tournaments}') 
    #     print(f'type(tournaments) TM167 : {type(tournaments)}') 
    #     return tournaments 
    

    @staticmethod 
    def get_registered(table): 
        # with open('tables/t_table.json', 'r') as file: 
        with open(f'tables/{table}', 'r') as file: 
            registered = json.load(file) 
        # print(f'registered AC16 : {registered}') 
        # print(f'type(registered) AC17 : {type(registered)}') 
        return registered 


    def serialize(self): 
        # print(f'one_tournament TM172 : {self}') 
        # print(f'type(one_tournament) TP193 : {type(self)}') 
        if not Tournament_model.check_if_json_empty(): 
            # tournaments = Tournament_model.get_tournaments() 
            tournaments = Tournament_model.get_registered('t_table.json') 
        else: 
            tournaments = [] 
        one_serialized_tournament = { 
            'name': self.name, 
            'site': self.site, 
            't_date': self.t_date, 
            # 'nb_rounds': self.tournament.nb_rounds, 
            # 'rounds': self.tournament.rounds, 
            'players': self.players,
            'duration': self.duration, 
            'description': self.description 
        } 
        # tournaments.append(self.to_dict()) 
        tournaments.append(one_serialized_tournament) 
        with open("tables/t_table.json", "w") as file: 
            json.dump(tournaments, file) 


if __name__ == "__main__": 
    new_tournament = {
        "name": "Nom 050", 
        "site": "Lieu 50", 
        "t_date": "2023/01/27", 
        "duration": "bullet", 
        "description": "description 050", 
    } 
    one_tournament = Tournament_model(**new_tournament) 
    print(f'new_tournament TP192 : {new_tournament}') 
    print(f'type(new_tournament) TP193 : {type(new_tournament)}') 
    one_tournament.serialize() 
    # print(f'get tournaments TM189 : {Tournament_model.get_tournaments()}') 
    # print(f'get registered TM189 : {Tournament_model.get_registered()}') 


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

