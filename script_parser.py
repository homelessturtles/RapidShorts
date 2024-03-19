mock_sample = ''
real_sample = "ChatCompletionMessage(content='Scene 1:\nKeywords: Busy schedule, meal prep\nNarrator: Are you struggling to lose weight due to a hectic schedule? Start by dedicating just a small amount of time each week to meal prep. It will help you stay on track and avoid unhealthy food choices.\n\nScene 2:\nKeywords: High-intensity workout, consistency\nNarrator: Incorporate high-intensity workouts into your routine to maximize fat burning in a short amount of time. Consistency is key, so aim to squeeze in quick but effective workouts whenever you can.\n\nScene 3:\nKeywords: Portion control, mindful eating\nNarrator: Practice portion control and mindful eating to avoid overeating and unnecessary weight gain. Being aware of what and how much you are consuming can make a big difference in achieving your weight loss goals.\n\nScene 4:\nKeywords: Support system, accountability\nNarrator: Surround yourself with a strong support system to hold you accountable and motivate you on your weight loss journey. Having friends or family members to cheer you on can make all the difference in staying committed and achieving lasting results.', role='assistant', function_call=None, tool_calls=None)"

def parse_script(scripttext):
    '''return keywords and narration for each scene respectively'''
    parsed_script = {'keywords': [], 'narration': []}
    
    keyword_lines = [x for x in scripttext.splitlines() if "Keywords" in x]
    keywords = [x.replace('Keywords: ', '') for x in keyword_lines]
    parsed_script['keywords'] = [x.rsplit(', ') for x in keywords]

    narration_lines = [x for x in scripttext.splitlines() if "Narrator" in x]
    parsed_script['narration'] = [x.replace('Narrator: ', '') for x in narration_lines]

    return parsed_script

