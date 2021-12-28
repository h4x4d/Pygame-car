import random
import pygame
from settings.constants import BOARD_SIZE, BOARD_POS
from settings.constants import CAR_SIZE
from loader import load_image
from exc import FinishException

x, y = BOARD_SIZE
collide = pygame.sprite.Group()


class ConeSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image('cone.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = random.randint(BOARD_POS[0], BOARD_SIZE[0] +
                                                  BOARD_POS[0] - 30), 100

    def update(self, car):
        self.rect.y += 10
        if self.rect.y > BOARD_POS[1] + BOARD_SIZE[1]:
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)


class CarTrSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        choice = random.choice(['car.png', 'car2.png', 'car3.png', 'car4.png'])
        self.image = load_image(choice)
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = random.randint(BOARD_POS[0], BOARD_SIZE[0] +
                                                  BOARD_POS[0] - 100), \
                                   BOARD_POS[1]
        if pygame.sprite.spritecollideany(self, collide):
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)
            self.rect.x = 1
            self.rect.y = 1

    def update(self, car):
        self.rect.y += 5
        if self.rect.y >= BOARD_POS[1] + BOARD_SIZE[1] - 200:
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)


class FieldSprite(pygame.sprite.Sprite):
    # игровое поле

    def __init__(self, *groups):
        super().__init__(*groups)
        self.full_image = load_image('road.png')
        self.image = pygame.Surface((500, 600))
        self.image.blit(self.full_image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = BOARD_POS

        self.cones = pygame.sprite.Group()

        self.p = 0

    def update(self, screen, car):
        self.p -= 10
        if self.p < 0:
            self.p = 600

        choice = random.randint(0, 200)
        if choice == 0 or choice == 2:
            c = ConeSprite(self.cones)
            collide.add(c)
        elif choice == 1:
            c = CarTrSprite(self.cones)
            collide.add(c)

        self.image.blit(self.full_image, (0, 0), (0, self.p, 500, 600))
        self.cones.update(car)

        self.cones.draw(screen)

        if pygame.sprite.groupcollide(car, self.cones, False, False):
            raise FinishException


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

    def coin(self):
        return self.text


class CarSprite(pygame.sprite.Sprite):
    # машинка

    def __init__(self, car, *groups):
        super().__init__(*groups)
        # машинка по-умолчанию
        self.image = pygame.transform.scale(load_image(f'{car}.png', -1),
                                            CAR_SIZE)

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
        self.image = pygame.transform.scale(load_image('play.png', -1),
                                            (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 35


def board_creator(car, all_sprites, screen, car_sprite, coins_sprite,
                  board_sprite):
    FieldSprite(board_sprite)

    CoinsSprite(screen, all_sprites, coins_sprite)

    CarSprite(car, all_sprites, car_sprite)

    PauseSprite(all_sprites)
