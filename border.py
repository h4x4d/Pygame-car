import pygame
from settings.constants import BORDER_SIZE
from settings.constants import CAR_SIZE
from loader import load_image

x, y = BORDER_SIZE


class FieldSprite(pygame.sprite.Sprite):
    # игровое поле

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(BORDER_SIZE, pygame.SRCALPHA, 32)

        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, x, y), 0)

        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 100


class CoinsSprite(pygame.sprite.Sprite):
    # цифры

    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen

        self.image = pygame.Surface((150, 35), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 150, 35), 2)

        self.font = pygame.font.Font('fonts/result-font.ttf', 20)
        self.text = '0'

        i = self.font.render(self.text, True, 'white')
        self.image.blit(i, (5, 5))

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 30

    def update(self):
        self.text = str(int(self.text) + 1)

        self.image = pygame.Surface((150, 35), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 150, 35), 2)

        i = self.font.render(self.text, True, 'white')
        self.image.blit(i, (5, 5))


class CarSprite(pygame.sprite.Sprite):
    # машинка

    def __init__(self, *groups):
        super().__init__(*groups)
        # машинка по-умолчанию
        self.image = pygame.transform.scale(load_image('car.png'), CAR_SIZE)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 475
        self.rect.y = 450

    def update(self, *args):
        if args:
            self.image = pygame.transform.scale(load_image(f'{args[0]}.png'), CAR_SIZE)


class PauseSprite(pygame.sprite.Sprite):
    # кнопка паузы и play

    def __init__(self, *groups):
        super().__init__(*groups)
        self.pause = pygame.transform.scale(load_image('pause.png'), (100, 100))
        self.play = pygame.transform.scale(load_image('play.png', -1), (100, 100))

        self.image = self.pause

        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 35

    # def update(self):
        # Если нажата кнопка pause, поменять на кнопку play, и наоборот
        # self.image = self.play


def border_creator(all_sprites, screen):
    FieldSprite(all_sprites)

    CoinsSprite(screen, all_sprites)

    CarSprite(all_sprites)

    PauseSprite(all_sprites)