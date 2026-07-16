import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption("What's in a name?")

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((WIDTH / 2 - 250, HEIGHT / 2 - 30), (500, 60)),
    manager=MANAGER,
    object_id="#main_text_entry"
)     

font = pygame.font.SysFont('freesans', 75)

def choice(player_decision):
    if player_decision in ("rock", "paper", "scissors"):
        SCREEN.fill("white")
        CLOCK.tick(60)
        pygame.display.update()
        pygame.time.delay(500)
        return player_decision

def player_text():
    running = True
    while running:
      RR = CLOCK.tick(60) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

        # Player input becomes text after pressing ENTRY key:

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
          text = event.text.lower().strip()

          result = choice(text)

          if result:               
             return result
          
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()

        MANAGER.process_events(event)

      MANAGER.update(RR)

      SCREEN.fill("white")

      MANAGER.draw_ui(SCREEN)

      pygame.display.update()


player_text()