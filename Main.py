import pygame

pygame.init()

pygame.display.set_caption("LC Guards")

pygame.display.set_icon(pygame.image.load('../Photos/Github-icon.jpg'))

window = pygame.display.set_mode((1800, 1000))  # an option pygame.NOFRAME
background = pygame.Surface((1600, 800))

# images
image = pygame.image.load('F:/Mohammad/Anime-images/desktop-wallpaper-cute-scary-anime-horror-anime-pfp.jpg')

run_Key = True

while run_Key:

    # default color
    window.fill((155, 155, 155))

    # background
    window.blit(background, (100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_Key = False

    pygame.draw.circle(background, (0, 0, 255), (800, 400), 75)

    pygame.display.flip()
    # pygame.display.update()

pygame.quit()
