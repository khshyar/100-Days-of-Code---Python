import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):

    how_many_cards = len(card_list)
    sum_score = 0
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

   # calculate sum with loop
    # score = 0
    # for n in range(0, len(card_list)):
    #     score += card_list[n]
    # return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        sum_user_cards = calculate_score(user_cards)
        sum_computer_cards = calculate_score(computer_cards)
        print(f"Yor cards: {user_cards}, current score: {sum_user_cards}")
        print(
            f"Computer first card: {computer_cards[0]}")

        if sum_user_cards == 0 or sum_computer_cards == 0 or sum_user_cards > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while sum_computer_cards != 0 and sum_computer_cards < 17:
        computer_cards.append(deal_card())
        sum_computer_cards = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {sum_user_cards}")
    print(
        f"Computer final hand: {computer_cards}, final score: {sum_computer_cards}")
    print(compare(sum_user_cards, sum_computer_cards))


while input("Do you want to play a game of Blackjack? Type 'y' of 'n': ") == "y":
    os.system("cls")
    play_game()

    # elif sum_computer_cards
# print(user_cards)
# print(computer_cards)
# print(sum_user_cards)
# print(sum_computer_cards)
