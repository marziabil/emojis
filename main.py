'''
The emoji class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
import py5
# from eyes import drawEyes
# from eyebrows import drawEyebrows
from face import drawFace
# from mouth import drawMouth
from fuzzyLogic import findEmotionalState
# from simpful import FuzzySystem, FuzzySet, Trapezoidal_MF, LinguisticVariable

#module mode

xValence = -0.18 #enter x coordinate here
yArousal = 0.72 #enter y coordinate here

def getEmotionalState():
    
    emotionalState = findEmotionalState(xValence, yArousal)
    return(emotionalState)

getEmotionalState()

# def setup():
#     py5.size(200,200)
#     py5.background(255)
    

def draw():
    drawFace(emotionalState)
# #     # drawEyes(eyeType)
# #     # drawEyebrows(ebType)
# #     # drawMouth(mouthType)

# py5.run_sketch()


# faceColour = "yellow"
# eyeType = "wideOpenEyes"
# mouthType = "happy"
# ebType = "no_eyebrows"



