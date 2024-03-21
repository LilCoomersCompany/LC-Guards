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
# font = pygame.font.SysFont('Arial', 10)


class Buttons_bar:
    def __init__(self, Screen, Font):

        self.width = 40
        self.height = 40
        self.screen = Screen
        self.font = Font
        self.buttons = [
            {
                'name': "Close",
                'location': 1560
            },
            {
                'name': "FullScreen",
                'location': 1520
            },
            {
                'name': "Minimize",
                'location': 1480
            }
        ]
        self.buttonRects = []
        self.buttonSurfs = []
        self.buttonSurfaces = []

        self.fillColors = {
            'normal': (64, 64, 64),
            'hover': (80, 80, 80),
            'pressed': (115, 115, 115),
            'special_hover': (255, 0, 10),
            'special_pressed': (157, 0, 6)
        }

        for button in self.buttons:
            self.buttonSurface = pygame.Surface((self.width, self.height))
            self.buttonRect = pygame.Rect(button['location'], 0, self.width, self.height)
            self.buttonSurf = self.font.render(button['name'], True, (255, 255, 255))
            self.buttonSurface.fill(self.fillColors['normal'])
            self.buttonRects.append(self.buttonRect)
            self.buttonSurfs.append(self.buttonSurf)
            self.buttonSurfaces.append(self.buttonSurface)

    def process(self):
        for button in self.buttons:
            self.buttonSurfaces[self.buttons.index(button)].blit(self.buttonSurfs[self.buttons.index(button)], [
                self.buttonRects[self.buttons.index(button)].width / 2 - self.buttonSurfs[
                    self.buttons.index(button)].get_rect().width / 2,
                self.buttonRects[self.buttons.index(button)].height / 2 - self.buttonSurfs[
                    self.buttons.index(button)].get_rect().height / 2
            ])
            self.screen.blit(self.buttonSurfaces[self.buttons.index(button)],
                             self.buttonRects[self.buttons.index(button)])

        mousePos = pygame.mouse.get_pos()
        for button in self.buttons:
            if self.buttonRects[self.buttons.index(button)].collidepoint(mousePos):
                if button['name'] == "Close":
                    self.buttonSurfaces[self.buttons.index(button)].fill(self.fillColors['special_hover'])
                else:
                    self.buttonSurfaces[self.buttons.index(button)].fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    if button['name'] == "Close":
                        self.buttonSurfaces[self.buttons.index(button)].fill(self.fillColors['special_pressed'])
                        pygame.quit()
                    elif button['name'] == "Minimize":
                        self.buttonSurfaces[self.buttons.index(button)].fill(self.fillColors['pressed'])
                        pygame.display.iconify()
                    elif button['name'] == "FullScreen":
                        self.buttonSurfaces[self.buttons.index(button)].fill(self.fillColors['pressed'])
                        pygame.display.toggle_fullscreen()

                self.buttonSurfaces[self.buttons.index(button)].blit(self.buttonSurfs[self.buttons.index(button)], [
                    self.buttonRects[self.buttons.index(button)].width / 2 - self.buttonSurfs[
                        self.buttons.index(button)].get_rect().width / 2,
                    self.buttonRects[self.buttons.index(button)].height / 2 - self.buttonSurfs[
                        self.buttons.index(button)].get_rect().height / 2
                ])
                self.screen.blit(self.buttonSurfaces[self.buttons.index(button)],
                                 self.buttonRects[self.buttons.index(button)])


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
#     Buttons_bar(screen, font).process()
#     pygame.display.flip()
