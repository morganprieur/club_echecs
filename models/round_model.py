
from .abstract_model import AbstractModel 
from .match_model import Match_model 


class Round_model(AbstractModel): 

    def __init__( 
        self, 
        id: int, 
        round_name: str, 
        tournament_id: int, 
        start_datetime: str, 
        matches: list, 
        end_datetime: str 
    ): 
        super().__init__('tournaments') 
        self.id = id 
        self.round_name = round_name 
        self.start_datetime = start_datetime 
        self.end_datetime = end_datetime 
        self.tournament_id = tournament_id 
        if matches and isinstance(matches[0], tuple): 
            self.matches = [Match_model(*data) for data in matches] 
        else: 
            self.matches = matches 

    def __str__(self): 
        if self.end_datetime: 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        return f'''
            \nID du round : {self.id}, nom : {self.round_name}, 
            début : {self.start_datetime}, 
            fin : {end_datetime}, 
            tournament_id : {self.tournament_id}, 
            matches : {self.matches}''' 

    def to_dict(self): 
        if self.end_datetime: 
            end_datetime = self.end_datetime 
        else: 
            end_datetime = '' 
        round = { 
            'id': self.id, 
            'round_name': self.round_name, 
            'start_datetime': self.start_datetime, 
            'end_datetime': end_datetime, 
            'tournament_id': self.tournament_id, 
            'matches': self.matches 
        } 
        return round 
