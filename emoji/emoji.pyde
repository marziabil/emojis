'''
The emoji class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''

from face import Face
from eyes import Eyes
from mouth import Mouth
from eyebrows import Eyebrows

faceColour = "yellow"
eyeType = "oval"
mouthType = "smile"
ebType = "straight"


def setup(): 
    size(200, 200)
    global face1, eyes, mouth1, eyeBrows
    face1 = Face(faceColour)
    eyes = Eyes(eyeType) 
    mouth1 = Mouth(mouthType) 
    eyeBrows = Eyebrows(ebType)
    
def draw():
    background(255)
    face1.display()
    eyes.display()
    mouth1.display()
    eyeBrows.display()
    