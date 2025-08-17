## Day 12 – Number Guessing Game

### Project Overview  
A simple console-based Python game that generates a random number (1–100) and lets the user guess it.  
After each guess, the player gets feedback (“Too high” / “Too low") and a limited number of attempts depending on the difficulty level.

### What I Learned
- **Local vs Global scope** (and how to update global variables in functions)
- **Constants** and when to use them (e.g., EASY_ATTEMPTS, HARD_ATTEMPTS)
- **Modular code** – splitting logic into reusable functions
- **User interaction** with feedback after every guess

### How It Works
- User chooses a difficulty: **easy** (10 tries) or **hard** (5 tries)
- A random number is generated between 1 and 100
- Player keeps guessing until:
  - They guess correctly → **win**
  - They run out of attempts → **lose**

### Code Highlights
- Functions used to organize logic:  
  `check_answer()`, `set_difficulty()`, and `play_game()`
- Game prints remaining attempts after each wrong guess and gives helpful feedback.
