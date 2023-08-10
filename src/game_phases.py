import sys
import time
import pygame

from src.components.game_status import GameStatus
from src.components.hand import Hand
from src.components.hand_side import HandSide
from src.components.player import Player
from src.components.scoreboard import ScoreBoard
from src.global_state import GlobalState
from src.services.visualisation_service import VisualisationService
from src.utils.tools import *


GlobalState.load_main_screen()
VisualisationService.load_main_game_display()

scoreboard = ScoreBoard()

P1 = Player()
H1 = Hand(HandSide.RIGHT)
H2 = Hand(HandSide.LEFT)

hands = pygame.sprite.Group()
hands.add(H1)
hands.add(H2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(H1)
all_sprites.add(H2)


def main_menu_phase():
    scoreboard.reset_score()

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return
        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualisationService.draw_background_with_scroll(
        GlobalState.SCREEN, GlobalState.SCROLL)
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualisationService.draw_main_menu(
        GlobalState.SCREEN, scoreboard.get_max_score(), GlobalState.PRESS_Y)


def gameplay_phase():

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            game_over()
            return
    
    P1.update()
    H1.move(scoreboard, P1.player_position)
    H2.move(scoreboard, P1.player_position)

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualisationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)

    P1.draw_rect(GlobalState.SCREEN)
    H1.draw(GlobalState.SCREEN)
    H2.draw(GlobalState.SCREEN)
    scoreboard.draw(GlobalState.SCREEN)

    if pygame.sprite.spritecollide(P1, hands, False, pygame.sprite.collide_mask):
        scoreboard.update_max_score()
        time.sleep(0.5)
        game_over()    


def exit_game_phase():
    pygame.quit()
    sys.exit()


def game_over():
    P1.reset()
    H1.reset()
    H2.reset()
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    time.sleep(0.5)
