import pygame
from settings.constants import *
from start import start_screen
from game import Game
from results import results_screen

pygame.init()
pygame.display.set_caption('Car')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

start = start_screen(screen)
if start == 'close':
    exit()
elif start == 'start':
    game = Game(screen)
elif start == 'results':
    results = results_screen(screen)
    if results == 'close':
        exit()
    elif results == 'start':
        game = Game(screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
