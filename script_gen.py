from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

sample_prompt = 'Create a video about a kid that wants to become a cowboy but his parents want himt to go to engineering school'


def format_sample_output(txt_output):
    with open(txt_output) as file:
        sample_output = file.readlines()
    return sample_output


def generate_script_mock(prompt):
    '''returns a pre defined generated script'''

    return f"prompt: {prompt}\nscript:{format_sample_output('script.txt')}"


def generate_script(prompt):
    '''return generated script from prompt using OpenAI GPT-3.5'''

    requirements = f"Create short form video script using the following requirements. {prompt} For each scene, specify ONE and ONLY ONE keyword describing the scene. USE THE FORMAT FOR EACH SCENE Keywords: [*Insert keywords*], Narrator: [*insert narration*]. Create 4 scenes."
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": requirements}
        ]
    )
    return completion.choices[0].message.content


def parse_script(script):
    scenes_dict = {}
    # Split the input string into scenes
    scenes = script.strip().split('\n\n')

    # Initialize lists to store narrations and keywords for each scene
    narrations = []
    keywords = []

    # Parse each scene to extract narration and keywords
    for scene in scenes:
        scene_lines = scene.split('\n')

        scene_narration = ""
        scene_keywords = ""

        # Iterate through the lines to find keywords and narration
        for line in scene_lines:
            if line.startswith("Keywords:"):
                scene_keywords = line.replace('Keywords: ', '').strip()
            elif line.startswith("Narrator:"):
                scene_narration = line.replace('Narrator: ', '').strip()
            else:
                continue

        # Append narration and keywords to the respective lists
        narrations.append(scene_narration)
        keywords.append(scene_keywords)

    for i, (narration, keyword) in enumerate(zip(narrations, keywords), start=1):
        item = {f'scene_{i}': {
            'keywords': keyword,
            'narration': narration
        }}
        scenes_dict.update(item)

    return scenes_dict
