import pygame
import moviepy.editor
import main.Parameters.Constants as C
import main.Parameters.keys as K
import main.Fields.Naming_field as NF
from main.Fields.Buttons_bar import run_button_bar
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ms@24663938",
    database="mua"
)
myCursor = mydb.cursor()
sql = "INSERT INTO names (name) VALUES (%s)"

pygame.init()

"Screens"
window = pygame.display.set_mode((C.WINDOW_WIDTH, C.WINDOW_HEIGHT), pygame.NOFRAME)
main_background = pygame.Surface((C.WINDOW_WIDTH, C.WINDOW_HEIGHT - C.BAR_SIZE))
bar_background = pygame.Surface((C.WINDOW_WIDTH, C.BAR_SIZE))
clear_background = pygame.Surface((C.WINDOW_WIDTH, C.WINDOW_HEIGHT - C.BAR_SIZE))


def background_maker():
    background = pygame.Surface((C.WINDOW_WIDTH, C.WINDOW_HEIGHT - C.BAR_SIZE))
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
font = pygame.font.SysFont(C.FONT_NAME, C.FONT_SIZE)

"Loop"
x = False
t = True
while K.MAIN_LOOP:

    "default color"
    window.fill(C.WINDOW_COLOR)
    bar_background.fill(C.BAR_COLOR)

    "background"
    window.blit(main_background, (0, C.BAR_SIZE))
    window.blit(bar_background, (0, 0))

    "Events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_Key = False
            "Naming_field"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if NF.input_rect.collidepoint(event.pos):
                NF.active = True
            else:
                NF.active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                NF.user_text = NF.user_text[:-1]

            elif event.key == pygame.K_KP_ENTER:
                if K.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
                    x = True
            else:
                NF.user_text += event.unicode

    "bar buttons"
    K.BUTTON_BAR = run_button_bar(window, font, K.BUTTON_BAR)

    if K.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
        if t:
            text_surface = NF.base_font.render(NF.user_text, True, (255, 255, 255))
            pygame.draw.rect(main_background, NF.color, NF.input_rect)
            main_background.blit(text_surface, (NF.input_rect.x + 5, NF.input_rect.y + 5))
            if x:

                myCursor.execute(sql, (NF.user_text,))
                mydb.commit()
                print(myCursor.rowcount, "record inserted.")
                background_maker()
                print("5")
                x = False
                t = False

    "preview"
    if K.CURRENT_FRAME_PREVIEW < len(video_frames) - 12:
        main_background.blit(video_frames[K.CURRENT_FRAME_PREVIEW], (0, 0))
        K.CURRENT_FRAME_PREVIEW += 1
        if K.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
            pygame.mixer.music.stop()

    # if K.CURRENT_FRAME_PREVIEW == len(video_frames) - 12:
    #     background_maker()

    "refresh page"
    pygame.display.flip()
    # pygame.display.update()
    pygame.time.Clock().tick(C.FPS)

"End"
pygame.quit()
