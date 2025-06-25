a = int(input("Enter your age: " ))
b = int(input("Enter your friend's age: "))

if a > b:
    print("Yoy are bigger than your friend")
elif a < b:
    print("your friend is bigger than you")
else:
    print("your age is same")
# ternarry operator
print("you are bigger" if a > b else "Your friend is bigger")


