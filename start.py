import pygame
from loader import load_image


def start_screen(screen):
    showing = True
    image = load_image('start_screen.png')
    screen.blit(image, (0, 0))
    start_button = pygame.Rect(0, 663, 369, 106)
    result_button = pygame.Rect(0, 531, 291, 106)
    pygame.display.flip()
    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'close'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(*event.pos):
                        return 'start'
                    elif result_button.collidepoint(*event.pos):
                        return 'results'
        pygame.display.flip()
