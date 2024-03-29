import sys
import pygame as p
import settings as s
from star import Star
from text import Text


class Menu:

    def __init__(self, title_img, game):
        self.game = game
        self.screen = game.screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        p.display.set_caption('Empire Invaders')
        self.stars = p.sprite.Group()

        self.play_button_img = p.image.load('images/play_button.bmp')
        self.quit_button_img = p.image.load('images/quit_button.bmp')

        self.title = Text(self.screen, title_img, self.width // 2, self.height // 4)
        self.quit_button = Text(self.screen, self.quit_button_img, self.width // 2, self.height // 1.3)
        self.play_button = Text(self.screen, self.play_button_img, self.width // 2, self.height // 1.7)

    def main_loop(self):
        if len(self.stars) == 0:
            self.create_stars()
        while True:
            self.check_events()
            self.screen.fill(color=s.SCREEN_COLOR)
            self.stars.update()
            self.quit_button.blit_text()
            self.play_button.blit_text()
            self.title.blit_text()
            p.display.flip()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()
                if self.quit_button.rect.collidepoint(mouse_pos):
                    sys.exit()
                if self.play_button.rect.collidepoint(mouse_pos):
                    self.game.main_loop()

    def create_stars(self):
        for _ in range(1000):
            star = Star(self.screen)
            self.stars.add(star)


class MainMenu(Menu):

    def __init__(self, game):
        self.title_img = p.image.load('images/title.bmp')
        super().__init__(self.title_img, game)

    def main_loop(self):
        p.mixer.music.load('sounds/main_theme.mp3')
        p.mixer.music.set_volume(0.1)
        p.mixer.music.play(-1)
        super().main_loop()


class LoseMenu(Menu):

    def __init__(self, game):
        self.lose_img = p.image.load('images/lose_title.bmp')
        super().__init__(self.lose_img, game)

    def main_loop(self):
        p.mixer.music.load('sounds/lose_theme.mp3')
        p.mixer.music.set_volume(0.1)
        p.mixer.music.play(-1)
        self.game.level = 1
        super().main_loop()


class WinMenu(Menu):

    def __init__(self, game):
        self.win_img = p.image.load('images/win_title.bmp')
        super().__init__(self.win_img, game)

    def main_loop(self):
        p.mixer.music.load('sounds/win_theme.mp3')
        p.mixer.music.play()
        self.game.level = 1
        super().main_loop()


class PauseMenu(Menu):

    def __init__(self, game):
        self.title_img = p.image.load('images/title.bmp')
        super().__init__(self.title_img, game)
        self.play_button_img = p.image.load('images/resume_button.bmp')
        self.play_button_img = p.transform.scale(self.play_button_img, (420, 140))
        self.play_button = Text(game.screen, self.play_button_img, self.width // 2, self.height // 1.7)


if __name__ == '__main__':
    pass
