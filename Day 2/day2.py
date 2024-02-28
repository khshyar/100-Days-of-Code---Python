total_bill = float(input("What was the total bill?"))
percentage_tip = float(input("What percentage tip would you like to give?"))
how_many_people = int(input("How many people to split the bill?"))


print(type(total_bill))
tip = (total_bill * percentage_tip) / 100
res = (total_bill+tip)/how_many_people

print(round(res, 2))
