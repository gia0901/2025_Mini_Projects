import tkinter as tk
from tkinter import font, colorchooser

class FormatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ctrl + V Formatter")

        self.applied_format = None

        # Default values
        self.formatting = {
            "bold": tk.BooleanVar(value=False),
            "italic": tk.BooleanVar(value=False),
            "underline": tk.BooleanVar(value=False),
            "font": tk.StringVar(value="Arial"),
            "size": tk.IntVar(value=12),
            "color": None   # RGB tuple
        }

        # Font Type entry
        tk.Label(root, text="Font:").grid(row=0, column=0, sticky=tk.W)
        fonts = list(font.families())
        fonts.sort()
        tk.OptionMenu(root, self.formatting["font"], *fonts).grid(row=0, column=1, sticky=tk.W)

        # Font Size (spin box)
        tk.Label(root, text="Font Size:").grid(row=1, column=0, sticky=tk.W)
        tk.Spinbox(root, from_=8, to=60, textvariable=self.formatting["size"]).grid(row=1, column=1, sticky=tk.W)

        # Font color
        tk.Button(root, text="Color:", command=self.pick_color).grid(row=2, column=0, columnspan=2, sticky=tk.W)

        # Font format
        tk.Checkbutton(root, text="Bold", variable=self.formatting["bold"]).grid(row=3, column=0, sticky=tk.W)
        tk.Checkbutton(root, text="Italic", variable=self.formatting["italic"]).grid(row=3, column=1, sticky=tk.W)
        tk.Checkbutton(root, text="Underline", variable=self.formatting["underline"]).grid(row=4, column=0, sticky=tk.W)

        # Apply button
        tk.Button(root, text="Apply", command=self.apply_format).grid(row=5, column=0, columnspan=2)

        # Guildline
        tk.Label(root, text="Press Ctrl + V to paste the content with this format.").grid(row=6, column=0, columnspan=2, sticky=tk.EW)


    def pick_color(self):
        color = colorchooser.askcolor()[0] # Return (r,g,b)
        self.formatting["color"] = tuple(map(int, color)) if color else None
    
    def get_formatting(self):
        return {
            "bold": self.formatting["bold"].get(),
            "italic": self.formatting["italic"].get(),
            "underline": self.formatting["underline"].get(),
            "font": self.formatting["font"].get(),
            "size": self.formatting["size"].get(),
            "color": self.formatting["color"]
        }

    def apply_format(self):
        self.applied_format = self.get_formatting()
        print("Format is applied!")
    
    def get_applied_format(self):
        return self.applied_format or self.get_formatting()
