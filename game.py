import pygame

from border import border_creator
from loader import load_image
from settings.constants import SIZE


class Game:
    def __init__(self, screen):
        self.screen = screen

        image = pygame.transform.scale(load_image('process.png'), SIZE)
        screen.blit(image, (0, 0))

        all_sprites = pygame.sprite.Group()


        border_creator(all_sprites, screen)

        showing = True
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.blit(image, (0, 0))

            all_sprites.draw(self.screen)
            all_sprites.update()

            pygame.display.flip()