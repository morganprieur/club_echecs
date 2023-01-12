


from controllers.main_controller import Main_controller 
from views.report_view import Report_view 
from views.input_view import Input_view 
import os

# # TinyDB 
# from tinydb import TinyDB 
# db = TinyDB('db.json') 
# players_table = db.table('players') 

# # Dossier du projet 
# folder = os.path.dirname(__file__) 
 
# from prompt_toolkit import PromptSession 
# # to use prompt as an instance 
# session = PromptSession() 


if __name__ == '__main__': 

    # Input_view.print_input(Input_view)  # ok 
    Main_controller.tourn_stream(Main_controller) 
    
    Report_view.display_today_s_tournament(Report_view) 

    # Main_controller.start() 
