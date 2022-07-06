class Mouth(object):
    
    #constructor
    def __init__(self, xEmotion, yEmotion):
        self.color = color(0)
        self.xEmotion = xEmotion #x coordinate of emotion - valence
        self.yEmotion = yEmotion #y coordinate of emotion - arousal
        
    def display(self):
        if self.xEmotion < -0.85: #zigzag mouth
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
        elif self.xEmotion < 0 and self.xEmotion > -0.69 and self.yEmotion < 0 and self.yEmotion > -0.69:
        #frowning face
            strokeWeight(6)
            noFill()
            arc(100, 140, 70, 40, PI, TWO_PI) 
        else:  #open mouth
            strokeWeight(6)
            fill(0)
            arc(100, 150, 70, 50, PI, TWO_PI, CHORD)
  
            
