


# # TinyDB 
from tinydb import TinyDB 
db = TinyDB('db.json') 
round_table = db.table('round_table') 
from tinydb.operations import add 


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




    def serialize_round(round, matches):  # matches = serialized_matches 

        print(f'matches RM37 : {matches}') 
        print(f'matches RM38 : {type(matches)}') 

        print(f'type(round) RM37 : {type(round)}') 

        serialized_round = {
            'round_name': round.round_name, 
            'round_matches': matches, 
            'start_datetime': round.start_datetime, 
            'end_datetime': round.end_datetime 
        } 
        print(f'serialized_round RM49 : {serialized_round}')         
        print(f'type(serialized_round["round_name"]) RM50 : {type(serialized_round["round_name"])}') 


        # round_table.truncate() 
        # Register the serialized matches into the DB: 
        # round_table.insert_multiple(serialized_rounds) 

        # round_table.insert(serialized_round) 
        
        # db.update(delete('key1'), User.name == 'John') 
        # db.upsert(Document({'name': 'John', 'logged-in': True}, doc_id=12)) 
        # round_table.update(add(1), round_table.end_datetime == 'John') 
        # db.get(User.name == 'John') 
        print(len(round_table)) 
        # r_table = round_table.all() 
        r_table = round_table.all() 
        # db.get(round_table.round_name=='round 2') 
        for i in r_table: 
            for key, value in i.items(): 
                if value=='round 2': 
                    # print(key, value) 
                    print(f'i : {i}') 
        # print(f'r_table : {r_table}') 
        # round_table.update(round_table({'end_datetime': '2022-12-15 18:28'}, doc_id=1)) 

        return serialized_round 


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

