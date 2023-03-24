
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 
from .round_model import Round_model 
# import json 
import re 
# d = re.compile('[\d]+') 
start = re.compile('[\[]+') 
end = re.compile('[\]]+') 


class Tournament_model(AbstractModel): 

    def __init__( 
        self, id: int, name: str, site: str, t_date: str,nb_rounds: int, rounds: list, duration: str, description: str 
    ):  # players: list 
        super().__init__('t_table') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.t_date = t_date 
        self.nb_rounds = nb_rounds 
        if rounds and isinstance(rounds[0], dict): 
            print(f'rounds TM23 : {rounds}') 
            self.rounds = [Round_model(**data) for data in rounds] 
        else:
            self.rounds = rounds 
        # self.rounds = None 
        # self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):  # , roundDicts        
        # return f'{begin_phrase}\n {round_name} {round_matches}players : 
        # # {playersList}heure début : {start_datetime}heure fin : {end_datetime}{middle_phrase}{end_phrase}' 
        tournament_string_start = (f'{self.id}, {self.name}, {self.site}, {self.t_date}, rounds : ') 
        tournament_string_end = (f'nb de rounds : {self.nb_rounds}, rounds : {self.rounds}, {self.duration}, {self.description}') 
        return tournament_string_start + tournament_string_end 

    """ comment """ 
    def to_dict(self): 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            't_date': self.t_date, 
            'nb_rounds': self.nb_rounds, 
            'rounds': self.rounds, 
            'duration': self.duration, 
            'description': self.description 
        } 


""" 
========== 

## TOURNOIS
Le programme utilise les fichiers de données JSON pour la persistance des informations sur
les tournois. Les fichiers de données sont généralement situés dans le dossier
data/tournaments.  

### DÉROULEMENT DE BASE DU TOURNOI
● Un tournoi a un nombre de tours défini.
● Chaque tour est une liste de matchs.
    ○ Chaque match consiste en une paire de joueurs.
● À la fin du match, les joueurs reçoivent des points selon leurs résultats.
    ○ Le gagnant reçoit 1 point.
    ○ Le perdant reçoit 0 point.
    ○ Chaque joueur reçoit 0,5 point si le match se termine par un match nul.  

### SCHÉMA DES TOURNOIS
Chaque tournoi doit contenir au moins les informations suivantes :
● nom ;
● lieu ;
● date de début et de fin ;
● nombre de tours 
    – réglez la valeur par défaut sur 4 ;
● numéro correspondant au tour actuel ;
● une liste des tours ;
● une liste des joueurs enregistrés ;
● description pour les remarques générales du directeur du tournoi.  

""" 
