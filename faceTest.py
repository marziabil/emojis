from py5 import Sketch

class Face(Sketch):

    # def __init__(self, faceColour):
    #     # self.xValence = xValence #x coordinate of emotion - valence
    #     # self.yArousal = yArousal #y coordinate of emotion - arousal
    #     self.faceColour = faceColour

    def settings(self):
        self.size(200,200)

    def draw(self):
        self.stroke_weight(5)
        self.stroke(0)
        self.fill(255, 204, 0)
        self.ellipse(self.width * 0.5, self.height * 0.5, 150, 150)

face = Face()
face.run_sketch()

    


    # def makeFace(self):
    #     self.stroke_weight(5)
    #     self.stroke(0)
    #     self.ellipse(self.width * 0.5, self.height * 0.5, 150, 150)

    # def display(self):
    #     if self.faceColour == "yellow":
    #         self.makeFace()
    #         self.fill(255, 204, 0) #yellow face
    #     else: 
    #         self.fill(255, 80, 80) #red color face
    #         self.makeFace()
           
        