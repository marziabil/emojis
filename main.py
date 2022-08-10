'''
The main class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
import py5
from eyebrows import drawEyebrows
from face import drawFace
from eyes import drawEyes
from mouth import drawMouth
from fuzzyLogic import findEmotionalState

xValence = -0.68 #enter x coordinate here
yArousal = -0.38 #enter y coordinate here

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
    drawEyebrows(emotionalState)
    drawEyes(emotionalState)
    drawMouth(emotionalState)
    

py5.run_sketch()



