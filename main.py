'''
The emoji class produces a set of emoji with different features i.e. eyes, mouth and eyebrows
These can be tweaked by entering the x and y coordinates of the emotion from the circumplex model. 
'''
# from py5 import Sketch
import py5
from face import Face
from eyes import Eyes
from mouth import Mouth
from eyebrows import Eyebrows
# from fuzzyLogic import mouthForEmoji
# from fuzzyLogic import mouthForEmoji, mouthType
# from simpful import FuzzySystem, FuzzySet, Trapezoidal_MF, LinguisticVariable

#module mode

faceColour = "yellow"
eyeType = "wideOpenEyes"
mouthType = "happy"
# mouthType = mouthForEmoji()
ebType = "no_eyebrows"

def setup():
    py5.size(200,200)
    py5.background(255)
    
    global face, eyes, mouth, eyeBrows
    face = Face(faceColour)
    eyes = Eyes(eyeType) 
    mouth = Mouth(mouthType) 
    eyeBrows = Eyebrows(ebType) 

def draw():
    face.draw()
    eyes.draw()
    mouth.draw()
    eyeBrows.draw()

py5.run_sketch()




#CLASS MODE
# class Emoji(Sketch):

#     def settings(self):
#         self.size(200,200)
#         self.background(255)
    
#     def setup(): 
#         global face, eyes, mouth, eyeBrows
#         face = Face(faceColour)
#         eyes = Eyes(eyeType) 
#         mouth = Mouth(mouthType) 
#         eyeBrows = Eyebrows(ebType)  
    
#     def draw():
#         face.display()
#         eyes.display()
#         mouth.display()
#         eyeBrows.display()
#     # mouthType()

# emoji = Emoji()
# emoji.run_sketch()

