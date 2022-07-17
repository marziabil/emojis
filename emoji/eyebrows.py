class Eyebrows(object):
    
    #constructor
    def __init__(self, xValence, yArousal):
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal
        
    def display(self):
        #no eyebrows:
        if (self.xValence > -0.25 and self.xValence < 0) or (self.xValence > 0 and self.xValence < 0.4 and self.yArousal > 0 and self.yArousal < 0.8) or (self.xValence < 0 and self.xValence > -0.4 and self.yArousal > 0 and self.yArousal < 1):
            noStroke()
            noFill()
        #horizontal arc
        elif self.xValence <= 0.55 and self.xValence >= -0.7 and self.yArousal < -0.1 and self.yArousal >= -0.3:
            strokeWeight(5)
            noFill()
            stroke(204, 153, 0)
            arc(75, 65, 37.5, 12.5, PI, TWO_PI) #left eyebrow
            arc(125, 65, 37.5, 12.5, PI, TWO_PI) #right eyebrow
        elif self.xValence <= -0.7 and self.xValence >= -0.8 and self.yArousal <= -0.3 and self.yArousal >= -0.8:
        #slightly furrowed 
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(50, 50, 80, 30, 0, HALF_PI) #left eyebrow
            arc(150, 50, 80, 30, HALF_PI, PI) #right eyebrow
           
        elif self.xValence > -0.5 and self.xValence <=0.8 and self.yArousal > -0.5 and self.yArousal <=0:
            #highly furrowed 
            stroke(204, 153, 0) #color of eyebrow
            strokeWeight(6) 
            line(60, 65, 85, 40) #left eyebrow
            line(115, 40, 140, 65) #right eyebrow 
        elif self.xValence >= 0.5 and self.xValence <= 1 and self.yArousal < 0.7 and self.yArousal < -1:
            #Raised eyebrows (lower placed)
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(160, 80, 220, 20, PI, PI+QUARTER_PI) #left eyebrow
            arc(115, 80, 65, 20, TWO_PI-HALF_PI, TWO_PI) #right eyebrow
        else: 
            #Raised eyebrows (higher placed)
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(165, 70, 220, 20, PI, PI+QUARTER_PI) #left eyebrow
            arc(115, 70, 65, 20, TWO_PI-HALF_PI, TWO_PI) #right eyebrow
        
    
