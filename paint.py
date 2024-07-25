import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.color = 'black'
        self.brush_size = 5
        self.current_tool = 'free_draw'
        self.start_x = None
        self.start_y = None

        self.setup_ui()

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def setup_ui(self):
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        color_button = ttk.Button(toolbar, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        self.size_var = tk.IntVar(value=self.brush_size)
        size_spinbox = ttk.Spinbox(toolbar, from_=1, to=100, textvariable=self.size_var, command=self.change_brush_size)
        size_spinbox.pack(side=tk.LEFT)

        free_draw_button = ttk.Button(toolbar, text="Free Draw", command=lambda: self.change_tool('free_draw'))
        free_draw_button.pack(side=tk.LEFT)

        line_button = ttk.Button(toolbar, text="Line", command=lambda: self.change_tool('line'))
        line_button.pack(side=tk.LEFT)

        rect_button = ttk.Button(toolbar, text="Rectangle", command=lambda: self.change_tool('rectangle'))
        rect_button.pack(side=tk.LEFT)

        circle_button = ttk.Button(toolbar, text="Circle", command=lambda: self.change_tool('circle'))
        circle_button.pack(side=tk.LEFT)

        clear_button = ttk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def change_brush_size(self):
        self.brush_size = self.size_var.get()

    def change_tool(self, tool):
        self.current_tool = tool

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.current_tool == 'free_draw':
            self.canvas.create_line(event.x, event.y, event.x, event.y, fill=self.color, width=self.brush_size, capstyle=tk.ROUND, smooth=True)

    def on_drag(self, event):
        if self.current_tool == 'free_draw':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=self.brush_size, capstyle=tk.ROUND, smooth=True)
            self.start_x = event.x
            self.start_y = event.y

    def on_release(self, event):
        if self.current_tool == 'line':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=self.brush_size)
        elif self.current_tool == 'rectangle':
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=self.brush_size)
        elif self.current_tool == 'circle':
            x0, y0 = self.start_x, self.start_y
            x1, y1 = event.x, event.y
            r = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline=self.color, width=self.brush_size)

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
