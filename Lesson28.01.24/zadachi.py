age = input("месяц рождения: ")

try:
    age = int(age)
except ValueError:
    print("ошибка")
else:
    if age == 12 or age == 1 or age == 2:
        print("За окном падал белый снег")
    elif age >= 3 and age <= 5:
        print("Птицы пели прекрасные песни")
    elif age >= 6 and age <= 8:
        print("Солнце светило ярче чем когда-либо")
    elif age >= 9 and age <= 11:
        print("Урожай был невероятным")
    else:
        print("такого месяца нет")
