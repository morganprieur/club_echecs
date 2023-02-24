
from .abstract_model import AbstractModel 
# for tests : 
# from abstract_model import AbstractModel 

import json 


class Round_model(AbstractModel): 

    def __init__(self, id:int, round_name:str, tournament_id:int):  # , matches:list, start_datetime:str, end_datetime:str  ### datetimes automatiques ### round_matches 
        super().__init__('t_table') 
        self.id = id 
        self.round_name = round_name 
        # self.matches = matches 
        # self.start_datetime = start_datetime 
        # self.end_datetime = end_datetime 
        self.tournament_id = tournament_id 

    def __str__(self):
        # round_matchesList = f'' 
        # for m in range(len(self.matches)): 
        #     round_matchesList += f' {str(self.matches[m])} \n' 

        return f'ID du round : {self.id}, nom : {self.round_name}, tournament_id : {self.tournament_id}'  # \nListe des matches : \n{round_matchesList}début : {self.start_datetime} \nfin : {self.end_datetime}' 


    def to_dict(self): 
        return { 
            'id': self.id, 
            'round_name': self.round_name, 
            # 'tournament_id': self.tournament_id 
        } 

    
    def serialize(self): 
        """ Rewrite method for serialize the round objects into the tournament table. """ 
        # pass  
        print(f'self RM38 :{self}') 
        # print(f'self.table RM37 :{self.table}') 

        # if not self.check_if_json_empty('t_table'): 
        if not self.check_if_json_empty(): 
            # objects = self.get_registered('t_table') 
            objects = self.get_registered() 
            with open(f'tables/t_table.json', 'r') as file: 
                # print(len(objects)) 
                t_id = self.tournament_id-1 

                # if not objects[t_id]: 
                if t_id > len(objects): 
                    return False 
                else: 
                    t_obj = objects[t_id] 
                    # print(f't_id RM50 : {t_id}') 
                    t_obj['rounds'] = [] 
                    t_obj['rounds'].append(self.to_dict()) 
                    # print(f't_obj["rounds"] RM51 : {t_obj["rounds"]}') 
        else: 
            # objects = [] 
            print('Erreur : la table t_table ne peut pas être vide.') 
        # print(f't_obj RM57 : {t_obj}') 
        # print(f'objects[6] RM59 : {objects[6]}') 
        with open(f"tables/t_table.json", "w") as file: 
            json.dump(objects, file) 



if __name__ == "__main__": 
    new_round = { 
        'id': 1, 
        'round_name': 'round_220', 
        'tournament_id': 7 
    } 
    one_round = Round_model(**new_round) 
    print(f'new_round RM85 : {new_round}') 
    one_round.serialize() 




""" 
liste des matches 
un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 
un champ Date et heure de début 
un champ Date et heure de fin, 
--> automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. 
Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.
""" 

