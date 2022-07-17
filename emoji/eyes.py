class Eyes(object):
    
    #constructor
    def __init__(self, xValence, yArousal):
        self.color = color(0) #color of eye - black
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal
    
    def display(self): 
        #x-shaped eyes   
        if (self.xValence <= -0.9 and self.xValence <=-1) or (self.yArousal <= -0.9 and self.yArousal <=-1 ):  
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
        elif (self.xValence < 0 and self.xValence >= -0.5) and (self.yArousal < 0 and self.yArousal >= -0.5):
            #oval eyes
            strokeWeight(10)
            stroke(0) #color black
            fill(self.color)
            ellipse(75,90,5,12) #left eye
            ellipse(125,90,5,12) #right eye
        elif self.xValence < -0.5 and self.xValence > -0.9 and self.yArousal < -0.5 and self.yArousal > - 0.9:
            #frowning eyes - shallow
            stroke(self.color)
            noFill()
            strokeWeight(6)
            arc(75, 90, 35, 32.5, 0, PI) #left eye
            arc(125, 90, 35, 32.5, 0, PI) #right eye
        elif self.xValence > 0 and self.xValence <= 0.55 and self.yArousal <= -0.6 and self.yArousal <= -1: 
            #frowning eyes (deeper)
            stroke(self.color)
            noFill()
            strokeWeight(6)
            arc(75, 90, 37, 40, 0, PI) #left eye
            arc(125, 90, 37, 40, 0, PI) #right eye
        elif self.xValence >= 0.6 and self.xValence <= 0.75 and self.yArousal <= -0.6 and self.yArousal >= 0.75:
            #upward shaped arc
            stroke(self.color)
            noFill()
            strokeWeight(6)
            arc(75, 95, 37.5, 20, PI, TWO_PI) #left eye
            arc(125, 95, 37.5, 20, PI, TWO_PI) #right eye
        else:
            #straight line 
            stroke(self.color)
            noFill()
            strokeWeight(6)
            line(55, 85, 90, 85) #left eye
            line(110, 85, 145, 85)

    

        
