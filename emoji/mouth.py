class Mouth(object):
    
    #constructor
    def __init__(self, mouthType):
        self.color = color(0)
        self.mouthType = mouthType #frowning; open and frowning 
        #self.g = g #mode of the arc
        
    def display(self):
        if self.mouthType == "frown":
            strokeWeight(6)
            noFill()
            arc(100, 140, 70, 40, PI, TWO_PI) #frowning face
        elif self.mouthType == "open": #open mouth
            strokeWeight(6)
            fill(0)
            #self.g = CHORD
            arc(100, 150, 70, 50, PI, TWO_PI, CHORD)
        else: #zigzag mouth
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
            
