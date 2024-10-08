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

# returns scenes in python dict format

def generate_script(topic):
    '''return generated script from prompt using OpenAI GPT-3.5'''

    prompt = """
    I need a script for short form video with 4 distinct scenes. Each scene should be related to the following topic: {topic}

    Each scene should have:
    - One word keyword summarizing the main element of the scene.
    - A brief narration for that scene.

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
