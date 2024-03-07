import requests
from dotenv import load_dotenv
import os
import json

mock_sample = ''
real_sample = "ChatCompletionMessage(content='Scene 1:\nKeywords: Busy schedule, meal prep\nNarrator: Are you struggling to lose weight due to a hectic schedule? Start by dedicating just a small amount of time each week to meal prep. It will help you stay on track and avoid unhealthy food choices.\n\nScene 2:\nKeywords: High-intensity workout, consistency\nNarrator: Incorporate high-intensity workouts into your routine to maximize fat burning in a short amount of time. Consistency is key, so aim to squeeze in quick but effective workouts whenever you can.\n\nScene 3:\nKeywords: Portion control, mindful eating\nNarrator: Practice portion control and mindful eating to avoid overeating and unnecessary weight gain. Being aware of what and how much you are consuming can make a big difference in achieving your weight loss goals.\n\nScene 4:\nKeywords: Support system, accountability\nNarrator: Surround yourself with a strong support system to hold you accountable and motivate you on your weight loss journey. Having friends or family members to cheer you on can make all the difference in staying committed and achieving lasting results.', role='assistant', function_call=None, tool_calls=None)"

load_dotenv()
pexels_key = os.getenv("PEXELS_API_KEY")
headers = {'Authorization': pexels_key}


def parse_script(scripttext):
    '''create map for each scene and its corresponding keywords'''


def source_clips_pexley(query):
    '''make api call to pexley, return author and video clips'''
    clips = []
    response = requests.get(
        f'https://api.pexels.com/videos/search?query={query}', headers=headers).json()
    for video in response['videos']:
        author = video['user']['name']
        for video_file in video['video_files']:
            if video_file['quality'] == 'hd':
                link = video_file['link']
                break
        clips.append({'author':author, 'link':link})
    return clips

for clip in source_clips_pexley('rocket ship'):
    print(clip)