import pygame
from loader import load_image


def start_screen(screen):
    showing = True

    image = load_image('start_screen.png')
    screen.blit(image, (0, 0))

    image_settings = pygame.transform.scale(
        load_image('settings_mask.png'), (100, 100))
    screen.blit(image_settings, (980, 670))

    start_button = pygame.Rect(0, 663, 369, 106)
    result_button = pygame.Rect(0, 531, 291, 106)
    settings_button = pygame.Rect(980, 670, 100, 100)

    pygame.display.flip()
    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(*event.pos):
                        return 'start'
                    elif result_button.collidepoint(*event.pos):
                        return 'results'
                    elif settings_button.collidepoint(*event.pos):
                        return 'settings'
        pygame.display.flip()
