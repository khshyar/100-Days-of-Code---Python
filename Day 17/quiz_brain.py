
# end_of_quiz = False
# counter = 0
# score = 0
# question_counter = len(question_bank)

# while not end_of_quiz:

#     answer = input(question_bank[counter].text)
#     if answer == question_bank[counter].answer:
#         score += 1
#         print(f"Correct. Your score is {score}")
#     else:
#         print(f"Not correct. Score: {score}")

#     counter += 1
#     if counter > question_counter:
#         end_of_quiz = True

# video 160


class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(
            f"Q.{self.q_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.q_number >= len(self.q_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.q_number}")
        print("\n")
