
from .abstract_model import AbstractModel 
import json 


class Match_model(AbstractModel): 

    def __init__( 
        self, player_1: list, player_2: list 
    ): 
        super().__init__('tournaments') 
        self.player_1 = player_1 
        self.player_2 = player_2 
        # self.match = match 
        # self.round_id = round_id 
        self.match = tuple(self.player_1, self.player_2) 
        # self.id_joueur_1 = id_joueur_1 
        # self.score_joueur_1 = score_joueur_1 
        # self.id_joueur_2 = id_joueur_2 
        # self.score_joueur_2 = score_joueur_2 

        # player_1 = [self.id_joueur_1, self.score_joueur_1] 
        # player_2 = [self.id_joueur_2, self.score_joueur_2] 

        # self.match = (self.player_1, self.player_2) 
        # self.match = ([self.id_joueur_1, self.score_joueur_1], [self.id_joueur_2, self.score_joueur_2]) 
        # print(f'self.match MM21 : {self.match}') 

    def __str__(self): 
        # match1 = self.player_1.strip("'") 
        # match2 = self.player_2.strip("'") 
        # match = (match1, match2) 
        # print(f'type(self.match) MM22 : {type(self.match)}')  # tuple ok 
        return f'{(self.player_1, self.player_2)}' 

    """ comment """ 
    def to_dict(self): 
        return {"match": (self.player_1, self.player_2)} 
        # pass 

    """ comment """ 
    def serialize_object(self, new): 
        """ Rewrite method for serialize the match objects into the tournament file 
            when adding a new match.""" 
        if not self.check_if_json_empty(): 
            # Get all the data from the tournaments file: 
            tournaments = self.get_registered() 
            # Get the current_tournament 
            # current_tournament = objects.pop() 
            current_tournament = tournaments[-1] 
            print(f'current_tournament MM44 : {current_tournament}') 
            # Get the rounds from the current_tournament 
            rounds = current_tournament['rounds'] 
            print(f'type(round_id) MM42 : {type(self.round_id)}')  
            print(f'type(round_id) MM42 : {int(self.round_id)}')  
            r_id = int(self.round_id) - 1 
            if r_id > len(rounds): 
                return False 
            else: 
                # Get the round with the match.round_id 
                current_round = rounds[r_id] 
                print(f'current_round MM53 : {current_round}') 

                if 'matches' not in current_round.keys(): 
                    current_round['matches'] = [] 
                else: 
                    if new == False: 
                        current_round['matches'] = current_round['matches'].pop() 
                    current_round['matches'].append(self.match) 

                print(f'current_round MM59 : {current_round}') 
                # print(f'current_tournament MM60 : {current_tournament}') 
        else: 
            print('Erreur : la table tournaments ne peut pas être vide.') 
        with open(f'data/{self.table}.json', 'w') as file: 
            json.dump(tournaments, file) 


    # """ comment """ 
    # def serialize_new_object(self): 
    #     """ Rewrite method for serialize the match objects into the tournament file 
    #         when adding a new match.""" 
    #     if not self.check_if_json_empty(): 
    #         # Get all the data from the tournaments file: 
    #         tournaments = self.get_registered() 
    #         # Get the current_tournament 
    #         # current_tournament = objects.pop() 
    #         current_tournament = tournaments[-1] 
    #         print(f'current_tournament MM44 : {current_tournament}') 
    #         # Get the rounds from the current_tournament 
    #         rounds = current_tournament['rounds'] 
    #         print(f'type(round_id) MM42 : {type(self.round_id)}')  
    #         print(f'type(round_id) MM42 : {int(self.round_id)}')  
    #         r_id = int(self.round_id) - 1 
    #         if r_id > len(rounds): 
    #             return False 
    #         else: 
    #             # Get the round with the match.round_id 
    #             current_round = rounds[r_id] 
    #             print(f'current_round MM53 : {current_round}') 

    #             if 'matches' not in current_round.keys(): 
    #                 current_round['matches'] = [] 
    #             else: 
    #                 current_round['matches'].append(self.match) 

    #             # print(f'current_round MM59 : {current_round}') 
    #             # print(f'current_tournament MM60 : {current_tournament}') 
    #     else: 
    #         print('Erreur : la table tournaments ne peut pas être vide.') 
    #     with open(f'data/{self.table}.json', 'w') as file: 
    #         json.dump(tournaments, file) 


""" 
## TOURS / MATCHS
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous forme de liste dans l'instance du tour auquel ils appartiennent.
En plus de la liste des matchs, chaque instance du tour doit contenir un nom. 
Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. 

## GÉNÉRATION DES PAIRES
● Au début du premier tour, mélangez tous les joueurs de façon aléatoire.
● Chaque tour est généré dynamiquement en fonction des résultats des joueurs dans le tournoi en cours.
○ Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
○ Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4 et ainsi de suite.)
○ Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
○ Lors de la génération des paires, évitez de créer des matchs identiques (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
■ Par exemple, si le joueur 1 a déjà joué contre le joueur 2,
associez-le plutôt au joueur 3.
● Mettez à jour les points de tous les joueurs après chaque tour et répétez le processus de triage et d’association jusqu'à ce que le tournoi soit terminé.
● Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ; il n'est donc pas nécessaire de mettre en place un équilibrage des couleurs.
""" 
