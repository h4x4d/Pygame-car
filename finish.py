import datetime
import sqlite3
import time
from settings.constants import WIDTH, HEIGHT
import pygame
from loader import load_image


def finish_screen(screen, number):
    time.sleep(0.5)
    showing = True
    image = load_image('final_screen.png')
    screen.blit(image, (0, 0))
    font = pygame.font.Font('fonts/result-font2.ttf', 70)
    i = font.render(number + ' очков', True, 'white')
    text_rect = i.get_rect(center=(WIDTH / 2, 330))
    conn = sqlite3.connect('result.db')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO results VALUES('
                f'"{datetime.date.today().strftime("%d.%m.%Y")}", {number})')
    conn.commit()
    screen.blit(i, text_rect)

    start_button = pygame.Rect(400, 70, 400, 400)
    main_button = pygame.Rect(400, 70, 400, 492)
    pygame.display.flip()

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(*event.pos):
                        return 'start'
                    elif main_button.collidepoint(*event.pos):
                        return 'main'

        pygame.display.flip()