import pygame

"run requirements"


# import sys
#
# pygame.init()
#
# width, height = 1800, 1000
# screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
# main_background = pygame.Surface((1800, 950))
# bar_background = pygame.Surface((1800, 50))
#
# font = pygame.font.SysFont('Arial', 20)


class Minimize_button:
    def __init__(self, sc, Font, ButtonText='Button'):

        self.width = 40
        self.height = 40
        self.screen = sc
        self.font = Font

        self.fillColors = {
            'hover': 'red',
            'pressed': 'dark red',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(1480, 0, self.width, self.height)

        self.buttonSurf = self.font.render(ButtonText, True, (255, 255, 255))
        self.buttonSurface.fill((15, 115, 15))

    def process(self):

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if pygame.MOUSEBUTTONUP:
                    pygame.display.iconify()

            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
            ])
            self.screen.blit(self.buttonSurface, self.buttonRect)


"run requirements"
# while True:
#     screen.fill((140, 45, 40))
#     bar_background.fill((90, 255, 45))
#     screen.blit(bar_background, (0, 0))
#     main_background.fill((140, 80, 41))
#     screen.blit(main_background, (0, 50))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     Minimize_button(screen, font, 'min').process()
#     pygame.display.flip()
