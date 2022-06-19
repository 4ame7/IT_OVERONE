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
vowels = 0
consonants = 0
for i in a:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print("Гласных %i\nСогласных %i" % (vowels, consonants))