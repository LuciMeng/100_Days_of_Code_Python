# Day 20–21: Snake Game Update

## Project Overview

This project builds on the Snake Game from previous lessons. The main enhancement is a **high score tracking system**. When the player achieves a new high score, it is saved to a file and remains available even after the game is closed. When the game starts again, the saved high score is loaded and displayed on the screen.

This feature was implemented using Python file handling (`read()` and `write()`) along with the `with` statement, which I learned in Day 24.

## What I Learned

### Reading from Files

The `read()` method is used to load data from a file. When the game starts, it reads the saved high score from `data.txt` and displays it on the scoreboard.

### Writing to Files

The `write()` method is used to save data to a file. When the player beats the current high score, the new high score is written to `data.txt`, replacing the previous record.

### Using the `with` Statement

The `with` statement automatically handles opening and closing files, making file operations cleaner and safer.

## How It Works

### `__init__()`

When the scoreboard is created, the game reads the saved high score from `data.txt` and stores it in `self.high_score`.

### `snake.reset()`

When the snake collides with a wall or itself, the snake is reset to its starting position and a new game begins.

### `reset_scoreboard()`

If the current score exceeds the saved high score, the new high score is written to `data.txt` and updated on the scoreboard.

## Project Highlights

- Added persistent high score tracking.
- Learned how to read from and write to files using Python.
- Used the `with` statement to manage file operations safely.
- High scores remain saved even after the game is closed and reopened.
