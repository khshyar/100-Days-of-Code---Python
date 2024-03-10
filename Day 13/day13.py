import random
from art import logo
from art import vs
from game_data import data


def compare(dict_a, dict_b):
    if dict_a['follower_count'] > dict_b['follower_count']:
        return "A"
    elif dict_a['follower_count'] < dict_b['follower_count']:
        return "B"
    else:
        return "Equal"


print(logo)

score = 0
end_of_game = False

while not end_of_game:
    random_choice_a = random.choice(data)
    random_choice_b = random.choice(data)
    more_follower = compare(random_choice_a, random_choice_b)

    print(
        f"Compare A: {random_choice_a['name']}, {random_choice_a['description']}, from {random_choice_a['country']}.")

    print(vs)

    print(
        f"Against B: {random_choice_b['name']}, {random_choice_b['description']}, from {random_choice_b['country']}.")

    select_object = input("Who has more follower? Type 'A' or 'B': ")
    if select_object == more_follower:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = True

        # print(which_data)
        # print(random_choice)
        # print(random.choice(data[0][2][3]))


#######################

# import random

# from replit import clear

# from art import logo, vs
# from game_data import data


# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess
#   and returns True if they got it right.
#   Or False if they got it wrong."""
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")

#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()
