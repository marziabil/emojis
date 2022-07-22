
class Face(object):

    def __init__(self, xValence, yArousal):
        self.xValence = xValence #x coordinate of emotion - valence
        self.yArousal = yArousal #y coordinate of emotion - arousal

    def drawFace(self):
        strokeWeight(5)
        stroke(0)
        ellipse(width * 0.5, height * 0.5, 150, 150)

    def display(self):
        if self.xValence < 0 and self.xValence >= -0.4 and self.yArousal >= 0.4 and self.yArousal <= 0.75: 
            fill(255, 204, 0) #red color face
            self.drawFace()
        else: 
            fill(255, 80, 80) #yellow face
            self.drawFace()
           