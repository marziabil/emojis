class Eyes(object):
    
    #constructor
    def __init__(self, eyeType):
        self.color = color(0) #color of eye - black
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.eyeType = eyeType
    
    def xShaped(self):
        stroke(self.color)
        strokeWeight(6) #upper half of x and thinner part
        line(45,75,65,85)
        strokeWeight(8) #upper half of x and thicker part
        line(65,85,85,95)
        strokeWeight(8) #lower half of x and thicker part
        line(65,105, 85, 95)
        strokeWeight(6) #lower half of x and thinner part
        line(45, 115, 65, 105)
        
        #right eye
        stroke(self.color)
        strokeWeight(8) #upper half of x
        line(115, 95, 135, 85)
        strokeWeight(6) #upper half of x
        line(135, 85, 155, 75)
        strokeWeight(8) # lower half of x
        line(115, 95, 135, 105)
        strokeWeight(6) # lower half of x
        line(135, 105, 155, 115)

    def ovalEyes(self):
        strokeWeight(10)
        stroke(self.color) #color black
        fill(self.color)
        ellipse(75,90,5,12) #left eye
        ellipse(125,90,5,12) #right eye
    
    def shallowDowncast(self):
        stroke(self.color)
        noFill()
        strokeWeight(6)
        arc(75, 90, 35, 32.5, 0, PI) #left eye
        arc(125, 90, 35, 32.5, 0, PI) #right eye

    def deepDowncast(self):
        stroke(self.color)
        noFill()
        strokeWeight(6)
        arc(75, 90, 37, 40, 0, PI) #left eye
        arc(125, 90, 37, 40, 0, PI) #right eye

    def shallowSmile(self):
        stroke(self.color)
        noFill()
        strokeWeight(6)
        arc(75, 95, 37.5, 20, PI, TWO_PI) #left eye
        arc(125, 95, 37.5, 20, PI, TWO_PI) #right eye 

    def straightEyes(self):
        stroke(self.color)
        noFill()
        strokeWeight(6)
        line(55, 85, 90, 85) #left eye
        line(110, 85, 145, 85) #right eye

    def wideOpenEyes(self):
        strokeWeight(10)
        stroke(255) #color white
        ellipse(75,90,17.5,17.5) #left eye
        fill(255) #color white
        stroke(0) #color black
        fill(self.color)
        ellipse(75,90,5,5) #left eye
    
        strokeWeight(10)
        stroke(255) #color white
        ellipse(125,90,17.5,17.5) #right eye
        fill(255) #color white
        stroke(0) #color black
        fill(self.color)
        ellipse(125,90,5,5) #left eye

    def deepSmile(self):
        stroke(self.color)
        noFill()
        strokeWeight(6)
        arc(75, 95, 37.5, 30, PI, TWO_PI) #left eye
        arc(125, 95, 37.5, 30, PI, TWO_PI) #right eye

    def whiteEyes(self):
        strokeWeight(2)
        stroke(0) #color black
        fill(255)
        ellipse(75,90,25,32) #left eye
        ellipse(125,90,25,32) #right eye

    def display(self):  
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
            
        

    

        
