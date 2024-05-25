import pygame
from config import *
import time


class Bricks:
    def __init__(self, x, y, color=RED):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)