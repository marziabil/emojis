
class Mouth(object):
    
    #constructor
    def __init__(self, mouthType):
        self.color = color(0)
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.mouthType = mouthType


    def crumpledMouth(self):
        stroke(0)
        strokeWeight(8)
        line(60, 135, 70, 145)
        stroke(0)
        strokeWeight(8)
        line(70, 145, 85, 130 )
        stroke(0)
        strokeWeight(8)
        line(85, 130, 100, 145 )
        stroke(0)
        strokeWeight(8)
        line(100, 145, 115, 130 )
        stroke(0)
        strokeWeight(8)
        line(115, 130, 130, 145 )
        stroke(0)
        strokeWeight(8)
        line(130, 145, 140, 135 )

    def frowningMouth(self):
        strokeWeight(6)
        noFill()
        arc(100, 140, 70, 40, PI, TWO_PI) 
    
    def openMouth(self):
        strokeWeight(6)
        fill(0)
        arc(100, 150, 70, 50, PI, TWO_PI, CHORD)

    def smilingMouth(self):
        strokeWeight(6)
        noFill()
        arc(width * 0.5, height * 0.67, 80, 37, 0, radians(180))

    def shortStraight(self):
        strokeWeight(6)
        noFill()
        line(80, 140, 120, 140)

    def happyMouth(self):
        strokeWeight(6)
        fill(0)
        arc(width * 0.5, height * 0.67, 80, 55, 0, radians(180), CHORD)
        #teeth
        stroke(255)
        fill(255)
        quad(66,137, 135, 137,134, 140, 67, 140)
        #tongue
        strokeWeight(2)
        stroke(255, 0, 102)
        fill(255, 0, 102)
        arc(width * 0.5, height * 0.80, 23, 15, PI, TWO_PI, CHORD)

    def smileHigh(self):
        strokeWeight(6)
        noFill()
        arc(width * 0.5, height * 0.6, 80, 37, 0, radians(180))
    
    def clenchedTeeth(self):
        stroke(0)
        fill(255)
        rect(65, 120, 70, 20, 7)
        line(65, 130, 135, 130) #horizontal line
        line(75, 120, 75, 140)
        line(85, 120, 85, 140)
        line(95, 120, 95, 140)
        line(105, 120, 105, 140)
        line(115, 120, 115, 140)
        line(125, 120, 125, 140)

    def longStraight(self):
        strokeWeight(5)
        line(65, 130, 135, 130)

    def display(self):
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