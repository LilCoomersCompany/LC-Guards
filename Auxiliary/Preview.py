import pygame
import moviepy.editor


class Preview:
    def __init__(self, Current_frame, Main_background, Image):
        self.preview = moviepy.editor.VideoFileClip("../Data/Preview.mp4")
        self.video_frames = []
        self.current_frame = Current_frame
        self.main_background = Main_background
        self.image = Image
        for frame in self.preview.iter_frames():
            self.video_frames.append(pygame.image.frombuffer(frame, self.preview.size, "RGB"))
        # self.preview_audio = preview.audio
        # self.preview_audio.write_audiofile("output_audio.mp3")
        pygame.mixer.music.load("../Data/output_audio.mp3")
        pygame.mixer.music.play()

    def run(self):
        if self.current_frame < len(self.video_frames):
            self.main_background.blit(self.video_frames[self.current_frame], (0, 0))
            self.current_frame += 1
            if self.current_frame == len(self.video_frames) - 10:
                pygame.mixer.music.stop()
        if self.current_frame == len(self.video_frames):
            self.main_background.blit(self.image, (0, 0))
