import pygame
import pygame_gui
import sys


pygame.init()

# Change width and height according to screen dimensions
WIDTH, HEIGHT = 800, 800

# Player stats
player_x, player_y = 300, 300
player_speed = 3
x_dir = 0
y_dir = 0

playerOG = pygame.image.load("/Users/simonsavine/Documents/Python/Java/GitHub/Koi-ller/Assets/Images/Front.png")

# Dimensions of fish should be relevant to screen width and height
player = pygame.transform.scale(playerOG, (200, 200))
player_rect = player.get_rect()
player_rect_x = 0
player_rect_y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Koi-ller")

timer = pygame.time.Clock()
fps = 60

def hitbox():

    # Replace rectangle with fish sprite

    # Rectangle for easy collisions with enemy fish
    
    # Change rectangle according to game window later

    pygame.draw.rect(screen, 'green', [player_x, player_y, 100, 100], 0, 5)

def draw_fish():

    screen.fill('white')
    screen.blit(player, player_rect)
    pygame.display.flip()


running = True
moving = True
while running:

    timer.tick(fps)
    screen.fill('white')

    if moving:
        hitbox()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement

        if moving:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                    x_dir = 3
                    player_rect_x = 3
                elif event.key == pygame.K_a:
                    x_dir = -3
                    player_rect_x = -3
                elif event.key == pygame.K_w:
                    y_dir = -3
                    player_rect_y = -3
                elif event.key == pygame.K_s:
                    y_dir = 3
                    player_rect_y = 3
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    x_dir = 0
                    player_rect_x = 0
                elif event.key == pygame.K_a:
                    x_dir = 0
                    player_x_rect = 0
                elif event.key == pygame.K_w:
                    y_dir = 0
                    player_rect_y = 0
                elif event.key == pygame.K_s:
                    y_dir = 0
                    player_rect_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit(0)

    if moving:
        player_x += player_speed * x_dir
        player_rect_x += player_speed * x_dir
        player_y += player_speed * y_dir
        player_rect_y += player_speed * y_dir

    draw_fish()
    pygame.display.flip()

pygame.quit()