import py5

def makeFace():
    py5.stroke_weight(5)
    py5.stroke(0)
    py5.ellipse(py5.width * 0.5, py5.height * 0.5, 150, 150)

def drawFace(faceColour):
    if faceColour == "yellow":
        py5.fill(255, 204, 0) #yellow face
        makeFace()
    else: 
        py5.fill(255, 80, 80) #red color face
        makeFace()
        