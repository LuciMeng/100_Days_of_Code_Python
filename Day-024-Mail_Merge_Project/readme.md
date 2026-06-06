# Day 24: Mail Merge

## Project Overview

This project automates the process of creating personalized invitation letters using Python. Given a template letter and a list of names, the program generates an individual letter for each recipient automatically.

While building this project, I learned how to work with files in Python using open(), read(), and write(), as well as how to use relative file paths to organize and access project files.

## What I Learned

### File Handling

I learned how to use:
- open() to access files
- read() and readlines() to retrieve file contents
- write() to create and save new files

### The with Statement

The with statement automatically handles opening and closing files, making file operations safer and more efficient.

### File Paths

I learned the difference between:
- Absolute paths, which specify a file's full location on a system
- Relative paths, which locate files based on the current project directory

This project uses relative paths to access files and folders within the project structure.

## How It Works

### Reading the Guest List

The program uses readlines() to load names from invited_names.txt. Each name is cleaned using strip() to remove newline characters.

### Loading the Template

The starting_letter.txt file is opened and read as a template. It contains a [name] placeholder that will be replaced with each guest's name.

### Creating Personalized Letters

The program loops through the list of names and uses the replace() method to substitute [name] with the actual recipient's name.

### Saving the Letters

For each guest, a new text file is created in the ReadyToSend folder containing the personalized invitation letter.

## Project Highlights

- Automated the creation of personalized letters.
- Used replace() to customize a template for multiple recipients.
- Applied the with statement to manage file operations safely.
- Practiced using relative file paths within a project.
- Learned how to read, create, and write files using Python.
