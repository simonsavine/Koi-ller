import pygame
import pygame_gui
import sys


pygame.init()

WIDTH, HEIGHT = 800, 800
player_x, player_y = 300, 300
player_speed = 3
x_dir = 0
y_dir = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Koi-ller")

timer = pygame.time.Clock()
fps = 60

def draw_player():

    # Replace rectangle with fish sprite

    # Rectangle for easy collisions with enemy fish
    
    # Change rectangle according to game window later

    pygame.draw.rect(screen, 'green', [player_x, player_y, 100, 100], 0, 5)


running = True
moving = True
while running:

    timer.tick(fps)
    screen.fill('white')

    if moving:
        draw_player()

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
    
    pygame.display.flip()

pygame.quit()