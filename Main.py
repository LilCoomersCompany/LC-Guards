""""""
"imports"
import pygame
import moviepy.editor
import mysql.connector
import main.Constants as c
import main.Fields.Naming_field as naming
from main.Fields.Buttons_bar import run_button_bar

pygame.init()


"SQL"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ms@24663938",
    database="mua"
)
myCursor = mydb.cursor()
sql = "INSERT INTO names (name) VALUES (%s)"


"Screens"
window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT), pygame.NOFRAME)
main_background = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT - c.BAR_SIZE))
bar_background = pygame.Surface((c.WINDOW_WIDTH, c.BAR_SIZE))
clear_background = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT - c.BAR_SIZE))


def background_maker():
    background = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT - c.BAR_SIZE))
    main_background.blit(background, (0, 0))
    return background


"images"
image = pygame.image.load('F:/Mohammad/Anime-images/desktop-wallpaper-cute-scary-anime-horror-anime-pfp.jpg')
preview = moviepy.editor.VideoFileClip("../Data/Preview.mp4")

"preview video settings"
video_frames = []
for frame in preview.iter_frames():
    video_frames.append(pygame.image.frombuffer(frame, preview.size, "RGB"))

"extract audio preview file"
# preview_audio = preview.audio
# preview_audio.write_audiofile("Preview_audio.mp3")
pygame.mixer.music.load("../Data/Preview_audio.mp3")
pygame.mixer.music.play()

"fonts"
font = pygame.font.SysFont(c.FONT_NAME, c.FONT_SIZE)

"Loop"
x = False
t = True
while c.MAIN_LOOP_KEY:

    "default color"
    window.fill(c.WINDOW_COLOR)
    bar_background.fill(c.BAR_COLOR)

    "background"
    window.blit(main_background, (0, c.BAR_SIZE))
    window.blit(bar_background, (0, 0))

    "Events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.MAIN_LOOP_KEY = False

            "Naming_field"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if naming.input_rect.collidepoint(event.pos):
                naming.active = True
            else:
                naming.active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                naming.user_text = naming.user_text[:-1]

            elif event.key == pygame.K_KP_ENTER:
                if c.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
                    x = True
            else:
                naming.user_text += event.unicode

    "bar buttons"
    c.BUTTON_BAR_KEY = run_button_bar(window, font, c.BUTTON_BAR_KEY)

    if c.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
        if t:
            text_surface = naming.base_font.render(naming.user_text, True, (255, 255, 255))
            pygame.draw.rect(main_background, naming.color, naming.input_rect)
            main_background.blit(text_surface, (naming.input_rect.x + 5, naming.input_rect.y + 5))
            if x:
                myCursor.execute(sql, (naming.user_text,))
                mydb.commit()
                print(myCursor.rowcount, "record inserted.")
                P = background_maker()
                P_text = naming.base_font.render('Welcome to LC Guards ' + naming.user_text, True, (255, 255, 255))
                main_background.blit(P_text, (650, 470))
                x = False
                t = False

    "preview"
    if c.CURRENT_FRAME_PREVIEW < len(video_frames) - 12:
        main_background.blit(video_frames[c.CURRENT_FRAME_PREVIEW], (0, 0))
        c.CURRENT_FRAME_PREVIEW += 1
        if c.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
            pygame.mixer.music.stop()

    "refresh page"
    pygame.display.flip()
    # pygame.display.update()
    pygame.time.Clock().tick(c.FPS)

"End"
pygame.quit()
