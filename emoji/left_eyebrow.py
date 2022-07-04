class lEyeBrow(object):
    
    #constructor
    def __init__(self, ebType):
        self.ebType = ebType #type of eyebrow
        
    def display(self):
        if self.ebType == 'none':
            noStroke()
            noFill()
        #horizontal arc
        elif self.ebType == 'horizontal':
            strokeWeight(5)
            noFill()
            stroke(204, 153, 0)
            arc(75, 65, 37.5, 12.5, PI, TWO_PI)
        elif self.ebType == 'high':
            stroke(204, 153, 0)
            strokeWeight(6) 
            line(60, 75, 85, 50)
        else:
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(50, 60, 80, 30, 0, HALF_PI)
        
        
    
