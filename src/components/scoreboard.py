from src.services.visualisation_service import VisualisationService
from src.services.score_service import ScoreService
from src.config import Config
from src.utils.tools import sine


class ScoreBoard:

    def __init__(self):

        self._current_score = 0
        self._max_score = ScoreService.get_max_score()

    def reset_score(self):
        self._current_score = 0

    def increase_score(self):
        self._current_score += 1

    def get_max_score(self):
        return self._max_score

    def get_current_score(self):
        return self._current_score

    def update_max_score(self):
        if self._current_score > self._max_score:
            ScoreService.update_max_score(self._current_score)
            self._max_score = self._current_score

    def draw(self, screen):
        y = sine(200, 1280., 10.0, 40)
        show_score = VisualisationService.get_main_font().render(
            f"{self._current_score}", False, (0, 0, 0))
        score_rect = show_score.get_rect(center=(180, y + 30))
        screen.blit(VisualisationService.get_scoreboard_image(), (113, y))
        screen.blit(show_score, score_rect)
