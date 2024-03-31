""""""
import moviepy.editor
import pygame
import sys
import main.Constants as c


def run_button_bar(Screen, Font, Previous_mouse, icon, icon3, video, icon11):
    # backgrounds = [
    #     {'name': "normal", 'location': 'C:/Users/h510/Desktop/LC Guards/Data/f.1.jpg'},
    #     {'name': "hover", 'location': "../Data/Amir2.mp4"},
    #     {'name': "pressed", 'location': 'C:/Users/h510/Desktop/LC Guards/Data/f.2.jpg'}
    # ]
    # icon_0 = pygame.image.load(backgrounds[0]['location'])
    # icon_1 = pygame.image.load(backgrounds[2]['location'])
    # icon_0 = pygame.transform.scale(icon_0, (60, 60))
    # icon_1 = pygame.transform.scale(icon_1, (60, 60))
    # icon_1_0 = moviepy.editor.VideoFileClip(backgrounds[1]['location'])
    # video_frames_icon = []
    # for frame in icon_1_0.iter_frames():
    #     video_frames_icon.append(pygame.image.frombuffer(frame, icon_1_0.size, "RGB"))

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
        # buttonSurf = Font.render(button['name'], True, c.FONT_COLOR)
        buttonSurface.fill(c.BAR_COLOR)
        buttonRects.append(buttonRect)
        # buttonSurfs.append(buttonSurf)
        buttonSurfaces.append(buttonSurface)

    if buttons[0]['name']:
        Screen.blit(icon, (buttons[0]['location'], 0))
    if buttons[1]['name']:
        Screen.blit(icon11, (buttons[2]['location'], 0))
    if buttons[2]['name']:
        Screen.blit(icon11, (buttons[1]['location'], 0))
        # buttonSurfaces[buttons.index(button)].blit(buttonSurfs[buttons.index(button)], [
        #     buttonRects[buttons.index(button)].width / 2 - buttonSurfs[
        #         buttons.index(button)].get_rect().width / 2,
        #     buttonRects[buttons.index(button)].height / 2 - buttonSurfs[
        #         buttons.index(button)].get_rect().height / 2
        # ])
        # Screen.blit(buttonSurfaces[buttons.index(button)],
        #             buttonRects[buttons.index(button)])

    mousePos = pygame.mouse.get_pos()
    for button in buttons:
        if buttonRects[buttons.index(button)].collidepoint(mousePos):
            if button['name'] == "Close":
                # buttonSurfaces[buttons.index(button)].fill(c.SPECIAL_HOVER_BAR_BUTTONS_COLOR)
                c.CURRENT_FRAME_DEMO += 1
                if c.CURRENT_FRAME_DEMO < len(video) - 2:
                    Screen.blit(video[c.CURRENT_FRAME_DEMO], (1540, 0))
                elif c.CURRENT_FRAME_DEMO >= len(video) - 2:
                    Screen.blit(icon3, (1540, 0))

                if Previous_mouse:
                    # buttonSurfaces[buttons.index(button)].fill(c.SPECIAL_PRESSED_BAR_BUTTONS_COLOR)
                    Screen.blit(icon3, (1540, 0))
                    c.CURRENT_FRAME_DEMO = 0
                    if not current_mouse:
                        pygame.quit()
            elif button['name'] == "Minimize" or button['name'] == "FullScreen":
                # buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_HOVER_BAR_BUTTONS_COLOR)
                if button['name'] == "Minimize":
                    c.CURRENT_FRAME_DEMO2 += 1
                    if c.CURRENT_FRAME_DEMO2 < len(video) - 2:
                        Screen.blit(video[c.CURRENT_FRAME_DEMO2], (1420, 0))
                    elif c.CURRENT_FRAME_DEMO2 >= len(video) - 2:
                        Screen.blit(icon3, (1420, 0))
                if button['name'] == "FullScreen":
                    c.CURRENT_FRAME_DEMO1 += 1
                    if c.CURRENT_FRAME_DEMO1 < len(video) - 2:
                        Screen.blit(video[c.CURRENT_FRAME_DEMO1], (1480, 0))
                    elif c.CURRENT_FRAME_DEMO1 >= len(video) - 2:
                        Screen.blit(icon3, (1480, 0))
                if Previous_mouse:
                    if button['name'] == "Minimize":
                        buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
                        Screen.blit(icon3, (1420, 0))
                        c.CURRENT_FRAME_DEMO2 = 0
                        if not current_mouse:
                            pygame.display.iconify()
                    elif button['name'] == "FullScreen":
                        # buttonSurfaces[buttons.index(button)].fill(c.DEFAULT_PRESSED_BAR_BUTTONS_COLOR)
                        Screen.blit(icon3, (1480, 0))
                        c.CURRENT_FRAME_DEMO1 = 0
                        if not current_mouse:
                            pygame.display.toggle_fullscreen()

                # buttonSurfaces[buttons.index(button)].blit(buttonSurfs[buttons.index(button)], [
                #     buttonRects[buttons.index(button)].width / 2 - buttonSurfs[
                #         buttons.index(button)].get_rect().width / 2,
                #     buttonRects[buttons.index(button)].height / 2 - buttonSurfs[
                #         buttons.index(button)].get_rect().height / 2
                # ])
                # Screen.blit(buttonSurfaces[buttons.index(button)],
                #             buttonRects[buttons.index(button)])
                if button['name'] == "Close":
                    Screen.blit(icon, (button['location'], 0))
                if button['name'] == "Minimize":
                    # Screen.blit(icon11, (button['location'], 0))
                    pass
                if button['name'] == "FullScreen":
                    # Screen.blit(icon11, button['location'], 0)
                    pass

    return current_mouse


if __name__ == "__main__":
    pygame.init()

    width, height = c.WINDOW_WIDTH, c.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    main_background = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT - c.BAR_SIZE))
    bar_background = pygame.Surface((c.WINDOW_WIDTH, c.BAR_SIZE))
    font = pygame.font.SysFont(c.FONT_NAME, c.FONT_SIZE)
    backgrounds = [
        {'name': "normal", 'location': 'C:/Users/h510/Desktop/LC Guards/Data/f.1.jpg'},
        {'name': "hover", 'location': "C:/Users/h510/Desktop/LC Guards/Data/amir2.mp4"},
        {'name': "pressed", 'location': 'C:/Users/h510/Desktop/LC Guards/Data/f.2.jpg'},
        {'name': "min", 'location': 'C:/Users/h510/Desktop/LC Guards/Data/f.11.jpg'},
    ]
    icon_0 = pygame.image.load(backgrounds[0]['location'])
    icon_1 = pygame.image.load(backgrounds[2]['location'])
    icon_00 = pygame.image.load(backgrounds[3]['location'])
    icon_0 = pygame.transform.scale(icon_0, (60, 60))
    icon_1 = pygame.transform.scale(icon_1, (60, 60))
    icon_00 = pygame.transform.scale(icon_00, (60, 60))
    icon_1_0 = moviepy.editor.VideoFileClip(backgrounds[1]['location'])
    video_frames_icon = []
    for frame in icon_1_0.iter_frames():
        video_frames_icon.append(pygame.image.frombuffer(frame, icon_1_0.size, "RGB"))

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

        previous_mouse = run_button_bar(screen, font, previous_mouse, icon_0, icon_1, video_frames_icon)

        pygame.display.flip()
