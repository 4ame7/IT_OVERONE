list=[15, 48, 'hello', 6, 19, 'world']
for el in (15, 48, 6, 19):
    if el %2 == 0:
        print(el)
num = 48
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)

for el1 in (15, 48, 6, 19):
    if el1 %2 != 0:
        print(el1)

ind = list.index(15)
inde = list.index(19)
list[inde] = 1
list[ind] = 1
print(list)

a = ("hello world")
count = 0
count1 = 0
vowels = set("aeiouy")
con = set("bcdfghjklmnpqrstvwxz")
for letter in a:
    if letter in vowels:
        count += 1
    else:
        for letter in a:
            if letter in con:
                count1 += 1
print("Количество гласных равно:", count)
print("Количество согласных букв равно:", count1)
print(list)