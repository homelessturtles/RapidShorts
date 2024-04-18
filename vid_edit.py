from moviepy.editor import *
from mutagen.mp3 import MP3

scenes_dict = {
    'scene1': {'clips: []'}
}

def get_audio_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None
    
def trim_clips(clips_dict): pass
