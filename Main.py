import pygame
import moviepy.editor
from main.Auxiliary.Buttons_bar import run_button_bar

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
preview = moviepy.editor.VideoFileClip("../Data/Preview.mp4")

"preview video settings"
video_frames = []
current_frame = 0
for frame in preview.iter_frames():
    video_frames.append(pygame.image.frombuffer(frame, preview.size, "RGB"))


"extract audio file"
# preview_audio = preview.audio
# preview_audio.write_audiofile("output_audio.mp3")
pygame.mixer.music.load("../Data/output_audio.mp3")
pygame.mixer.music.play()

"fonts"
font = pygame.font.SysFont('Arial', 10)

"Loop"
run_Key = True
preview_key = True
buttons_bar_key = False
while run_Key:

    "default color"
    window.fill((155, 155, 155))
    bar_background.fill((200, 200, 200))

    "background"
    window.blit(main_background, (0, 40))
    window.blit(bar_background, (0, 0))
    main_background.blit(video_frames[current_frame], (0, 0))

    "Events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_Key = False

    "bar buttons"
    buttons_bar_key = run_button_bar(window, font, buttons_bar_key)

    "refresh page"
    pygame.display.flip()
    current_frame += 1
    if current_frame >= len(video_frames):
        preview_key = False
    # pygame.display.update()
    pygame.time.Clock().tick(35)

"End"
pygame.quit()
