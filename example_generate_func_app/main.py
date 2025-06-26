# main.py
import tkinter as tk
from view import FunctionGeneratorView
from controller import FunctionGeneratorController

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionGeneratorView(root, controller=None)  # Controller tạm thời là None
    controller = FunctionGeneratorController(app)
    app.setup_controller(controller)  # Gán controller thực sự
    root.mainloop()
