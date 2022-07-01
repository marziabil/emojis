from face import Face
from left_eye import LeftEye
from right_eye import RightEye


def setup(): 
    size(200, 200)
    #background(0)
    global face1
    global eyeL
    global eyeR
    face1 = Face(width * 0.5, height * 0.5, 150, 150)
    eyeL = LeftEye(width * 0.375,height * 0.4,5,12,'x')
    eyeR = RightEye(width * 0.625,height * 0.4,5,12, 'x')
    
def draw():
    background(255)
    face1.display()
    eyeL.display()
    eyeR.display()
