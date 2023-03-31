
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

    def __init__( 
        self, id: int, name: str, site: str, start_date: str, end_date: str, rounds: list, duration: str, description: str 
    ):  # players: list,  nb_rounds:int,  
        super().__init__('tournaments') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.start_date = start_date 
        self.end_date = end_date 
        # self.nb_rounds = nb_rounds 
        if rounds and isinstance(rounds[0], dict): 
            print(f'\nrounds TM26 : {rounds}')  # (list of dicts)
            self.rounds = [Round_model(**data) for data in rounds] 
        else: 
            self.rounds = rounds 
        # self.players = players 
        self.duration = duration 
        self.description = description 

    def __str__(self):  # , roundDicts        
        tournament_string_start = (f'{self.id}, {self.name}, {self.site}, {self.start_date}, {self.end_date},') 
        tournament_string_end = (f' rounds : \n{self.rounds}, {self.duration}, {self.description}') 
        return tournament_string_start + tournament_string_end 

    """ comment """ 
    def to_dict(self): 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            'start_date': self.start_date, 
            'end_date': self.end_date, 
            'rounds': self.rounds, 
            'duration': self.duration, 
            'description': self.description 
        } 
    
    def serialize_modified_object(self):
        """ Abstract method for serialize the objects from the models. """ 
        if not self.check_if_json_empty(): 
            objects = self.get_registered() 
            print(f'\nobjects TM56 : {objects}') 
            print(f'\ndir(self) TM57 : {dir(self)}') 
            # suppress the last tournament : 
            objects.pop() 
            # serialize the rounds 
            objects.append(self.to_dict()) 
            print(f'\nobjects TM62 : {objects}') 
            t = objects[-1] 
            print(f'\nt TM64 : {t}') 
            rounds_obj = t['rounds'] 
            print(f'\nrounds TM66 : {rounds_obj}') 
            rounds = [] 
            for round in rounds_obj: 
                print(f'\nround TM69 : {round}') 
                print(f'\ntype(round) TM70 : {type(round)}') 
                # rounds.append(round.to_dict()) 
                rounds.append(round) 
            print(f'\nrounds TM73 : {rounds}') 
            objects[-1]['rounds'] = rounds 
            print(f'\nobjects TM75 : {objects}') 
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(objects, file) 

    ### 
    # def serialize_modified_object(self): 
    #     """ Abstract method for serialize the objects from the models. """ 
    #     if not self.check_if_json_empty(): 
    #         objects = self.get_registered() 
    #         # select the last tournament : 
    #         t_dict = objects[-1] 
    #         t_dict['rounds'].pop() 
    #         # print(f't_dict RM90 : {t_dict}') 
    #         t_dict['rounds'].append(self.to_dict()) 
    #         # print(f't_dict["rounds"] RM83 : {t_dict["rounds"]}') 
    #     else: 
    #         print('Erreur : le fichier tournaments ne peut pas être vide.') 
    #     with open(f"data/{self.table}.json", "w") as file: 
    #         json.dump(objects, file) 
    ### 


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
