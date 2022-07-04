from face import Face
from left_eye import LeftEye
from right_eye import RightEye
from mouth import Mouth
from left_eyebrow import lEyeBrow
from right_eyebrow import rEyeBrow

def setup(): 
    size(200, 200)
    #background(0)
    global face1, eyeL, eyeR, mouth1, ebL, ebR
    face1 = Face()
    eyeL = LeftEye('oval') #eye type - enter frown, oval or v shaped
    eyeR = RightEye('oval') # eye type - frown, oval or v shaped
    mouth1 = Mouth( 'frown') # mouth type, frown, open or zig-zag
    ebL = lEyeBrow('none') #left eyebrow - none, horizontal, high or slightly furrowed
    ebR = rEyeBrow('none') #right eyebrow - none, horizontal, high or slightly furrowed
    
def draw():
    background(255)
    face1.display()
    eyeL.display()
    eyeR.display()
    mouth1.display()
    ebL.display()
    ebR.display()
    
