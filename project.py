
from controllers.main_controller import Main_controller 
from views.dashboard_view import Dashboard_view 
from views.report_view import Report_view 
from views.input_view import Input_view 
from datetime import datetime, date 



""" comment """ 
if __name__ == "__main__": 
    # now = datetime.now()  # comment 
    # today = date.today() 
    new_board = Dashboard_view() 
    # new_input_view = Input_view(now)  # comment 
    new_input_view = Input_view()  # comment 
    new_reporter = Report_view() 
    new_controller = Main_controller( 
        board=new_board, 
        in_view=new_input_view, 
        report_view=new_reporter, 
    ) 
    restart = True
    while restart: 
        restart = new_controller.start(True)
