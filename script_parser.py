import re

mock_sample = ''
scenes_info = 'Scene 1 Keywords: Productivity, Focus Narrator: "Feeling scatterbrained and lacking focus? Say goodbye to distractions and hello to enhanced productivity with our mushroom supplement." Scene 2 Keywords: Energy, Clarity Narrator: "Watch as your energy levels soar and your mind gains crystal-clear clarity with our powerful mushroom blend." Scene 3 Keywords: Natural, Boost Narrator: "Experience a natural boost in productivity and focus, without the crash or jitters that come with synthetic alternatives." Scene 4 Keywords: Success, Results Narrator: "Unlock your full potential and achieve success in every aspect of your life, thanks to the incredible results of our mushroom supplement.'


def parse_script(scripttext):
    '''return keywords and narration for each scene respectively'''

    scripts = scripttext.split('\n')
    scenes_dict = {'keywords': [], 'narrations': []}

    for script in scripts:
        keywords = re.findall("(?<=Keywords: )(.*?)(?= Narrator)", script)
        narrations = re.findall("(?<=Narrator: )(.*?)(?= Scene)", script)
        scenes_dict['keywords'].append(keywords)
        scenes_dict['narrations'].append(narrations)

    return scenes_dict
