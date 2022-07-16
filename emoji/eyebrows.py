class Eyebrows(object):
    
    #constructor
    def __init__(self, xEmotion, yEmotion):
        self.xEmotion = xEmotion #x coordinate of emotion - valence
        self.yEmotion = yEmotion #y coordinate of emotion - arousal
        
    def display(self):
        #no eyebrows:
        if (self.xEmotion > -0.25 and self.xEmotion < 0) or (self.xEmotion > 0 and self.xEmotion < 0.4 and self.yEmotion > 0 and self.yEmotion < 0.8) or (self.xEmotion < 0 and self.xEmotion > -0.4 and self.yEmotion > 0 and self.yEmotion < 1):
            noStroke()
            noFill()
        #horizontal arc
        elif self.xEmotion <= 0.55 and self.xEmotion >= -0.7 and self.yEmotion < -0.1 and self.yEmotion >= -0.3:
            strokeWeight(5)
            noFill()
            stroke(204, 153, 0)
            arc(75, 65, 37.5, 12.5, PI, TWO_PI) #left eyebrow
            arc(125, 65, 37.5, 12.5, PI, TWO_PI) #right eyebrow
        elif self.xEmotion <= -0.7 and self.xEmotion >= -0.8 and self.yEmotion <= -0.3 and self.yEmotion >= -0.8:
        #slightly furrowed 
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(50, 50, 80, 30, 0, HALF_PI) #left eyebrow
            arc(150, 50, 80, 30, HALF_PI, PI) #right eyebrow
           
        elif self.xEmotion < -0.8 or self.yEmotion < -0.8:
            #highly furrowed 
            stroke(204, 153, 0) #color of eyebrow
            strokeWeight(6) 
            line(60, 65, 85, 40) #left eyebrow
            line(115, 40, 140, 65) #right eyebrow 
        else:
            #Raised eyebrows (lower placed)
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(160, 80, 220, 20, PI, PI+QUARTER_PI) #left eyebrow
            arc(115, 80, 65, 20, TWO_PI-HALF_PI, TWO_PI) #right eyebrow
        
        
    
