import pygame
pygame.init()
size = width, height = 500, 500

screen = pygame.display.set_mode(size)
hyp = line(screen, (255,0,0), (100,400), (400,100), 1)

clock.tick(20)
pygame.display.flip()
