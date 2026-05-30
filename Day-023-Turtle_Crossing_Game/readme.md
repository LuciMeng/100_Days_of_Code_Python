# Day 23 - Turtle Crossing Game

## Project Overview
Built a Turtle Crossing Game using Python’s Turtle graphics module. The player guides a turtle across a busy road while avoiding moving cars. Each successful crossing increases the level and car speed, making the game progressively more challenging.

## What I Learned
- Applying OOP to organize a project into multiple classes
- Using inheritance to create custom `Player` and `Scoreboard` classes
- Handling keyboard input with `screen.onkey()`
- Managing game loops and timing with the `time` module
- Tracking game state and increasing difficulty over time

## Methods & Features Used
- `screen.onkey()` and `screen.listen()` for player controls
- `move_cars()` to move the turtle
- `goto()` to reset the player position
- `distance()` to detect collisions with cars
- `time.sleep()` to control game speed
- `is_at_finish_line()` to detect level completion
- `speed_up()` to make cars move faster each level

## Key Takeaways
- Strengthened OOP and inheritance skills
- Practiced collision detection and game state management
- Built a multi-class game with increasing difficulty
- Combined Turtle graphics, user input, and timing to create an interactive game
