from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_question():
    new_quiz.next_question() # new_question() is a method
