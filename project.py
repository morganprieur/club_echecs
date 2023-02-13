
from controllers.main_controller import Main_controller 
from views.dashboard_view import Dashboard_view 
from views.report_view import Report_view 
from views.input_view import Input_view 



if __name__ == "__main__": 
    new_board = Dashboard_view() 
    new_input_view = Input_view() 
    new_reporter = Report_view() 
    new_controller = Main_controller( 
        board=new_board, 
        in_view=new_input_view, 
        report_view=new_reporter 
    ) 
    new_controller.start() 


