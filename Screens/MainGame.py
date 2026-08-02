import pygame, pygame_gui, sys, LoadingBar

pygame.init()

# Change width and height according to screen dimensions
WIDTH, HEIGHT = 800, 800

background_img = pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/Background.jpg")
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Player stats
player_x, player_y, player_speed = WIDTH / 3, 0 , 3
x_dir, y_dir = 0, 0

playerOG = pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/Front.png")

# Dimensions of fish should be relevant to screen width and height
player = pygame.transform.scale(playerOG, (WIDTH / 8, HEIGHT / 8))
player_rect = player.get_rect()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Koi-ller")

timer = pygame.time.Clock()
fps = 60

def draw_fish():

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))


running, moving = True, True
while running:

    timer.tick(fps)
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement

        if moving:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                    x_dir = 3
                elif event.key == pygame.K_a:
                    x_dir = -3
                elif event.key == pygame.K_w:
                    y_dir = -3
                elif event.key == pygame.K_s:
                    y_dir = 3
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    x_dir = 0
                elif event.key == pygame.K_a:
                    x_dir = 0
                elif event.key == pygame.K_w:
                    y_dir = 0
                elif event.key == pygame.K_s:
                    y_dir = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit(0)

    if moving:
        player_x += player_speed * x_dir
        player_y += player_speed * y_dir

    draw_fish()
    pygame.display.flip()

pygame.quit()