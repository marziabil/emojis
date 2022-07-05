class Eyebrows(object):
    
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
            arc(75, 65, 37.5, 12.5, PI, TWO_PI) #left eyebrow
            arc(125, 65, 37.5, 12.5, PI, TWO_PI) #right eyebrow
        elif self.ebType == 'high': #highly furrowed
            stroke(204, 153, 0) #color of eyebrow
            strokeWeight(6) 
            line(60, 65, 85, 40) #left eyebrow
            line(115, 40, 140, 65) #right eyebrow
        else: #slightly furrowed
            stroke(204, 153, 0)
            strokeWeight(6)
            noFill()
            arc(50, 50, 80, 30, 0, HALF_PI) #left eyebrow
            arc(150, 50, 80, 30, HALF_PI, PI) #right eyebrow
        
        
    
