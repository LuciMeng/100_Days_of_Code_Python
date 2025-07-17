# Day 6 – Reeborg’s World Maze Challenge

## What I Learned
- **Functions**: Wrote reusable blocks to simplify and structure the code.
- **While Loops**: Repeatedly checked conditions to control Reeborg’s movements.
- **Code Organization**: Improved logic clarity through better structure and reuse.

## Project Overview
In this challenge, Reeborg starts at a random location and direction in a maze. The task is to guide it to the goal using logical, repeatable steps.

## How It Works
- A setup `while` loop gets Reeborg into the correct starting orientation.
- The main loop uses a wall-following strategy to navigate the maze.
- A custom `turn_right()` function supports movement control, since only `turn_left()` is built-in.

## Code Highlights
- Used multiple condition checks: `wall_in_front()`, `wall_on_right()`, `at_goal()`.
- Two `while` loops handle different phases of the solution: setup and navigation.

This project helped improve my understanding of conditionals, loops, and function-based problem-solving in Python.
