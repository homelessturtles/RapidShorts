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

def get_scene_clips(queries):
    '''get clips for keywords from all scenes'''
    scene_clips_info = {}
    for query in queries:
        scene_clips_info[query] = source_clips_pexley(query)

    return scene_clips_info

def download_video(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the local file in binary write mode and write the video data
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Video downloaded successfully.")
            return True
        else:
            print(f"Failed to download video. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error occurred while downloading video: {e}")
        return False


'''
example output

{'breakfast': [{'author': 'Pressmaster', 'vid_link': 'https://videos.pexels.com/video-files/3191902/3191902-hd_1920_1080_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/3191902/pictures/preview-0.jpg'}, {'author': 'Pressmaster', 'vid_link': 'https://videos.pexels.com/video-files/3115338/3115338-hd_1920_1080_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/3115338/pictures/preview-0.jpg'}, {'author': 'Monserrat Soldú', 'vid_link': 'https://videos.pexels.com/video-files/2959312/2959312-hd_1920_1080_30fps.mp4', 'img_link': 'https://images.pexels.com/videos/2959312/pictures/preview-0.jpg'}], 'excited': [{'author': 'Alexy Almond', 'vid_link': 'https://videos.pexels.com/video-files/3760881/3760881-hd_1920_1080_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/3760881/pictures/preview-0.jpg'}, {'author': 'Diva Plavalaguna', 'vid_link': 'https://videos.pexels.com/video-files/6194825/6194825-hd_1920_1080_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/6194825/pictures/preview-0.jpg'}, {'author': 'Diva Plavalaguna', 'vid_link': 'https://videos.pexels.com/video-files/6194810/6194810-hd_1280_720_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/6194810/pictures/preview-0.jpg'}], 'running': [{'author': 'Pressmaster', 'vid_link': 'https://videos.pexels.com/video-files/3125907/3125907-hd_1280_720_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/3125907/pictures/preview-0.jpg'}, {'author': 'Pressmaster', 'vid_link': 'https://videos.pexels.com/video-files/3209550/3209550-hd_1920_1080_25fps.mp4', 'img_link': 'https://images.pexels.com/videos/3209550/pictures/preview-0.jpg'}, {'author': 'fauxels', 'vid_link': 'https://videos.pexels.com/video-files/3048876/3048876-hd_1280_720_24fps.mp4', 'img_link': 'https://images.pexels.com/videos/3048876/pictures/preview-0.jpg'}]}

'''