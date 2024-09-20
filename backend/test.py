import clips_gen
import script_gen
import vid_edit
import voice_gen
from uploadtest import upload_video, get_url
def test(prompt):
    scenes_dict = {}
    keywords = []
    narration_file_names = []

    scenes = script_gen.generate_script(prompt)
    print(scenes)

    i = 0
    for scene in scenes.values():
        keywords.append(scene['keyword'])
        tts = f'scene{i}.mp3'
        voice_gen.create_speech_buffer(scene['narration'], tts)
        narration_file_names.append(tts)
        i += 1

    j = 0
    vid_num = 1
    print(keywords)
    clips = clips_gen.get_scene_clips(keywords)
    for query in clips.values():
        item = {f'scene{j}': {
            'clips': [],
            'narration': narration_file_names[j]
        }}
        for clip in query:
            save_path = f'{vid_num}.mp4'
            url = clip
            clips_gen.download_video(url=url, save_path=save_path)
            item[f'scene{j}']['clips'].append(save_path)
            vid_num += 1
        scenes_dict.update(item)
        j += 1

    print(scenes_dict)
    final_vid = vid_edit.edit_clips(scenes_dict)
    temp_file = 'test_video.mp4'
    fname = 'finalvid.mp4'
    final_vid.write_videofile(temp_file, codec='libx264', fps=24)
    upload_video(temp_file, fname)
    return get_url(fname)

