import random
p = 0
x = 0
z = 0
dict1 = {}
while p <= 7:
    a = int(input("Введите первое число от 1 до 20: "))
    b = int(input("Введите второе число от 1 до 20: "))
    c = random.randint(1, 20)
    d = random.randint(1, 20)
    print("Третье число: ", c)
    print("Четвёртое число: ", d)
    sum1 = a+b
    sum2 = c+d
    print("Сумма введённых чисел: ", sum1)
    print("Сумма рандомных чисел: ", sum2)
    new_key_values_dict= {p:(c,d)}
    dict1.update(new_key_values_dict)

    print(dict1)
    if sum1 > sum2:
        print("Введённые больше")
        x = x + 1
    else:
        print("Рандомные больше")
        z = z+1
    p = p+1
print("Пара больше на ",x," раз")
if x == z:
    print(dict1[3])