import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("River.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font("Times New Roman", FONT_SIZE)

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.color('dodgerblue'))

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

        def move(self, x_change, y_change):
            self.rect.x = max(min(self.rect.x + x_change, 0), SCREEN_WIDTH - self.rect.width)
            self.rect.y = max(min(self.rect.y + y_change, 0), SCREEN_HEIGHT - self.rect.height)

SCREEN = pygame.display.set_mode("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = sprite(pygame.color('Black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = sprite(pygame.color('Black'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
