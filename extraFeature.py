from math import radians
from turtle import width
import py5

def noFeature():
    py5.no_stroke()

def flushedCheeks():
    py5.no_stroke()
    py5.fill(247,137,74)
    py5.ellipse(60, 110, 22, 22) #left cheek
    py5.ellipse(140, 110, 22, 22 ) #right cheek
    py5.no_fill()

def darkFlushedCheeks():
    py5.no_stroke()
    py5.fill(172, 11, 25)
    py5.ellipse(60, 110, 22, 22) #left cheek
    py5.ellipse(140, 110, 22, 22 ) #right cheek
    py5.no_fill()

def tearDrop():
    py5.no_stroke()
    py5.fill(0,188,242) #fill with blue
    lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in range(0, len(lis), 1):
        py5.ellipse(60, 90 + i*2, i*2, i*2)
    py5.no_fill()


def drawFeature(emotionalState):
    if (emotionalState > 26 and emotionalState < 29.6) or (emotionalState > 12 and emotionalState < 13):
        flushedCheeks()
    elif (emotionalState > 16 and emotionalState < 24):
        tearDrop()
    elif (emotionalState <-21 and emotionalState >-23):
        darkFlushedCheeks()
    else: 
        noFeature()