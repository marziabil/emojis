class Mouth(object):
    
    #constructor
    def __init__(self, mouthType, g):
        self.color = color(0)
        self.mouthType = mouthType #frowning; open and frowning 
        self.g = g #mode of the arc
        
    def display(self):
        if self.mouthType == "frown":
            strokeWeight(6)
            arc(self.x, self.y, self.c, self.d, PI, TWO_PI) #frowning face
        elif self.mouthType == "open": #open mouth
            strokeWeight(6)
            fill(0)
            self.g = CHORD
            arc(self.x, self.y, self.c, self.d, PI, TWO_PI, self.g)
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
            
