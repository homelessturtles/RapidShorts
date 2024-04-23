import pyttsx3

def create_speech_file(speech, name):
    engine = pyttsx3.init()
    engine.save_to_file(speech, f'{name}.mp3')
    engine.runAndWait()


create_speech_file('Feeling scatterbrained and lacking focus? Say goodbye to distractions and hello to enhanced productivity with our mushroom supplement.', 'scene1')

create_speech_file('Watch as your energy levels soar and your mind gains crystal-clear clarity with our powerful mushroom blend.', 'scene2')

create_speech_file('Experience a natural boost in productivity and focus, without the crash or jitters that come with synthetic alternatives.', 'scene3')



