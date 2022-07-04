class LeftEye(object):
    
    #constructor
    def __init__(self, eyeType):
        self.color = color(0) #color of eye
        self.eyeType = eyeType #frowning, oval 
    
    def display(self):
        if self.eyeType == 'oval': #oval eyes
            strokeWeight(10)
            stroke(0)
            fill(self.color)
            ellipse(75,90,5,12)
        elif self.eyeType == 'frown': #frowning eyes
            stroke(0)
            noFill()
            strokeWeight(6)
            arc(75, 90, 35, 32.5, 0, PI)
        else: #horizontal v-shaped
            strokeWeight(6) #upper half of v and thinner part
            line(45,75,65,85)
            strokeWeight(8) #upper half of v and thicker part
            line(65,85,85,95)
            strokeWeight(8) #lower half of v and thicker part
            line(65,105, 85, 95)
            strokeWeight(6) #lower half of v and thinner part
            line(45, 115, 65, 105)
            
        
