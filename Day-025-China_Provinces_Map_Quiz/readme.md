# Day 25: China Province Map Quiz

## Project Overview

This project is an interactive geography quiz where players try to name all 34 provincial-level divisions of China. Each correct answer is displayed in its corresponding location on the map. The game continues until all provinces are guessed or the player chooses to exit.

If the player enters `"Exit"`, the program generates a `provinces_to_learn.csv` file containing the provinces that were not guessed correctly, making it easy to review and study them later.

This project uses Turtle graphics for the map interface and Pandas for working with CSV data.

## How It Works

- Displays a blank map of China using Turtle graphics.
- Loads province names and coordinates from `Coordinates.csv`.
- Prompts the user to guess province names and keeps track of correct answers.
- Displays correctly guessed provinces on the map and updates the score.
- Creates a `provinces_to_learn.csv` file with any missed provinces when the user exits.
- Ends when all 34 provincial-level divisions have been guessed.

## Project Highlights

- Built an interactive map-based quiz using Turtle graphics.
- Used Pandas to read and process CSV data.
- Implemented score tracking and answer validation.
- Generated a custom study file for missed provinces.
- Practiced working with user input, coordinates, and data filtering.
