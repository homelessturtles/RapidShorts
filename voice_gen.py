from gtts import gTTS
from moviepy.editor import AudioFileClip
import tempfile

def create_speech_buffer(speech):
    tts = gTTS(text=speech, lang='en')

    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        tts.save(temp_file.name)

    audio_clip = AudioFileClip(temp_file.name)

    temp_file.close()

    return audio_clip

    