import py5

def crumpledMouth():
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(60, 135, 70, 145)
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(70, 145, 85, 130 )
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(85, 130, 100, 145 )
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(100, 145, 115, 130 )
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(115, 130, 130, 145 )
    py5.stroke(0)
    py5.stroke_weight(8)
    py5.line(130, 145, 140, 135 )

def frowningMouth():
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(100, 140, 70, 40, py5.PI, py5.TWO_PI) 

def openMouth():
    py5.stroke_weight(6)
    py5.fill(0)
    py5.arc(100, 150, 70, 50, py5.PI, py5.TWO_PI, py5.CHORD)

def smilingMouth():
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(py5.width * 0.5, py5.height * 0.67, 80, 37, 0, py5.radians(180))

def shortStraight():
    py5.stroke_weight(6)
    py5.no_fill()
    py5.line(80, 140, 120, 140)

def happyMouth():
    py5.stroke_weight(6)
    py5.fill(0)
    py5.arc(py5.width * 0.5, py5.height * 0.67, 80, 55, 0, py5.radians(180), py5.CHORD)
    #teeth
    py5.stroke(255)
    py5.fill(255)
    py5.quad(66,137, 135, 137,134, 140, 67, 140)
    #tongue
    py5.stroke_weight(2)
    py5.stroke(255, 0, 102)
    py5.fill(255, 0, 102)
    py5.arc(py5.width * 0.5, py5.height * 0.80, 23, 15, py5.PI, py5.TWO_PI, py5.CHORD)

def smileHigh():
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(py5.width * 0.5, py5.height * 0.6, 80, 37, 0, py5.radians(180))

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

def longStraight():
    py5.stroke_weight(5)
    py5.line(65, 130, 135, 130)

def drawMouth(mouthType):
    if mouthType == "crumpled":
        crumpledMouth()
    elif mouthType == "frowning":
        frowningMouth()
    elif mouthType == "open":
        openMouth()
    elif mouthType == "smile":   
        smilingMouth()
    elif mouthType == "shortStraight": 
        shortStraight()
    elif mouthType == "happy":
        happyMouth()
    elif mouthType == "smileHigh":
        smileHigh()
    elif mouthType == "clenched":
        clenchedTeeth()
    else: 
        longStraight()