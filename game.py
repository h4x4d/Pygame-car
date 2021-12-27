import pygame

from board import board_creator
from loader import load_image
from settings.constants import SIZE


class Game:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.transform.scale(load_image('process.png'), SIZE)
        screen.blit(self.image, (0, 0))

        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Group()
        self.pause = pygame.sprite.Group()
        self.pause_button = pygame.Rect(950, 35, 100, 100)

        board_creator(self.all_sprites, self.screen, self.car, self.pause)

        self.screen.blit(self.image, (0, 0))

    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

    def update_car(self, state):
        self.car.update(state)