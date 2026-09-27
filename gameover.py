import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH

pygame.font.init()
font = pygame.font.Font(None,36)
game_over_screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.Surface.fill(game_over_screen,"Red")
game_over_screen.set_alpha(100)
game_over_text = font.render("Game Over! Try Again?",True,"White",)