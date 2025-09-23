# Day 17 – Quiz Game Project

## Project Overview
For this project, I built a simple Quiz Game using object-oriented programming (OOP). 
The program presents a series of True/False questions, gives instant feedback, and shows a final score at the end.  

It was a hands-on way to apply concepts like classes, methods, attributes, and objects while also practicing code organization across multiple files.  

---

## Key Learnings
- Creating and working with classes in Python  
- Initializing attributes using the `__init__` method  
- Writing methods inside classes to manage behavior  
- Storing multiple objects in a list and iterating through them  
- Passing objects between classes  
- Structuring a project with separate files for data, models, and logic  

---

## How the Quiz Works
1. A list of dictionaries (`question_data`) provides the quiz questions and answers.  
2. Each dictionary is turned into a `Question` object, storing both text and the correct answer.  
3. All `Question` objects are collected in a `question_bank` list.  
4. A `QuizBrain` object runs the game: it tracks the question number, asks each question, checks the answer, updates the score, and decides when the quiz ends.  
5. Score is displayed as each question is answered.

---

## Highlights
- Practiced OOP principles: classes, attributes, methods, and objects  
- Organized code into separate files: `question_model.py`, `data.py`, `quiz_brain.py`, and `main.py`  
- Gained experience managing lists of objects and controlling program flow with class methods  
