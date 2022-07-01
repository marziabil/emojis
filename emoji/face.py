class Face(object):
    
    #constructor
    def __init__(self, x, y, a, b):
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.diameter = 150 #Diameter of the face
        self.color = color(255, 204, 0) #color of skin
        
    def display(self):
        strokeWeight(6)
        fill(self.color)
        ellipse(self.x, self.y, self.diameter, self.diameter)
