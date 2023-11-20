import tkinter as tk
from tkinter import ttk, simpledialog
from PIL import Image, ImageTk
import cv2
import os
from tools.variables import *

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = ttk.Button(window, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.update()
        self.window.mainloop()

    def snapshot(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Предпросмотр снимка
                self.preview_window = tk.Toplevel(self.window)
                self.preview_window.title("Snapshot Preview")
                self.preview_canvas = tk.Canvas(self.preview_window, width=frame.shape[1], height=frame.shape[0])
                self.preview_canvas.pack()

                self.preview_photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.preview_canvas.create_image(0, 0, image=self.preview_photo, anchor=tk.NW)

                # Запрос имени файла для сохранения
                self.filename = simpledialog.askstring("Save Snapshot", "Enter filename (without extension):")
                if self.filename:
                    self.save_snapshot(frame)
                self.preview_window.destroy()

    def save_snapshot(self, frame):
        if not os.path.exists(FILE_FOLDER):
            os.makedirs(FILE_FOLDER)
        cv2.imwrite(f"{FILE_FOLDER}/{self.filename}.jpg", frame)

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(15, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

if __name__ == '__main__':
    root = tk.Tk()
    app = WebcamApp(root, "Tkinter and OpenCV")
