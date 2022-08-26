import datetime

droid_price_list = []
week = str(datetime.datetime.now())
droid_number = 0

while True:
    try:
        user_input = int(input("Price of droid: "))
        droid_price_list.append(user_input)
    except ValueError:
        print()
        print("The program has been stopped. Here are the received results.")
        print()
        break

with open("Droid_Stats.txt", "w") as f:
    print("For the week of:" + week, file=f)
    for price in droid_price_list:
        droid_number += 1
        print(f"Price of droid {droid_number} is: $", price, file=f)

    number_of_droids = len(droid_price_list)
    total_cost = sum(droid_price_list)
    average_cost = sum(droid_price_list)/len(droid_price_list)

print("For the week of: " + week)
print()
print(f"Number of droids: {number_of_droids}")
print(f"Total cost: {total_cost}")
print(f"Average cost per droid: {average_cost}")
