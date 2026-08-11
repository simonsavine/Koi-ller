import pygame, pygame_gui, sys, LoadingBar, IntroText

pygame.init()

# Change width and height according to screen dimensions
WIDTH, HEIGHT = IntroText.WIDTH, IntroText.HEIGHT

background_img = pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/Background.jpg")
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Player stats
player_x, player_y, player_speed = WIDTH / 3, 0 , 3
player_width = WIDTH / 8
x_dir, y_dir = 0, 0

playerOG = pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/Front.png")

# Dimensions of fish should be relevant to screen width and height
player = pygame.transform.scale(playerOG, (WIDTH / 8, HEIGHT / 8))
player_rect = player.get_rect()
#player.rect.topleft = (player_x, player_y)

'''
Use mask for eventual collisions with enemies
player_mask = pygame.mask.from_surface(player)
player_image = player_mask.to_surface()
'''

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Koi-ller")

timer = pygame.time.Clock()
fps = 60

def draw_fish():
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)

running, moving = True, True
while running:

    timer.tick(fps)
    screen.fill('white')

    for event in pygame.event.get():

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background = pygame.transform.scale(background_img, (event.w, event.h))

        if event.type == pygame.QUIT:
            running = False

        # Movement

        if moving:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_dir = 3
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_dir = -3
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    y_dir = -3
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y_dir = 3
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_dir = 0
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_dir = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    y_dir = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y_dir = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Movement + collisions
    if moving:

        player_rect.x += player_speed * x_dir
        player_rect.y += player_speed * y_dir

        player_rect.clamp_ip(screen.get_rect())

    draw_fish()
    pygame.display.flip()

pygame.quit()