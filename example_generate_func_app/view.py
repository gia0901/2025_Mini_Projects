# view.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import pyperclip
import controller
class FunctionGeneratorView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("C/C++ Function Generator")
        self.root.geometry("700x500")
        self.style = ttk.Style("litera")  # Theme hiện đại

        # --- Frame nhập liệu chính ---
        input_frame = ttk.Frame(root, padding=10)
        input_frame.pack(fill=X)

        ttk.Label(input_frame, text="Function Name").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.func_name_entry = ttk.Entry(input_frame)
        self.func_name_entry.grid(row=0, column=1, sticky=EW, padx=5)

        ttk.Label(input_frame, text="Return Type").grid(row=1, column=0, sticky=W, padx=5)
        self.return_type_entry = ttk.Entry(input_frame)
        self.return_type_entry.grid(row=1, column=1, sticky=EW, padx=5)

        # --- Tham số ---
        self.param_frame = ttk.Labelframe(root, text="Parameters", padding=10)
        self.param_frame.pack(fill=X, padx=10, pady=10)
        self.param_entries = []
        self.add_param_row()

        self.add_btn = ttk.Button(self.param_frame, text="Add", command=self.add_param_row, bootstyle=SUCCESS)
        self.add_btn.pack(pady=5)

        # --- Button generate ---
        self.generate_btn = ttk.Button(root, text="Generate Function", bootstyle=PRIMARY)
        self.generate_btn.pack(pady=10)

        # --- Output ---
        self.output = tk.Text(root, height=10, wrap=WORD)
        self.output.pack(fill=BOTH, expand=True, padx=10)

        # --- Copy/Delete ---
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Copy", command=self.copy_output, bootstyle=INFO).pack(side=LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.clear_output, bootstyle=DANGER).pack(side=LEFT, padx=5)

    def add_param_row(self):
        row = ttk.Frame(self.param_frame)
        row.pack(fill=X, pady=2)
        pname_entry = ttk.Entry(row)
        pname_entry.pack(side=LEFT, padx=5)
        ptype_entry = ttk.Entry(row)
        ptype_entry.pack(side=LEFT, padx=5)
        self.param_entries.append((pname_entry, ptype_entry))

    def get_inputs(self):
        func_name = self.func_name_entry.get()
        return_type = self.return_type_entry.get()
        params = [(e1.get(), e2.get()) for e1, e2 in self.param_entries if e1.get() and e2.get()]
        return func_name, return_type, params

    def show_output(self, text):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)

    def copy_output(self):
        pyperclip.copy(self.output.get(1.0, tk.END).strip())

    def clear_output(self):
        self.output.delete(1.0, tk.END)

    # Trong class FunctionGeneratorView:
    def setup_controller(self, controller):
        self.controller = controller
        # Gán lại command cho nút sau khi controller đã có
        self.generate_btn.config(command=self.controller.generate_function)