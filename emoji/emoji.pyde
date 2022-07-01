from face import Face
from left_eye import LeftEye
from right_eye import RightEye
from mouth import Mouth


def setup(): 
    size(200, 200)
    #background(0)
    global face1
    global eyeL
    global eyeR
    global mouth1
    face1 = Face(width * 0.5, height * 0.5, 150, 150)
    eyeL = LeftEye(width * 0.375,height * 0.4,5,12,'x')
    eyeR = RightEye(width * 0.625,height * 0.4,5,12, 'x')
    mouth1 = Mouth(100, 150, 70, 50, PI, TWO_PI)
    
def draw():
    background(255)
    face1.display()
    eyeL.display()
    eyeR.display()
    mouth1.display()
