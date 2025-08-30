# Day 14 - Higher Lower Game

## Project Overview
This project is a console-based guessing game called **Higher Lower**, where players compare social media follower counts. 
The objective is to test your guessing skills by choosing between two public figures and deciding who has more followers.

## How It Works
1. The game begins by showing two public figures with their **name**, **profession**, and **country**.
2. The player guesses who has more followers by typing **'A'** or **'B'**.
3. If the guess is correct:
   - The score increases by 1.
   - The correctly guessed figure carries forward into the next round:
     - If B was correct, it becomes the new A.
     - If A was correct, A stays the same.
   - A new random account is selected for B.
4. If the guess is incorrect:
   - The game ends.
   - The final score is displayed.

## Code Highlights
- **`format_data` function**: Converts account data (dictionary) into a clean, printable sentence.  
- **Account rollover**: After each round, the correct option is carried forward to ensure continuity.  
- **Score tracking**: Keeps track of the player’s score and displays progress after each correct guess.  
- **Duplicate check**: Ensures A and B are never the same person.  
- **Game loop**: Repeats until the player guesses incorrectly, providing continuous play.

## Reflection
This project was a good practice in:
- Working with **functions** to keep code organized.
- Using **loops** for repeated gameplay.
- Handling **conditionals** to compare values and check correctness.
- Building a complete game that combines multiple Python concepts.

