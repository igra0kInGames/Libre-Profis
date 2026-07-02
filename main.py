import pygame

from classes import *

pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
text = Text(screen, "Hello, world!", 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    text.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()