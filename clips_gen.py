import requests
from dotenv import load_dotenv
import os
import json
from parse import search

load_dotenv()
pexels_key = os.getenv("PEXELS_API_KEY")
headers = {'Authorization': pexels_key}

def source_clips_pexley(query):
    '''make api call to pexley, return author and video clips'''

    clips = []
    response = requests.get(
        f'https://api.pexels.com/videos/search?query={query}', headers=headers).json()
    for video in response['videos']:
        author = video['user']['name']
        img_link = video['video_pictures'][0]['picture']
        for video_file in video['video_files']:
            if video_file['quality'] == 'hd':
                vid_link = video_file['link']
                break
        clips.append({'author':author, 'vid_link':vid_link, 'img_link': img_link})
    return clips[0:3]

