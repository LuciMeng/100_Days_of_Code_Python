## Day 8 – Caesar Cipher Project 🔐

### What I Built  
The Caesar Cipher is a classic encryption technique that shifts each letter in a message by a certain number of places in the alphabet. 
It’s a fun way to get hands-on with basic cryptography concepts, while also reinforcing Python fundamentals like loops, functions, and string manipulation.

### How It Works  
- The user inputs:
  - A direction: `encode` or `decode`
  - A shift amount (how far to move each letter)
  - A message (text to be encrypted or decrypted)  
- The program shifts each letter accordingly:
  - If encoding, it moves letters forward.
  - If decoding, it shifts them backward.
- Non-letter characters like numbers, symbols, and spaces stay unchanged.
- The program keeps looping, letting the user try again until they choose to exit.

### Code Highlights  
- Used `index()` to find a character's position in the alphabet.
- Applied the modulo operator (`%`) to wrap around the alphabet when shifting past "z".
- Built a reusable function with keyword arguments for flexibility.
- Used a `while` loop to allow the program to restart based on user input.
- Practiced how to separate logic cleanly using functions and arguments.

### What I Learned  
This project really helped me understand how to combine logic, string handling, and control flow to build a real-world tool. 
It was also a good intro to how encryption works at a basic level — and a great exercise in keeping user experience interactive and smooth.
