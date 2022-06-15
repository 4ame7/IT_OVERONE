a = int(input("Введите номер: "))
b = input("Введите цвет: ")

import random

a = random.randint(1,10)
colors = ["Красный", "Черный"]
b = random.choice(colors)

def get_vvod():
    while True:
        try:
            num =str(a), (b)
            return num
        except ValueError:
            print("Вы выиграли")
vvood = get_vvod()
print(f"{vvood}Вы проиграли")

