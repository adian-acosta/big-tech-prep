greeting = input("Geeting: ").lower().lstrip().split(" ", 1)[0].strip(",.!?")

if greeting == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
