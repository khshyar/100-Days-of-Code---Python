# video 92
# example

# country = input()  # add country name
# visits = int(input())  # number of visits
# list_of_cities = eval(input())

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Frankfurt", "Hamburg"]
#     }
# ]


# def add_new_country(country, visits, list_of_cities):

#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = list_of_cities

#     travel_log.append(new_country)


# add_new_country(country, visits, list_of_cities)
# print(
#     f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
# print(f"My favorite city was {travel_log[2]['cities'][0]}")

# Testing
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# for key in dict:
#     dict[key] += 1
#     print(dict)

# dict[1] = 4
# print(dict[1])
# print(dict)

import os

bid_dict = {}
end_of_biding = False


def find_highest_bidder(bids_record):
    if bids_record:
        max_value = max(bids_record.values())
        return max_value
    else:
        return "The dictionary is empty"


def find_key_of_max_value(input_dict):
    # Check if the dictionary is not empty
    if input_dict:
        # Find the key with the maximum value
        max_key = max(input_dict, key=input_dict.get)
        return max_key
    else:
        return "The dictionary is empty."


while not end_of_biding:
    name = input("What is your name? ")
    bid_price = int(input("What is you bid price? "))

    bid_dict[name] = bid_price

    asking = input(
        "Is there other users who want to bid? (Yes) or (No) ").lower()
    if asking == "no":
        winner_value = find_highest_bidder(bid_dict)
        winner_key = find_key_of_max_value(bid_dict)
        print(
            f"The winner of our object is {winner_key} with {winner_value} Euro")
        end_of_biding = True

    elif asking == "yes":
        os.system("cls")
