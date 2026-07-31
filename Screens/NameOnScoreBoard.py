import pygame
import pygame_gui
import sys
import random

pygame.init()

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

#CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((WIDTH / 2 - 250, HEIGHT / 2 - 30), (500, 60)),
    manager=MANAGER,
    object_id="#main_text_entry"
) 

# Then display new page with top 5 best scores with attributed names




