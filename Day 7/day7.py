# step 1
import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

# TODO 1
# word_list = ["apple", "camel", "lion"]
chosen_word = random.choice(word_list)
list_of_letters = list(chosen_word)
end_of_game = False
display = []
how_many_letters = len(list_of_letters)
guess = ""
lives = 6
print(chosen_word)
print(logo)

# TODO 2
for n in range(0, how_many_letters):
    display.append("_")
print(display)

while display != list_of_letters and not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    if guess in display:
        print(f"You've already guessed this letter.\"{guess}\"")

    for index, value in enumerate(list_of_letters):
        if guess == value:
            display[index] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    if "_" not in display:
        print("You win.")
    print(stages[lives])


# another way to create loop
# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     for index, value in enumerate(list_of_letters):
#         if guess == value:
#             display[index] = guess
#     print(display)

#     if "_" not in display:
#         end_of_game = True

# Another way to create a loop with index
# sequence = ['apple', 'banana', 'cherry']
# for index in range(len(sequence)):
#     value = sequence[index]
#     print(f"Index: {index}, Value: '{value}'")


# print(display)
# print(type(guess))
# print(type(list_of_letters))

# print(list_of_letters)
# print(guess)
