
# from .abstract_model import AbstractModel  
# for tests : 
from models.abstract_model import AbstractModel 

import json 


# class Player(Persist_entity): 
class Player_model(AbstractModel): 

    def __init__( 
            self, 
            id:int, 
            lastname:str, 
            firstname:str, 
            ine:str,  # Identifiant National d'Echecs 
            birthdate: str, 
            local_score: float, 
            global_score: float 
        ): 
        super().__init__('players') 
        self.id = id  
        self.lastname = lastname  
        self.firstname = firstname 
        self.ine = ine 
        self.birthdate = birthdate 
        self.local_score = local_score 
        self.global_score = global_score 
        # players.append(self)   # pas bonnes pratiques 

    def __str__(self): 
        return f'\nJoueur {self.id} : {self.firstname} {self.lastname}, INE {self.ine} date de naissance : {self.birthdate}, score dans ce tournoi : {self.local_score}, score global : {self.global_score}.' 


    def to_dict(self): 
        return { 
            'id': self.id, 
            'lastname': self.lastname, 
            'firstname': self.firstname, 
            'ine': self.ine, 
            'birthdate': self.birthdate, 
            'local_score': self.local_score, 
            'global_score': self.global_score 
        } 

    """ comment """ # à vérifier 
    def serialize_object(self, new=True): 
    #     # return super().serialize_object(new) 
    #     # self -> score et id d'1 joueur 
        # print(f'dir(self) PM50 : {dir(self)}') 
        # print(f'self.table PM51 : {str(self.table)}') ### à remplacer dans PM53 et PM55 
    
    # Get the list of registered players : 
    #     # if not self.check_if_json_empty('players'): 
        if not self.check_if_json_empty(self.table): 
            # print(f'\ntype(t_dicts) TM76 : {type(t_dicts)}') 
            # Get the tournaments from the JSON file 
            p_dicts = self.get_registered_dict(self.table) 
            # print(f'\np_dicts PM59 : {p_dicts}') # list of dicts 
            
            new_players = [] 
            # if we must replace a registered player 
            if not new: 
                # Get the player's id from sent data 
                new_player_id = int(self.id) 
                print(f'\nnew_player_id PM66 : {new_player_id}') # ok 
                # print(f'\ntype(new_player_id) PM67 : {type(new_player_id)}') 
                # new players to register 
                # new_p_dicts = [] 
                # Get the sent players from the JSON file 
                for p in p_dicts: 
                    if p['id'] == new_player_id: 
                        registered_player = p_dicts.pop(p_dicts.index(p)) 
                        # print(f'registered_player PM74 : {registered_player}') 
                        # print(f'p_dicts PM72 : {p_dicts}') 

                        # Replace the registered local score with the new local score 
                        registered_player['local_score'] = self.local_score 
                        print(f'registered_player PM80 : {registered_player}') 

                        # Put again the players into the new_players list 
                        new_players=p_dicts 
                        new_players.append(registered_player) 
            print(f'\nnew_players PM85 : {new_players}') 
        
        else: 
            print('Erreur : le fichier tournaments ne peut pas être vide.') 
        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(new_players, file, indent=4) 



    #         if not new: 
    #             # Get the players' data from the registered 
    #             for p in p_dicts: 
    #                 # print(f'p PM66 : {p}') 
    #                 # player = p_dicts[new_player_id-1] 
    #                 # player = p_dicts['player'] where p_dicts['id'] = new_player_id 
    #                 # if "d" in dict.keys(): 
    #                 if "id" in p.keys(): 
    #                     print('yes') 
    #                     if p['id'] == int(new_player_id): 
    #                         p_dict_player = p 
    #                         print(f'p PM74 : {p}')  
    #             # Replace the player's local_score from the registered players with the sent local_score 
    #                         p['local_score'] = self.local_score 
                    
        
    #                 else: 
    #                     print('Erreur : le fichier tournaments ne peut pas être vide.') 
    #                 with open(f"data/{self.table}.json", "w") as file: 
    #                     json.dump(p, file, indent=4) 
                


    #             # last_t_dict = t_dicts.pop() 
    #             # print(f'\nt_dicts TM88 : {t_dicts}')  # ok 
    #             # print(f'\nlast_t_dict TM89 : {last_t_dict}')  ### 
    #             pass # TODO 

        #     """ 
        #     last_tournament_dict = self.to_dict() 
        #     print(f"\nlast_tournament_dict['rounds'][0].matches[0].__str__() TM93 : {last_tournament_dict['rounds'][0].matches[0].__str__()}")  ### 

        #     last_rounds_list = [] 
        #     for last_round_obj in last_tournament_dict['rounds']: 
        #         last_round_dict = Round_model.to_dict(last_round_obj) 
        #         print(f"\nlast_round_dict['rounds'][0]['matches'][0] TM98 : {last_round_dict['matches'][0]}") # [2, 0.5], [3, 0.5] ok 

        #         last_matches_list = [] 
        #         for last_match_obj in last_round_dict['matches']: 
        #             print(f'\nlast_match_obj.__str__() TM102 : {last_match_obj.__str__()}')  ### 
        #             last_match_dict = Match_model.to_dict(last_match_obj) ### 
        #             print(f'\nlast_match_dict TM104 : {last_match_dict}')  ### 

        #             last_matches_list.append(last_match_dict) 
        #         last_round_dict['matches'] = last_matches_list 

        #         last_rounds_list.append(last_round_dict) 
        #     last_tournament_dict['rounds'] = last_rounds_list 

        #     t_dicts.append(last_tournament_dict) 
        #     print(f't_dicts TM109 : {t_dicts}') 
                
        # else: 
        #     print('Erreur : le fichier tournaments ne peut pas être vide.') 
        # with open(f"data/{self.table}.json", "w") as file: 
        #     json.dump(t_dicts, file, indent=4) 
        #     """ 

""" Enoncé : 
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
    



