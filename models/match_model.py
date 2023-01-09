


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

