# Day 20-21 - Snake Game

## Project Overview
Built a classic Snake Game using Python’s Turtle graphics module. The snake grows when it eats food, while the score updates dynamically. The game ends if the snake collides with the wall or its own body.

## What I Learned
- Applying Object-Oriented Programming (OOP) with classes and modules
- Using inheritance with Turtle-based `Food` and `Scoreboard` classes
- Managing object movement and collision detection
- Using list slicing (`snake.segments[1:]`) for self-collision checks
- Handling keyboard controls with event listeners
- Organizing projects across multiple Python files

## Methods & Features Used
- `create_snake()` and `add_segment()` to build the snake body
- `move()` to update snake movement
- `extend()` to grow the snake after eating food
- `goto()` to position objects on the screen
- `distance()` to detect collisions with food and snake segments
- `score_update()` and `game_over()` for score tracking and end-game display
- `screen.listen()` and `screen.onkey()` for keyboard controls

## Key Takeaways
- Improved understanding of OOP and inheritance
- Practiced real-time game logic and collision detection
- Learned to structure larger projects using multiple modules
- Built an interactive game using Turtle graphics
