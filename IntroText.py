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
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)

# Not entirely sure this is needed
CLOCK = pygame.time.Clock()

font = pygame.font.SysFont('freesans', 75)

box_width, box_height = WIDTH * 0.375, HEIGHT * 0.075

rect = pygame.Rect(0, 0, box_width, box_height)
rect.center = (WIDTH / 2, HEIGHT / 2)

# Looooong text incoming:

IntroText = font.render(
    "You are a killer koi fish, thirsy for revenge and angered by the" \
    "fishy peacemakers that rule the bottom of the ocean. You are equipped with a gun" \
    "that can richochet off of walls and an immaculate sense of ballistic physics. Let them know" \
    "your rage! Press ENTER to continue..", True, (80, 80, 80)
)

text_rect = IntroText.get_rect()

# Infinite loop for display:

running = True
while running:
    SCREEN.blit(IntroText, text_rect)
    running = False

    # Upon pressing ENTER, the player goes to the next screen (Main game loop)

    for event in pygame.event.get():

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            running = False
            
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()

pygame.display

