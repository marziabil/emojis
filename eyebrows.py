from py5 import Sketch

class Eyebrows(Sketch):
    
    #constructor
    def __init__(self, ebType):
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.ebType = ebType

    #no eyebrows
    def noEyebrows(self): 
        self.no_stroke()
        self.no_fill()

    #straight eyebrows
    def straightEyebrows(self):
        self.stroke_weight(5)
        self.no_fill()
        self.stroke(204, 153, 0)
        self.arc(75, 65, 37.5, 12.5, self.PI, self.TWO_PI) #left eyebrow
        self.arc(125, 65, 37.5, 12.5, self.PI, self.TWO_PI) #right eyebrow
    
    #slightly furrowed
    def slightlyFurrowed(self):
        self.stroke(204, 153, 0)
        self.stroke_weight(6)
        self.no_fill()
        self.arc(50, 50, 80, 30, 0, self.HALF_PI) #left eyebrow
        self.arc(150, 50, 80, 30, self.HALF_PI, self.PI) #right eyebrow

    #highly furrowed
    def highlyFurrowed(self):
        self.stroke(204, 153, 0) #color of eyebrow
        self.stroke_weight(6) 
        self.line(60, 65, 85, 40) #left eyebrow
        self.line(115, 40, 140, 65) #right eyebrow 

    #raised eyebrows (lower positioned)
    def raisedEyebrows(self):
        self.stroke(204, 153, 0)
        self.stroke_weight(6)
        self.no_fill()
        self.arc(160, 80, 220, 20, self.PI, self.PI+self.QUARTER_PI) #left eyebrow
        self.arc(115, 80, 65, 20, self.TWO_PI-self.HALF_PI, self.TWO_PI) #right eyebrow
    
    #raised eyebrows (higher placed)
    def raisedEyebrowsHigh(self):
        self.stroke(204, 153, 0)
        self.stroke_weight(6)
        self.no_fill()
        self.arc(165, 70, 220, 20, self.PI, self.PI+self.QUARTER_PI) #left eyebrow
        self.arc(115, 70, 65, 20, self.TWO_PI-self.HALF_PI, self.TWO_PI) #right eyebrow  


    def draw(self):
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