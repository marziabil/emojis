from face import Face
from left_eye import LeftEye
from right_eye import RightEye
from mouth import Mouth
from left_eyebrow import lEyeBrow


def setup(): 
    size(200, 200)
    #background(0)
    global face1, eyeL, eyeR, mouth1, ebL
    face1 = Face()
    eyeL = LeftEye('oval') #eye type - enter frown, oval or v shaped
    eyeR = RightEye('oval') # eye type - frown, oval or v shaped
    mouth1 = Mouth( 'zig-zag') # mouth type, frown, open or zig-zag
    ebL = lEyeBrow('x') 
    
def draw():
    background(255)
    face1.display()
    eyeL.display()
    eyeR.display()
    mouth1.display()
    ebL.display()
    
