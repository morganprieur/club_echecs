
from controllers.main_controller import Main_controller 
from controllers.register_controller import Register_controller 
from controllers.report_controller import Report_controller 
from views.dashboard_view import Dashboard_view 
from views.report_view import Report_view 
from views.input_view import Input_view 

""" Executes the program """ 
if __name__ == "__main__": 
    new_board = Dashboard_view() 
    new_input_view = Input_view() 
    new_reporter = Report_view() 
    new_register_controller = Register_controller(new_input_view, new_reporter)  # 
    new_report_controller = Report_controller(new_reporter)  # 
    new_controller = Main_controller( 
        board=new_board, 
        register_controller=new_register_controller, 
        report_controller=new_report_controller, 
        in_view=new_input_view, 
        report_view=new_reporter, 
    ) 
    restart = True
    while restart: 
        restart = new_controller.start(True)

