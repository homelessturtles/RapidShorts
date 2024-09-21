from gtts import gTTS
import tempfile

def create_speech_buffer(speech, fname):
    tts = gTTS(text=speech, lang='en')
    tts.save(fname)

    