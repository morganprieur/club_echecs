
from .abstract_model import AbstractModel 
from .player_model import Player_model 
from .round_model import Round_model 
from .match_model import Match_model 

import json 


class Tournament_model(AbstractModel): 

    def __init__( 
        self, id: int, 
        name: str, 
        site: str, 
        start_date: str, 
        end_date: str, 
        rounds_left: int, 
        players: list, 
        rounds: list, 
        description: str 
    ): 
        super().__init__('tournaments') 
        self.id = id 
        self.name = name 
        self.site = site 
        self.start_date = start_date 
        self.end_date = end_date 
        self.rounds_left = rounds_left 
        if players and isinstance(players[0], dict): 
            self.players = [Player_model(**data) for data in players] 
        else: 
            self.players = players 
        if rounds and isinstance(rounds[0], dict): 
            self.rounds = [Round_model(**data) for data in rounds] 
        else: 
            self.rounds = rounds 
        self.description = description 

    def __str__(self): 
        return (f'''
            \n{self.id}, {self.name}, {self.site}, 
            {self.start_date}, 
            {self.end_date}, 
            nombre de rounds : {self.rounds_left}, 
            joueurs : {self.players} 
            rounds : \n{self.rounds}, 
            {self.description}''') 

    def to_dict(self): 
        player_ids = [player for player in self.players] 
        return { 
            'id': self.id, 
            'name': self.name, 
            'site': self.site, 
            'start_date': self.start_date, 
            'end_date': self.end_date, 
            'rounds_left': self.rounds_left, 
            'players': player_ids, 
            'rounds': self.rounds, 
            'description': self.description 
        } 

    def serialize_object(self, new):
        """ Abstract method to serialize the object 
            Args:
                new (boolean): if the object is new: True, 
                if the data modifies the last entity into the json: False. 
        """ 
        t_dicts = self.get_registered_dict('tournaments') 
        if not new: 
            t_dicts.pop() 
        new_tournament_dict = self.to_dict() 

        new_rounds_list = [] 
        for new_round in new_tournament_dict['rounds']: 
            # print(f'\ntype(new_round) TM76 : {type(new_round)}') 
            new_round_dict = Round_model.to_dict(new_round) 
            # print(f'\ntype(new_round_dict) TM78 : {type(new_round_dict)}') 

            new_matches_list = [] 
            for new_match in new_round_dict['matches']: 
                if new_match and isinstance(new_match, Match_model): 
                    # print('\nYes, new_match -> object') 
                    new_match_tuple = Match_model.to_dict(new_match) 
                else: 
                    # print(f'\nNo, type(new_match) : {type(new_match)}') 
                    new_match_tuple = new_match 

                new_matches_list.append(new_match_tuple) 

            new_round_dict['matches'] = new_matches_list 
            new_rounds_list.append(new_round_dict) 

            new_tournament_dict['rounds'] = new_rounds_list 
        t_dicts.append(new_tournament_dict) 

        with open(f"data/{self.table}.json", "w") as file: 
            json.dump(t_dicts, file, indent=4) 
        return True 

