import pyttsx3

def create_speech_file(speech):
    engine = pyttsx3.init()
    engine.save_to_file(speech, 'test.mp3')
    engine.runAndWait()


