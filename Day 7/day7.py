# step 1
import random

# TODO 1
word_list = ["apple", "camel", "Lion"]
chosen_word = random.choice(word_list)
list_of_letters = list(chosen_word)

# TODO 2
guess = input("Guess a letter: ").lower()


for n in list_of_letters:
    if guess == n:
        print("true")
    else:
        print("false")

print(type(guess))
print(type(list_of_letters))
print(chosen_word)
print(list_of_letters)
# print(guess)
