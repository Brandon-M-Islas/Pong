import pygame
import pygame.freetype

pygame.init()
GAME_FONT        = pygame.freetype.SysFont("Ariel", 24)
SCOREBOARD, text_rect = GAME_FONT.render(f"0           SCORE           1", (255, 255, 255))


print(SCOREBOARD, text_rect, SCOREBOARD.get_rect())