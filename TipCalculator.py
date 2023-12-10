print("Welcome to the waste your money on tips calculator!")
bill = input(str("What is the total bill? "))
tip_percent = input(str("What percentage tip would you like to waste? 10, 15, or 25? "))
people_split = input(str("How many people are splitting the bill? "))

tip = float(bill) * float(tip_percent) / 100
total_bill = float(tip) + float(bill)
each_split = float(total_bill) / float(people_split)


total = round(each_split, 2)

print("Each person should pay $" + str(total))