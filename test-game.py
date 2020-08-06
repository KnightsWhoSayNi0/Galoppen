#!/usr/bin/python

#galoppen game written in python with pygame
#TODO: Fix quit

import pygame, sys, serial, array
from pygame.locals import *
from pygame import *

#serial things
port = "/dev/ttyACM0"
s1=serial.Serial(port,9600)
s1.flushInput()

#init pygame
pygame.init()

beep = pygame.mixer.Sound("beep.wav")
highBeep = pygame.mixer.Sound("high.wav")
mediumBeep = pygame.mixer.Sound("med.wav")
lowBeep = pygame.mixer.Sound("low.wav")

gameWindow = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Galoppen')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

gameWindow.fill(WHITE)

#horse/hole init
#position = 50
#pygame.draw.rect(gameWindow, RED, (50, 50, 50, position))

YellowX = [400, 350, 450, 300, 500, 250, 550]
YellowY = [550, 500, 500, 450, 450, 400, 400]
BlueX = [400, 350, 450, 300, 500, 250, 550]
BlueY = [500, 450, 450, 400, 400, 350, 350]
RedX = [400, 400]
RedY = [450, 400]

#Yellow and Blue Holes
for x in range(7):
    pygame.draw.circle(gameWindow, YELLOW, (YellowX[x], YellowY[x]), 20, 4)
    pygame.draw.circle(gameWindow, BLUE, (BlueX[x], BlueY[x]), 20, 4)

#Red Holes
pygame.draw.circle(gameWindow, RED, (RedX[0], RedY[0]), 20, 4)
pygame.draw.circle(gameWindow, RED, (RedX[1], RedY[1]), 20, 4)

pygame.display.update()

# main pygame loop
while True:
    for event in pygame.event.get(): #TODO: fix broken quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    tdata =s1.read()
    cdata =tdata.decode("utf-8")
        
    # if serial read 1 (yellow hole); blink yellow hole and beep
    if cdata == "0":
        tdata =s1.read()
        cdata =tdata.decode("utf-8")
        if cdata == "o":
            pygame.draw.circle(gameWindow, YELLOW, (400, 550), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(lowBeep)
        else:
            pygame.draw.circle(gameWindow, WHITE, (400, 550), 16)
            pygame.display.update()
        
        #position = position + 50
        #pygame.draw.rect(gameWindow, YELLOW, (50, 50, position, 50))
    
    # if serial read 2 (blue hole); blink blue hole and beep
    if cdata == "1":
        tdata =s1.read()
        cdata =tdata.decode("utf-8")
        if cdata == "o":
            pygame.draw.circle(gameWindow, BLUE, (400, 500), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(mediumBeep)
        else:
            pygame.draw.circle(gameWindow, WHITE, (400, 500), 16)
            pygame.display.update()
        
        #position = position + 100
        #pygame.draw.rect(gameWindow, BLUE, (50, 50, position, 50))
        
    # if serial read 3 (red hole); blink 
    if cdata == "2":
        tdata =s1.read()
        cdata =tdata.decode("utf-8")
        if cdata == "o":
            pygame.draw.circle(gameWindow, RED, (400, 450), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(highBeep)
        else:
            pygame.draw.circle(gameWindow, WHITE, (400, 450), 16)
            pygame.display.update()
        
        #position = position + 200
        #pygame.draw.rect(gameWindow, RED, (50, 50, position, 50))

sys.exit()
            
            