import pygame, pygame_gui, sys, LoadingBar, IntroText

screen = pygame.display.set_mode(IntroText.WIDTH, IntroText.HEIGHT)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit("Fuck your mom")
    pygame.display.flip()