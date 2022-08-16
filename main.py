'''
The main class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
import py5
from extraFeature import drawFeature
from eyebrows import drawEyebrows
from face import drawFace
from eyes import drawEyes
from mouth import drawMouth
from extraFeature import drawFeature
from fuzzyLogic import findEmotionalState
# from gui import getArousal, getValence

#dictionaries to store emotions and their valence & arousal
emotionValence = {"Adventurous": 0.49, "Afraid": -0.12, "Alarmed": -0.08, "Ambitious": 0.45, "Amorous": 0.85, "Amused": 0.55, "Angry": -0.4, "Annoyed": -0.45, "Anxious": -0.725, "Apathetic": -0.2, "Aroused": 0.36, "Ashamed": -0.45, "Astonished": 0.42, "At Ease": 0.75, "Attentive": 0.49, "Bellicose": -0.12, "Bitter": -0.8, "Bored": -0.35, "Compassionate": 0.38, "Conceited": 0.19, "Confident": 0.51, "Conscientious": 0.32, "Contemplative": 0.59, "Contemptuous": -0.58, "Content": 0.81, "Convinced": 0.42, "Courageous": 0.9, "Defiant": -0.62, "Dejected": -0.51, "Delighted": 0.89, "Depressed": -0.81, "Desperate": -0.8, "Despondent": -0.567, "Determined": 0.725, "Disappointed": -0.8, "Discontented": -0.625, "Disgusted": -0.66, "Dissatisfied": -0.6, "Distressed": -0.7, "Distrustful": -0.48, "Doubtful": -0.275, "Droopy": -0.32, "Embarassed": -0.31, "Enraged": -0.18, "Enthusiastic": 0.5, "Envious": -0.28, "Excited": 0.7, "Expectant": 0.32, "Feel Guilt": -0.4, "Feel Well": 0.91, "Feeling Superior": 0.325, "Friendly": 0.75, "Frustrated": -0.6, "Glad": 0.95, "Gloomy": -0.86, "Happy": 0.9, "Hateful": -0.58, "Hesitant": -0.31, "Hopeful": 0.61, "Hostile": -0.28, "Impatient": -0.05, "Impressed": 0.39, "Indignant": -0.25, "Insulted": -0.725, "Interested": 0.65, "Jealous": -0.06, "Joyous": 0.95, "Languid": -0.22, "Light Hearted": 0.4, "Loathing": -0.8, "Longing": 0.22, "Lusting": 0.22, "Melancholic": -0.66, "Miserable": -0.925, "Passionate": 0.32, "Peaceful": 0.55, "Pensive": 0.125, "Pleased": 0.89, "Polite": 0.39, "Relaxed": 0.72, "Reverent": 0.31, "Sad": -0.825, "Satisfied": 0.78, "Selfconfident": 0.81, "Serene": 0.85, "Serious": 0.21, "Sleepy": 0.125, "Solemn": 0.81, "Startled": -0.925, "Suspicious": -0.32, "Taken Aback": -0.4, "Tense": -0.04, "Tired": -0.02, "Triumphant": 0.6, "Uncomfortable": -0.675, "Wavering": -0.6, "Worried": -0.06}
emotionArousal = {"Adventurous": 0.91, "Afraid": 0.79, "Alarmed": 0.89, "Ambitious": 0.65, "Amorous": -0.15, "Amused": 0.2, "Angry": 0.79, "Annoyed": 0.65, "Anxious": -0.8, "Apathetic": -0.11, "Aroused": 0.92, "Ashamed": -0.5, "Astonished": 0.79, "At Ease": -0.6, "Attentive": -0.48, "Bellicose": 0.85, "Bitter": 0.26, "Bored": -0.725, "Compassionate": -0.925, "Conceited": 0.66, "Confident": -0.2, "Conscientious": -0.8, "Contemplative": -0.6, "Contemptuous": 0.66, "Content": -0.59, "Convinced": 0.42, "Courageous": 0.59, "Defiant": 0.725, "Dejected": -0.86, "Delighted": 0.35, "Depressed": -0.46, "Desperate": -0.5, "Despondent": -0.425, "Determined": 0.26, "Disappointed": -0.04, "Discontented": 0.32, "Disgusted": 0.49, "Dissatisfied": -0.175, "Distressed": 0.55, "Distrustful": 0.1, "Doubtful": -0.95, "Droopy": -0.925, "Embarassed": -0.6, "Enraged": 0.72, "Enthusiastic": 0.32, "Envious": 0.82, "Excited": 0.725, "Expectant": 0.6, "Feel Guilt": -0.425, "Feel Well": -0.8, "Feeling Superior": 0.55, "Friendly": -0.6, "Frustrated": 0.39, "Glad": -0.15, "Gloomy": -0.48, "Happy": 0.25, "Hateful": 0.85, "Hesitant": -0.725, "Hopeful": -0.3, "Hostile": 0.85, "Impatient": 0.3, "Impressed": -0.18, "Indignant": 0.45, "Insulted": 0.2, "Interested": 0.3, "Jealous": 0.56, "Joyous": 0.25, "Languid": -0.5, "Light Hearted": 0.3, "Loathing": 0.425, "Longing": -0.42, "Lusting": 0.85, "Melancholic": -0.5, "Miserable": -0.13, "Passionate": 0.12, "Peaceful": -0.8, "Pensive": -0.5, "Pleased": -0.1, "Polite": -0.68, "Relaxed": -0.65, "Reverent": -0.85, "Sad": -0.4, "Satisfied": -0.62, "Selfconfident": 0.66, "Serene": -0.47, "Serious": -0.68, "Sleepy": -0.99, "Solemn": -0.47, "Startled": 0.04, "Suspicious": 0.26, "Taken Aback": -0.23, "Tense": 0.85, "Tired": -0.99, "Triumphant": 0.79, "Uncomfortable": -0.375, "Wavering": -0.7, "Worried": -0.34}

word = "Impressed"

xValence = float(emotionValence[word])
yArousal = float(emotionArousal[word])

# xValence = 0.42 #enter x coordinate here
# yArousal = 0.79 #enter y coordinate here

def getWeightValue():
    global weight
    weight = yArousal + 1.25
    return(weight)

getWeightValue()

# xValence = getValence #enter x coordinate here
# yArousal = getArousal #enter y coordinate here

if xValence > 1 or xValence < -1:
     raise Exception("Error: Enter xValence values between 1 and -1")
elif yArousal > 1 or yArousal < -1:
    raise Exception("Error: Enter yArousal values between 1 and -1")

def getEmotionalState():
    global emotionalState
    emotionalState = findEmotionalState(xValence, yArousal)
    return(emotionalState)

getEmotionalState()
print (emotionalState)

def setup():
    py5.size(200,200)
    py5.background(255)   

def draw():
    drawFace(emotionalState)
    drawEyebrows(emotionalState, weight)
    drawFeature(emotionalState, weight)
    drawEyes(emotionalState, weight)
    drawMouth(emotionalState, weight)   
    py5.save_frame('/tmp/e.png')

py5.run_sketch()

# hello
