import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import imageio
import os
from tools.variables import *


class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.video_source = "<video0>"
        self.vid = imageio.get_reader(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get_meta_data()['size'][0],
                                height=self.vid.get_meta_data()['size'][1])
        self.canvas.pack()

        self.btn_snapshot = tk.Button(window, text="Сделать снимок", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.save_snapshot_button = tk.Button(window, text="Сохранить снимок", width=50, command=self.save_snapshot)

        self.snapshot_image = None
        self.displaying_snapshot = False

        self.update()

        self.window.mainloop()

    def snapshot(self):
        try:
            self.snapshot_image = self.vid.get_next_data()
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.snapshot_image))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.displaying_snapshot = True
            self.btn_snapshot.pack_forget()
            self.save_snapshot_button.pack(anchor=tk.CENTER, expand=True)
        except Exception as e:
            print("Ошибка при захвате изображения:", e)

    def save_snapshot(self):
        if self.snapshot_image is not None:
            filename = simpledialog.askstring("Сохранить снимок", "Введите имя файла:")
            if filename:
                path = f"{FILE_FOLDER}/{filename}.jpg"
                Image.fromarray(self.snapshot_image).save(path)
                self.displaying_snapshot = False
                self.save_snapshot_button.pack_forget()
                self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        if not self.displaying_snapshot:
            try:
                frame = self.vid.get_next_data()
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            except Exception as e:
                print("Ошибка при обновлении кадра:", e)
        self.window.after(15, self.update)


# Создание окна и запуск приложения
if __name__ == '__main__':
    root = tk.Tk()
    app = CameraApp(root, "Tkinter и Камера")
