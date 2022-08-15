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

xValence = 0.55 #enter x coordinate here
yArousal = -0.8 #enter y coordinate here

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
    
py5.run_sketch()

# hello
