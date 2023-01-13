
# model.py
class MyModel:
    def method_to_call(self):
        # model logic
        return result

# controller.py
from model import MyModel

class MyController:
    def call_model_method(self):
        model = MyModel()
        result = model.method_to_call()
        # Do something with the result
