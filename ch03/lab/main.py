import pygame
import random
import math

#Part A: Create dartboard
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("black")

pygame.draw.circle(screen, "white", (300,300), 300)
pygame.display.flip()
pygame.draw.line(screen, "black", (300,0), (300,600), width=2)
pygame.display.flip()
pygame.draw.line(screen, "black", (0,300), (600,300), width=2)
pygame.display.flip()

#Part B: Throwing darts
for i in range(10):
    x = random.randrange(0,600)
    y = random.randrange(0,600)
    x0 = 300
    y0 = 300
    width = 600

    distance_from_center = math.hypot(x-x0, y-y0) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width

    if is_in_circle == True:
        pygame.draw.circle(screen, "green", (x,y), 5)
        pygame.display.flip()
    elif is_in_circle == False:
        pygame.draw.circle(screen, "red", (x,y), 5)
        pygame.display.flip()

    #pygame.display.update()
    pygame.time.wait(500)