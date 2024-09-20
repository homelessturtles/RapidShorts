from gtts import gTTS
from moviepy.editor import AudioFileClip
import tempfile

def create_speech_buffer(speech, fname):
    tts = gTTS(text=speech, lang='en')
    tts.save(fname)

    