'''
The emoji class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
import py5
from eyes import drawEyes
from eyebrows import drawEyebrows
from face import drawFace
from mouth import drawMouth

# from fuzzyLogic import mouthForEmoji
# from fuzzyLogic import mouthForEmoji, mouthType
# from simpful import FuzzySystem, FuzzySet, Trapezoidal_MF, LinguisticVariable

#module mode

xValence = 0.5 #enter x coordinate here
vArousal = 0.7 #enter y coordinate here



faceColour = "yellow"
eyeType = "wideOpenEyes"
mouthType = "happy"
# mouthType = mouthForEmoji()
ebType = "no_eyebrows"

def setup():
    py5.size(200,200)
    py5.background(255)
    
#     global face, eyes, mouth, eyeBrows
#     face = Face(faceColour)
#     eyes = Eyes(eyeType) 
#     mouth = Mouth(mouthType) 
#     eyeBrows = Eyebrows(ebType) 

def draw():
    drawFace(faceColour)
    drawEyes(eyeType)
    drawEyebrows(ebType)
    drawMouth(mouthType)

py5.run_sketch()




