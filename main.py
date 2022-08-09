'''
The main class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
import py5
# from eyes import drawEyes
from eyebrows import drawEyebrows
from face import drawFace
from eyes import drawEyes
from mouth import drawMouth
from fuzzyLogic import findEmotionalState

xValence = -0.51 #enter x coordinate here
yArousal = -0.86 #enter y coordinate here

def getEmotionalState():
    
    global emotionalState
    emotionalState = findEmotionalState(xValence, yArousal)
    return(emotionalState)

getEmotionalState()

def setup():
    py5.size(200,200)
    py5.background(255)   

def draw():
    drawFace(emotionalState)
    drawEyebrows(emotionalState)
    drawEyes(emotionalState)
    drawMouth(emotionalState)

py5.run_sketch()



