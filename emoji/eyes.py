class Eyes(object):
    
    #constructor
    def __init__(self, xValence, yArousal):
        self.color = color(0) #color of eye - black
        #self.eyeType = eyeType #frowning, oval 
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal
    
    def display(self):    
        if self.xValence <= -0.9 or self.yArousal <= -0.9:  #v-shaped eyes
            stroke(self.color)
            strokeWeight(6) #upper half of v and thinner part
            line(45,75,65,85)
            strokeWeight(8) #upper half of v and thicker part
            line(65,85,85,95)
            strokeWeight(8) #lower half of v and thicker part
            line(65,105, 85, 95)
            strokeWeight(6) #lower half of v and thinner part
            line(45, 115, 65, 105)
            
            #right eye
            stroke(self.color)
            strokeWeight(8) #upper half of v
            line(115, 95, 135, 85)
            strokeWeight(6) #upper half of v
            line(135, 85, 155, 75)
            strokeWeight(8) # lower half of v
            line(115, 95, 135, 105)
            strokeWeight(6) # lower half of v
            line(135, 105, 155, 115) 
        elif (self.xValence < 0 and self.xValence >= -0.5) or (self.yArousal < 0 and self.yArousal >= -0.5):
            #oval eyes
            strokeWeight(10)
            stroke(0) #color black
            fill(self.color)
            ellipse(75,90,5,12) #left eye
            ellipse(125,90,5,12) #right eye
        else: #frowning eyes
            stroke(self.color)
            noFill()
            strokeWeight(6)
            arc(75, 90, 35, 32.5, 0, PI) #left eye
            arc(125, 90, 35, 32.5, 0, PI) #right eye
            #left eye
   
           
            
        
