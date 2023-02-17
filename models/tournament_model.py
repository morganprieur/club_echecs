
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 

import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 


class Tournament_model(AbstractModel): 

    # players = list 

    def __init__(self, name:str, site:str, t_date:str, duration:str, description:str):  # rounds, #  name, site, t_date, nb_rounds, players:list, duration, description  
        super().__init__('t_table') 
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
        # return f'{begin_phrase}\n {round_name} {round_matches}players : {playersList}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}' 
        return f'{self.name}, {self.site}, {self.t_date}, {self.duration}, {self.description}'  # , players : {self.players} 
    

    def to_dict(self): 
        return { 
            'name': self.name, 
            'site': self.site, 
            't_date': self.t_date, 
            # 'players': self.players, 
            'duration': self.duration, 
            'description': self.description 
        }



if __name__ == "__main__": 
    new_tournament = {
        "name": "Nom 050", 
        "site": "Lieu 50", 
        "t_date": "2023/01/27", 
        "duration": "bullet", 
        "description": "description 050", 
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

