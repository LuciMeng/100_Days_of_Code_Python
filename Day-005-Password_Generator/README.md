# Day 005 - Password Generator 🔐

## What I Learned
- **For Loops**: Used loops to repeat tasks efficiently.
- **Range Function**: Applied `range()` to control loop iterations and generate precise character counts.
- **Random Module**: Practiced using `random.choice()` to select characters and `random.shuffle()` to randomize sequences.
- **String and List Conversion**: Learned how to build and shuffle a password by converting between strings and lists, since `random.shuffle()` only works on mutable sequences.

## Project Overview
I built a password generator that creates two types of passwords:
- **Sequence Password**: A structured password where letters come first, followed by numbers, then symbols.
- **Strong Password**: A fully randomized mix of letters, numbers, and symbols for stronger security.

## How It Works
- The user inputs how many letters, symbols, and numbers they want in their password.
- The program generates the characters using loops and `random.choice()`.
- For the **strong password**, the character list is shuffled before being joined into a string.
- For the **sequence password**, characters are kept in a specific order.

## Code Highlights
- `random.choice()`: Picks random characters with the possibility of duplicates.
- `random.shuffle()`: Shuffles a list in-place.
- Looping with `range()` allowed precise control over how many characters were added.

## Reflection
This project helped me practice loop logic, string manipulation, and randomization in Python. 
