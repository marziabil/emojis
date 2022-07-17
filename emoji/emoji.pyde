'''
The emoji class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''

from face import Face
from eyes import Eyes
from mouth import Mouth
from eyebrows import Eyebrows

xValence = 0.7 #enter x coordinate here (only negative coordinates will work for now)
yArousal = -0.8 #enter y coordinate here (only negative coordinates will work for now)

def setup(): 
    size(200, 200)
    global face1, eyes, mouth1, eyeBrows
    face1 = Face()
    eyes = Eyes(xValence, yArousal) 
    mouth1 = Mouth(xValence, yArousal) 
    eyeBrows = Eyebrows(xValence, yArousal)
    
def draw():
    background(255)
    face1.display()
    eyes.display()
    mouth1.display()
    eyeBrows.display()
    
