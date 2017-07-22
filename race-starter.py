#This code WILL NOT run in repl.it!  You must 

#load it on a computer with pygame!

#get the required libraries

import pygame, sys

from pygame.locals import *



#start up pygame

pygame.init()



#two free colours!  Feel free to add more!

#a great colour scheme creator is coolors.co

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
L_RED = (255, 100, 100)
#import the clock and get the window set up

clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Amazing Racer") #sets the title for the window



#controls when we will be done

done = False

p1x = 0
p1y = 200
p2x = 0
p2y = 300
#main drawing loop

while not done:

    #you can fill the screen with anything!

    screen.fill(WHITE)
    #starting line
    pygame.draw.line(screen, RED, (50, 0), (50, 400), 3)
    pygame.draw.rect(screen, BLUE, (p1x, 200, 50, 50), 0)
    pygame.draw.rect(screen, GREEN, (p2x, 300, 50, 50), 0)
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
          if(event.key == pygame.K_SPACE):
            print("you pressed space!")
          if event.key == pygame.K_RIGHT:
            p1x = p1x + 10
          if event.key == pygame.K_d:
            p2x = p2x + 10
          #do stuff here!
    pygame.display.flip()

    clock.tick(10)

pygame.quit()


