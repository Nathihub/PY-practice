
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.draw.rect(

screen,

(0, 125, 255),

pygame.Rect(30, 30, 60, 60)
)
pygame.draw.circle(screen, 'GREEN', (300, 300), 50) # solid

pygame.draw.circle(screen, 'GREEN', (100, 100), 50, 3) # hollow, 3px outline