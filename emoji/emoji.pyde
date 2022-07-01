from face import Face
from left_eye import LeftEye
from right_eye import RightEye
from mouth import Mouth


def setup(): 
    size(200, 200)
    #background(0)
    global face1, eyeL, eyeR, mouth1
    face1 = Face(width * 0.5, height * 0.5, 150, 150)
    eyeL = LeftEye(width * 0.375,height * 0.4,5,12,'frown') #eye type - frown, oval
    eyeR = RightEye(width * 0.625,height * 0.4,5,12, 'frown') # #eye type - frown, oval
    mouth1 = Mouth(100, 150, 70, 50, PI, TWO_PI, "frown", CHORD)
    
def draw():
    background(255)
    face1.display()
    eyeL.display()
    eyeR.display()
    mouth1.display()
