from py5 import Sketch

class Eyes(Sketch):
    
    #constructor
    def __init__(self, eyeType):
        # self.color = self.color(0) #color of eye - black
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.eyeType = eyeType
    
    def xShaped(self):
        self.stroke(0)
        self.stroke_weight(6) #upper half of x and thinner part
        self.line(45,75,65,85)
        self.stroke_weight(8) #upper half of x and thicker part
        self.line(65,85,85,95)
        self.stroke_weight(8) #lower half of x and thicker part
        self.line(65,105, 85, 95)
        self.stroke_weight(6) #lower half of x and thinner part
        self.line(45, 115, 65, 105)
        
        #right eye
        self.stroke(0)
        self.stroke_weight(8) #upper half of x
        self.line(115, 95, 135, 85)
        self.stroke_weight(6) #upper half of x
        self.line(135, 85, 155, 75)
        self.stroke_weight(8) # lower half of x
        self.line(115, 95, 135, 105)
        self.stroke_weight(6) # lower half of x
        self.line(135, 105, 155, 115)

    def ovalEyes(self):
        self.stroke_weight(10)
        self.stroke(0) #color black
        self.fill(0)
        self.ellipse(75,90,5,12) #left eye
        self.ellipse(125,90,5,12) #right eye
    
    def shallowDowncast(self):
        self.stroke(0)
        self.no_fill()
        self.stroke_weight(6)
        self.arc(75, 90, 35, 32.5, 0, self.PI) #left eye
        self.arc(125, 90, 35, 32.5, 0, self.PI) #right eye

    def deepDowncast(self):
        self.stroke(0)
        self.no_fill()
        self.stroke_weight(6)
        self.arc(75, 90, 37, 40, 0, self.PI) #left eye
        self.arc(125, 90, 37, 40, 0, self.PI) #right eye

    def shallowSmile(self):
        self.stroke(0)
        self.no_fill()
        self.stroke_weight(6)
        self.arc(75, 95, 37.5, 20, self.PI, self.TWO_PI) #left eye
        self.arc(125, 95, 37.5, 20, self.PI, self.TWO_PI) #right eye 

    def straightEyes(self):
        self.stroke(0)
        self.no_fill()
        self.stroke_weight(6)
        self.line(55, 85, 90, 85) #left eye
        self.line(110, 85, 145, 85) #right eye

    def wideOpenEyes(self):
        self.stroke_weight(10)
        self.stroke(255) #color white
        self.ellipse(75,90,17.5,17.5) #left eye
        self.fill(255) #color white
        self.stroke(0) #color black
        self.fill(0)
        self.ellipse(75,90,5,5) #left eye
    
        self.stroke_weight(10)
        self.stroke(255) #color white
        self.ellipse(125,90,17.5,17.5) #right eye
        self.fill(255) #color white
        self.stroke(0) #color black
        self.fill(0)
        self.ellipse(125,90,5,5) #left eye

    def deepSmile(self):
        self.stroke(0)
        self.no_fill()
        self.stroke_weight(6)
        self.arc(75, 95, 37.5, 30, self.PI, self.TWO_PI) #left eye
        self.arc(125, 95, 37.5, 30, self.PI, self.TWO_PI) #right eye

    def whiteEyes(self):
        self.stroke_weight(2)
        self.stroke(0) #color black
        self.fill(255)
        self.ellipse(75,90,25,32) #left eye
        self.ellipse(125,90,25,32) #right eye

    def draw(self):  
        if self.eyeType == "xShaped":
            self.xShaped()  
        elif self.eyeType == "oval":
            self.ovalEyes()  
        elif self.eyeType == "shallowDowncast":
            self.shallowDowncast()
        elif self.eyeType == "deepDowncast":
            self.deepDowncast()
        elif self.eyeType == "shallowSmile":
            self.shallowSmile()
        elif self.eyeType == "straightEyes":
            self.straightEyes()
        elif self.eyeType == "wideOpenEyes": 
            self.wideOpenEyes()    
        elif self.eyeType == "deepSmile":    
           self.deepSmile()
        else: 
            self.whiteEyes()
            
        

    

        
