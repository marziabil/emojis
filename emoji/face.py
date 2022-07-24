
class Face(object):

    def __init__(self, faceColour ):
        # self.xValence = xValence #x coordinate of emotion - valence
        # self.yArousal = yArousal #y coordinate of emotion - arousal
        self.faceColour = faceColour

    def drawFace(self):
        strokeWeight(5)
        stroke(0)
        ellipse(width * 0.5, height * 0.5, 150, 150)

    def display(self):
        if self.faceColour == "yellow":
            fill(255, 204, 0) #yellow face
            self.drawFace()
        else: 
            fill(255, 80, 80) #red color face
            self.drawFace()
           
        