spisok = [9, 1, 2, 3, 4, 5, 6, 7]

count = 0
count2 = 0

for i in spisok:
    if i %2 == 0:
        count += 1
    else:
        count2 += 1
print("Четных:", count, "Нечетные:", count2)

sum = 0
pr = 1
if count > count2:
    for i in spisok:
        sum += i
    print("Сумма:", sum)
else:
    pr = spisok[0] * spisok[2] * spisok[5]
    print("Произведение:", pr)