import pygame
from settings.constants import *
from settings_window import settings_screen
from start import start_screen
from game import Game
from results import results_screen
from paused import pause_screen
from finish import finish_screen

args = ARGS
areas = None

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
            game = Game(screen, args[0])
        elif action == 'settings':
            if areas:
                action, areas, *args = settings_screen(screen, areas)
            else:
                action, areas, *args = settings_screen(screen)
            if action == 'close':
                exit()
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
                        game = Game(screen, args[0])
                    elif pause == 'main':
                        break

        if pause == 'main':
            break

        finish = game.update()
        n = game.coins.sprites()[0].text
        if int(n) % 500 == 0:
            game.board.sprites()[0].speed += 5

        if finish is None:
            if pygame.key.get_pressed()[pygame.K_RIGHT] or \
                    pygame.key.get_pressed()[pygame.K_d]:
                finish = game.update_car(args[1], args[2])

            elif pygame.key.get_pressed()[pygame.K_LEFT] or \
                    pygame.key.get_pressed()[pygame.K_a]:
                finish = game.update_car(args[1], -args[2])

        if finish:
            finish = finish_screen(screen, game.coins.sprites()[0].coin())
            if finish == 'start':
                game = Game(screen, args[0])
            elif finish == 'main':
                pause = 'main'
                break

        pygame.display.flip()
        clock.tick(FPS)

    if pause == 'main':
        continue

    pygame.quit()
    break
