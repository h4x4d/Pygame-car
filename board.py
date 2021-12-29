import random
import pygame
from settings.constants import BOARD_SIZE, BOARD_POS
from settings.constants import CAR_SIZE
from loader import load_image
from exc import FinishException

collide = pygame.sprite.Group()


class ConeSprite(pygame.sprite.Sprite):
    def __init__(self, speed, p, *groups):
        super().__init__(*groups)
        self.image = load_image('cone.png')
        self.rect = self.image.get_rect()
        if p == 0:
            r1, r2 = BOARD_POS[0], BOARD_POS[0] + BOARD_SIZE[0] // 3 - 50
        if p == 1:
            r1, r2 = BOARD_POS[0] + BOARD_SIZE[0] // 3 - 50, \
                     BOARD_POS[0] + BOARD_SIZE[0] // 3 * 2 - 50
        if p == 2:
            r1, r2 = BOARD_POS[0] + BOARD_SIZE[0] // 3 * 2 - 50, \
                     BOARD_POS[0] + BOARD_SIZE[0] - 50
        self.rect.x, self.rect.y = random.randint(r1, r2), BOARD_POS[1]
        self.speed = speed
        if pygame.sprite.spritecollideany(self, collide):
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)
            self.rect.x = 1
            self.rect.y = 1

    def update(self, car):
        self.rect.y += self.speed
        if self.rect.y > BOARD_POS[1] + BOARD_SIZE[1]:
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)


class CarTrSprite(pygame.sprite.Sprite):
    def __init__(self, speed, p, *groups):
        super().__init__(*groups)
        choice = random.choice(['car.png', 'car2.png', 'car3.png', 'car4.png'])
        self.image = load_image(choice, -1)
        self.speed = speed
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        if p == 0:
            r1, r2 = BOARD_POS[0], BOARD_POS[0] + BOARD_SIZE[0] // 3 - 100
        if p == 1:
            r1, r2 = BOARD_POS[0] + BOARD_SIZE[0] // 3 - 50, \
                     BOARD_POS[0] + BOARD_SIZE[0] // 3 * 2 - 100
        if p == 2:
            r1, r2 = BOARD_POS[0] + BOARD_SIZE[0] // 3 * 2 - 50, \
                     BOARD_POS[0] + BOARD_SIZE[0] - 100
        self.rect.x, self.rect.y = random.randint(r1, r2), -50
        if pygame.sprite.spritecollideany(self, collide):
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)
            self.rect.x = 1
            self.rect.y = 1

    def update(self, car):
        self.rect.y += self.speed
        if self.rect.y >= BOARD_POS[1] + BOARD_SIZE[1]:
            self.image = pygame.Surface([1, 1], pygame.SRCALPHA, 32)


class FieldSprite(pygame.sprite.Sprite):
    # игровое поле

    def __init__(self, *groups):
        super().__init__(*groups)
        self.full_image = load_image('road.png')
        self.image = pygame.Surface(BOARD_SIZE)
        self.image.blit(self.full_image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = BOARD_POS

        self.cones = pygame.sprite.Group()

        self.speed = 5

        self.p = 0

    def update(self, screen, car):
        self.p -= self.speed
        if self.p < 0:
            self.p = 600

        if self.p % 500 == 0:
            choice = random.randint(0, 6)
            if choice == 0:
                for i in range(2):
                    r = random.randint(0, 1)
                    if r == 0:
                        c = ConeSprite(self.speed, i, self.cones)
                    else:
                        c = CarTrSprite(self.speed, i, self.cones)
                    collide.add(c)

            elif choice == 1:
                for i in range(0, 3, 2):
                    r = random.randint(0, 1)
                    if r == 0:
                        c = ConeSprite(self.speed, i, self.cones)
                    else:
                        c = CarTrSprite(self.speed, i, self.cones)
                    collide.add(c)

            elif choice == 2:
                for i in range(1, 3):
                    r = random.randint(0, 1)
                    if r == 0:
                        c = ConeSprite(self.speed, i, self.cones)
                    else:
                        c = CarTrSprite(self.speed, i, self.cones)
                    collide.add(c)

            elif choice == 3:
                i = 0
                r = random.randint(0, 1)
                if r == 0:
                    c = ConeSprite(self.speed, i, self.cones)
                else:
                    c = CarTrSprite(self.speed, i, self.cones)
                collide.add(c)

            elif choice == 4:
                i = 1
                r = random.randint(0, 1)
                if r == 0:
                    c = ConeSprite(self.speed, i, self.cones)
                else:
                    c = CarTrSprite(self.speed, i, self.cones)
                collide.add(c)

            elif choice == 5:
                i = 2
                r = random.randint(0, 1)
                if r == 0:
                    c = ConeSprite(self.speed, i, self.cones)
                else:
                    c = CarTrSprite(self.speed, i, self.cones)
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
            if BOARD_POS[0] + BOARD_SIZE[0] - CAR_SIZE[0] >= \
                    self.rect.x + args[0] >= BOARD_POS[0]:
                self.rect.x += args[0]
            else:
                if args[-1] == 'вкл':
                    raise FinishException


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

