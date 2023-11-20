from gtts import gTTS
import os
from tools.variables import *


def text_to_speech(text, lang='ru'):
    tts = gTTS(text=text, lang=lang)
    tts.save(f"{FILE_FOLDER}/speech.mp3")
    os.system(f"mpg321 {FILE_FOLDER}/speech.mp3")
    os.remove(f"{FILE_FOLDER}/speech.mp3")


if __name__ == '__main__':
    text_to_speech("Привет, как дела? Делаем курсач по микроконтроллерам")