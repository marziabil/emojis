class RightEye(object):
    
    #constructor
    def __init__(self, eyeType):
        self.color = color(0) #color of eye
        self.eyeType = eyeType
        
    def display(self):
        if self.eyeType == 'oval':
            strokeWeight(8)
            fill(self.color)
            #ellipse(self.x, self.y, self.eyeWidth, self.eyeHeight)
            ellipse(125,80,5,12)
        elif self.eyeType == 'frown': #frowning eyes
            arc(125, 75, 32.5, 32.5, 0, PI)
        else: #horizontal v-shaped
            strokeWeight(8) #upper half of v
            line(115, 95, 135, 85)
            strokeWeight(6) #upper half of v
            line(135, 85, 155, 75)
            strokeWeight(8) # lower half of v
            line(115, 95, 135, 105)
            strokeWeight(6) # lower half of v
            line(135, 105, 155, 115)
        
             
