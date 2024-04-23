from moviepy.editor import *
import soundfile as sf

scenes_dict = {
    'scene1': {'clips': ['Test_Assets/family_1.mp4', 'Test_Assets/family_2.mp4'], 'narration': 'Test_Assets/scene1.mp3'},
    'scene2': {'clips': ['Test_Assets/nature_1.mp4', 'Test_Assets/nature_2.mp4'], 'narration': 'Test_Assets/scene2.mp3'},
    'scene3': {'clips': ['Test_Assets/lions_1.mp4', 'Test_Assets/lions_2.mp4'], 'narration': 'Test_Assets/scene3.mp3'}
}

def get_audio_length(filename):
    try:
        audio_data, sample_rate = sf.read(filename)
        length_in_seconds = len(audio_data) / sample_rate
        return length_in_seconds
    except Exception as e:
        print("Error:", e)
        return None
    
def edit_clips(scenes_dict): 
    for k,v in scenes_dict:
        clip_1 = VideoFileClip(scenes_dict[k]['clips'][0])
        clip_2 = VideoFileClip(scenes_dict[k]['clips'][1])
        narration = scenes_dict[k]['narration']
        narration_length = get_audio_length(narration)


def concatenate_clips(clip1, clip2, duration):
    duration_clip1 = clip1.duration
    duration_clip2 = clip2.duration

    if duration >= duration_clip1 + duration_clip2:
        final_clip = concatenate_videoclips([clip1, clip2])
    elif duration < duration_clip1:
        final_clip = clip1.subclip(0, duration)
    else:
        final_clip = concatenate_videoclips([clip1, clip2.subclip(0, duration - duration_clip1)])

    return final_clip

clip1 = VideoFileClip(scenes_dict['scene1']['clips'][0])
clip2 = VideoFileClip(scenes_dict['scene1']['clips'][1])
scene1_audio_length = get_audio_length('Test_Assets/scene1.mp3')
test = concatenate_clips(clip1, clip2, scene1_audio_length)
test.write_videofile('test_video.mp4', codec='libx264', fps=24)

clip1.close()
clip2.close()

