a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


while a < b:
    a += 1
    if a == 0:
        break


    print(a)