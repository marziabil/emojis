
class Face(object):

    def __init__(self, xValence, yArousal):
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal

    # def faceColor(self):
    #     strokeWeight(5)
    #     stroke(0)
    #     ellipse(width * 0.5, height * 0.5, 150, 150)

    # def display(self):
    #     if self.xValence < 0 and self.xValence >= -0.4 and self.yArousal >= 0.4 and self.yArousal <= 0.75: 
    #         def faceColor(self): 
    #             fill(255, 204, 0) #red color face
    #     else: 
    #         def faceColor(self): 
    #             fill(255, 80, 80)    

    
    def display(self):
        if self.xValence < 0 and self.xValence >= -0.4 and self.yArousal >= 0.4 and self.yArousal <= 0.75:
        #red color face
            strokeWeight(5)
            stroke(0)
            fill(255, 204, 0)
            ellipse(width * 0.5, height * 0.5, 150, 150)
        else: 
        #yellow color face
            strokeWeight(5)
            stroke(0)
            fill(255, 80, 80)
            ellipse(width * 0.5, height * 0.5, 150, 150)
