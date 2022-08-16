import py5

def crumpledMouth():
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(60, 135, 70, 145)
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(70, 145, 85, 130 )
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(85, 130, 100, 145 )
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(100, 145, 115, 130 )
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(115, 130, 130, 145 )
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(130, 145, 140, 135 )

def frowningMouth(weight):
    py5.stroke_weight(6*weight)
    py5.stroke(0)
    py5.arc(100, 142, 65, 20*weight, py5.PI, py5.TWO_PI) 

def openMouth(weight):
    py5.fill(0)
    py5.arc(100, 150, 50*weight, 40, py5.PI, py5.TWO_PI, py5.CHORD)
    py5.no_fill()
   
def smilingMouth(weight):
    py5.stroke_weight(6*weight)
    py5.stroke(0)
    py5.arc((py5.width*0.5), (py5.height*0.67), 80, 37*weight, 0, py5.radians(180))
    

def shortStraight(weight):
    py5.stroke_weight(6*weight)
    py5.stroke(0)
    py5.line(80-weight, 140+weight, 120+weight, 140+weight)
    

def happyMouth(weight):
    py5.stroke_weight(6)
    py5.fill(0)
    py5.arc(py5.width*0.5, (py5.height* 0.67)-weight, 80, 55, 0, py5.radians(180), py5.CHORD)
    #teeth
    py5.stroke(255)
    py5.fill(255)
    py5.quad(66-weight,137-weight, 135+weight, 137-weight,134+weight, 140, 67-weight, 140)
    #tongue
    py5.stroke_weight(2)
    py5.stroke(255, 0, 102)
    py5.fill(255, 0, 102)
    py5.arc(py5.width*0.5, py5.height*0.80, 23, 15, py5.PI, py5.TWO_PI, py5.CHORD)

def smileHigh(weight):
    py5.stroke_weight(5*weight)
    py5.no_fill()
    py5.arc((py5.width*0.5), (py5.height* 0.6), 80, 37*weight, 0, py5.radians(180), py5.OPEN)   

def clenchedTeeth():
    py5.stroke(0)
    py5.fill(255)
    py5.rect(65, 120, 70, 20, 7)
    py5.line(65, 130, 135, 130) #horizontal line
    py5.line(75, 120, 75, 140)
    py5.line(85, 120, 85, 140)
    py5.line(95, 120, 95, 140)
    py5.line(105, 120, 105, 140)
    py5.line(115, 120, 115, 140)
    py5.line(125, 120, 125, 140)
    
def longStraight(weight):
    py5.stroke_weight(5*weight)
    py5.line(65-weight, 130+weight, 135+weight, 130+weight)
    
def frowningOpen(weight):
    py5.stroke_weight(6)
    py5.fill(0)
    py5.arc(py5.width*0.5, py5.height*0.72, 80, 30*weight, py5.PI, py5.TWO_PI, py5.CHORD)
    #teeth
    py5.stroke(255)
    py5.fill(255)
    py5.arc(py5.width* 0.5, 124, 40,6+weight, py5.PI, py5.TWO_PI, py5.CHORD)

def openShocked(weight):
    py5.fill(0)
    py5.ellipse(py5.width*0.5, py5.height*0.7, 30+weight, 37+weight)
    #teeth
    py5.stroke(255)
    py5.fill(255)
    py5.arc(py5.width*0.5, 125, 15+weight,0.5+weight, py5.PI, py5.TWO_PI, py5.CHORD)
    

def drawMouth(emotionalState, weight):
    if (emotionalState > 22 and emotionalState < 23):
        crumpledMouth()
    elif (emotionalState > 19 and emotionalState < 24.5) or (emotionalState < -12 and emotionalState > -25):
        frowningMouth(weight)
    elif (emotionalState < 17 and emotionalState > 13):
        openMouth(weight)
    elif (emotionalState < -25 and emotionalState > -28) or ( emotionalState < -29 and emotionalState > -30):   
        smilingMouth(weight)
    elif (emotionalState > 10 and emotionalState < 13): 
        shortStraight(weight)
    elif (emotionalState > 29.7 and emotionalState < 36):
        happyMouth(weight)
    elif (emotionalState < 29.7 and emotionalState > 29.2):
        openShocked(weight)
    elif (emotionalState > 25 and emotionalState < 28.5):
        smileHigh(weight)
    elif (emotionalState < -22 and emotionalState > -23):
        clenchedTeeth()
    elif (emotionalState > 17 and emotionalState < 25) or (emotionalState < -28 and emotionalState > -29):
        frowningOpen(weight)
    else: 
        longStraight(weight)
