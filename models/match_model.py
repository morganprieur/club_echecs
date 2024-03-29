
from .abstract_model import AbstractModel 


class Match_model(AbstractModel): 

    def __init__( 
        self, match: tuple 
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
        return f'([{self.player_1_id}, {self.player_1_score}], [{self.player_2_id},{self.player_2_score}])' 


    def to_dict(self): 
        return ([self.player_1_id, self.player_1_score], [self.player_2_id, self.player_2_score]) 

