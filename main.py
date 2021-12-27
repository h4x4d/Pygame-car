import pygame
from settings.constants import *
from start import start_screen
from game import Game
from results import results_screen

pygame.init()
pygame.display.set_caption('Car')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
