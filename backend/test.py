import clips_gen
import script_gen
import vid_edit
import voice_gen

sample_prompt = 'how to cut hair'

scenes_dict = {
    
}

keywords = []
narration_file_names = []

script = script_gen.generate_script(sample_prompt)
print(script)
scenes = script_gen.parse_script(script)
print(scenes)

i=0
for scene in scenes.values():
    keywords.append(scene['keywords'])
    voice_gen.create_speech_buffer(scene['narration'])
    narration_file_names.append(f'scene{i}.mp3')
    i+=1

j=0
vid_num = 1
clips = clips_gen.get_scene_clips(keywords)
for query in clips.values():
    item = {f'scene{j}': {
        'clips': [],
        'narration': narration_file_names[j]
    }}
    for clip in query:
        save_path = f'{vid_num}.mp4'
        url = clip['vid_link']
        clips_gen.download_video(url=url, save_path=save_path)
        item[f'scene{j}']['clips'].append(save_path)
        vid_num+=1
    scenes_dict.update(item)
    j+=1

print(scenes_dict)
final_vid = vid_edit.edit_clips(scenes_dict)
final_vid.write_videofile('test_video.mp4', codec='libx264', fps=24)