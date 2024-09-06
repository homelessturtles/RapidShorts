from moviepy.editor import *
import soundfile as sf

# example format for video editing algorithm
scenes_dict = {
    'scene1': {'clips': ['Test_Assets/family_1.mp4', 'Test_Assets/family_2.mp4'], 'narration': 'Test_Assets/scene1.mp3'},
    'scene2': {'clips': ['Test_Assets/nature_1.mp4', 'Test_Assets/nature_2.mp4'], 'narration': 'Test_Assets/scene2.mp3'},
    'scene3': {'clips': ['Test_Assets/lions_1.mp4', 'Test_Assets/lions_2.mp4'], 'narration': 'Test_Assets/scene3.mp3'}
}

def edit_clips(scenes_dict):
    scenes = []

    for k, v in scenes_dict.items():
        clip_1 = VideoFileClip(scenes_dict[k]['clips'][0])
        clip_2 = VideoFileClip(scenes_dict[k]['clips'][1])
        narration = scenes_dict[k]['narration']
        audio_file = narration
        narration_length = audio_file.duration
        scenes.append(concatenate_clips(clip_1, clip_2,
                      narration_length, audio_file))

    final_edit = concatenate_videoclips(scenes, method='compose')
    return final_edit


def concatenate_clips(clip1, clip2, duration, narration):
    duration_clip1 = clip1.duration
    duration_clip2 = clip2.duration

    if duration >= duration_clip1 + duration_clip2:
        final_clip = concatenate_videoclips([clip1, clip2], method='compose')
    elif duration < duration_clip1:
        final_clip = clip1.subclip(0, duration)
    else:
        final_clip = concatenate_videoclips(
            [clip1, clip2.subclip(0, duration - duration_clip1)], method='compose')

    final_clip_w_audio = final_clip.set_audio(narration)

    return final_clip_w_audio


'''
testing
test_edit = edit_clips(scenes_dict)
test_edit.write_videofile('test_video.mp4', codec='libx264', fps=24)
'''
