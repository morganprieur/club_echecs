
from .abstract_model import AbstractModel 
from .player_model import Player_model 
import json 


class Match_model(AbstractModel): 
    
    def __init__( 
        self, match:tuple 
    ): 
        super().__init__('tournaments') 
        self.match = match 
        self.player_1 = self.match[0] 
        self.player_2 = self.match[1] 
        self.player_1_id = self.player_1[0] 
        self.player_2_id = self.player_2[0] 
        self.player_1_score = self.player_1[1] 
        self.player_2_score = self.player_2[1] 
        
    
    def __str__(self): 
        return f'{self.match}' 

     
    def to_dict(self): 
        # return {'match': self.match}
        # return (self[0].__str__(), self[1].__str__()) 
        # return ([self[0][0], self[0][1]], [self[1][0], self[1][1]]) 
        # return ([self.player_1[0], self.player_1[1]], [self.player_2[0], self.player_2[1]]) 
        return ([self.player_1_id, self.player_1_score], [self.player_2_id, self.player_2_score]) 
 



""" 
## TOURS / MATCHS
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, 
chacune contenant deux éléments : un joueur et un score. Les matchs doivent 
être stockés sous forme de liste dans l'instance du tour auquel ils 
appartiennent.
En plus de la liste des matchs, chaque instance du tour doit contenir un nom. 
Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit 
également contenir un champ Date et heure de début et un champ Date et heure 
de fin, qui doivent tous deux être automatiquement remplis lorsque l'utilisateur 
crée un tour et le marque comme terminé. 

## GÉNÉRATION DES PAIRES 
● Au début du premier tour, mélangez tous les joueurs de façon aléatoire.
● Chaque tour est généré dynamiquement en fonction des résultats des joueurs 
dans le tournoi en cours.
    ○ Triez tous les joueurs en fonction de leur nombre total de points 
    dans le tournoi.
    ○ Associez les joueurs dans l’ordre 
    (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4 et ainsi 
    de suite.)
    ○ Si plusieurs joueurs ont le même nombre de points, vous pouvez les 
    choisir de façon aléatoire.
    ○ Lors de la génération des paires, évitez de créer des matchs 
    identiques (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un 
    contre l’autre).
        ■ Par exemple, si le joueur 1 a déjà joué contre le joueur 2,
        associez-le plutôt au joueur 3.
● Mettez à jour les points de tous les joueurs après chaque tour et répétez 
le processus de triage et d’association jusqu'à ce que le tournoi soit 
terminé.
● Un tirage au sort des joueurs définira qui joue en blanc et qui joue en 
noir ; il n'est donc pas nécessaire de mettre en place un équilibrage des 
couleurs.
""" 
