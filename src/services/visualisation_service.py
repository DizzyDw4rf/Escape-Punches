import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualisationService:

    @staticmethod
    def get_right_hand_image():
        return pygame.image.load(ASSETS_DIR / "hand_right.png").convert_alpha()

    @staticmethod
    def get_left_hand_image():
        return pygame.image.load(ASSETS_DIR / "hand_left.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "slimepurple_step1_right.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_scoreboard_image():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_button.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title.png").convert_alpha()

    @staticmethod
    def get_intro_image():
        return pygame.image.load(MENU_DIR / "slimepurple_intro.png")

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "Pixeltype.ttf", 40)

    @staticmethod
    def get_credit_font():
        return pygame.font.Font(ASSETS_DIR / "Pixeltype.ttf", 40)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSETS_DIR / "Pixeltype.ttf", 30)

    @staticmethod
    def load_main_game_display():
        pygame.display.set_caption("Escape Punches")
        slime = VisualisationService.get_player_image()
        pygame.display.set_icon(slime)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualisationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_author_credit(screen):
        credit_font = VisualisationService.get_credit_font()
        author_credit = credit_font.render("Made by Dizzy", False, (0, 0, 0))
        credits_rect = author_credit.get_rect(center=(Config.WIDTH // 2, 620))
        screen.blit(author_credit, credits_rect)

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualisationService.get_score_font()
        best_score = score_font.render(f"Best: {max_score}", False, (0, 0, 0))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 250))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 100)
        title = VisualisationService.get_title_image()
        screen.blit(title, (30, y))
        intro = VisualisationService.get_intro_image()
        screen.blit(intro, (130, 330))

    @staticmethod
    def draw_press_any_key(screen, press_y):
        press_any = VisualisationService.get_press_key_image()
        screen.blit(press_any, (100, press_y))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualisationService.draw_author_credit(screen)
        VisualisationService.draw_best_score(screen, max_score)
        VisualisationService.draw_title(screen)
        VisualisationService.draw_press_any_key(screen, press_y)
