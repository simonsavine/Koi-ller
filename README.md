# Koi-ller

A physics-based 2D game in Python and Pygame. You play a killer koi fish who wants revenge on the fishy peacemakers that rule the bottom of the ocean. Fight endless waves of tuna cops and big bad salmon with a gun whose bullets ricochet off the walls.

**Status:** work in progress. The intro, loading screen, player movement and enemy sprites work. Enemy behaviour, bullet physics and the scoreboard are still under development.

## How it plays

1. An intro text sets the scene. Press ENTER to continue.
2. A loading animation plays.
3. You control the koi and face waves of tunas and salmon. Bullets bounce off walls, so aim with the angles in mind.

Controls: move with WASD or the arrow keys. Press ESC to leave the game.

## Run it

```bash
pip install pygame pygame_gui
cd Screens
python MainGame.py
```

## Tech

Python, Pygame, pygame_gui, and [ptext](https://github.com/cosmologicon/pygame-text) for the intro text.

## Project layout

- `Screens/` holds the intro, loading bar, main game and scoreboard name entry.
- `Enemies/` holds enemy movement and AI.
- `Player/` holds the bullet physics.
- `Assets/Images/` holds the sprites and background.
