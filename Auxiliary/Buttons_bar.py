import pygame
import sys


def run_button_bar(Screen, Font, Previous_mouse):
    Width = 40
    Height = 40
    buttons = [
        {'name': "Close", 'location': 1560},
        {'name': "FullScreen", 'location': 1520},
        {'name': "Minimize", 'location': 1480}
    ]
    buttonRects = []
    buttonSurfs = []
    buttonSurfaces = []

    current_mouse = pygame.mouse.get_pressed()[0]

    fillColors = {
        'normal': (64, 64, 64),
        'hover': (80, 80, 80),
        'pressed': (115, 115, 115),
        'special_hover': (255, 0, 10),
        'special_pressed': (157, 0, 6)
    }

    for button in buttons:
        buttonSurface = pygame.Surface((Width, Height))
        buttonRect = pygame.Rect(button['location'], 0, Width, Height)
        buttonSurf = Font.render(button['name'], True, (255, 255, 255))
        buttonSurface.fill(fillColors['normal'])
        buttonRects.append(buttonRect)
        buttonSurfs.append(buttonSurf)
        buttonSurfaces.append(buttonSurface)

    for button in buttons:
        buttonSurfaces[buttons.index(button)].blit(buttonSurfs[buttons.index(button)], [
            buttonRects[buttons.index(button)].width / 2 - buttonSurfs[
                buttons.index(button)].get_rect().width / 2,
            buttonRects[buttons.index(button)].height / 2 - buttonSurfs[
                buttons.index(button)].get_rect().height / 2
        ])
        Screen.blit(buttonSurfaces[buttons.index(button)],
                    buttonRects[buttons.index(button)])

    mousePos = pygame.mouse.get_pos()
    for button in buttons:
        if buttonRects[buttons.index(button)].collidepoint(mousePos):
            if button['name'] == "Close":
                buttonSurfaces[buttons.index(button)].fill(fillColors['special_hover'])
                if Previous_mouse:
                    buttonSurfaces[buttons.index(button)].fill(fillColors['special_pressed'])
                    if not current_mouse:
                        pygame.quit()
            elif button['name'] == "Minimize" or button['name'] == "FullScreen":
                buttonSurfaces[buttons.index(button)].fill(fillColors['hover'])
                if Previous_mouse:
                    if button['name'] == "Minimize":
                        buttonSurfaces[buttons.index(button)].fill(fillColors['pressed'])
                        if not current_mouse:
                            pygame.display.iconify()
                    elif button['name'] == "FullScreen":
                        buttonSurfaces[buttons.index(button)].fill(fillColors['pressed'])
                        if not current_mouse:
                            pygame.display.toggle_fullscreen()

            buttonSurfaces[buttons.index(button)].blit(buttonSurfs[buttons.index(button)], [
                buttonRects[buttons.index(button)].width / 2 - buttonSurfs[
                    buttons.index(button)].get_rect().width / 2,
                buttonRects[buttons.index(button)].height / 2 - buttonSurfs[
                    buttons.index(button)].get_rect().height / 2
            ])
            Screen.blit(buttonSurfaces[buttons.index(button)],
                        buttonRects[buttons.index(button)])

    return current_mouse


if __name__ == "__main__":
    pygame.init()

    width, height = 1600, 1000
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    main_background = pygame.Surface((1600, 960))
    bar_background = pygame.Surface((1600, 40))
    font = pygame.font.SysFont('Arial', 10)

    previous_mouse = False

    while True:
        screen.fill((140, 45, 40))
        bar_background.fill((200, 200, 200))
        screen.blit(bar_background, (0, 0))
        main_background.fill((0, 0, 0))
        screen.blit(main_background, (0, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        previous_mouse = run_button_bar(screen, font, previous_mouse)

        pygame.display.flip()
