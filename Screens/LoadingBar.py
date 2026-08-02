import pygame, pygame_gui, threading, IntroText, sys

pygame.init()

fps = 60
font = pygame.font.SysFont("cobo", 100)
clock = pygame.time.Clock()

bar_width = int(IntroText.WIDTH * 0.5)
bar_height = int(bar_width * (110 / 1200))

screen = pygame.display.set_mode((IntroText.WIDTH, IntroText.HEIGHT))
pygame.display.set_caption("Loading screen")

# Work
WORK = 100000000

loading_bg = pygame.transform.smoothscale(
pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/LoadingBarBG.png"), (bar_width, bar_height))

loading_bg_rect = loading_bg.get_rect(center = (IntroText.WIDTH / 2, IntroText.HEIGHT/ 2))

loading_bar_original = pygame.transform.smoothscale(
    pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/LoadingBar.png"), (bar_width, bar_height))

loading_bar_rect = loading_bar_original.get_rect(midleft = (IntroText.WIDTH / 4, IntroText.HEIGHT / 2))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    # Do some math to build up progress on bar
    global loading_finished, loading_progress
    for i in range(WORK):
        math_equation = 523687 / 789456 * 89456
        loading_progress = i

    loading_finished = True

threading.Thread(target = doWork).start()

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

    screen.fill('white')

    if not loading_finished:
        loading_bar_width = int(loading_progress / WORK * bar_width)
        loading_bar = pygame.transform.scale(loading_bar_original, (int(loading_bar_width), bar_height))
        loading_bar_rect = loading_bar.get_rect(midleft=(IntroText.WIDTH / 4, IntroText.HEIGHT / 2))
        screen.blit(loading_bg, loading_bg_rect)
        screen.blit(loading_bar, loading_bar_rect)

        screen.blit(loading_bar_original, loading_bar_rect, pygame.Rect(0, 0, loading_bar_width, bar_height))
    else:
        running = False

    clock.tick(fps)

    pygame.display.flip()
