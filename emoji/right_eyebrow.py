class rEyeBrow(object):
    
    #constructor
    def __init__(self, ebType):
        self.ebType = ebType #type of eyebrow
        
    def display(self):
        #horizontal arc
        if self.ebType == 'none':
            noStroke()
            noFill()
        elif self.ebType == 'horizontal':
            strokeWeight(5)
            noFill()
            stroke(204, 153, 0)
            arc(125, 65, 37.5, 12.5, PI, TWO_PI)
        elif self.ebType == 'high':
            stroke(204, 153, 0)
            noFill()
            strokeWeight(6) 
            line(115, 50, 140, 75)
        else:
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(150, 60, 80, 30, HALF_PI, PI)
