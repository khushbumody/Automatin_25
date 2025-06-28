num1 = int(input("Enter number1\n"))
num2 = int(input("Enter number2\n"))
num3 = int(input("Enter number3\n"))

if num1 == num2 and num2 == num3 and num3 == num1:
    print("Equilateral Triangle")
elif (num1 == num2 and num1 != num3) or (num2 == num3 and num2 != num1) or (num1 == num3 and num1 != num2):
    print("Isosceles Triangle")
else:
    print("Scalene")
