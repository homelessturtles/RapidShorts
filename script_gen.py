from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

sample_prompt = 'Create a short form content video script for an ebike company that marketing a safe and comfortable bike aimed towards men in their 30s with young children.'


def format_sample_output(txt_output):
    with open(txt_output) as file:
        sample_output = file.readlines()
    return sample_output


def generate_script_mock(prompt):
    '''returns a pre defined generated script'''

    return f"prompt: {prompt}\nscript:{format_sample_output('script.txt')}"


def generate_script(prompt):
    '''return generated script from prompt using OpenAI GPT-3.5'''

    requirements = f"Create short form video script using the following requirements. {prompt} For each scene, specify one keyword describing the scene. USE THE FORMAT FOR EACH SCENE Keywords: [*Insert keywords*], Narrator: [*insert narration*]. Create a MAXIMUM of 4 scenes."
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": requirements}
        ]
    )
    return completion.choices[0].message
