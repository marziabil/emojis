import py5

    #no eyebrows
def noEyebrows(): 
    py5.no_stroke()
    py5.no_fill()

#straight eyebrows
def straightEyebrows():
    py5.stroke_weight(5)
    py5.no_fill()
    py5.stroke(204, 153, 0)
    py5.arc(75, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #left eyebrow
    py5.arc(125, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #right eyebrow

#slightly furrowed
def slightlyFurrowed():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(50, 50, 80, 30, 0, py5.HALF_PI) #left eyebrow
    py5.arc(150, 50, 80, 30, py5.HALF_PI, py5.PI) #right eyebrow

#highly furrowed
def highlyFurrowed():
    py5.stroke(204, 153, 0) #color of eyebrow
    py5.stroke_weight(6) 
    py5.line(60, 65, 85, 40) #left eyebrow
    py5.line(115, 40, 140, 65) #right eyebrow 

#raised eyebrows (lower positioned)
def raisedEyebrows():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(160, 80, 220, 20, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115, 80, 65, 20, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow

#raised eyebrows (higher placed)
def raisedEyebrowsHigh():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.no_fill()
    py5.arc(165, 70, 220, 20, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115, 70, 65, 20, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow  


def drawEyebrows(ebType):
    if ebType == "no_eyebrows":
        noEyebrows() #no eyebrows:
    elif ebType == "straight":
        straightEyebrows() # straight eyebrows
    elif ebType == "slightly_furrowed":
        slightlyFurrowed() 
    elif ebType == "highly_furrowed":
        highlyFurrowed()
    elif ebType == "raised_eyebrows":
        raisedEyebrows()    
    else: 
        raisedEyebrowsHigh()