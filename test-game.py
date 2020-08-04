#!/usr/bin/python

#galoppen game written in python with pygame
#TODO: 

import pygame, sys, serial
from pygame.locals import *

#serial things
port = "/dev/ttyACM0"
s1=serial.Serial(port,9600)
s1.flushInput()

#init pygame
pygame.init()

beep = pygame.mixer.Sound("beep.wav")
#pygame.mixer.Sound.play(beep)

gameWindow = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Galoppen')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

gameWindow.fill(WHITE)

#horse init
position = 50
#pygame.draw.rect(gameWindow, RED, (50, 50, 50, position))

pygame.draw.circle(gameWindow, YELLOW, (400, 550), 20, 4)

pygame.display.update()

while True:
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    tdata =s1.read()
    cdata =tdata.decode("utf-8")
        
    # if serial read 1 (yellow hole); give 50 points
    if cdata == "0":
        tdata =s1.read()
        cdata =tdata.decode("utf-8")
        if cdata == "o":
            pygame.draw.circle(gameWindow, YELLOW, (400, 550), 20)
            pygame.display.update()
            pygame.mixer.Sound.play(beep)
        else:
            pygame.draw.circle(gameWindow, WHITE, (400, 550), 16)
            pygame.display.update()
        
        #position = position + 50
        #pygame.draw.rect(gameWindow, YELLOW, (50, 50, position, 50))
    
    # if serial read 2 (blue hole); give 100 points
    if cdata == "1":
        position = position + 100
        pygame.draw.rect(gameWindow, BLUE, (50, 50, position, 50))
        pygame.display.update()
        
    # if serial read 3 (red hole); give 200 points
    if cdata == "2":
        position = position + 200
        pygame.draw.rect(gameWindow, RED, (50, 50, position, 50))
        pygame.display.update()
        

sys.exit()
            
            