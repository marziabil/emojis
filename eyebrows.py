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
    py5.arc(50-weight, 50+weight, 80+weight, 30+weight, 0, py5.HALF_PI) #left eyebrow
    py5.arc(150-weight, 50+weight, 80+weight, 30+weight, py5.HALF_PI, py5.PI) #right eyebrow
    print("a")
    

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
    py5.line(60-weight, 50+weight, 85, 75+weight) #left eyebrow
    py5.line(115-weight, 75+weight, 140, 50+weight) #right eyebrow 
    

#raised eyebrows (lower positioned)
def raisedEyebrowsLow(weight):
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6*weight)
    py5.arc(160-weight, 75+weight, 225+weight, 20+weight, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115+weight, 75+weight, 65+weight, 20+weight, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow
    

#raised eyebrows (higher placed)
def raisedEyebrowsHigh(weight):
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6*weight)
    py5.arc(165-weight, 70+weight, 220+weight, 20+weight, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115+weight, 70+weight, 65+weight, 20+weight, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow  
    
    
def drawEyebrows(emotionalState, weight):
    if (emotionalState > 25.6 and emotionalState < 29 and emotionalState > 30 and emotionalState < 36.899):
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



# def drawEyebrows(emotionalState):
#     if (emotionalState > 25.6 and emotionalState < 36.899) or (emotionalState > -25.34 and emotionalState < -12.1250158):
#         noEyebrows() #no eyebrows:
#     elif (emotionalState > 3.1 and emotionalState < 9.42):
#         straightEyebrows() # straight eyebrows
#     elif (emotionalState > 9.42 and emotionalState < 15.74): 
#         slightlyFurrowed() 
#     elif (emotionalState > 15.74 and emotionalState < 22.06):
#         highlyFurrowed()
#     elif (emotionalState <-25.94 and emotionalState > -29.81):
#         raisedEyebrows() #lower
#     else: 
#         raisedEyebrowsHigh() #higher places

# def drawEyebrows(emotionalState):
#     if (emotionalState > 25.6 and emotionalState < 36.899) or (emotionalState < -25.34 and emotionalState > -12.1250158):
#         noEyebrows() #no eyebrows:
#     elif (emotionalState > 12.46 and emotionalState < 22.06 and emotionalState < 19.5 and emotionalState < 18.91):
#         straightEyebrows() # straight eyebrows
#     elif (emotionalState > 23.1 and emotionalState > 20.96 and emotionalState < -20 and emotionalState < -28.59) or (emotionalState > 24.4 and emotionalState > -22 and emotionalState < 18.91 and emotionalState < 25.6):
#         slightlyFurrowed() 
#     elif (emotionalState > 24.4 and emotionalState > 23.959 and emotionalState < 20.96 and emotionalState <23.01 ):
#         highlyFurrowed()
#     elif (emotionalState > 25.75 and emotionalState > 27.87 and emotionalState < 28.979 and emotionalState < 29.81):
#         raisedEyebrows() #lower
#     else: 
#         raisedEyebrowsHigh() #higher places