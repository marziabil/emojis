class Mouth(object):
    
    #constructor
    def __init__(self, x, y, c, d, e, f, mouthType, g):
        self.x = 100 # x-coordinate
        self.y = 150 # y-coordinate
        self.c = 70 #width of the arc's ellipse
        self.d = 50 # height of the arc's ellipse 
        self.color = color(0)
        self.mouthType = mouthType #frowning; open and frowning 
        self.g = g #mode of the arc
        
    def display(self):
        if self.mouthType == "frown":
            strokeWeight(6)
            arc(self.x, self.y, self.c, self.d, PI, TWO_PI) #frowning face
        else: #open mouth
            strokeWeight(6)
            fill(0)
            self.g = CHORD
            arc(self.x, self.y, self.c, self.d, PI, TWO_PI, self.g)
