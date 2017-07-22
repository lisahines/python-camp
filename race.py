#This code WILL NOT run in repl.it!  You must 

#load it on a computer with pygame!

#get the required libraries

import pygame, sys, random

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

player1 = pygame.image.load("player1.png").convert()
player1 = pygame.transform.scale(player1, (50, 50))
player1.set_colorkey(BLACK)

player2 = pygame.image.load("player2.png").convert()
player2 = pygame.transform.scale(player2, (50, 50))
player2.set_colorkey(BLACK)


font = pygame.font.SysFont('Calibri', 25, True, False)



laser = False
#controls when we will be done

done = False

p1x = 0
p1y = 200
p2x = 0
p2y = 300
bulletx =         bulletx = random.randint(75, 350)        

bullety = 0
fireBullet = False
#main drawing loop
start_time = pygame.time.get_ticks() #keep track of starting time
l_sound = pygame.mixer.Sound("laser.wav")

while not done:

    #you can fill the screen with anything!

    screen.fill(WHITE)
    #starting line
    pygame.draw.line(screen, RED, (50, 0), (50, 400), 3)
    screen.blit(player1, [p1x, 200])
    screen.blit(player2, [p2x, 300])
    pygame.draw.circle(screen, BLACK, (bulletx, bullety), 20, 0)
    if fireBullet == True:
        bullety += 7
    if bullety > 400:
       fireBullet = False
       bulletx = random.randint(75, 350)        

       bullety = 0
    if p1x > bulletx - 60 and p1x < bulletx + 10 and bullety > 200 and bullety < 250:
       p1x = 0

    if p2x > bulletx - 60 and p2x < bulletx + 10 and bullety > 300 and bullety < 350:
       p2x = 0 
       
    if(pygame.time.get_ticks()-start_time >= 5000):#5000 = 5 seconds
        fireBullet = True
        if laser == True:
             laser = False
        else:
             laser = True        
        start_time = pygame.time.get_ticks() #reset the timer
    
    if laser == True:
         pygame.draw.line(screen, L_RED, (300, 0), (300, 400), 10)
    if laser == True and p1x > 250 and p1x < 300:
         p1x = 0
         l_sound.play()
    if laser == True and p2x > 250 and p2x < 300:
         p2x = 0
         l_sound.play()
    if p1x > 400:
         text = font.render("Player 1 wins",True,BLACK) 
         screen.blit(text, [250, 250])
         p2x = 0
    if p2x > 400:
         text = font.render("Player 2 wins", True, BLACK)
         screen.blit(text, [250, 250])
         p1x = 0

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

    clock.tick(30)

pygame.quit()


