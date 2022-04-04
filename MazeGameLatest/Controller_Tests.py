import pygame
from pygame.locals import *
pygame.joystick.init()
pygame.init()

testing = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((100, 100))

while testing:
    joystick = pygame.joystick.get_count()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                testing = False
            elif event.key == K_UP:
                print('Hi')
    clock.tick(30)