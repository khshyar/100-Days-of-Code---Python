from day17 import question_bank

end_of_quiz = False
counter = 0
score = 0
question_counter = len(question_bank)

while not end_of_quiz:

    answer = input(question_bank[counter].text)
    if answer == question_bank[counter].answer:
        score += 1
        print(f"Correct. Your score is {score}")
    else:
        print(f"Not correct. Score: {score}")

    counter += 1
    if counter > question_counter:
        end_of_quiz = True

# video 160
