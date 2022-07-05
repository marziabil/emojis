from face import Face
from eyes import Eyes
from mouth import Mouth
from eyebrows import Eyebrows


def setup(): 
    size(200, 200)
    global face1, eyes, mouth1, eyeBrows
    face1 = Face()
    eyes = Eyes('x') #eye type - enter frown, oval or v shaped
    mouth1 = Mouth( 'frown') # mouth type, frown, open or zig-zag
    eyeBrows = Eyebrows('horizontal') #none, horizontal, high or slightly furrowed
    
def draw():
    background(255)
    face1.display()
    eyes.display()
    mouth1.display()
    eyeBrows.display()
    
