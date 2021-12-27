import pygame
from settings.constants import BOARD_SIZE, BOARD_POS
from settings.constants import CAR_SIZE
from loader import load_image

x, y = BOARD_SIZE


class FieldSprite(pygame.sprite.Sprite):
    # игровое поле

    def __init__(self, *groups):
        super().__init__(*groups)
        self.full_image = load_image('road.png')
        self.image = pygame.Surface((500, 600))
        self.image.blit(self.full_image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = BOARD_POS

        self.p = 0

    def update(self):
        self.p -= 10
        if self.p < 0:
            self.p = 600

        self.image.blit(self.full_image, (0, 0), (0, self.p, 500, 600))


class CoinsSprite(pygame.sprite.Sprite):
    # цифры

    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen

        self.image = pygame.Surface((150, 35), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, 'white', (0, 0, 150, 35), 2)

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
        pygame.draw.rect(self.image, 'white', (0, 0, 150, 35), 2)

        i = self.font.render(self.text, True, 'white')
        self.image.blit(i, (5, 5))


class CarSprite(pygame.sprite.Sprite):
    # машинка

    def __init__(self, *groups):
        super().__init__(*groups)
        # машинка по-умолчанию
        self.image = pygame.transform.scale(load_image('car2.png'), CAR_SIZE)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = BOARD_POS[0] + BOARD_SIZE[0] // 2 - 50
        self.rect.y = BOARD_POS[1] + BOARD_SIZE[1] // 2 + 50

    def update(self, *args):
        if args:
            if BOARD_POS[0] + BOARD_SIZE[0] - CAR_SIZE[0] > \
                    self.rect.x + args[0] > BOARD_POS[0]:
                self.rect.x += args[0]


class PauseSprite(pygame.sprite.Sprite):
    # кнопка паузы и play

    def __init__(self, *groups):
        super().__init__(*groups)
        self.pause = pygame.transform.scale(load_image('pause.png'),
                                            (100, 100))
        self.play = pygame.transform.scale(load_image('play.png', -1),
                                           (100, 100))

        self.image = self.pause

        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 35

    # def update(self):
        # Если нажата кнопка pause, поменять на кнопку play, и наоборот
        # self.image = self.play


def board_creator(all_sprites, screen, car_sprite, pause_sprite):
    FieldSprite(all_sprites)

    CoinsSprite(screen, all_sprites)

    CarSprite(all_sprites, car_sprite)

    PauseSprite(all_sprites, pause_sprite)