class Eyes(object):
    
    #constructor
    def __init__(self, eyeType):
        self.color = color(0) #color of eye - black
        self.eyeType = eyeType #frowning, oval 
    
    def display(self):
        if self.eyeType == 'oval': #oval eyes
            strokeWeight(10)
            stroke(0) #color black
            fill(self.color)
            ellipse(75,90,5,12) #left eye
            ellipse(125,90,5,12) #right eye
        elif self.eyeType == 'frown': #frowning eyes
            stroke(self.color)
            noFill()
            strokeWeight(6)
            arc(75, 90, 35, 32.5, 0, PI)
            arc(125, 90, 35, 32.5, 0, PI)
        else: #horizontal v-shaped
            #left eye
            strokeWeight(6) #upper half of v and thinner part
            line(45,75,65,85)
            strokeWeight(8) #upper half of v and thicker part
            line(65,85,85,95)
            strokeWeight(8) #lower half of v and thicker part
            line(65,105, 85, 95)
            strokeWeight(6) #lower half of v and thinner part
            line(45, 115, 65, 105)
            
            #right eye
            strokeWeight(8) #upper half of v
            line(115, 95, 135, 85)
            strokeWeight(6) #upper half of v
            line(135, 85, 155, 75)
            strokeWeight(8) # lower half of v
            line(115, 95, 135, 105)
            strokeWeight(6) # lower half of v
            line(135, 105, 155, 115)
            
        
