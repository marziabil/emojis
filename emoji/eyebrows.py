class Eyebrows(object):
    
    #constructor
    def __init__(self, ebType):
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.ebType = ebType

    #no eyebrows
    def noEyebrows(self): 
        noStroke()
        noFill()

    #straight eyebrows
    def straightEyebrows(self):
        strokeWeight(5)
        noFill()
        stroke(204, 153, 0)
        arc(75, 65, 37.5, 12.5, PI, TWO_PI) #left eyebrow
        arc(125, 65, 37.5, 12.5, PI, TWO_PI) #right eyebrow
    
    #slightly furrowed
    def slightlyFurrowed(self):
        stroke(204, 153, 0)
        strokeWeight(6)
        noFill()
        arc(50, 50, 80, 30, 0, HALF_PI) #left eyebrow
        arc(150, 50, 80, 30, HALF_PI, PI) #right eyebrow

    #highly furrowed
    def highlyFurrowed(self):
        stroke(204, 153, 0) #color of eyebrow
        strokeWeight(6) 
        line(60, 65, 85, 40) #left eyebrow
        line(115, 40, 140, 65) #right eyebrow 

    #raised eyebrows (lower positioned)
    def raisedEyebrows(self):
        stroke(204, 153, 0)
        strokeWeight(6)
        noFill()
        arc(160, 80, 220, 20, PI, PI+QUARTER_PI) #left eyebrow
        arc(115, 80, 65, 20, TWO_PI-HALF_PI, TWO_PI) #right eyebrow
    
    #raised eyebrows (higher placed)
    def raisedEyebrowsHigh(self):
        stroke(204, 153, 0)
        strokeWeight(6)
        noFill()
        arc(165, 70, 220, 20, PI, PI+QUARTER_PI) #left eyebrow
        arc(115, 70, 65, 20, TWO_PI-HALF_PI, TWO_PI) #right eyebrow  


    def display(self):
        if self.ebType == "no_eyebrows":
            self.noEyebrows() #no eyebrows:
        elif self.ebType == "straight":
            self.straightEyebrows() # straight eyebrows
        elif self.ebType == "slightly_furrowed":
            self.slightlyFurrowed() 
        elif self.ebType == "highly_furrowed":
            self.highlyFurrowed()
        elif self.ebType == "raised_eyebrows":
            self.raisedEyebrows()    
        else: 
            self.raisedEyebrowsHigh()
            
    
