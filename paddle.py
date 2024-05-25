import pygame

BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700

    def collide_with_ball(self, ball):
        if ball.rect.colliderect(self.rect):
            if ball.rect.right >= self.rect.left and ball.rect.left < self.rect.left:
                ball.velocity[1] = -ball.velocity[1]
                ball.rect.right = self.rect.left - 1
            elif ball.rect.left <= self.rect.right and ball.rect.right > self.rect.right:
                ball.velocity[1] = -ball.velocity[1]
                ball.rect.left = self.rect.right + 1
            else:
                ball.bounce()
