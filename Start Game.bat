@echo off
cd /d "%~dp0"
python game.py
if errorlevel 1 (
    echo.
    echo The game could not start. Check that Python and Pygame are installed.
    pause
)
