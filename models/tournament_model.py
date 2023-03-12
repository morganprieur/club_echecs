
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 
from .round_model import Round_model 
import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 


class Tournament_model(AbstractModel): 

    def __init__(self, id:int, name:str, site:str, t_date:str, rounds:list, duration:str, description:str):  #  name, site, t_date, nb_rounds, players:list, duration, description  
        super().__init__('t_table') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.t_date = t_date 
        # self.nb_rounds = nb_rounds
        if rounds and isinstance(rounds[0], dict): 
            print(f'rounds TM38 : {rounds}') 
            self.rounds = [Round_model(**data) for data in rounds] 
        else:
            self.rounds = rounds 
        # self.rounds = None 
        # self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):  # , roundDicts        
        # return f'{begin_phrase}\n {round_name} {round_matches}players : {playersList}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}' 
        return f'{self.id}, {self.name}, {self.site}, {self.t_date}, rounds : {self.rounds}, {self.duration}, {self.description}' 
    

    def to_dict(self): 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            't_date': self.t_date, 
            'rounds': self.rounds, 
            'duration': self.duration, 
            'description': self.description 
        }

    

if __name__ == "__main__": 
    
    new_tournament = { 
        "id": 7, 
        "name": "Nom 220", 
        "site": "Lieu 220", 
        "t_date": "2023/02/22", 
        "rounds": [ 
            [(1,0), (2,0)], 
            [(3,0), (4,0)], 
            [(5,0), (6,0)], 
            [(7,0), (8,0)],  
        ], 
        "duration": "bullet", 
        "description": "description 220", 
    } 
    one_tournament = Tournament_model(**new_tournament) 
    # print(f'new_tournament TP192 : {new_tournament}') 
    # print(f'type(new_tournament) TP193 : {type(new_tournament)}') 
    one_tournament.serialize() 
    # print(f'get tournaments TM189 : {Tournament_model.get_tournaments()}') 
    # print(f'get registered TM189 : {Tournament_model.get_registered()}') 


""" 
    Chaque tournoi doit contenir au moins les informations suivantes :
    • Nom
    • Lieu :
    • Date
        ◦ Jusqu'à présent, tous nos tournois sont des événements d'un jour, 
            mais nous pourrions en organiser de plusieurs jours à l'avenir, 
            ce qui devrait donc permettre de varier les dates.
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

