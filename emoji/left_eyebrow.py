class lEyeBrow(object):
    
    #constructor
    def __init__(self, ebType):
        self.ebType = ebType #type of eyebrow
        
    def display(self):
        #horizontal arc
        if self.ebType == 'horizontal':
            strokeWeight(5)
            noFill()
            stroke(204, 153, 0)
            arc(75, 55, 37.5, 12.5, PI, TWO_PI)
        else:
            stroke(0) 
            line(75, 55, 95, 55)
        
        
        
    
