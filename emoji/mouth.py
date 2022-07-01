class Mouth(object):
    
    #constructor
    def __init__(self, x, y, c, d, e, f):
        self.x = 100 # x-coordinate
        self.y = 150 # y-coordinate
        self.c = 70 #width of the arc's ellipse
        self.d = 50 # height of the arc's ellipse 
        self.color = color(0)
        
    def display(self):
        strokeWeight(6)
        arc(self.x, self.y, self.c, self.d, PI, TWO_PI) #frowning face
        
        #now write code for open mouth
