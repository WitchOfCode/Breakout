import pygame
from config import *
import time

class Ball:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(BALL_X_VELOCITY, BALL_Y_VELOCITY)
        self.radius = BALL_RADIUS

    def update(self):
        self.position += self.velocity
        self.check_collision_with_walls()

    def check_collision_with_walls(self):
        if self.position.x <= 0 or self.position.x >= WINDOW_WIDTH:
            self.velocity.x *= -1
        if self.position.y <= 0:
            self.velocity.y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.position.x), int(self.position.y)), self.radius)


