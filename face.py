import py5

def makeFace():
    py5.stroke_weight(8.5)
    py5.stroke(0)
    py5.ellipse(py5.width * 0.5, py5.height * 0.5, 150, 150)
    py5.no_fill()
    
def drawFace(emotionalState):
    if (emotionalState <-21 and emotionalState >-23):
        py5.fill(240, 58, 23) #red face
        makeFace()
    else: 
        py5.fill(255, 204, 0) #yellow face
        makeFace()


        