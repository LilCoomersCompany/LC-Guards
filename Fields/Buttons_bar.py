""""""
import pygame
import sys
import main.Constants as c


def run_button_bar(Screen, Font, Previous_mouse):

    buttons = [
        {'name': "Close", 'location': c.WINDOW_WIDTH - c.BAR_SIZE},
        {'name': "FullScreen", 'location': c.WINDOW_WIDTH - 2 * c.BAR_SIZE},
        {'name': "Minimize", 'location': c.WINDOW_WIDTH - 3 * c.BAR_SIZE}
    ]
    buttonRects = []
    buttonSurfs = []
    buttonSurfaces = []

    current_mouse = pygame.mouse.get_pressed()[0]

    for button in buttons:
        buttonSurface = pygame.Surface((c.BAR_SIZE, c.BAR_SIZE))
        buttonRect = pygame.Rect(button['location'], 0, c.BAR_SIZE, c.BAR_SIZE)
        buttonSurf = Font.render(button['name'], True, c.FONT_COLOR)
        buttonSurface.fill(c.BAR_COLOR)
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
                buttonSurfaces[buttons.index(button)].fill(c.SPECIAL_HOVER_BAR_BUTTONS_COLOR)
                if Previous_mouse:
                    buttonSurfaces[buttons.index(button)].fill(c.SPECIAL_PRESSED_BAR_BUTTONS_COLOR)
                    if not current_mouse:
                        pygame.quit()
            elif button['name'] == "Minimize" or button['name'] == "FullScreen":
                buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_HOVER_BAR_BUTTONS_COLOR)
                if Previous_mouse:
                    if button['name'] == "Minimize":
                        buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
                        if not current_mouse:
                            pygame.display.iconify()
                    elif button['name'] == "FullScreen":
                        buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
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

    width, height = c.WINDOW_WIDTH, c.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    main_background = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT - c.BAR_SIZE))
    bar_background = pygame.Surface((c.WINDOW_WIDTH, c.BAR_SIZE))
    font = pygame.font.SysFont(c.FONT_NAME, c.FONT_SIZE)

    previous_mouse = False

    while True:
        screen.fill(c.WINDOW_COLOR)
        bar_background.fill(c.BAR_COLOR)
        screen.blit(bar_background, (0, 0))
        main_background.fill((0, 0, 0))
        screen.blit(main_background, (0, c.BAR_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        previous_mouse = run_button_bar(screen, font, previous_mouse)

        pygame.display.flip()
