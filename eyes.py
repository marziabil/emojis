import py5
    
def xShaped():
    py5.stroke(0)
    py5.stroke_weight(6) #upper half of x and thinner part
    py5.line(45,75,65,85)
    py5.stroke_weight(8) #upper half of x and thicker part
    py5.line(65,85,85,95)
    py5.stroke_weight(8) #lower half of x and thicker part
    py5.line(65,105, 85, 95)
    py5.stroke_weight(6) #lower half of x and thinner part
    py5.line(45, 115, 65, 105)
    
    #right eye
    py5.stroke(0)
    py5.stroke_weight(8) #upper half of x
    py5.line(115, 95, 135, 85)
    py5.stroke_weight(6) #upper half of x
    py5.line(135, 85, 155, 75)
    py5.stroke_weight(8) # lower half of x
    py5.line(115, 95, 135, 105)
    py5.stroke_weight(6) # lower half of x
    py5.line(135, 105, 155, 115)

def ovalEyes():
    py5.stroke_weight(10)
    py5.stroke(0) #color black
    py5.ellipse(75,90,5,12) #left eye
    py5.ellipse(125,90,5,12) #right eye

def shallowDowncast():
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.arc(75, 90, 35, 32.5, 0, py5.PI) #left eye
    py5.arc(125, 90, 35, 32.5, 0, py5.PI) #right eye

def deepDowncast():
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.arc(75, 90, 37, 40, 0, py5.PI) #left eye
    py5.arc(125, 90, 37, 40, 0, py5.PI) #right eye

def smilingEyes():
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.arc(75, 95, 37.5, 20, py5.PI, py5.TWO_PI) #left eye
    py5.arc(125, 95, 37.5, 20, py5.PI, py5.TWO_PI) #right eye 

def straightEyes():
    py5.stroke(0)
    py5.stroke_weight(6)
    py5.line(55, 85, 90, 85) #left eye
    py5.line(110, 85, 145, 85) #right eye

def wideOpenEyes():
    py5.stroke_weight(10)
    py5.stroke(255) #color white
    py5.ellipse(75,90,25,25) #left eye
    py5.fill(255) #color white
    py5.stroke(0) #color black
    py5.fill(0)
    py5.ellipse(75,90,8,8) #left eye

    py5.stroke_weight(10)
    py5.stroke(255) #color white
    py5.ellipse(125,90,25,25) #right eye
    py5.fill(255) #color white
    py5.stroke(0) #color black
    py5.fill(0)
    py5.ellipse(125,90,8,8) #left eye

def whiteEyes():
    py5.stroke_weight(2)
    py5.stroke(0) #color black
    py5.fill(255)
    py5.ellipse(75,90,25,32) #left eye
    py5.ellipse(125,90,25,32) #right eye
    py5.no_fill()
    

def drawEyes(emotionalState):  
    if (emotionalState > 22 and emotionalState < 23):
        xShaped()  
    elif (emotionalState > 13 and emotionalState < 17) or (emotionalState < -21 and emotionalState > -25.34) or (emotionalState > 23 and emotionalState < 24) or (emotionalState < -28 and emotionalState > -30):
        ovalEyes()  
    elif (emotionalState > 24 and emotionalState <  26):
        shallowDowncast()
    elif (emotionalState <-20 and emotionalState > -28):
        deepDowncast()
    elif (emotionalState > 26 and emotionalState < 29):
        smilingEyes()
    elif (emotionalState < -12 and emotionalState > -21):
        straightEyes()
    elif (emotionalState < 37 and emotionalState > 29) or (emotionalState > 12 and emotionalState < 13): 
        wideOpenEyes()    
    else: 
        whiteEyes()
            
        
# def deepSmile():
#     py5.stroke(0)
#     py5.no_fill()
#     py5.stroke_weight(6)
#     py5.arc(75, 95, 37.5, 30, py5.PI, py5.TWO_PI) #left eye
#     py5.arc(125, 95, 37.5, 30, py5.PI, py5.TWO_PI) #right eye

        
