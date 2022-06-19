food = [5, 77, 6, 9]
a = int(input("Введите число:"))



for el in food:
    if el == a:
        print("Я не спользую 6 ")
        break
    print("Отлично " + str(el))
else:
    print("Хорошо, что не было 6 ")

print("Конец")