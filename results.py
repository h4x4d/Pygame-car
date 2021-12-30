import sqlite3

import pygame
from loader import load_image


def results_screen(screen):
    showing = True
    image = load_image('result_screen.png')
    screen.blit(image, (0, 0))
    start_button = pygame.Rect(0, 31, 334, 86)
    pygame.display.flip()

    font = pygame.font.Font('fonts/result-font.ttf', 36)

    conn = sqlite3.connect('result.db')
    cur = conn.cursor()
    best_results = cur.execute('SELECT * FROM results').fetchall()
    best_results = list(sorted(best_results, key=lambda x: x[1],
                               reverse=True))[:5]
    text = ['Лучшие результаты:'] + [f'{j + 1}: {i[0]} - {i[1]} очков'
                                     for j, i in enumerate(best_results)]

    p = 175

    for i in text:
        i = font.render(i, True, 'white')
        screen.blit(i, (30, p))
        p += 50

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(*event.pos):
                        return 'first'

        pygame.display.flip()
