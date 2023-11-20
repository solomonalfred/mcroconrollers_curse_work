import tkinter as tk
from tkinter import filedialog
from text_speech_core.text_speecher import text_to_speech
from web_core.webcam import WebcamApp
from paint_core.paint_window import PaintApp
from image_to_text_core.image_to_text import image_text_analysis


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        self.setup_ui()
        self.text_label = None
        self.speech_button = None

    def setup_ui(self):
        # Buttons for Paint, camera, and file selection
        tk.Button(self.root, text="Запустить Paint", command=self.open_paint).pack()
        tk.Button(self.root, text="Использовать камеру", command=self.open_webcam).pack()
        tk.Button(self.root, text="Выбрать фотографии", command=self.select_files).pack()

    def open_paint(self):
        paint_root = tk.Toplevel(self.root)
        PaintApp(paint_root)

    def open_webcam(self):
        webcam_root = tk.Toplevel(self.root)
        WebcamApp(webcam_root, "Камера")

    def select_files(self):
        filetypes = [('JPEG Files', '*.jpg'), ('All files', '*.*')]
        filenames = filedialog.askopenfilenames(title='Выберите фотографии', filetypes=filetypes)
        if filenames:
            self.process_images(filenames)

    def process_images(self, filenames):
        text = image_text_analysis(filenames, lang="ru")
        if self.text_label:
            self.text_label.destroy()
        self.text_label = tk.Label(self.root, text=text)
        self.text_label.pack()

        if self.speech_button:
            self.speech_button.destroy()
        self.speech_button = tk.Button(self.root, text="Озвучить текст", command=lambda: text_to_speech(text))
        self.speech_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

