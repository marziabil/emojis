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

xValence = 1 #enter x coordinate here
yArousal = -1 #enter y coordinate here

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
    # py5.background(255)   

def draw():
    drawFace(emotionalState)
    drawEyebrows(emotionalState)
    drawFeature(emotionalState)
    drawEyes(emotionalState)
    drawMouth(emotionalState)   
    
py5.run_sketch()

#dictionary to store emotions and their valence & arousal
emotion_Valence = {"Lusting": 0.22, "Aroused": 0.36, "Astonished": 0.42, "Conceited": 0.19, "Ambitious": 0.45, "Feeling Superior": 0.325, "Adventurous": 0.49, "Triumphant": 0.6, "Excited": 0.7, "Selfconfident": 0.81, "Courageous": 0.9, "Convinced": 0.42, "Delighted": 0.89, "Enthusiastic": 0.5, "Determined": 0.725, "Happy": 0.9, "Joyous": 0.95, "Interested": 0.65, "Light Hearted": 0.4, "Amused": 0.55, "Passionate": 0.32, "Expectant": 0.32, "Bellicose": -0.12, "Alarmed": -0.08, "Tense": -0.04, "Afraid": -0.12, "Hostile": -0.28, "Envious": -0.28, "Enraged": -0.18, "Angry": -0.4, "Annoyed": -0.45, "Jealous": -0.06, "Hateful": -0.58, "Defiant": -0.62, "Contemptuous": -0.58, "Distressed": -0.7, "Indignant": -0.25, "Impatient": -0.05, "Suspicious": -0.32, "Frustrated": -0.6, "Disgusted": -0.66, "Loathing": -0.8, "Discontented": -0.625, "Bitter": -0.8, "Insulted": -0.725, "Distrustful": -0.48, "Startled": -0.925, "Disappointed": -0.8, "Miserable": -0.925, "Dissatisfied": -0.6, "Uncomfortable": -0.675, "Sad": -0.825, "Gloomy": -0.86, "Desperate": -0.8, "Depressed": -0.81, "Despondent": -0.567, "Apathetic": -0.2, "Taken Aback": -0.4, "Worried": -0.06, "Feel Guilt": -0.4, "Languid": -0.22, "Ashamed": -0.45, "Embarassed": -0.31, "Melancholic": -0.66, "Hesitant": -0.31, "Bored": -0.35, "Droopy": -0.32, "Doubtful": -0.275, "Tired": -0.02, "Wavering": -0.6, "Anxious": -0.725, "Dejected": -0.51, "Impressed": 0.39, "Confident": 0.51, "Attentive": 0.49, "Longing": 0.22, "Pensive": 0.125, "Polite": 0.39, "Serious": 0.21, "Conscientious": 0.32, "Reverent": 0.31, "Sleepy": 0.125, "Compassionate": 0.38, "Feel Well": 0.91, "Pleased": 0.89, "Amorous": 0.85, "Glad": 0.95, "Hopeful": 0.61, "Solemn": 0.81, "Serene": 0.85, "Content": 0.81, "At Ease": 0.75, "Satisfied": 0.78, "Relaxed": 0.72, "Friendly": 0.75, "Contemplative": 0.59, "Peaceful": 0.55}
emotion_Arousal = {"Lusting": 0.85, "Aroused": 0.92, "Astonished": 0.79, "Conceited": 0.66, "Ambitious": 0.65, "Feeling Superior": 0.55, "Adventurous": 0.91, "Triumphant": 0.79, "Excited": 0.725, "Selfconfident": 0.66, "Courageous": 0.59, "Convinced": 0.42, "Delighted": 0.35, "Enthusiastic": 0.32, "Determined": 0.26, "Happy": 0.25, "Joyous": 0.25, "Interested": 0.3, "Light Hearted": 0.3, "Amused": 0.2, "Passionate": 0.12, "Expectant": 0.6, "Bellicose": 0.85, "Alarmed": 0.89, "Tense": 0.85, "Afraid": 0.79, "Hostile": 0.85, "Envious": 0.82, "Enraged": 0.72, "Angry": 0.79, "Annoyed": 0.65, "Jealous": 0.56, "Hateful": 0.85, "Defiant": 0.725, "Contemptuous": 0.66, "Distressed": 0.55, "Indignant": 0.45, "Impatient": 0.3, "Suspicious": 0.26, "Frustrated": 0.39, "Disgusted": 0.49, "Loathing": 0.425, "Discontented": 0.32, "Bitter": 0.26, "Insulted": 0.2, "Distrustful": 0.1, "Startled": 0.04, "Disappointed": -0.04, "Miserable": -0.13, "Dissatisfied": -0.175, "Uncomfortable": -0.375, "Sad": -0.4, "Gloomy": -0.48, "Desperate": -0.5, "Depressed": -0.46, "Despondent": -0.425, "Apathetic": -0.11, "Taken Aback": -0.23, "Worried": -0.34, "Feel Guilt": -0.425, "Languid": -0.5, "Ashamed": -0.5, "Embarassed": -0.6, "Melancholic": -0.5, "Hesitant": -0.725, "Bored": -0.725, "Droopy": -0.925, "Doubtful": -0.95, "Tired": -0.99, "Wavering": -0.7, "Anxious": -0.8, "Dejected": -0.86, "Impressed": -0.18, "Confident": -0.2, "Attentive": -0.48, "Longing": -0.42, "Pensive": -0.5, "Polite": -0.68, "Serious": -0.68, "Conscientious": -0.8, "Reverent": -0.85, "Sleepy": -0.99, "Compassionate": -0.925, "Feel Well": -0.8, "Pleased": -0.1, "Amorous": -0.15, "Glad": -0.15, "Hopeful": -0.3, "Solemn": -0.47, "Serene": -0.47, "Content": -0.59, "At Ease": -0.6, "Satisfied": -0.62, "Relaxed": -0.65, "Friendly": -0.6, "Contemplative": -0.6, "Peaceful": -0.8}

