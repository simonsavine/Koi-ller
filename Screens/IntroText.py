import pygame, ptext

pygame.init()

pygame.display.set_caption("Intro")

# Resize as you desire:
WIDTH, HEIGHT = 1400, 800

font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
timer = pygame.time.Clock()
message = """You are a killer koi fish, thirsty for revenge and angered by the fishy peacemakers that rule the bottom of the ocean. You are equipped with a gun that can richochet off of walls and an immaculate sense of ballistic physics. Let them know your rage!



 Press ENTER to continue.. """
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False


    snip = message[0:counter//speed]
    ptext.draw(snip, (0, WIDTH / 11), width = WIDTH, color = 'black', fontsize = 75)

    pygame.display.flip()


