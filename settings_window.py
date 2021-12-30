import pygame
from loader import load_image


class Area1:
    def __init__(self):
        self.font = pygame.font.Font('fonts/result-font.ttf', 40)
        self.font_small = pygame.font.Font('fonts/result-font.ttf', 20)

        image = pygame.Surface([1080, 200], pygame.SRCALPHA, 32)
        self.area = image.convert_alpha()

        self.area.blit(self.font.render('Выбор машинки', True, 'white'), (375, 10))
        pygame.draw.rect(self.area, 'black', (26, 100, 250, 80), 2)
        pygame.draw.rect(self.area, 'black', (292, 100, 250, 80), 2)
        pygame.draw.rect(self.area, 'black', (558, 100, 250, 80), 2)
        pygame.draw.rect(self.area, 'black', (824, 100, 250, 80), 2)

        self.button1 = pygame.Rect(28, 230, 250, 82)
        self.button2 = pygame.Rect(294, 230, 250, 82)
        self.button3 = pygame.Rect(560, 230, 250, 82)
        self.button4 = pygame.Rect(826, 230, 250, 82)

        self.cur_button = (28, 102, 246, 76)

    def update(self, pos):
        pygame.draw.rect(self.area, 'grey', (28, 102, 246, 76))
        pygame.draw.rect(self.area, 'grey', (294, 102, 246, 76))
        pygame.draw.rect(self.area, 'grey', (560, 102, 246, 76))
        pygame.draw.rect(self.area, 'grey', (826, 102, 246, 76))

        if self.button1.collidepoint(*pos):
            self.cur_button = (28, 102, 246, 76)
        elif self.button2.collidepoint(*pos):
            self.cur_button = (294, 102, 246, 76)
        elif self.button3.collidepoint(*pos):
            self.cur_button = (560, 102, 246, 76)
        elif self.button4.collidepoint(*pos):
            self.cur_button = (826, 102, 246, 76)

        pygame.draw.rect(self.area, 'yellow', self.cur_button)

        self.area.blit(self.font_small.render('Красная', True, 'black'), (100, 125))
        self.area.blit(self.font_small.render('Синяя', True, 'black'), (380, 125))
        self.area.blit(self.font_small.render('Жёлтая', True, 'black'), (640, 125))
        self.area.blit(self.font_small.render('Белая', True, 'black'), (920, 125))

        return self.get_area()

    def get_area(self):
        return self.area

    def get_value(self):
        if self.cur_button == (28, 102, 246, 76):
            return 'car2'
        elif self.cur_button == (294, 102, 246, 76):
            return 'car'
        elif self.cur_button == (560, 102, 246, 76):
            return 'car3'
        elif self.cur_button == (826, 102, 246, 76):
            return 'car4'


class Area2:
    def __init__(self):
        self.font = pygame.font.Font('fonts/result-font.ttf', 40)
        self.font_small = pygame.font.Font('fonts/result-font.ttf', 20)

        image = pygame.Surface([1080, 200], pygame.SRCALPHA, 32)
        self.area = image.convert_alpha()

        self.area.blit(self.font.render('Стенки поля - препятствия', True, 'white'), (265, 10))
        pygame.draw.rect(self.area, 'black', (183, 100, 280, 80), 2)
        pygame.draw.rect(self.area, 'black', (636, 100, 280, 80), 2)

        self.button1 = pygame.Rect(183, 442, 280, 80)
        self.button2 = pygame.Rect(636, 442, 280, 80)

        self.cur_button = (185, 102, 276, 76)

    def update(self, pos):
        pygame.draw.rect(self.area, 'grey', (185, 102, 276, 76))
        pygame.draw.rect(self.area, 'grey', (638, 102, 276, 76))

        if self.button1.collidepoint(*pos):
            self.cur_button = (185, 102, 276, 76)
        elif self.button2.collidepoint(*pos):
            self.cur_button = (638, 102, 276, 76)

        pygame.draw.rect(self.area, 'yellow', self.cur_button)

        self.area.blit(self.font_small.render('Выключить', True, 'black'), (260, 125))
        self.area.blit(self.font_small.render('Включить', True, 'black'), (725, 125))

        return self.get_area()

    def get_area(self):
        return self.area

    def get_value(self):
        if self.cur_button == (185, 102, 276, 76):
            return 'выкл'
        elif self.cur_button == (638, 102, 276, 76):
            return 'вкл'


class Area3:
    def __init__(self):
        self.font = pygame.font.Font('fonts/result-font.ttf', 40)
        image = pygame.Surface([1080, 200], pygame.SRCALPHA, 32)
        self.area = image.convert_alpha()
        self.cur_x = 245
        self.im = load_image('settings_area3.png')

    def update(self, x):
        self.area.blit(self.im, (0, 0))
        self.area.blit(self.font.render('Чувствительность машинки', True, 'white'), (255, 10))
        pygame.draw.rect(self.area, 'grey', (245, 150, 600, 10))

        self.cur_x = x

        pygame.draw.circle(self.area, 'red', (self.cur_x - 9, 155), 25)
        return self.get_area()

    def get_area(self):
        return self.area

    def get_value(self):
        return (self.cur_x - 245) // 40 + 5


def settings_screen(screen, areas=None):
    showing = True

    image = load_image('settings_screen.png')
    start_button = pygame.Rect(0, 30, 335, 89)

    if areas:
        area1, area2, area3 = areas[0], areas[1], areas[2]

        image.blit(area1.get_area(), (10, 130))
        image.blit(area2.get_area(), (10, 340))
        image.blit(area3.get_area(), (10, 550))
    else:
        area1 = Area1()
        area2 = Area2()
        area3 = Area3()

        image.blit(area1.update((28, 102)), (10, 130))
        image.blit(area2.update((189, 109)), (10, 340))
        image.blit(area3.update(245), (10, 550))

    screen.blit(image, (0, 0))

    pygame.display.flip()
    clock = pygame.time.Clock()

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                return 'close'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(*event.pos):
                        return 'first', [area1, area2, area3], \
                               area1.get_value(), area2.get_value(), area3.get_value()
                    if event.pos[1]:
                        image.blit(area1.update(event.pos), (10, 130))
                    if event.pos[1]:
                        image.blit(area2.update(event.pos), (10, 340))

        button = pygame.mouse.get_pressed()
        if button[0]:
            pos = pygame.mouse.get_pos()
            x, y = pos
            if 245 <= x <= 845 and 675 <= y <= 725:
                image.blit(area3.update(x), (10, 550))
        screen.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(50)
