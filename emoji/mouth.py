class Mouth(object):
    
    #constructor
    def __init__(self, xValence, yArousal):
        self.color = color(0)
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal
        
    def display(self):
        if self.xValence < -0.85: #zigzag mouth
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
        elif self.xValence < 0 and self.xValence >= -0.7 and self.yArousal < 0 and self.yArousal >= -0.7:
        #frowning face
            strokeWeight(6)
            noFill()
            arc(100, 140, 70, 40, PI, TWO_PI) 
        else:  #open mouth
            strokeWeight(6)
            fill(0)
            arc(100, 150, 70, 50, PI, TWO_PI, CHORD)
  
            
