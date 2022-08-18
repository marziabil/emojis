import py5

#no eyebrows
def noEyebrows(): 
    py5.no_stroke()

#straight eyebrows
def straightEyebrows(weight):
    py5.stroke_weight(5*weight)
    py5.stroke(204, 153, 0)
    py5.arc(75, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #left eyebrow
    py5.arc(125, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #right eyebrow

#slightly furrowed
def slightlyFurrowed(weight):
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6*weight)
    py5.arc(50-weight, 50+weight, 80+weight, 30, 0, py5.HALF_PI) #left eyebrow
    py5.arc(150-weight, 50+weight, 80+weight, 30, py5.HALF_PI, py5.PI) #right eyebrow

#highly furrowed orange
def highlyFurrowedOrange(weight):
    py5.stroke(204, 153, 0) #color of eyebrow - orange
    py5.stroke_weight(6*weight) 
    py5.line(60-weight, 65+weight, 85, 40+weight) #left eyebrow
    py5.line(115-weight, 40+weight, 140, 65+weight) #right eyebrow 
    

#highly furrowed black
def highlyFurrowedBlack(weight):
    py5.stroke(0) #color of eyebrow - black
    py5.stroke_weight(6*weight) 
    py5.line(60-weight, 50*weight, 85, 75) #left eyebrow
    py5.line(115-weight, 75, 140, 50*weight) #right eyebrow 
    

#raised eyebrows (lower positioned)
def raisedEyebrowsLow(weight):
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6*weight)
    py5.arc(160+weight, 75+weight, 225, 26*weight, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115+weight, 75+weight, 65, 20*weight, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow

#raised eyebrows (higher placed)
def raisedEyebrowsHigh(weight):
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6*weight)
    py5.arc(165+weight, 70+weight, 225, 26*weight, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115+weight, 70+weight, 65, 20*weight, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow  
    
    
def drawEyebrows(emotionalState, weight):
    if (emotionalState > 25.6 and emotionalState < 29) or (emotionalState > 30 and emotionalState < 36.899):
        noEyebrows() #no eyebrows
        
    elif (emotionalState > 16 and emotionalState < 21):
        straightEyebrows(weight) # straight eyebrows
        
    elif (emotionalState > 21 and emotionalState < 22.07) or (emotionalState > 29 and emotionalState < 30): 
        slightlyFurrowed(weight) 
        
    elif (emotionalState < -23 and emotionalState > -25):
        highlyFurrowedOrange(weight)
        
    elif (emotionalState < -21 and emotionalState > -23):
        highlyFurrowedBlack(weight)
    elif (emotionalState <-25 and emotionalState > -29):
        raisedEyebrowsLow(weight) #lower
    else: 
        raisedEyebrowsHigh(weight) #higher placed
