import pygame
import sys
from pygame.locals import *

Walls = []
Edges = []

pygame.init()
from EnemyTest import *

level = 0
red = (255, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (40, 40, 40)
brown = (129, 68, 15)

o.player_pos = (0, 0)


def LevelSetup(_level):
    _x = 0
    _y = 0
    for row in Levelslist[_level]:
        for col in row:
            if col == "W":
                Wall((_x, _y, screen_x / 50, screen_y / 40))  #Wall
            if col == "E":
                o.end_point = (_x + 2, _y + 2, screen_x / 62.5, screen_y / 50)  # End Point for that level
            if col == "O":
                Edge((_x, _y, screen_x / 50, screen_y / 40))  # Border (O for visibility)
            #if col == "D":
            #    DeathPoint((_x, _y, 20, 20))  Not used
            if col == 'P':
                o.player_pos = (_x + 2, _y + 2)
            _x += screen_x / 50
        _y += screen_y / 40
        _x = 0


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(o.player_pos[0], o.player_pos[1], screen_x / 62.5, screen_y / 50)
        self.ghost = False
        self.level = 0
        self.safe = True
        self.speed = 4

    def move(self, dx, dy):
        if dx != 0:
            self.move_single(dx, 0)
        if dy != 0:
            self.move_single(0, dy)

    def move_single(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if not self.ghost:
            for wall in o.Walls:
                if self.rect.colliderect(wall.rect):
                    if dx < 0:
                        self.rect.left = wall.rect.right
                    if dx > 0:
                        self.rect.right = wall.rect.left
                    if dy < 0:
                        self.rect.top = wall.rect.bottom
                    if dy > 0:
                        self.rect.bottom = wall.rect.top

        for edge in o.Edges:
            if self.rect.colliderect(edge.rect):
                if dx < 0:
                    self.rect.left = edge.rect.right
                if dx > 0:
                    self.rect.right = edge.rect.left
                if dy < 0:
                    self.rect.top = edge.rect.bottom
                if dy > 0:
                    self.rect.bottom = edge.rect.top

        if self.rect.colliderect(pygame.Rect(o.end_point)):
            if self.level == 0:
                self.rect = pygame.Rect(22, 22, 16, 16)
            o.Walls = []
            o.end_point = ()
            o.Edges = []
            self.level += 1
            if self.level >= o.LevelsCount:
                pygame.display.update()
                print('-----------------------Good job!--------------------')
                print('----------------More levels coming soon!------------')
                pygame.quit()
                sys.exit()
            LevelSetup(self.level)
            self.rect.x = o.player_pos[0]
            self.rect.y = o.player_pos[1]
            self.rect.width = screen_x / 62.5
            self.rect.height = screen_y / 50

        #for enemy in Enemies:
        #    if player.rect.colliderect(enemy.rect) and (enemy.level == player.level):
        #        print('I got you!  HAHAHAHAHA')
        #        print('-The Little Square')
        #        pygame.quit()
        #        sys.exit()