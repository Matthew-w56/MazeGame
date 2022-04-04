import sys
import pygame
from pygame.locals import *
import random
from Levels import *

red = (255, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (40, 40, 40)
brown = (129, 68, 15)

from Levels import *
import os

player = (0, 0, 20, 20)

x, y = 10, 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen_x, screen_y = (100 * 8, 80 * 8)

Screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Maze Game 2.1')


class Organizer():
    def __init__(self):
        self.end_point = (-10, -10, 10, 10)
        self.Levels = Levelslist
        self.LevelsCount = LevelsCount
        self.Walls = []
        self.Enemies = []
        self.Edges = []
        self.Doors = []
        self.DeathPoints = []
        self.player_pos = (0, 0)

o = Organizer()


def write(text='[--Enter Text To Write!--]', color=black, pos=(0, 0), bold=False, size=20, font='Arial'):
    Font = pygame.font.SysFont(font, size, bold)
    Finaltext = Font.render(text, 1, color)
    Screen.blit(Finaltext, pos)


class Wall(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])
        o.Walls.append(self)


class Edge(object):
    def __init__(self, pos):
        o.Edges.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])


class DeathPoint(object):
    def __init__(self, pos):
        o.DeathPoints.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])


class Door(object):
    def __init__(self, pos, openD):
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        self.openD = openD


class Key(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])


class Enemy(object):
    def __init__(self, level, color=blue, pos=(200, 200), ghost=False, speed=4, height=16, length=16):
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], length, height)
        o.Enemies.append(self)
        self.ghost = ghost
        self.level = level
        self.walls = []
        self.speed = speed
        self.length = length
        self.height = height

    def Find(self, _player):
        if self.rect.x < _player.rect.x:
            self.move(self.speed, 0)
        if self.rect.x > _player.rect.x:
            self.move(-self.speed, 0)
        if self.rect.y < _player.rect.y:
            self.move(0, self.speed)
        if self.rect.y > _player.rect.y:
            self.move(0, -self.speed)
            for wall in o.Walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.top = wall.rect.bottom

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
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

            for enemy in o.Enemies:
                if (enemy != self) and (enemy.level == self.level):
                    if self.rect.colliderect(enemy.rect):
                        if dx < 0:
                            self.rect.left = enemy.rect.right
                        if dx > 0:
                            self.rect.right = enemy.rect.left
                        if dy < 0:
                            self.rect.top = enemy.rect.bottom
                        if dy > 0:
                            self.rect.bottom = enemy.rect.top

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

        if self.rect.colliderect(player):
            print('I got you!  BWAHAHAHAHAHAHAHA!!!!!')
            pygame.quit()
            sys.exit()

    def draw(self):
        if self.color == white:
            pygame.draw.rect(Screen, self.color, self.rect)
            pygame.draw.rect(Screen, black, (self.rect.x + 2, self.rect.y + 2, self.length - 4, self.height - 4), 1)
        if self.color == black:
            pygame.draw.rect(Screen, self.color, self.rect)
            pygame.draw.rect(Screen, white, self.rect, 2)
        else:
            pygame.draw.rect(Screen, self.color, self.rect)
