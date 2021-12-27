import pygame
from settings.constants import *
from start import start_screen
from game import Game
from results import results_screen
from paused import pause_screen

pygame.init()
pygame.display.set_caption('Car')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

while True:
    action = 'first'

    while action == 'first':
        action = start_screen(screen)
        if action == 'close':
            exit()
        elif action == 'start':
            game = Game(screen)
        elif action == 'results':
            action = results_screen(screen)
            if action == 'close':
                exit()

    running = True
    pause = ''

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.pause_button.collidepoint(*event.pos):
                    pause = pause_screen(screen)
                    if pause == 'start':
                        game = Game(screen)
                    elif pause == 'main':
                        break

        if pause == 'main':
            break

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            game.update_car(5)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            game.update_car(-5)
        game.update()
        pygame.display.flip()
        clock.tick(FPS)

    if pause == 'main':
        continue

    pygame.quit()
    break
