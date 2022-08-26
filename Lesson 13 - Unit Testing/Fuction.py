x = float(input("Enter a number"))
y = float(input("Enter a number"))
z = float(input("Enter a number"))

def doing_stuff(a, b, c):
    items = a + b + c
    tax = 1.15
    total = items + tax
    return total

print(doing_stuff(x, y, z))