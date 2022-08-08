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
    py5.fill(0)
    py5.ellipse(75,90,5,12) #left eye
    py5.ellipse(125,90,5,12) #right eye

def shallowDowncast():
    py5.stroke(0)
    py5.no_fill()
    py5.stroke_weight(6)
    py5.arc(75, 90, 35, 32.5, 0, py5.PI) #left eye
    py5.arc(125, 90, 35, 32.5, 0, py5.PI) #right eye

def deepDowncast():
    py5.stroke(0)
    py5.no_fill()
    py5.stroke_weight(6)
    py5.arc(75, 90, 37, 40, 0, py5.PI) #left eye
    py5.arc(125, 90, 37, 40, 0, py5.PI) #right eye

def smilingEyes():
    py5.stroke(0)
    py5.no_fill()
    py5.stroke_weight(6)
    py5.arc(75, 95, 37.5, 20, py5.PI, py5.TWO_PI) #left eye
    py5.arc(125, 95, 37.5, 20, py5.PI, py5.TWO_PI) #right eye 

def straightEyes():
    py5.stroke(0)
    py5.no_fill()
    py5.stroke_weight(6)
    py5.line(55, 85, 90, 85) #left eye
    py5.line(110, 85, 145, 85) #right eye

def wideOpenEyes():
    py5.stroke_weight(10)
    py5.stroke(255) #color white
    py5.ellipse(75,90,17.5,17.5) #left eye
    py5.fill(255) #color white
    py5.stroke(0) #color black
    py5.fill(0)
    py5.ellipse(75,90,5,5) #left eye

    py5.stroke_weight(10)
    py5.stroke(255) #color white
    py5.ellipse(125,90,17.5,17.5) #right eye
    py5.fill(255) #color white
    py5.stroke(0) #color black
    py5.fill(0)
    py5.ellipse(125,90,5,5) #left eye

def whiteEyes():
    py5.stroke_weight(2)
    py5.stroke(0) #color black
    py5.fill(255)
    py5.ellipse(75,90,25,32) #left eye
    py5.ellipse(125,90,25,32) #right eye

def drawEyes(emotionalState):  
    if (emotionalState > 22 and emotionalState < 24):
        xShaped()  
    elif (emotionalState > 12 and emotionalState < 22):
        ovalEyes()  
    elif (emotionalState <-22 and emotionalState > -29):
        shallowDowncast()
    elif (emotionalState <-20 and emotionalState > -29):
        deepDowncast()
    elif (emotionalState < 29 and emotionalState > 22):
        smilingEyes()
    elif eyeType == "straightEyes":
        straightEyes()
    elif (emotionalState < 37 and emotionalState > 29): 
        wideOpenEyes()    
    else: 
        whiteEyes()
            
        
# def deepSmile():
#     py5.stroke(0)
#     py5.no_fill()
#     py5.stroke_weight(6)
#     py5.arc(75, 95, 37.5, 30, py5.PI, py5.TWO_PI) #left eye
#     py5.arc(125, 95, 37.5, 30, py5.PI, py5.TWO_PI) #right eye

        
