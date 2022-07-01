class LeftEye(object):
    
    #constructor
    def __init__(self, x, y, a, b, eyeType):
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.eyeWidth = 5 #Diameter of the eye
        self.eyeHeight = 12 #Eye height
        self.color = color(0) #color of eye
        self.eyeType = eyeType #frowning, oval 
        
    def display(self):
        if self.eyeType == 'oval': #oval eyes
            strokeWeight(8)
            fill(self.color)
            ellipse(self.x, self.y, self.eyeWidth, self.eyeHeight)
        elif self.eyeType == 'frown': #frowning eyes
            arc(75, 75, 32.5, 32.5, 0, PI)
        else: #horizontal v-shaped
            strokeWeight(6) #upper half of v
            line(45,75,65,85)
            strokeWeight(8)
            line(65,85,85,95)
            strokeWeight(8) #lower half of v
            line(65,105, 85, 95)
            strokeWeight(6)
            line(45, 115, 65, 105)
