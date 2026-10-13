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

## Reasons for the changes

- **Added a controllable red player and falling blue blocks** to make the
  project a simple game with a clear objective: dodge obstacles.
- **Added keyboard controls and screen-edge limits** so the player can steer
  precisely without leaving the play area.
- **Added collision detection and a game-over screen** to give dodging a
  consequence and show the player's survival time.
- **Made blocks speed up as time passes** to increase the challenge and reward
  longer survival.
- **Added a timer and speed display** so players can see their progress and
  understand the rising difficulty.
- **Added restart and quit keys** so players can replay without restarting the
  program.
- **Added `Start Game.bat` and `requirements.txt`** to make installing and
  launching the game easier on Windows.
- **Added this README** to explain the controls, implementation, and Pygame
  APIs used.

This project uses Pygame's documented event, display, drawing, time, keyboard,
rectangle, and font APIs:

- [Pygame documentation](https://www.pygame.org/docs/)
