
# ex1

# student_heights = input().split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# print(student_heights)
# print(len(student_heights))

# sum_heights = 0

# for n in range(0, len(student_heights)):
#     sum_heights += student_heights[n]

# average_heights = sum_heights / len(student_heights)

# print(sum_heights)
# print(average_heights)

# ex2

# student_heights = input().split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# highest_height = 0

# for n in range(0, len(student_heights)):
#     if highest_height < student_heights[n]:
#         highest_height = student_heights[n]


# print(highest_height)
# Project of day 5
import random
print("Welcome to the PyPassword Generator!")
how_many_letters = int(
    input("How many letters would you like in your password? "))
how_many_symbols = int(input("How many symbols would you like? "))
how_many_numbers = int(input("How many numbers would you like? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all_lists = [letters, numbers, symbols]

how_many = how_many_letters + how_many_numbers + how_many_symbols


# easy way
# my_password = ""
# for x in range(1, how_many_letters + 1):
#     my_password += random.choice(letters)

# for x in range(1, how_many_symbols + 1):
#     my_password += random.choice(numbers)

# for x in range(1, how_many_numbers + 1):
#     my_password += random.choice(symbols)

# print(my_password)

# hard way

my_password_list = []
for x in range(1, how_many_letters + 1):
    my_password_list.append(random.choice(letters))

for x in range(1, how_many_symbols + 1):
    my_password_list += random.choice(numbers)

for x in range(1, how_many_numbers + 1):
    my_password_list += random.choice(symbols)


random.shuffle(my_password_list)

my_password_str = ""

for char in my_password_list:
    my_password_str += char

print(my_password_str)
