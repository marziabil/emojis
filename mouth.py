from py5 import Sketch

class Mouth(Sketch):
    
    #constructor
    def __init__(self, mouthType):
        # self.color = color(0)
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.mouthType = mouthType


    def crumpledMouth(self):
        self.stroke(0)
        self.stroke_weight(8)
        self.line(60, 135, 70, 145)
        self.stroke(0)
        self.stroke_weight(8)
        self.line(70, 145, 85, 130 )
        self.stroke(0)
        self.stroke_weight(8)
        self.line(85, 130, 100, 145 )
        self.stroke(0)
        self.stroke_weight(8)
        self.line(100, 145, 115, 130 )
        self.stroke(0)
        self.stroke_weight(8)
        self.line(115, 130, 130, 145 )
        self.stroke(0)
        self.stroke_weight(8)
        self.line(130, 145, 140, 135 )

    def frowningMouth(self):
        self.stroke_weight(6)
        self.no_fill()
        self.arc(100, 140, 70, 40, self.PI, self.TWO_PI) 
    
    def openMouth(self):
        self.stroke_weight(6)
        self.fill(0)
        self.arc(100, 150, 70, 50, self.PI, self.TWO_PI, self.CHORD)

    def smilingMouth(self):
        self.stroke_weight(6)
        self.no_fill()
        self.arc(self.width * 0.5, self.height * 0.67, 80, 37, 0, self.radians(180))

    def shortStraight(self):
        self.stroke_weight(6)
        self.no_fill()
        self.line(80, 140, 120, 140)

    def happyMouth(self):
        self.stroke_weight(6)
        self.fill(0)
        self.arc(self.width * 0.5, self.height * 0.67, 80, 55, 0, self.radians(180), self.CHORD)
        #teeth
        self.stroke(255)
        self.fill(255)
        self.quad(66,137, 135, 137,134, 140, 67, 140)
        #tongue
        self.stroke_weight(2)
        self.stroke(255, 0, 102)
        self.fill(255, 0, 102)
        self.arc(self.width * 0.5, self.height * 0.80, 23, 15, self.PI, self.TWO_PI, self.CHORD)

    def smileHigh(self):
        self.stroke_weight(6)
        self.no_fill()
        self.arc(self.width * 0.5, self.height * 0.6, 80, 37, 0, self.radians(180))
    
    def clenchedTeeth(self):
        self.stroke(0)
        self.fill(255)
        self.rect(65, 120, 70, 20, 7)
        self.line(65, 130, 135, 130) #horizontal line
        self.line(75, 120, 75, 140)
        self.line(85, 120, 85, 140)
        self.line(95, 120, 95, 140)
        self.line(105, 120, 105, 140)
        self.line(115, 120, 115, 140)
        self.line(125, 120, 125, 140)

    def longStraight(self):
        self.stroke_weight(5)
        self.line(65, 130, 135, 130)

    def draw(self):
        if self.mouthType == "crumpled":
            self.crumpledMouth()
        elif self.mouthType == "frowning":
            self.frowningMouth()
        elif self.mouthType == "open":
            self.openMouth()
        elif self.mouthType == "smile":   
            self.smilingMouth()
        elif self.mouthType == "shortStraight": 
            self.shortStraight()
        elif self.mouthType == "happy":
            self.happyMouth()
        elif self.mouthType == "smileHigh":
            self.smileHigh()
        elif self.mouthType == "clenched":
            self.clenchedTeeth()
        else: 
            self.longStraight()