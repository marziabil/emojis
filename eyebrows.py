import py5

    #no eyebrows
def noEyebrows(): 
    py5.no_stroke()

#straight eyebrows
def straightEyebrows():
    py5.stroke_weight(5)
    py5.stroke(204, 153, 0)
    py5.arc(75, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #left eyebrow
    py5.arc(125, 65, 37.5, 12.5, py5.PI, py5.TWO_PI) #right eyebrow

#slightly furrowed
def slightlyFurrowed():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.arc(50, 50, 80, 30, 0, py5.HALF_PI) #left eyebrow
    py5.arc(150, 50, 80, 30, py5.HALF_PI, py5.PI) #right eyebrow

#highly furrowed orange
def highlyFurrowedOrange():
    py5.stroke(204, 153, 0) #color of eyebrow - orange
    py5.stroke_weight(6) 
    py5.line(60, 65, 85, 40) #left eyebrow
    py5.line(115, 40, 140, 65) #right eyebrow 

#highly furrowed black
def highlyFurrowedBlack():
    py5.stroke(0) #color of eyebrow - black
    py5.stroke_weight(6) 
    py5.line(60, 65, 85, 40) #left eyebrow
    py5.line(115, 40, 140, 65) #right eyebrow 
    

#raised eyebrows (lower positioned)
def raisedEyebrowsLow():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.arc(160, 80, 220, 20, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115, 80, 65, 20, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow

#raised eyebrows (higher placed)
def raisedEyebrowsHigh():
    py5.stroke(204, 153, 0)
    py5.stroke_weight(6)
    py5.arc(165, 70, 220, 20, py5.PI, py5.PI+py5.QUARTER_PI) #left eyebrow
    py5.arc(115, 70, 65, 20, py5.TWO_PI-py5.HALF_PI, py5.TWO_PI) #right eyebrow  

def drawEyebrows(emotionalState):
    if (emotionalState > 25.6 and emotionalState < 29 and emotionalState > 30 and emotionalState < 36.899):
        noEyebrows() #no eyebrows
        
    elif (emotionalState > 16 and emotionalState < 21):
        straightEyebrows() # straight eyebrows
        
    elif (emotionalState > 21 and emotionalState < 22.07) or (emotionalState > 29 and emotionalState < 30): 
        slightlyFurrowed() 
        
    elif (emotionalState < -23 and emotionalState > -25):
        highlyFurrowedOrange()
        
    elif (emotionalState < -20 and emotionalState > -23):
        highlyFurrowedBlack()
    elif (emotionalState <-25 and emotionalState > -29):
        raisedEyebrowsLow() #lower
    else: 
        raisedEyebrowsHigh() #higher placed



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