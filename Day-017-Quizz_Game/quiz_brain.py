class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.question} (True/False)?: ").capitalize()
        self.check_answer(user_answer, current_question.correct_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self, user_response, correct_answer):
        if user_response == correct_answer:
            self.score += 1
            print(f"You got it correct! \n"
                  f"The correct answer was: {correct_answer} \n"
                  f"Your current score is: {self.score}/{self.question_number} \n")
        else:
            print(f"That is wrong. \n"
                  f"The correct answer was: {correct_answer} \n"
                  f"Your current score is: {self.score}/{self.question_number} \n")
