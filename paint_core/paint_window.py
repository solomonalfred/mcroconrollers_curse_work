import os
import tkinter as tk
from tkinter import colorchooser, simpledialog
from PIL import Image, ImageDraw
from tools.variables import *


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Paint")

        self.color = 'black'
        self.brush_size = 2
        self.last_x = None
        self.last_y = None
        self.eraser_on = False
        self.canvas = tk.Canvas(root, bg='white', width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.setup_ui()
        self.setup_bindings()

        self.image = Image.new("RGB", (600, 400), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def setup_ui(self):
        self.toolbar = tk.Frame(self.root, bg='gray')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.pen_button = tk.Button(self.toolbar, text='Pen', command=self.use_pen)
        self.pen_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(self.toolbar, text='Eraser', command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        self.color_button = tk.Button(self.toolbar, text='Color', command=self.set_brush_color)
        self.color_button.pack(side=tk.LEFT)

        self.size_button = tk.Button(self.toolbar, text='Size', command=self.set_brush_size)
        self.size_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.toolbar, text='Save', command=self.save_image)
        self.save_button.pack(side=tk.LEFT)

    def setup_bindings(self):
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-1>', self.set_last_position)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def set_last_position(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        if self.last_x and self.last_y:
            color = 'white' if self.eraser_on else self.color
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=color, width=self.brush_size, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=color, width=self.brush_size)

        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x = None
        self.last_y = None

    def use_pen(self):
        self.eraser_on = False

    def use_eraser(self):
        self.eraser_on = True

    def set_brush_size(self):
        size = tk.simpledialog.askinteger("Brush size", "Enter brush size:", minvalue=1, maxvalue=50)
        if size:
            self.brush_size = size

    def set_brush_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color

    def save_image(self):
        if not os.path.exists(FILE_FOLDER):
            os.makedirs(FILE_FOLDER)

        file_name = simpledialog.askstring("File name", "Enter the file name:")
        if file_name:
            file_path = os.path.join(FILE_FOLDER, file_name + '.jpg')
            self.image.save(file_path, 'JPEG')

if __name__ == '__main__':
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
