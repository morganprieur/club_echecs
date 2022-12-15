


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
round_table = db.table('round_table') 

# liste des matches 
# un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 
# un champ Date et heure de début 
# un champ Date et heure de fin, 
# --> automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. 
# Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.

class Round_model(): 

    def __init__(self, round_name, matches, start_datetime, end_datetime):  ### datetimes automatiques ### round_matches 
        self.round_name = round_name 
        self.matches = matches 
        self.start_datetime = start_datetime 
        self.end_datetime = end_datetime 
    

    def __str__(self):
        round_matchesList = f'' 
        for m in range(len(self.matches)): 
            round_matchesList += f' {str(self.matches[m])} \n' 

        return f'Nom du round : {self.round_name} \nListe des matches : \n{round_matchesList}début : {self.start_datetime} \nfin : {self.end_datetime}' 




    def serialize_round(rounds, matches):  # matches = serialized_matches 

        print(f'matches RM37 : {matches}') 
        print(f'matches RM38 : {type(matches)}') 

        print(f'type(rounds[0]) RM37 : {type(rounds[0])}') 

        serialized_rounds = [] 

        for r_obj in rounds: 
            print(f'rounds.index(r_obj) RM48 : {rounds.index(r_obj)}') 
            serialized_round = {
                'round_name': r_obj.round_name, 
                # 'round_matches': r_obj.round_matches, 
                # 'round_matches': r_obj.matches, 
                # 'round_matches': matches[rounds.index(r_obj)] if matches[rounds.index(r_obj)] != None else '',  # marche mais c'est pas ça qu'il faut... 
                'round_matches': matches, 
                'start_datetime': r_obj.start_datetime, 
                'end_datetime': r_obj.end_datetime 
            } 
            serialized_rounds.append(serialized_round) 
            print(f'serialized_round RM49 : {serialized_round}')         
            print(f'type(serialized_round["round_name"]) RM50 : {type(serialized_round["round_name"])}') 


        round_table.truncate() 
        # Register the serialized matches into the DB: 
        round_table.insert_multiple(serialized_rounds) 

        return serialized_rounds 


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

