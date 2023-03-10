import pygame
import settings as s


class Spaceship:

    def __init__(self, screen):
        self.image = self.load_image_of_spaceship()
        self.spaceship_rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = s.SPACESHIP_SPEED

        self.spaceship_rect.midbottom = self.screen_rect.midbottom
        self.spaceship_x_float = float(self.spaceship_rect.x)

    def move(self, right=False, left=False):
        if right and self.spaceship_rect.right < self.screen_rect.right:
            self.spaceship_x_float += self.speed
            self.spaceship_rect.x = self.spaceship_x_float
        if left and self.spaceship_rect.left > 0:
            self.spaceship_x_float -= self.speed
            self.spaceship_rect.x = self.spaceship_x_float

    @staticmethod
    def load_image_of_spaceship():
        image = pygame.image.load('images/x-wing.png')
        return image


if __name__ == '__main__':
    pass
