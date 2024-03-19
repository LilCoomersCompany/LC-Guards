import pygame

pygame.init()

"Default bar"
# pygame.display.set_caption("LC Guards")
# pygame.display.set_icon(pygame.image.load('../Photos/Github-icon.jpg'))


"Screens"
window = pygame.display.set_mode((1800, 1000), pygame.NOFRAME)
main_background = pygame.Surface((1600, 800))
bar_background = pygame.Surface((1800, 50))

"images"
image = pygame.image.load('F:/Mohammad/Anime-images/desktop-wallpaper-cute-scary-anime-horror-anime-pfp.jpg')

"Loop"
run_Key = True
while run_Key:

    "default color"
    window.fill((155, 155, 155))
    bar_background.fill((90, 255, 45))

    "background"
    window.blit(main_background, (100, 50))
    window.blit(bar_background, (0, 0))

    "Events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_Key = False

    pygame.draw.circle(main_background, (0, 0, 255), (800, 400), 75)

    "refresh page"
    pygame.display.flip()
    # pygame.display.update()

"End"
pygame.quit()
