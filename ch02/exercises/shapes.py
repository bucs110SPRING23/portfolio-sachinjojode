import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("black")

pygame.draw.circle(screen, "white", (300,400), 150)
pygame.display.flip()
pygame.draw.circle(screen, "white", (300,225), 100)
pygame.display.flip()
pygame.draw.circle(screen, "white", (300,100), 50)
pygame.display.flip()

#pygame.display.update()
pygame.time.wait(1000)
