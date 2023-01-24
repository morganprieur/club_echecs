

class Tournament(): 

    def __init__(self, name, date, description) -> None: 
        self.name = name, 
        self.date = date, 
        self.description = description 

    def __str__(self) -> str: 
        return f'{self.name} {self.date} {self.description}' 
    
    def to_dict(self, exclude=None):
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and not callable(getattr(self, key))
            and isinstance(getattr(self, key), (str, int, float))
        } 
    
    def serialize_multi(self): 
        serialized_multi = [] 
        serialized = {} 
        serialized_multi.append(self.to_dict(**self.tournament)) 
    

class Input(): 

    def __init__(self) -> None: 
        pass 

    def input_tournament(self): 
        pass 


class Report(): 
    pass 


class controller(): 

    input = Input() 
    report = Report() 
    tournament = Tournament(name="name 01", date="20/01/23", description="Description 01") 

    def __init__(self, input: Input, report: Report, tournament) -> None: 
        self.input = input 
        self.report = report 
        self.tournament = None 
    

    







