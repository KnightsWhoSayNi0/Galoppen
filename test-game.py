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

# score setup
#TODO: add game star button and subsequent code.
score = 0

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'Score: {score}', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (800 // 2, 100 // 2)

# main pygame loop
while True:
    
    # draw score text
    text = font.render(f'Score: {score}', True, BLACK, WHITE)
    gameWindow.blit(text, textRect)
    pygame.display.update()
    
    tdata1 =s1.read()
    cdata1 =tdata1.decode("utf-8")
    num1 = cdata1
    tdata2 =s1.read()
    cdata2 =tdata2.decode("utf-8")
    num2 = cdata2
    fullnum = int(num1 + num2)
        
    tdata = s1.read()
    cdata = tdata.decode("utf-8")
    if cdata == "o":
        if fullnum < 7:
            pygame.draw.circle(gameWindow, YELLOW, (YellowX[fullnum], YellowY[fullnum]), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(lowBeep)
            score = score + 1
        if fullnum > 6 and fullnum < 14:
            pygame.draw.circle(gameWindow, BLUE, (BlueX[fullnum-7], BlueY[fullnum-7]), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(mediumBeep)
            score = score + 2
        if fullnum > 13 and fullnum < 16:
            pygame.draw.circle(gameWindow, RED, (RedX[fullnum-14], RedY[fullnum-14]), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(highBeep)
            score = score + 3
    else:
        if fullnum < 7:
            pygame.draw.circle(gameWindow, WHITE, (YellowX[fullnum], YellowY[fullnum]), 16)
            pygame.display.update()
        if fullnum > 6 and fullnum < 14:
            pygame.draw.circle(gameWindow, WHITE, (BlueX[fullnum-7], BlueY[fullnum-7]), 16)
            pygame.display.update()
        if fullnum > 13 and fullnum < 16:
            pygame.draw.circle(gameWindow, WHITE, (RedX[fullnum-14], RedY[fullnum-14]), 16)
            pygame.display.update()
        
    for event in pygame.event.get(): #TODO: fix broken quit
        if event.type == QUIT:
            pygame.quit()
            quit()
            sys.exit()


sys.exit()
            
            
