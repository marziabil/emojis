
class Mouth(object):
    
    #constructor
    def __init__(self, xValence, yArousal):
        self.color = color(0)
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal
        
    def display(self):
        if self.xValence < -0.85: #crumpled mouth
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
        elif self.xValence < 0 and self.xValence >= -0.85 and self.yArousal < 0 and self.yArousal >= -0.9:
            #open mouth
            strokeWeight(6)
            fill(0)
            arc(100, 150, 70, 50, PI, TWO_PI, CHORD)
        elif self.xValence >= 0.5 and self.xValence <= 1 and self.yArousal <= -0.5 and self.yArousal <= -0.8:   
            #smiling mouth
            strokeWeight(6)
            noFill()
            arc(width * 0.5, height * 0.67, 80, 37, 0, radians(180))
        elif self.xValence >= 0.1 and self.xValence <= 0.3 and self.yArousal <= -0.5 and self.yArousal >= -0.7: 
            #straight mouth (shorter)
            strokeWeight(6)
            noFill()
            line(80, 140, 120, 140)
        elif self.xValence >= 0.5 and self.xValence <= 1 and self.yArousal > 0 and self.yArousal < 0.7:
            #open mouth with tongue and teeth
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
        elif self.xValence > 0 and self.xValence <= 0.9 and self.yArousal >= 0.3 and self.yArousal <= 0.7:
            strokeWeight(6)
            noFill()
            arc(width * 0.5, height * 0.6, 80, 37, 0, radians(180))
        else: 
            