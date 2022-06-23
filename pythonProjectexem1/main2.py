a = str(input("Введите текст"))
b = ('a', 'e', 'i', 'o', 'u', 'y')
l = []
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
for buk in a:
    if buk in b:
        l.append(buk)
    else:
        continue
l.sort()
print(l)


