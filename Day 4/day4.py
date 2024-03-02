import random
# import my_module

# print(my_module.pi)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choose = random.randint(0, 2)

game_lists = [rock, paper, scissors]

print("Your choose:" + game_lists[player_choose])
print("Computer choose: "+game_lists[computer_choose])


if player_choose == 0 and computer_choose == 2:
    print("You win!")
elif computer_choose > player_choose:
    print("You lose")
elif player_choose == computer_choose:
    print("It's a draw")
elif player_choose == 2 and computer_choose == 0:
    print("You lose")
elif computer_choose < player_choose:
    print("You win!")
else:
    print("You entered something wrong!")
