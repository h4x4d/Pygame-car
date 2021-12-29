import pygame
from exc import FinishException
from board import board_creator
from loader import load_image
from settings.constants import SIZE


class Game:
    def __init__(self, screen, car):
        self.screen = screen

        self.image = pygame.transform.scale(load_image('process.png'), SIZE)
        screen.blit(self.image, (0, 0))

        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.board = pygame.sprite.Group()
        self.pause_button = pygame.Rect(950, 35, 100, 100)

        board_creator(car, self.all_sprites, self.screen, self.car, self.coins,
                      self.board)

        self.screen.blit(self.image, (0, 0))

    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.update()
        self.board.draw(self.screen)
        try:
            self.board.update(self.screen, self.car)
        except FinishException:
            return 'finish'
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.image, (0, 0))
        self.coins.draw(self.screen)

    def update_car(self, state):
        self.car.update(state)