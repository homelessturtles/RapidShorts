import pyttsx3


def create_speech_file(speech, name):
    engine = pyttsx3.init()
    engine.save_to_file(speech, f'{name}.mp3')
    engine.runAndWait()
