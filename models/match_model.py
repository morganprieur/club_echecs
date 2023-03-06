


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
match_table = db.table('match') 


class Match_model(): 

    def __init__(self, match): 
        self.match = match 

    def __str__(self):  # , roundDicts 
        return f'Match : \n{self.match}\n' 


    def serialize_matches(matches): 
        print(f'type(matches[0]) MM21 : {type(matches[0])}') 
        print(f'matches[0] MM22 : {matches[0]}') 

        serialized_matches = [] 

        for m_obj in matches: 
            serialized_match = {
                'match': m_obj 
                # m_obj: matches[matches.index(m_obj)+1] 
            } 
            serialized_matches.append(serialized_match) 
            print(f'serialized_match TM32 : {serialized_match}')         
            print(f'type(serialized_match["match"]) MM33 : {type(serialized_match["match"])}') 

        return serialized_matches 

    
""" 
    Un match unique doit être stocké sous la forme d'un tuple 
    contenant deux listes, 
    chacune contenant deux éléments : 
    une référence à une instance de joueur et un score. 
    Les matchs multiples doivent être stockés sous forme de liste 
    sur l'instance du tour.
""" 

