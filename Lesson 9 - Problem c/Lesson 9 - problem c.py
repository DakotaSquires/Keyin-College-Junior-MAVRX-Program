message = ["Apple", "Banana", "Orange", "Kiwi", "Dragonfruit"]

try:
    b = open("message.txt")
    text = b.read()
    print(text)
except FileNotFoundError:
    print("There is no file by that name")

