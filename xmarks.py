#This code WILL NOT run in repl.it!  You must 
#load it on a computer with pygame!
#get the required libraries
import pygame, sys, random, math
from pygame.locals import *

#start up pygame
pygame.init()

#two free colours!  Feel free to add more!
#a great colour scheme creator is coolors.co
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#import the clock and get the window set up
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Spots!") #sets the title for the window
spots = []
guesses = []
#controls when we will be done
done = False
font = pygame.font.SysFont('Calibri', 25, True, False)
x = random.randint(0, 375)
y = random.randint(0, 375)
cols = [(100, 255, 100), (255, 100, 100), (100, 100, 255)]
#main drawing loop
while not done:
#you can fill the screen with anything!
	screen.fill(WHITE)
	
	for i in range(len(spots)):
		text = font.render(str(i), True, BLACK)
		
		a = spots[i]
		pygame.draw.rect(screen, a[2], (a[0], a[1], 8,8), 0)
		screen.blit(text, [a[0], a[1]])
		t = guesses[i]
		pygame.draw.circle(screen, t[2], (t[0], t[1]), 10, 0)
		screen.blit(text, [t[0], t[1]])
	text = font.render("Click on point (" + str(x) + ", " + str(y) + ")",True,BLACK) 
	screen.blit(text, [0, 250])
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
		if event.type == pygame.MOUSEBUTTONDOWN:
			psn = pygame.mouse.get_pos()
			mx = psn[0]
			my = psn[1]
			col = cols[random.randint(0, len(cols)-1)]
			spots.append([x, y, col])
			guesses.append([mx, my, col])
			d = math.sqrt((mx - x)**2 + (my - y)**2)
			if d > 100:
				text = font.render("A little far!", True, BLACK)
				screen.blit(text, [0, 350])
			else:
				print("Great!", d)
				text = font.render("Great!", True, BLACK)
				screen.blit(text, [0, 350])
			pygame.draw.circle(screen, BLACK, (x, y), 10, 0)
			x = random.randint(0, 375)
			y = random.randint(0, 375)
                
	pygame.display.flip()
	clock.tick(10)
pygame.quit()

