import pygame
from main.Auxiliary.Buttons_bar import Buttons_bar

pygame.init()

"Default bar"
# pygame.display.set_caption("LC Guards")
# pygame.display.set_icon(pygame.image.load('../Photos/Github-icon.jpg'))


"Screens"
window = pygame.display.set_mode((1600, 1000), pygame.NOFRAME)
main_background = pygame.Surface((1600, 960))
bar_background = pygame.Surface((1600, 40))

"images"
image = pygame.image.load('F:/Mohammad/Anime-images/desktop-wallpaper-cute-scary-anime-horror-anime-pfp.jpg')

"fonts"
font = pygame.font.SysFont('Arial', 10)

"Loop"
run_Key = True
while run_Key:

    "default color"
    window.fill((155, 155, 155))
    bar_background.fill((200, 200, 200))

    "background"
    window.blit(main_background, (0, 40))
    window.blit(bar_background, (0, 0))

    "Events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_Key = False

    pygame.draw.circle(main_background, (0, 0, 255), (800, 480), 75)

    "bar buttons"
    Buttons_bar(window, font).process()

    "refresh page"
    pygame.display.flip()
    # pygame.display.update()
    pygame.time.Clock().tick(60)

"End"
pygame.quit()
