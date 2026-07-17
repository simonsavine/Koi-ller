import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption("Intro")

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))


# Not entirely sure this is needed
CLOCK = pygame.time.Clock()

font = pygame.font.SysFont('freesans', 75)

pygame.display()

# Looooong text incoming:

IntroText = font.render(
    "You are a killer koi fish, thirsy for revenge and angered by the" \
    "the fishy peacemakers that rule the bottom of the ocean. You are equipped with a gun" \
    "that can richochet off of walls and an immaculate sense of ballistic physics. Let them know" \
    "your rage!"
)

SCREEN.blit(


)

pygame.display

