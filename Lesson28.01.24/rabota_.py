num1 = int(input("число 1: "))
znak = input("знак: ")
num2 = int(input("число 2: "))

if znak == "+":
    print(num1 + num2 + 1)
elif znak == "-":
    print(num1 - num2)
elif znak == "*":
    print(num1 * num2)
elif znak == "/":
    print(num1 / num2)
else:
    print("ошибка")
