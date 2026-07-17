import pygame
import pygame_gui
import sys
import time

def typewriter_effect(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.1)

pygame.init()

pygame.display.set_caption("Intro")

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Not entirely sure this is needed
CLOCK = pygame.time.Clock()

font = pygame.font.SysFont('freesans', 75)

box_width, box_height = WIDTH * 0.375, HEIGHT * 0.075

rect = pygame.Rect(0, 0, box_width, box_height)
rect.center = (WIDTH / 2, HEIGHT / 2)

# Looooong text incoming:

IntroText = font.render(
    "You are a killer koi fish, thirsy for revenge and angered by the" \
    "the fishy peacemakers that rule the bottom of the ocean. You are equipped with a gun" \
    "that can richochet off of walls and an immaculate sense of ballistic physics. Let them know" \
    "your rage!", True, (80, 80, 80)
)

# Infinite loop for display:

running = True
while running:
    SCREEN.blit(IntroText, rect)
    running = False

pygame.display

