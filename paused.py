import pygame
from loader import load_image


def pause_screen(screen):
    showing = True
    image = load_image('pause_screen.png')
    screen.blit(image, (0, 0))
    start_button = pygame.Rect(400, 319, 300, 70)
    main_button = pygame.Rect(400, 411, 300, 70)
    continue_button = pygame.Rect(950, 35, 100, 100)
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
                    elif continue_button.collidepoint(*event.pos):
                        return ''

        pygame.display.flip()