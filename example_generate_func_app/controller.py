import model

class FunctionGeneratorController:
    def __init__(self, view):
        self.view = view
    
    def generate_function(self):
        func_name, return_type, params = self.view.get_inputs()

        if not func_name or not return_type:
            self.view.show_output("// Please fill function name and return type.")
            return
        code = model.generate_c_function(func_name, return_type, params)
        self.view.show_output(code)