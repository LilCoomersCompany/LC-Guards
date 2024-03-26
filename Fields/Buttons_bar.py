""""""
import pygame
import sys
import main.Constants as C


def run_button_bar(Screen, Font, Previous_mouse):
    Width = C.BAR_SIZE
    Height = C.BAR_SIZE
    buttons = [
        {'name': "Close", 'location': C.WINDOW_WIDTH - C.BAR_SIZE},
        {'name': "FullScreen", 'location':  C.WINDOW_WIDTH - 2 * C.BAR_SIZE},
        {'name': "Minimize", 'location':  C.WINDOW_WIDTH - 3 * C.BAR_SIZE}
    ]
    buttonRects = []
    buttonSurfs = []
    buttonSurfaces = []

    current_mouse = pygame.mouse.get_pressed()[0]

    for button in buttons:
        buttonSurface = pygame.Surface((Width, Height))
        buttonRect = pygame.Rect(button['location'], 0, Width, Height)
        buttonSurf = Font.render(button['name'], True, (255, 255, 255))
        buttonSurface.fill(C.BAR_COLOR)
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
                buttonSurfaces[buttons.index(button)].fill(C.SPECIAL_HOVER_BAR_BUTTONS_COLOR)
                if Previous_mouse:
                    buttonSurfaces[buttons.index(button)].fill(C.SPECIAL_PRESSED_BAR_BUTTONS_COLOR)
                    if not current_mouse:
                        pygame.quit()
            elif button['name'] == "Minimize" or button['name'] == "FullScreen":
                buttonSurfaces[buttons.index(button)].fill(C.DEFAULT_HOVER_BAR_BUTTONS_COLOR)
                if Previous_mouse:
                    if button['name'] == "Minimize":
                        buttonSurfaces[buttons.index(button)].fill(C.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
                        if not current_mouse:
                            pygame.display.iconify()
                    elif button['name'] == "FullScreen":
                        buttonSurfaces[buttons.index(button)].fill(C.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
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

    width, height = C.WINDOW_WIDTH, C.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    main_background = pygame.Surface((C.WINDOW_WIDTH, C.WINDOW_HEIGHT - C.BAR_SIZE))
    bar_background = pygame.Surface((C.WINDOW_WIDTH, C.BAR_SIZE))
    font = pygame.font.SysFont(C.FONT_NAME, C.FONT_SIZE)

    previous_mouse = False

    while True:
        screen.fill(C.WINDOW_COLOR)
        bar_background.fill(C.BAR_COLOR)
        screen.blit(bar_background, (0, 0))
        main_background.fill((0, 0, 0))
        screen.blit(main_background, (0, C.BAR_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        previous_mouse = run_button_bar(screen, font, previous_mouse)

        pygame.display.flip()
