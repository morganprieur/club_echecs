



from models.model import Tournament_model 


class Main_controller(): 
    
    def start(): 

        print('start main controller') 

        Tournament_model.instantiate_tournoi(Tournament_model) 
        Tournament_model.serialize_tournament(Tournament_model) 

        print(f'Tournament_model.tournament_x C17 : {Tournament_model.tournament_x}') 
        # print(f'type(Tournament_model.tournament_x) TM18 : {type(Tournament_model.tournament_x)}') 


    



