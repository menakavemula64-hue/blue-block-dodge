# Blue Block Dodge

A small dodge game made with Python and Pygame. Move the red player, avoid the
falling blue blocks, and try to survive as long as you can. The blocks get
faster as time passes.

## Start the game

On Windows, install Python and Pygame, then double-click **Start Game.bat**.
This launcher runs `game.py` from the project folder.

To install Pygame from a terminal instead:

```powershell
python -m pip install -r requirements.txt
```

You can also start the game directly with:

```powershell
python game.py
```

## How to play

- Move with the **arrow keys** or **W**, **A**, **S**, **D**.
- Avoid the blue blocks falling from the top of the window.
- The block speed increases every 10 seconds. Your survival time and speed
  level are shown in the top-left corner.
- After a collision, press **R** to restart or **Esc** to quit.

## How the game works

- `pygame.init()` initializes Pygame, and `pygame.display.set_mode()` creates
  the 800 x 600 game window.
- The main loop processes window and keyboard events, updates the game state,
  draws the scene, and refreshes the display.
- `pygame.time.Clock().tick(FPS)` limits the game to 60 frames per second and
  provides elapsed frame time for the survival timer.
- A Pygame timer event periodically creates a block at a random horizontal
  position. Blocks move downward, and their speed increases every 10 seconds.
- `pygame.Rect` represents the player and blocks. Its boundary-clamping and
  collision methods keep the player in the window and detect when a block hits
  the player.
- Pygame drawing, font, and display functions render the player, blocks,
  timer, speed level, and game-over screen.

This project uses Pygame's documented event, display, drawing, time, keyboard,
rectangle, and font APIs:

- [Pygame documentation](https://www.pygame.org/docs/)
- [Pygame website](https://www.pygame.org/)
