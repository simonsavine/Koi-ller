import pygame

pygame.init()

pygame.display.set_caption("Intro")

# Resize as you desire:
WIDTH, HEIGHT = 1400, 800

font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
timer = pygame.time.Clock()
message = "You are a killer koi fish, thirsty for revenge and angered by the " \
    "fishy peacemakers that rule the bottom of the ocean. You are equipped with a gun " \
    "that can richochet off of walls and an immaculate sense of ballistic physics. Let them know " \
    "your rage! Press ENTER to continue.."
snip = font.render('', True, 'white')
counter = 0
speed = 1
done = False

running = True
while running:

    screen.fill('white')
    timer.tick(60)

    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True

    # The first letter to cross the WIDTH threshold goes to next line:

    for char in message:
        if font.size(char)[0] < WIDTH:
            # blit next part of message on next line

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    snip = font.render(message[0:counter//speed], True, 'black')
    screen.blit(snip, (0, 0))

    pygame.display.flip()


