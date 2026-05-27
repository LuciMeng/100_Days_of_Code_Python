# Day 22 - Pong Game

## Project Overview

I built a classic Pong Game using Python’s Turtle graphics module. Players control paddles to bounce the ball back and forth, 
while points are scored when the opponent misses the ball. The first player to reach 3 points wins the game.

## What I Learned

- Applying Object-Oriented Programming (OOP) to structure a game into reusable classes

- Using inheritance with custom `Paddle`, `Ball`, and `Scoreboard` classes

- Handling keyboard input with `listen()` and `onkey()`

- Implementing collision detection and real-time game updates

- Organizing code across multiple Python modules

## Methods & Features Used

- `goto()` to position paddles and ball objects

- `move()` to control ball movement

- `distance()` to detect paddle collisions

- `bounce_y()` and `bounce_x()` to reverse ball direction

- `screen.listen()` and `screen.onkey()` for paddle controls

- The ball speeds up every time hit by a paddle 

- `update_score()` and `game_over()` for score tracking and winner display

## Key Takeaways

- Improved understanding of OOP and inheritance

- Practiced collision detection and game loop logic

- Learned to build interactive games with real-time input handling

- Structured a larger project using multiple files and classes
