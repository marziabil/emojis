import py5

def makeFace():
    py5.stroke_weight(5)
    py5.stroke(0)
    py5.ellipse(py5.width * 0.5, py5.height * 0.5, 150, 150)

def drawFace(emotionalState):
    if emotionalState >= -28.33173105 and emotionalState <= 25.60251348:
        makeFace()
        py5.fill(255, 80, 80) #red color face
    else: 
        makeFace()
        py5.fill(255, 204, 0) #yellow face
        