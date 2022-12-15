


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
match_table = db.table('match') 


class Match_model(): 

    def __init__(self, match): 
        self.match = match 

    def __str__(self):  # , roundDicts        
        return f'Matches : \n{self.match}\n' 


    def serialize_match(matches): 

        print(f'type(matches[0]) MM109 : {type(matches[0])}') 

        serialized_matches = [] 

        for m_obj in matches: 
            serialized_match = {
                'match': m_obj.match 
            } 
            serialized_matches.append(serialized_match) 
            print(f'serialized_match TM32 : {serialized_match}')         
            print(f'type(serialized_match["match"]) MM30 : {type(serialized_match["match"])}') 


        # match_table.truncate() 
        # # Register the serialized matches into the DB: 
        # match_table.insert_multiple(serialized_matches) 

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

