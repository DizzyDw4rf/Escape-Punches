import pygame

from src.config import Config
from src.services.visualisation_service import VisualisationService


vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = VisualisationService.get_player_image()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec((200, 640))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.player_position = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()


        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = - Config.ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = + Config.ACC
        if pressed_keys[pygame.K_UP]:
            self.acc.y = - Config.ACC
        if pressed_keys[pygame.K_DOWN]:
            self.acc.y = + Config.ACC

        self.acc.x += self.vel.x * Config.FRIC
        self.acc.y += self.vel.y * Config.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        if self.pos.x > Config.WIDTH:
            self.pos.x = Config.WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > Config.HEIGHT:
            self.pos.y = Config.HEIGHT
        if self.pos.y < 200:
            self.pos.y = 200

        self.rect.center = self.pos

    def draw_rect(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.pos = vec((200, 640))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
