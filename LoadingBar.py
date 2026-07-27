import pygame
import pygame_gui

import IntroText

pygame.init()

screen = pygame.display.set_mode((IntroText.WIDTH, IntroText.HEIGHT))

# Temp message while I build the actual loading bar:
font = pygame.font.Font(None, 74)
loadingBarMsg = font.render("This is the loading bar page!", True, 'white')

running = True
while running:

    screen.blit(loadingBarMsg, (0, 0))

    running = False

    pygame.display.flip()

    pygame.time.delay(2000)