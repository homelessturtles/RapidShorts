from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from string import Template

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


sample_prompt = 'how to make an iphone application'


def format_sample_output(txt_output):
    with open(txt_output) as file:
        sample_output = file.readlines()
    return sample_output


def generate_script_mock(prompt):
    '''returns a pre defined generated script'''

    return f"prompt: {prompt}\nscript:{format_sample_output('script.txt')}"


#returns scenes in json format
def generate_script(topic):
    '''return generated script from prompt using OpenAI GPT-3.5'''

    prompt = """
    I need a list of 4 distinct scenes. Each scene should be related to the following topic: {topic}

    Each scene should have:
    - A keyword summarizing the main element of the scene.
    - A brief narration describing the scene.

    Please return the output in the following JSON format:

    {{
    "Scene 1": {{
        "keyword": "Keyword 1",
        "narration": "Narration for scene 1."
    }},
    "Scene 2": {{
        "keyword": "Keyword 2",
        "narration": "Narration for scene 2."
    }},
    "Scene 3": {{
        "keyword": "Keyword 3",
        "narration": "Narration for scene 3."
    }},
    "Scene 4": {{
        "keyword": "Keyword 4",
        "narration": "Narration for scene 4."
    }}
    }}
    """.format(topic=topic)

    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return json.loads(completion.choices[0].message.content)


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


